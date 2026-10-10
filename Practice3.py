class student:
    def __init__(self):
        self.name="Sourav"
        self.roll_no=34

    def update(self):
        self.name="zen"
        self.roll_no=34


sam=student()
print(sam.name)  #init function doesn't need to call
print(sam.roll_no)

rahul=student()
rahul.update()  #other function needs to call
print(rahul.name)
print(rahul.roll_no)











