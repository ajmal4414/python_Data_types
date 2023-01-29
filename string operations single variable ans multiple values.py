#string operations single variable multiple values

#len()
a1=("uk","uae","germany","ireland")
print(len(a1))

#concatenation
a1=("uk","uae","germany","ireland")
a2=("japan",)
print(a1+a2)
print(a1)

#slicing tuple
print(a1[2:4])
print(a1[-2:-3:-1])

#remove
mytuple=("uk","uae")
w=list(mytuple)
w.remove("uk")
mytuple=tuple(w)
print(mytuple)

#print each item on a list

for i in range(len(a1)):
    print(a1[i],i)

# print same items using * operations
a5=a1*1
print(a5)
#index and count
print(a5.count("uk"))
print(a5.index("germany"))