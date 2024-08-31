# list , range , string
ls = [1,5,9]
strng = "Manish Soni"

for i in range(0,5):
    print("index:",i)

# for i in ls:
#     print("index:",str(i))

for i in strng:
    print(i,end="")

# print([i for i in strng])
# 2x1
# 00
# 10
# /01

for i in range(0,2):
    for j in range(0,2) :
        print("\ni:",str(i))
        print("j:",str(j))