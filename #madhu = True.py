#madhu = True
#while (madhu):
 #   num1 = input("Enter the first Number: ")
  #  num2 = input("Enter the second Number: ")
   # operation = input("Operation: ")
    #if num1 != 'q' and num2 != 'q' and operation != 'q':
     #   num1 = int(num1)
      #  num2 = int(num2)
       # if operation == '+':
        #    print(num1 + num2)
        #elif operation == '-':
           # print(num1 - num2)
        #elif operation == '*':
            #print(num1 * num2)
        #elif operation == '/':
            #print(num1 / num2)
        #else:
         #   print("Error in your input please cross-check")
   # else:
     #   madhu = False
     #   print("Found q in input Exiting the program.")



#list_b= [10,30,'madhu',True,3.3]
#list_b.insert(10,122)
#print(list_b)
#list_b.remove(122)
#print(list_b)
#list_b.pop()
#print(list_b)
#list_b.remove(True)
#print(list_b)

#creating calculator using functions
def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    return(x/y)

num1= eval(input("enter the first number:"))
num2= eval(input("enter the second number"))

print("select the option")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

while(True):
    choice= int(input("enter the choice from (1/2/3/4/5)"))
    if choice in (1,2,3,4,5):
        if choice==1:
            print("addition of two number",num1,"and",num2,"is->",add(num1,num2))
        elif choice == 2:
            print("substraction of two number", num1, "and", num2, "is->", subtract(num1, num2))
        elif choice == 3:
            print("multiplication of two number", num1, "and", num2, "is->", multiply(num1, num2))

        elif choice == 4:
            print("division of two number", num1, "and", num2, "is->", divide(num1, num2))

    elif choice == 5:
        exit("thank you:")
        print()


    else:
        print("invalid choice try again")


















