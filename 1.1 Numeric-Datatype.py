#DATA TYPES:
   #Data types are the classification or categorization of data items.
   #It represents the kind of value that tells what operations can be performed on a particular data.
   #Since everything is an object in python programming,data types are actually class and variables
        #are instance(object) of these classes.
#Following are the standard or built-in data type in python:
'''      *Numeric
         *Sequence Type
         *Boolean
         *Set
         *Dicitionary
         *Range

'''

#None :-When you have a variable and if that varaible is not assinged with any value its in none.
   #Normally we use a keyword as null in other language but in python we use none.

#1.Numeric :-
# In python,numeric data type represent the data which has numeric value can be int,float,complex.
   #1.int (Integer):
       #This Value is represented by int class.
       #It contains postive or negative whole numbers(without fraction or decimal)
       #In python there is no limit to how long an integer value can be.
    #2.float (Decimal):
       #This value is represented by float class.
       #It is a real number with floating point representation.
       #It is specified by a decimal point.
       #Optionally,the character e or E followed by a positive or negative integer may be appended to specify scientific notataion.
   #3.complex Numbers:
       #Complex Number is represented by complex class.
       #It is specified as (real part) + (imaginary part). Ex : 2+3j
a = 5
print("1.Integer:",a)
print("Type of a:",type(a))

b = 5.0
print("Float:",b)
print("Type of b:",type(b))

c = 5+3j
d=complex(5,5)
print("Complex:",c,d)
print("Type of c:",type(c))
print("Type of d:",type(d))




