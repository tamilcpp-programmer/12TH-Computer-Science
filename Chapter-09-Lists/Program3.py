#Program to print the marks in each subject and the total marks
marks = [ ]
subjects=['Tamil','English','Physics','Chemistry','Comp.Science','Maths']
for i in range(6):
    m=int(input("Enter Mark = "))
    marks.append(m)
for j in range(len(marks)):
    print("{}.{} Mark= {}".format(j+1,subjects[j],marks[j]))    
print("Total Marks=",sum(marks))    