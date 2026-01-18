#Py_Calc

print("                         Welcome to PYTHON_CALCULATOR                  \n\n           ")

print("1)  +")
print("2)  -")
print("3)  *")
print("4)  /")

op=input("Choose an operator : ")
while op not in ["1","2","3","4"]:
    print("Enter a valid Operator : ") 
    op=input("Choose an operator : ")

if op=="1" :
    print("Enter two digits for sum ")
    s1=int(input("Enter 1st no : "))
    s2=int(input("Enter 2nd no : "))
    sum=s1+s2
    print("Sum=",sum)


elif op=="2" :
    print("Enter two digits for subtract ")
    su1=int(input("Enter 1st no : "))
    su2=int(input("Enter 2nd no : "))
    sub=su1-su2
    print("Subtraction=",sub)

elif op=="3" :
    print("Enter two digits for subtract ")
    pr1=int(input("Enter 1st no : "))
    pr2=int(input("Enter 2nd no : "))
    pro=pr1*pr2
    print("Multiple=",pro)

    
elif op=="4" :
    print("Enter two digits for subtract ")
    div1=int(input("Enter 1st no : "))
    div2=int(input("Enter 2nd no : "))
    di=div1/div2
    print("Division=",di)
    
else :
    print("invalid operator")
    
    


