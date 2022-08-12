# TODO :Create a Boolean variable named x
x = True

# TODO :Create an integer variable named y
y = 1907

# TODO :Create a float variable named z
z = 85.45

# TODO :Create a string variable names s
s = "JFT74"

# TODO :Convert the int variable to float
F = float(y)

# TODO :Can we convert the str to int ? >>> Yes and no
# Yes  :when strange contain number
s = "10"
n = int(s)
# no   :when str contain words
s = "Hello"
#n = int(s) # will produce an error

# TODO :Create a list of numbers from 1 to 5
my_list = [1, 2, 3, 4, 5]
print(my_list)

# TODO :Create a Tuple of numbers from 10 to 15
my_tuple = (10, 11, 12, 13, 14, 15)
print(my_tuple)

# TODO :Convert the list to tuple
my_list_2_tuple = tuple(my_list)
print(type(my_list_2_tuple))

# TODO :Create a dict of 3 values
my_dict = { 1 : "Ali", 2 : "Mohammed", 3 : "Khaled" }

'''
Can we use semi colon ; with python
>>> No

Python is interpreted or compiled ?
>>> Interpreted
'''
# What is the differences between low level & high level?
'''
>> Low Level Language that the computer undersatnd with out compiler
>> Hige Level Language is what programmer use with intermidate language to inateract with the comoputer
'''
# What is the differences between = , == , !=
'''
= >>>> "equal" is an equal sign that assign the value to the variable

== >>> "is equal" check if the value in the rigth equal to the value of the left
        variable or value

!= >>> "is not equal" check if the value in the rigth not equal
        to the value of the left variable
'''
# What is the operator precedence
'''
PEMDAS
Parenthese
Exponents
Multipication
Division 
Addition
Subtraction
'''
'''
● Create a variable x with value of 10
● Increase x value by 15 using assignment operators
● Divide the x value by 5 using assignment operators
● Multiply the x value by 10 using assignment operator
● Get module of x on 3 using assignment operators
 x = 10
 x += 15
 x /= 5
 x *=10
 x %= 3
'''
# TODO :print the module of 11 to 4 ,exponent of 2,3
print(11%4)
print(2**3)

# TODO :Divide 11 by 3 using python division
div = 11/3

# TODO :Can we divide 11 by 3 and get an integer number ?
div = 11//3

"""
● Check if 10 is bigger than 15 or not
● If 10 is not bigger than15 print x is smaller than 15
"""
if 10 > 15:
    pass
else:
    print("x is smaller than 15")

# In which cases we will use all
'''
when all the value pass the condition
if all[10,5,12,15,9,2] > 20
then it will be true
'''

# What is the differences between (all , and), and differences between (any ,or)
"""
>> No diffrence in meaning but in syntax there is 
>> (And , All) mean all the condition must be ture so the final result equal to ture
>> (or , any) opposite to (and ,all) that if one get true the the final result will eqal to true
"""
# If we need all the conditions to be true we will use >> all

# What is the differences between if , elif
# What is the differences between elif else          
'''
we start with if for the firt condition
on the other conditions we use elif
if all condition get false the else will be excuted
'''
# Can we use more than one elif >>> yes
# Can we use more than one else >>> no

# write s simple ternary operator
print("True") if x>5 else print("false")

"""
in elif , python will check all the conditions no matter what ? >> no it will stop check when on condition comes true

in elif we use else for ... ? >> when all condiction comes false"""

"""
● if we have this list [2,4,6,8,10] :
## check to see if 4 in this list or not
#>>
lis_t = [2,4,6,8,10]
if 4 in lis_t:
    print("4 in the list")

## check to see if 4 and 6 in this list on not
#>>
if all[4,6] in lis_t:
    print("4, 6 in the list")

## check to see if 3 or 6 in this list
#>>
if any[3,6] in lis_t:
    print("3 or 6 in the list")
    
## check to see if 2 , 4 and 5 in this list
#>>
if all[2, 4, 5] in lis_t:
    print("2, 4 and 5 in the list")
"""
