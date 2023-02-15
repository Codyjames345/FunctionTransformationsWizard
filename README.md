# FunctionTransformationsWizard
## Function Transformations Wizard (FTW™) V1.2
## created by Cody Lincoln with the supervision of Stack Overflow

The program asks for two user inputs - the object and image functions - and returns a list of steps required to transform the object into the image.
I started building this as a fun project but I would like to see it finished one day.

Dependencies
- RegEx Python library

Instructions
1. download transformationsWizard.py
2. if you don't already have the Python RegEx library you can install that with `pip install regex` or `python -m pip install regex`.
3. get a Victory Royale in the popular third-person shooter game "Fortnite"
4. run with any Python interpreter.

TODO
- [x] allow spaces in user input
- [x] support f(x) notation
- [ ] allow variables other than x to be used
- [ ] add support for other function formats like 1/x and sin(x)
- [ ] add check for different powers
- [ ] more idiot-proofing
- [ ] simplify steps including variables
- [ ] fix RegEx matches
- [ ] allow no brackets in cases like x**2
- [ ] allow user entry of object function and transformation steps and return image function (V2 Update)

Changelog

V1.2 - The Horse Update
- separated function name from equation
- added support for f(x) notation
- added header before steps showing function names

V1.1 - Redstone Update
- separate SanitiseInput function created
- spaces are able to be processed

V1.0 - Infdev
- findSeq function returns list of transformation steps when provided the object and image functions
- basic functionality
- limited input variability