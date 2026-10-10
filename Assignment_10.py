#convert your  full name into initial name
full_name=input("Enter Your name: ").strip().upper()
splitted_name=(full_name.split())
first_name=splitted_name[0]
last_name=splitted_name[-1]
Initial=splitted_name[0][0]+splitted_name[-1][0]
print(splitted_name)
print(f"Your name initial is {Initial}")



