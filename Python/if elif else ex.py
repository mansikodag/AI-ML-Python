#if elif else example
#grade updating
'''
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade
'''
gr=int(input("Enter the Marks:"))
if(gr<25):
  print("Grade F")
elif(gr>=25 and gr<45):
  print("Grade E")
elif(gr>=45 and gr<50):
  print("Grade D")
elif(gr>=50 and gr<60):
  print("Grade C")
elif(gr>=60 and gr<=80):
  print("Grade B")
else:
  print("Grade A")
