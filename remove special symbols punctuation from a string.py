# remove special symbols punctuation from a string

str1="/*johnis2developer&musicdirector"

string2=""
for i in str1:
    if i.isalnum() and i.isalpha():
        string2=string2+i

print(string2)
