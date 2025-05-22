name=input("Enter your full name:")
age=int(input("Enter your age:"))
student_Id=input("Enter your student id:")
fav_subject=input("Enter your favorite subject:")
math_score=int(input("Enter your math score out of 100:"))
science_score=int(input("Enter your science score out of 100:"))
english_score=int(input("Enter your english score out of 100:"))

sub_average=int(math_score+science_score+english_score)/3
print("Average of the three scors is:" +str(sub_average))
grade=0-100
if grade < 60:
    print("Grade F")

elif grade <=69:
    print("Grade D")
elif grade  <= 79:
    print("Grade C")
elif grade <= 89:
    print("Grade B")
else:
    print("Grade A")
    print("--------------------")

    print("Student Report")
    print("Name",name)
    print("Age:",age)
    print("Student ID:", stude,fav_subject)

    print("Average Score:",sub_average)
    print("Grade:",grade)
 