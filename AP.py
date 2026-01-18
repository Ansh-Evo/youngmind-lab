#Arithmetic Progression Program--->
import time

print("This is a Arithmetic Progression Python Program ---->")

a=float(input("Enter first value (a) : "))

d=float(input("Enter common difference (d) : "))

n=float(input("Enter which value to find (n) : "))

formula="an=a+(n-1)*d "
for f in formula:
    print(f,end="")
    time.sleep(0.09)
si="**********"
for sin in si:
    print(sin,end="" ,)
    time.sleep(0.4)


print()  # moves cursor to new line
an=a+(n-1)*d
print("a"+(str(n)),"=",an)



