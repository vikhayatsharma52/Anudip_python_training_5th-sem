#wap to input a string from user and
#  count the no of char present in it without using len

strings=str(input("enter a string:"))
count=0
for ch in strings:
        count=count + 1
print("the count of characters:", count )