print("STRING")
print()
'''
1.2.1 STRING:
        *In python, Strings are arrays of bytes represting Unicode characters.
        *A String is a collection of one or more characters put in a single quote,double quote or triple quote.
        *In python there is no charcter data type, a character is a string of length one.It is represented by str class.
1.Creating String:
        Strings in python can be created using single quote,double quote or even triple quotes.
'''
print("1.String Creation:")
String1 = 'String Creation using single quote'
String2 = "String Creation using double quote"
String3 = '''String Creation using triple quote'''
print(String1 ,"- type of String 1:",type(String1))
print(String2 ,"- type of String 2:",type(String2))
print(String3 ,"- type of String 3:",type(String3))
'''
2.Multi-line String
'''
print()
String4 = '''2.Multi-line 
             String'''
print(String4 ,"- type of String 4:",type(String3))

'''
3.Accessing elements of strings(Index):
        *In python,individual characters of a string can be accessed by using the method of indexing.
        *Indexing allows negatuve address references to access characters from the back of the string,
            e.g, -1 refers to the last character, -2 refers to the second last character and so on.
        *While accessing an index out of the range will cause an IndexError.
        *Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError.
'''
# Python Program to Access
# characters of String
print()
print("3.Accessing the element of string(index)")
String1 = "characters of String"
print("Initial String:",String1 )
# Printing First character
print("First character of String is:",String1[0])
# Printing Last character
print("Last character of String is:",String1[-1])
'''
4. Reversing a Python String
            *With Accessing Characters from a string, we can also reverse them. 
            *We can Reverse a string by writing [::-1] and the string will be reversed.
'''
#Program to reverse a string
print()
print("4.Reverse a string:")
rev = "Reverse String"
print("Before Reverse :",rev)
print("After Reverse :",rev[::-1])
print()
'''We can also reverse a string by using built-in join and reversed function.'''
# Program to reverse a string
# Reverse the string using reversed and join function
print("Reverse the string using reversed and join function")
revjoin = "string Reverse"
print("Before Reverse:",revjoin)
print("After Reverse: ","".join(reversed(revjoin)))
'''
5.String Slicing:
            *To access a range of characters in the String, the method of slicing is used. 
            *Slicing in a String is done by using a Slicing operator (colon). 
'''
# Python Program to
# demonstrate String slicing
# Creating a String
print()
print("5.String Slicing:")
String1 = "Slicing"
#String = "0123456"
#String = "7654321"
print("Initial String:",String1)
# Printing 3rd to 12th character
print("Slicing characters from 3-7: ")
print(String1[3:7])
# Printing characters between
# 3rd and 2nd last character
print("Slicing characters between 3rd and 2nd last character: ")
print(String1[3:-2])
'''
6.Deleting/Updating from a String:
        *In Python, Updation or deletion of characters from a String is not allowed.
        *This will cause an error because item assignment or item deletion from a String is not supported.
        *Although deletion of the entire String is possible with the use of a built-in del keyword. 
        *This is because Strings are immutable(unchangeable),
               hence elements of a String cannot be changed once it has been assigned.
        *Only new strings can be reassigned to the same name. 
'''
#Updation of a character
print()
print("6.Updation of a character")
# character of a String
String1 = "Updation"
print("Initial String:",String1)
# Updating a character of the String
## As python strings are immutable, they don't support item updation directly
### there are following two ways
#1
print("Method 1:")
print("Convert string into list:")
list1 = list(String1)
print("list before update :")
print(list1)
list1[2] = 'p'
String2 = ''.join(list1)
print("Updating character at 2nd Index d to p:")
print(list1)
print("After Updation:",String2)
#2
print("Method 2:")
print("Concatnate the string using slicing")
String3 = String1[0:2] + 'p' + String1[3:]
print(String3)
#Updating Entire String
print("Method 3:")
print("Updating Entire String")
# Python Program to Update
# entire String
String1 = "Update Str"
print("Initial String:",String1)
# Updating a String
String1 = "Update String"
print("Updated String:",String1)
#Deletion of a character
print()
print("Deletion of a character")
String1 = "Deletion"
print("Initial String:",String1)
# Deleting a character using concatnate
print("Method 1:")
print("Concatnate the string using slicing")
String2 = String1[0:3] + String1[4:]
print("Deleting character at 2nd Index:",String2)
'''
Deleting Entire String:
        *Deletion of the entire string is possible with the use of del keyword. 
        *Further,if we try to print the string, 
             this will produce an error because String is deleted and is unavailable to be printed.
'''
print("Method 2:")
print("Delete entire String using del keyword")
print("Initial String:",String1)
# Deleting a String
# with the use of del
print('''
Deletion of the entire string is possible with the use of del keyword.
Further, if we try to print the string,this will produce an error because String is deleted and is unavailable to be printed.")
''')
del String1
print("Deleting entire String:",String1)
















