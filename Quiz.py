score = 0
total = 20
answer = ''
print('Let\'s start the Quiz')

print('\n1. Who developed Python Programming Language?')
print("""your options are:
        a) Wick van Rossum
        b) Rasmus Lerdorf
        c) Guido van Rossum
        d) Niene Stom""")
answer = input("\nenter your option(eg:a/b/c/d): ").lower()
if answer=='c':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n2. Which type of Programming does Python support?')
print("""your options are:
        a) object-oriented programming
        b) structured programming
        c) functional programming
        d) all of the mentioned""")
answer = input("\nenter your option: ").lower()
if answer=='d':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n3. Is Python case sensitive when dealing with identifiers?')
print("""your options are:
        a) no
        b) yes
        c) machine dependent
        d) none of the mentioned""")
answer = input("\nenter your option: ").lower()
if answer=='b':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n4. Which of the following is the correct extension of the Python file?')
print("""your options are:
        a) .python
        b) .pl
        c) .py
        d) .p""")
answer = input("\nenter your option: ").lower()
if answer=='c':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n5. Is Python code compiled or interpreted?')
print("""your options are:
        a) Python code is both compiled and interpreted
        b) Python code is neither compiled nor interpreted
        c) Python code is only compiled
        d) Python code is only interpreted""")
answer = input("\nenter your option: ").lower()
if answer=='a':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n6. All keywords in Python are in _________.')
print("""your options are:
        a) Capitalized
        b) lower case
        c) UPPER CASE
        d) None of the mentioned""")
answer = input("\nenter your option: ").lower()
if answer=='d':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n7. What will be the value of the following Python expression? 4 + 3 % 5')
print("""your options are:
        a) 7
        b) 2
        c) 4
        d) 1""")
answer = input("\nenter your option: ").lower()
if answer=='a':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n8. Which of the following is used to define a block of code in Python language?')
print("""your options are:
        a) Indentation
        b) Key
        c) Brackets
        d) All of the mentioned""")
answer = input("\nenter your option: ").lower()
if answer=='a':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n9. Which keyword is used for function in Python language?')
print("""your options are:
        a) Function
        b) def
        c) Fun
        d) Define""")
answer = input("\nenter your option: ").lower()
if answer=='b':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n10. Which of the following character is used to give single-line comments in Python?')
print("""your options are:
        a) //
        b) #
        c) !
        d) /*""")
answer = input("\nenter your option: ").lower()
if answer=='b':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print("""\n11. What will be the output of the following Python code?

i = 1
while True:
    if i%3 == 0:
        break
    print(i)
 
    i + = 1""")
print("""your options are:
        a) 1 2 3
        b) error
        c) 1 2
        d) none of the mentioned""")
answer = input("\nenter your option: ").lower()
if answer=='b':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n12. Which of the following functions can help us to find the version of python that we are currently working on?')
print("""your options are:
        a) sys.version(1)
        b) sys.version(0)
        c) sys.version()
        d) sys.version""")
answer = input("\nenter your option: ").lower()
if answer=='d':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n13. Python supports the creation of anonymous functions at runtime, using a construct called __________')
print("""your options are:
        a) pi
        b) anonymous
        c) lambda
        d) none of the mentioned""")
answer = input("\nenter your option: ").lower()
if answer=='c':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n14. What is the order of precedence in python?')
print("""your options are:
        a) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction
        b) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction
        c) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition
        d) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction""")
answer = input("\nenter your option: ").lower()
if answer=='d':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n15. What will be the output of the following Python code snippet if x=1? x<<2')
print("""your options are:
        a) 4
        b) 2
        c) 1
        d) 8""")
answer = input("\nenter your option: ").lower()
if answer=='a':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n16. What does pip stand for python?')
print("""your options are:
        a) Pip Installs Python
        b) Pip Installs Packages
        c) Preferred Installer Program
        d) All of the mentioned""")
answer = input("\nenter your option: ").lower()
if answer=='c':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n17. Which of the following is true for variable names in Python?')
print("""your options are:
        a) underscore and ampersand are the only two special characters allowed
        b) unlimited length
        c) all private members must have leading and trailing underscores
        d) none of the mentioned""")
answer = input("\nenter your option: ").lower()
if answer=='b':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print("""\n18. What are the values of the following Python expressions?

 2**(3**2)
 (2**3)**2
 2**3**2""")
print("""your options are:
        a) 512, 64, 512
        b) 512, 512, 512
        c) 64, 512, 64
        d) 64, 64, 64""")
answer = input("\nenter your option: ").lower()
if answer=='a':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print('\n19. Which of the following is the truncation division operator in Python?')
print("""your options are:
        a) |
        b) //
        c) /
        d) %""")
answer = input("\nenter your option: ").lower()
if answer=='b':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print("""\n20. What will be the output of the following Python code?

l=[1, 0, 2, 0, 'hello', '', []]
list(filter(bool, l))""")
print("""your options are:
        a) [1, 0, 2, ‘hello’, ”, []]
        b) Error
        c) [1, 2, ‘hello’]
        d) [1, 0, 2, 0, ‘hello’, ”, []]""")
answer = input("\nenter your option: ").lower()
if answer=='c':
    score += 1
    print('correct!')
else:
    print('incorrect!')
print("-------------------------------------------------------------------")
print("\n----------------Congrats you completed the Quiz!!-----------------")
print("\n------------------Your got",score,"/",total,"questions right-----------------")

percentage = (score/total)*100

print("\n----------------------your score is:",percentage,"-------------------------")

if score==20:
    grade = 'AWESOME!!'
elif score<20 :
    grade = 'GREAT!'
elif score<18 :
    grade = 'GOOD!'
elif score<15 :
    grade = 'PASSED'
else:
    grade = 'NOOB -_-'

print("\n-------------------------YOU ARE",grade,"---------------------------")

#Answer: cdbcadaabbbdcdacbabc
