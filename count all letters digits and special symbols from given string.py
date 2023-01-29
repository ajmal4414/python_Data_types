# count all letters digits and special symbols from given string

str1="p@#$yn26at^i5ve"
alphabet=0
digit=0
special_symbols=0
for j in str1:
    if j.isalpha():
        alphabet=alphabet+1
    elif j.isdigit():
        digit=digit+1
    else:
        special_symbols=special_symbols+1

print("alphabet is" ,alphabet)
print("digit is",digit)
print("special_symbols is", special_symbols)

