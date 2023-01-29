# remove special symbols

str1='/* jon is @developer & musician!!'
str2=['/','*','@','&','!']

for i in str2:
    if i in str1:
        str1=str1.replace(i,'#')

print(str1)