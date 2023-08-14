name ="Shane"
last_name ="Pooler"
age = 99

print(name + "  " + last_name)
print("My age is: " + str(age))


# conditionals

if age < 100:
    print("Don't worry you are still young")
    print("still inside the if")
elif age == 100:
    print("Congratulation on the century!!!")    
else:
    print("Sorry, you are getting old")    

print("outside the if")    

def say_hello():
    print("Hello from a function")
    
def sum(num1, num2):
    total = num1 + num2
    print("The result " + str(total))
    
say_hello()
say_hello()