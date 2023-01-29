# string operations single variable  single value
#string concatenation
str1="your favorite fruit"
str2=" is pineapple"
print(str1+str2)

#methods
#capitalize method
a1="your favorite fruit is pineapple"
print(a1.capitalize())
#upper method
print(a1.upper())
#lower method
print(a1.lower())
#count method
print(a1.count('a'))
#center
print(a1.center(50))
#find
print(a1.find("pineapple"))
#endswith
print(a1.endswith('e'))
#format
a2="hello {name} welcome to the shop which type of mobile you want? i want this model,{mobile}"
print(a2.format(name="MUHAMMED AJMAL S",mobile="samsung"))
#isalpha
print(a1.isalpha())
#isalnum
print(a1.isalnum())
#isascci
print(a1.isascii())
#isdecimal
print(a1.isdecimal())
#isdigit
print(a1.isdigit())
#isupper
print(a1.isupper())
#islower
print(a1.islower())
#partition
print(a1.partition("pineapple"))
#replace
print(a1.replace("pineapple","orange"))
#lstrip
a4="travelling"
a=a4.lstrip()
print("i love",a,)
#rfind
print(a1.rfind('t'))
#zfill()
r3="8"
print(r3.zfill(6))