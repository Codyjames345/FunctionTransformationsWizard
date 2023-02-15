# Function Transformations Wizard (FTW™) V1.2
# created by Cody Lincoln with the supervision of Stack Overflow

import re # import Python RegEx library

def SanitiseInput(rawInput): # define SanitiseInput funciton

    funcName = None # initialise function name

    # strip whitespace from inputs
    cleanInput = re.sub(r'\s+', '', rawInput)
    if "=" in rawInput:
        # get equation after equals sign to prevent f(x) notation triggering the RegEx
        # update function name with content before equals sign
        funcName, cleanInput = rawInput.split("=")

    #TODO more sanitisation

    return [funcName, cleanInput] # return function name and sanitised input in a list

def FindSeq(obj_raw, img_raw): # define FindSeq function

    # call SanitiseInput function on both the object and image
    obj_san, img_san = SanitiseInput(obj_raw), SanitiseInput(img_raw)
    
    # store function name and equation (after equals sign)
    obj_func, obj = obj_san
    img_func, img = img_san

    # get variables from object and image
    a = re.search(r"(\-*[a-zA-Z0-9.]+)\(", obj)
    ad = re.search(r"(\-*[a-zA-Z0-9.]+)\(", img)
    b = re.search(r"(\-*[a-zA-Z0-9.]+)x", obj)
    bd = re.search(r"(\-*[a-zA-Z0-9.]+)x", img)
    h = re.search(r"x([-+][a-zA-Z0-9.]+)", obj)
    hd = re.search(r"x([-+][a-zA-Z0-9.]+)", img)
    k = re.search(r"([-+][a-zA-Z0-9.]+)$", obj)
    kd = re.search(r"([-+][a-zA-Z0-9.]+)$", img)

    # set default values for shorthand writing (e.g. x = 1x) if match not found
    # capture variables with regex group

    # check for negative sign without number
    if a is None:
        a = re.search(r"(\-\()", obj)
        if a is None: a = 1
        else: a = -1
    else: a = a.group(1)
    if ad is None:
        ad = re.search(r"(\-\()", img)
        if ad is None: ad = 1
        else: ad = -1
    else: ad = ad.group(1)
    if b is None:
        b = re.search(r"(\-x)", obj)
        if b is None: b = 1
        else: b = -1
    else: b = b.group(1)
    if bd is None:
        bd = re.search(r"(\-x)", img)
        if bd is None: bd = 1
        else: bd = -1
    else: bd = bd.group(1)

    # test for alternate layout h - bx
    if h is None:
        h = re.search(r"\((\-*[a-zA-Z0-9.]+)[-+]", obj)
        if h is None: h = 0
        else: h = h.group(1)
    else: h = h.group(1)
    if hd is None:
        hd = re.search(r"\((\-*[a-zA-Z0-9.]+)[-+]", img)
        if hd is None: hd = 0
        else: hd = hd.group(1)
    else: hd = hd.group(1)

    if k is None: k = 0
    else: k = k.group(1)
    if kd is None: kd = 0
    else: kd = kd.group(1)

    steps = [] # initiate empty steps list

    # dilation/reflection from x-axis
    try:
        dil_x = float(ad)/float(a)
        if dil_x < 0:
            steps.append("Reflect across the x-axis") # reflect if negative dilation
            dil_x = -dil_x
        if dil_x != 1.0:
            steps.append(f"Dilate * {dil_x} units from the x-axis") # dilation from x-axis = b/bd
    except ValueError:
        steps.append(f"Dilate * {ad}/{a} units from the x-axis") # variable was entered
    
    # dilation/reflection from y-axis
    try:
        dil_y = float(b)/float(bd)
        if dil_y < 0:
            steps.append("Reflect across the y-axis") # reflect if negative dilation
            dil_y = -dil_y
        if dil_y != 1.0:
            steps.append(f"Dilate * {dil_y} units from the y-axis") # dilation from y-axis = ad/a
    except ValueError:
        steps.append(f"Dilate * {b}/{bd} units from the y-axis") # variable was entered

    # translation in x-axis
    try: 
        trans_x = -(float(hd)-float(h))/float(bd) # negative because -h = translation of +h right
        if trans_x < 0:
            steps.append(f"Translate {-trans_x} units to the left") # negative translation right = positive translation left
        elif trans_x > 0:
            steps.append(f"Translate {trans_x} units to the right") # translate (hd-h)/bd right, if trans_x = 0 nothing will be added
    except ValueError:
        steps.append(f"Translate ({hd}-{h})/{bd} right") # variable was entered
    
    # translation in y-axis
    try: 
        trans_y = (float(kd)*float(a)-float(k)*float(ad))/float(a)
        if trans_y < 0:
            steps.append(f"Translate {-trans_y} units down") # negative translation up = positive translation down
        elif trans_y > 0:
            steps.append(f"Translate {trans_y} units up") # translate (kd*a-k*ad)/a up, if trans_y = 0 nothing will be added
    except ValueError:
        steps.append(f"Translate ({kd}*{a}-{k}*{ad})/{a} up") # variable was entered

    return [obj_func, img_func, steps] # return function names and list of calculated steps

print("Enter all equations in the form y = a(bx-h)**n+k")
obj = input("Enter the object: ")
img = input("Enter the image: ") # input object and image functions from user

obj_func, img_func, steps = FindSeq(obj, img) # get function names and list of steps from FindSeq function

if obj_func and img_func:
    print(f"Steps required to transform {obj_func} --> {img_func}")

if not steps:
    print("No transformations required bruh") # no steps were added because you entered the same function twice you goofball
else:
    for i in range(len(steps)): # iterate through list of steps
        print(f"{i+1}. {steps[i]}") # print step number + step