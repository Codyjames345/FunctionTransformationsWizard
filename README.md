# FunctionTransformationsWizard
Allows entry of an object and image function and returns the transformation steps required.


Function Transformations Wizard (FTW™) V1.1
created by Cody Lincoln with the supervision of Stack Overflow

The program asks for two user inputs - the object and image functions - and returns a list of steps required to transform the object into the image.
I started building this as a fun project but I would like to see it finished one day.

Instructions
- download transformationsWizard.py
- if you don't already have the Python RegEx library you can install that with "pip install regex" or "python -m pip install regex".
- get a Victory Royale in the popular third-person shooter game "Fortnite"
- run with any Python interpreter.

TODO
- revise maths (some wrong answers)
- add support for other function formats like 1/x and sin(x)
- add check for different powers
- more idiot-proofing
- simplify steps including variables
- allow user entry of object function and transformation steps and return image function
- fix RegEx matches

Changelog

V1.1 - Redstone Update
- separate SanitiseInput function created
- spaces are able to be processed

V1.0 - Infdev
- findSeq function returns list of transformation steps when provided the object and image functions
- basic functionality
- limited input variability
