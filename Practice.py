class student():
    def __init__(self,roll_no,name,address,ph_no):
        self.roll_no=roll_no
        self.name=name
        self.address=address
        self.ph_no=ph_no

    def display(self):
        print("Roll No",self.roll_no)
        print("Name", self.name)
        print("address", self.address)
        print("ph_no", self.ph_no)

print("Main program starts from here: ")
students_num=int(input("How many students are there: "))
student_obj_dict={}
for i in range(students_num):
    print(f"Enter the details of student no {i+1}")
    roll_no=input("Enter the student roll_no: ")
    name=input("Enter the student name: ")
    address=input("Enter the student address: ")
    ph_no=input("Enter the student ph_no: ")
    obj_name="student"+str(i+1)
    student_object=student(roll_no,name,address,ph_no)
    student_obj_dict[obj_name]=student_object

res=input("if you want to see details for any particular student press 'p' or press 'a' for all students: ").lower()
if res=="p":
   roll_no=input("Enter the roll no: ")
   for s in student_obj_dict.values():
       if s.roll_no==roll_no:
           print("Here is the details")
           s.display()

elif res=="a":
    for s in student_obj_dict.values():
        print("Here are the details..")
        s.display()
else:
    print(" Wrong Input..Try again")













