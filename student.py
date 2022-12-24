student=[[4,'arshad',77,89],[5,'arun',81,86],[13,'gangully',82,79],[39,'naveen',77,80],[45,'prathap',76,86]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
