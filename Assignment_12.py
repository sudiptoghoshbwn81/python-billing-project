#String Searching and Replacing

paragraph=input("Enter the paragraph: ").strip().lower()
splitted_paragraph=paragraph.split()
count_of_word=len(splitted_paragraph)
old_word=input("Enter the word which you want to replace: ").strip().lower()
new_word=input("Enter the word which you want to replace with: ").strip().lower()
new_paragraph=paragraph.replace(old_word,new_word)
print(splitted_paragraph)
print(new_paragraph)
print(count_of_word)
