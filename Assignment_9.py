## Taking a string as input and counts the number of occurrences of a specific character entered by the user
para=input("Please enter your paragraph or sentence: ").lower().strip()
sp_char=input("Please enter your specific character which you want to search: ").lower().strip()
result=para.count(sp_char)
if result>1:
    print(f"Your word {sp_char} occurs {result} times ")
elif result==1:
    print(f"Your word {sp_char} occurs {result} time")
else:
    print(f"Your word or letter does not exist in main paragraph")