a = int(input())
b = int(input())

x = a*((b%100)%10)
y = a*((b%100)//10)
z = a*(b//100)
result = a*b

print(x,y,z,result, sep='\n')