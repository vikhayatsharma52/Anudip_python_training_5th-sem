#WAP TO INPUT A SENTENCE AND DISPLAY THE FREQUENCY OF VOWEL WHICH ARE PRESENT IN THE GIVEN SENTECNCE

string = str(input("enter the string"))
count = 0
for ch in string:
     if ch in "AEIOUaeiou":
         count = count+1
         print("the frequency of vowel is present:")
