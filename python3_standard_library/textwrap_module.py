import textwrap


some_text = """    Course 3 is a continuation of the previous course, 
and will focus on teaching you how to work with tools you need to do your everyday work. 
    The course begins by introducing you to numerous essential command line tools that are used daily. 
    Then, it focuses on bash scripting - you will learn how to construct scripts and how to do very 
complicated tasks in an automated way. 
"""

print("No Dedent: ")
print(textwrap.fill(some_text))

print("\nDedent: ")
print(textwrap.dedent(some_text))

print("\nFill: ")
print(textwrap.fill(textwrap.dedent(some_text), width=100))

print("\nControlling Indent:")
print(textwrap.fill(textwrap.dedent(some_text), initial_indent="   ", subsequent_indent="       "))

print("\nShortening text:")
print(textwrap.shorten("Then, it focuses on bash scripting", width=25, placeholder="..."))
