# Function Transformations Wizard (FTW™) V2.0b
## created by Cody Lincoln for personal usage

The program asks for two user inputs - the object and image functions - and returns a list of steps required to transform the object into the image.
I started building this as a fun project but I would like to see it finished one day.
Currently only x is supported as a variable and other unknowns will not be processed.

Dependencies
- RegEx Python library

Instructions
1. download transformationsWizard.py
2. if you don't already have the Python RegEx library you can install that with `pip install regex` or `python -m pip install regex`.
3. get a Victory Royale in the popular third-person shooter game "Fortnite"
4. run with any Python interpreter.

Planned Features
- [x] allow spaces in user input
- [x] support f(x) notation
- [x] add support for other function formats like 1/x and sin(x)
- [x] fix RegEx matches
- [x] allow no brackets in cases like x**2
- [ ] add check for different powers
- [ ] integrate simplification process
- [ ] support fractions in both user input and function output when applicable


Future Release
- [ ] allow variables other than x to be used
- [ ] allow input of unknown variables
- [ ] allow user entry of object function and transformation steps and return image function (V3 Update)
- [ ] simplify steps including variables

Changelog

V2.0b - The Update That Changed The World (beta)
- a variety of new functions are supported, including but not limited to
    - sin(x), cos(x), tan(x)
    - 1/x, 1/x**2 ...
    - |x|
- added FindGroup function which fixes cases where multiple RegEx matches occur
- added NumConvert function which greatly de-spaghettifies the coefficient check
- finally fixed the goofy ahh RegEx matches
- greatly increased compatibility with alternate function layouts
- moved some comments to be above the relevant code for readability
- revised the scope of the project to be more relevant

V1.2.1 - Snapshot Update
- fixed variable reference in SanitiseInput function

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