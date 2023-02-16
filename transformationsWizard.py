# Function Transformations Wizard (FTW™) V2.0b
# created by Cody Lincoln

# this is a beta version, functionality might break with certain inputs (I haven't added input validation yet 💀)
# some answers may be incorrect

import re # import Python RegEx library

def FindGroup(search): # define FindGroup function
    for i in range(len(search.groups())): # iterate through length of groups tuple
        if search.group(i+1) is not None: # find the first value that is not None
            return search.group(i+1) # return the value
    return None # every group contained None

def GrabXY(func): # define GrabXY function

    # grab x terms with RegEx
    x_match = re.compile(r"[(|]([^)|]*x+[^)|]*)[|)]|(x)") # this actually grabs the x terms correctly 99% of the time lol

    # grab y terms with RegEx
    # TODO more robust matching
    y_match = re.compile(r"([a-zA-Z]*[(|][^)|]*x+[^)|]*[|)](?:\*\*[0-9.]+)*)|(x(?:\*\*[0-9.]+)*)")

    # FindGroup function returns content of first group that is not None
    # this means matching has left to right priority
    x_part = FindGroup(re.search(x_match, func)) # get all x (horizontal) transformations
    y_part = re.sub(y_match, "f", func) # replace x portion with "f" which leaves y (vertical) transformations

    base_func = None # TODO grab base function

    return [base_func, x_part, y_part] # return base function, and separated x and y portions

def SanitiseInput(rawInput): # define SanitiseInput funciton

    funcName = None # initialise function name

    # strip whitespace from inputs
    cleanInput = re.sub(r'\s+', '', rawInput)

    if "=" in cleanInput:
        # get equation after equals sign to prevent f(x) notation triggering the RegEx
        # update function name with content before equals sign
        funcName, cleanInput = cleanInput.split("=")

    # TODO more sanitisation

    return [funcName, cleanInput] # return function name and sanitised input in a list
def NumConvert(number, default): # define NumConvert function
    try:
        if number is None or number == "" or number == "-": # if user inputted "-" or omitted coefficient
            # return fixed number with default value appended (- becomes -1, no coefficient becomes 1)
            # default for translation is 0, dilation is 1
            return float(f"{number}{default}")
        else:
            return float(number) # else return input
    except ValueError: # if input was bad
        return "ValueError - Bad input" # return error


def FindSeq(obj_raw, img_raw): # define FindSeq function

    # call SanitiseInput function on both the object and image
    # store function name and equation (after equals sign)
    obj_func_name, obj_sanitised = SanitiseInput(obj_raw)
    img_func_name, img_sanitised = SanitiseInput(img_raw)

    # grab separated x and y parts from GrabXY function
    obj_base_func, obj_x_part, obj_y_part = GrabXY(obj_sanitised)
    img_base_func, img_x_part, img_y_part = GrabXY(img_sanitised)

    # strip "/" in 1/x cases so that b/f = bf where f = (1/x) which is a dilation of b from the x-axis (vertical)
    obj_y_part = obj_y_part.replace("/", "")
    img_y_part = img_y_part.replace("/", "")

    # get transformation variables from object and image using RegEx groups
    # TODO parse maths with library rather than hardcode

    # call NumConvert function on each variable to properly format as floating point number

    # finds coefficient of x (dilate from y-axis horizontal)
    dil_x_match = re.compile(r"([+-]?[0-9.]*)x")
    b = NumConvert(FindGroup(re.search(dil_x_match, obj_x_part)), 1)
    bd = NumConvert(FindGroup(re.search(dil_x_match, img_x_part)), 1)

    # finds coefficient of f (dilate from x-axis vertical)
    dil_y_match = re.compile(r"([+-]?[0-9.]*)f")
    a = NumConvert(FindGroup(re.search(dil_y_match, obj_y_part)), 1)
    ad = NumConvert(FindGroup(re.search(dil_y_match, img_y_part)), 1)

    # finds added or subtracted float in x part (horizontal translation)
    trans_x_match = re.compile(r"([+-]?[0-9.]*)(?![0-9.]*x)")
    h = NumConvert(FindGroup(re.search(trans_x_match, obj_x_part)), 0)
    hd = NumConvert(FindGroup(re.search(trans_x_match, img_x_part)), 0)

    # finds added or subtracted float in y part (vertical translation)
    trans_y_match = re.compile(r"([+-]?[0-9.]*)(?![0-9.]*f)")
    k = NumConvert(FindGroup(re.search(trans_y_match, obj_y_part)), 0)
    kd = NumConvert(FindGroup(re.search(trans_y_match, img_y_part)), 0)

    steps = [] # initiate empty steps list

    # dilation/reflection from y-axis (horizontal)
    dil_x = b/bd
    if dil_x < 0:
        steps.append("Reflect across the y-axis") # reflect if negative dilation
        dil_x = -dil_x
    if dil_x != 1.0:
        steps.append(f"Dilate * {dil_x} units from the y-axis") # dilation from y-axis = b/bd, if dil_x = 1 nothing will be added

    # dilation/reflection from x-axis (vertical)
    dil_y = ad/a
    if dil_y < 0:
        steps.append("Reflect across the x-axis") # reflect if negative dilation
        dil_y = -dil_y
    if dil_y != 1.0:
        steps.append(f"Dilate * {dil_y} units from the x-axis") # dilation from x-axis = ad/a, if dil_y = 1 nothing will be added

    # translation in x-axis
    trans_x = -(hd-h)/bd # negative because -h = translation of +h right
    if trans_x < 0:
        steps.append(f"Translate {-trans_x} units to the left") # negative translation right = positive translation left
    elif trans_x > 0:
        steps.append(f"Translate {trans_x} units to the right") # translate (hd-h)/bd right, if trans_x = 0 nothing will be added
    
    # translation in y-axis
    trans_y = (kd*a-k*ad)/a
    if trans_y < 0:
        steps.append(f"Translate {-trans_y} units down") # negative translation up = positive translation down
    elif trans_y > 0:
        steps.append(f"Translate {trans_y} units up") # translate (kd*a-k*ad)/a up, if trans_y = 0 nothing will be added

    return [obj_func_name, img_func_name, steps] # return function names and list of calculated steps


# not needed for now as multiple function types are supported (beta)
# print("Enter all equations in the form y = a(bx-h)**n+k")

# testing
# print(float("-0"))

# input object and image functions from user
obj = input("Enter the object: ")
img = input("Enter the image: ")

# get function names and list of steps from FindSeq function
obj_func, img_func, steps = FindSeq(obj, img)

if obj_func and img_func:
    print(f"Steps required to transform {obj_func} --> {img_func}")

if not steps:
    print("No transformations required bruh") # no steps were added because you entered the same function twice you goofball
else:
    for i in range(len(steps)): # iterate through list of steps
        print(f"{i+1}. {steps[i]}") # print step number + step