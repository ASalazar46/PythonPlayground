Project Number: 1
Title: Calculator No GUI
Team: Andrew Salazar (just me)
Overview: 
    A command line application that functions as a calculator. Will
    save implementing a GUI for a different project.
Context:
    After reading through the Python tutorial provided by the official 
    docs page (http://docs.python.org/3.10/tutorial) I searched for
    beginner Python projects. This idea was one of the first that I saw, 
    and I chose to do this project first. 
Goals:
    From this project, I will:
    - Learn the basics of organizing Python code into applications (no 
    matter how small or useless they are to anyone). 
    - Take my first steps towards becoming accustomed to project building. 
    - Become familiar with writing design documents (even if small at first).
    - Create an application that functions as a standard, not scientific, 
    calculator.
Achieved Milestones:
    - [5/20/2022] Project folder and design document (this README.md) created.
    - [5/21/2022]
Proposed Solution:
    This calculator should be able to handle EMDAS operations, at minimum, to
    be considered complete. EMDAS stands for: exponentials, multiplication, 
    division, addition, and subtraction.
    Running the script should display these things first:
        - A greeting message
        - A list of commands
        - The syntax required to properly pass arguments to the script
        which is: <operator> <value1> <value2>
    The script should then wait for user input that follows the syntax. Perhaps 
    store user arguments in a list. If it does not follow the syntax, display 
    an error and continue waiting for input. If the operator is invalid or 
    undefined, display an error and continue waiting for input. 
    Internally, functions will handle singular mathematical operation and 
    prevent unhandled errors. If the values passed to the functions are invalid 
    for the operator (e.g: giving strings instead of ints to an addition 
    operator), display an error and wait for more user input. Specifically, for 
    division-type ops, display an error if value2 is zero (no dividing by zero). 
    Print the result upon success, and continue to wait for more user input. 
    Quitting the script should be its own command, possibly something like '-Quit.'
Current Progress/Solution:
    adsf