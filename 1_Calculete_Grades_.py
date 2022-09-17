def grade(sname,mark):
    #print("Student name is :",sname)
    if mark>=90 and mark<=100:
        print('\n',sname,"'s Grade is A")
    elif mark>=80 and mark<=89:
        print('\n',sname,"'s Grade is B")
    elif mark>=70 and mark<=79:
        print('\n',sname,"'s Grade is C")
    elif mark>=60 and mark<=69:
        print('\n',sname,"'s Grade is D")
    elif mark>=0 and mark<=59:
        print('\n',sname,"'s Grade is E")
    else:
        print("\n Enter the valid mark")

def tot_avg(mark1):
    if mark1>=90 and mark1<=100:
        print("\n The average grade of all the students in the class is : A ")
    elif mark1>=80 and mark1<=89:
        print("\n The average grade of all the students in the class is : B ")
    elif mark1>=70 and mark1<=79:
        print("\n The average grade of all the students in the class is : C ")
    elif mark1>=60 and mark1<=69:
        print("\n The average grade of all the students in the class is : D ")
    elif mark1>=0 and mark1<=59:
        print("\n The average grade of all the students in the class is : E ")
    else:
        print("\n Enter the valid mark")
        
n=int(input("\n Enter how many students :"))
tot=0

for i in range(n):
    names=input("\n Enter the name :")
    maark=int(input("\n Enter the mark :"))
    tot=tot+maark
    avg=int(tot/n)
    grade(names,maark)

#print('Total is : ',tot)
#print("Average is :",avg)

tot_avg(avg)