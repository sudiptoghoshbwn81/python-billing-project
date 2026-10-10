# prints it in reverse order (last name, first name).
# Then, count and display the total number of characters in the full name.
# Finally, extract and display the initials of the first and last names.
name=input("Enter Your Full name: ").strip().title()
spiltted_name=name.split()
reverse_list=spiltted_name[::-1]
reverse_name=reverse_list[0]+" "+reverse_list[-1]
join_reverse_name="-".join(reverse_list)
count_of_punctuations=(name.count(" ")+name.count(".") + name.count(",")
                               + name.count("!") + name.count("?") + name.count(";") + name.count(":"))
length_of_name=len(name)
count_total_no_of_character=length_of_name-count_of_punctuations
print(spiltted_name)
print(reverse_name)
print(f"Hi is your name in reverse order {reverse_name}")
print(f"Hi is your name in reverse order {join_reverse_name}")
print(f"The no of character of your name: {count_total_no_of_character}")
print(name.index('i'))