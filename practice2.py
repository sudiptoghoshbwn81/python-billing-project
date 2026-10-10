class student():
    def __init__(self,roll_no,name,address,ph_no):
        self.roll_no=roll_no
        self.name=name
        self.address=address
        self.ph_no=ph_no

    def display(self):
        print("Roll Number", self.roll_no)
        print("Name",self.name)
        print("address",self.address)
        print("Ph_no",self.ph_no)

print("Main program starts here......")

student_obj_list=[]
student_num=int(input("How Many students are there: "))
for i in range(student_num):
    input(f"Enter the student sr. no {i+1}")
    roll_no=input("Enter the roll no: ")
    name=input("Enter the student name: ")
    address=input("Enter the address: ")
    ph_no=input("Enter the ph_no: ")

    student_obj=student(roll_no,name,address,ph_no)
    student_obj_list.append(student_obj)

print("\nstudent_details")

for s in student_obj_list:
    s.display()
