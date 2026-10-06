# type() Function 
# x="Sam"
# print(type(x))
# y=type(x)
# print(y)
# .........................................
# Multiple values to multiple variables

# a=12
# b=13
# c=14
# print(a,b,c)
# a,b,c=12,13,14
# print(a,b,c)
# ...........................................
# One value to multiple variables
# a=12
# b=12
# c=12
# print(a,b,c)
# a=b=c=12
# print(a,b,c)
# .........................................
# formatted String
# name="Sam"
# course="BCA"
# section="D"
# Room=109
# print(f"My name is {name}. I am from {course} course section {section}. The class is in room number {Room} ")
# ............................................................
# Mathematical Operators 
# a=4
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b)
# .......................................................
# maths=34
# science1_marks=12
# # 1englisghmarks=55  #error 
# englisghmarks=55 
# # hindi@marks=67     #error
# hindi_marks=67
# # print(hindi_marks, hindi@marks)
# totalMarks=science1_marks+maths+englisghmarks+hindi_marks
# print(totalMarks)
# # print(totalMarks/4)
# avg=totalMarks/4
# print(avg)
# .........................................................
# comparison operators

# ram = "ram"
# print(5 == 5)              
# print("dam" == "dam")      
# print(5 == "5")            
# print(ram == "ram")        
# print(5 == "ram")          
# print(5 >= 5)              
# print(5 != 5)              
# print(6 == "6")            
# print(6 != "6")            
# print(6 != 7)  

# fan = 5
# a = "fan"
# b = fan
# print(a == b)    
# print(a != b)  

# Problem 1:
# sunil_marks = 36; passing_marks = 35;
# Check whether Sunil is passed or not, where the passing mark is 35
sunil_marks = 33
passing_marks = 33
print(sunil_marks >=passing_marks)
# ..................................
# Problem 2:
# sunil_marks = 34; passing_marks = 35;
# Check whether Sunil failed or not, where the passing mark is 35
sunil_marks = 35
passing_marks = 35
print(sunil_marks < passing_marks)

# ..................................
# Problem 3:
# Those customers will be eligible for the amazon discount
# whose spending is equal to or above 4000.
# Check whether a customer Sam is eligible for a discount or not
# Sam_Spendings = 4500