# functions

def exc1():
    print(" List ===")
    
    colors = ["white", "black"]
    print(colors)
    
    # add elements
    colors.append("red")
    colors.append("blue")
    
    #read elements
    print(colors[0])
    print(colors[2])
    
    # travel with for loop
    for color in colors:
        print(color)
    
    
    def exc2():
        numbers = [123,483,37,21,56,34,251,63,451,456,378,83,65,934, 100, 472]
    
        # 1 print every number
        for num in numbers:
            print(num)
            
        print("--------------")
        # 2 print how many elements there are in the list
        count= len(numbers)
        print("There are" + str(count) + "numbers in the list")
        
        print("-------------")
        #3 sum all numbers
        # 4 how many numbers are greater than 250?
        #5 how many are equal or lower than 100
        
        total = 0
        count = 0
        count_lower = 0
        for num in numbers:
            total+= num
            
            if num > 250:
                count += 1
                
            if num <= 100:
                count_lower += 1    
            
            print(total)
            print(count)
            print(count_lower)
            
            
            
            
def  how_many_times(color): 
       colors = ["Red", 'yEllow', "BLUE", "RED", "GreeN", "YELLOW", "reD", "green"]
       # parse color to lowercase
       # for loop 
       # if color in lower is equal to cl in lower
       # increase count
       count = 0
       for cl in colors:
           if cl.lower() == color.lower:
              count += 1
       print("There are " + "occurrences of " + color)
    
# call the fns
#exc1()
#exc2 ()

how_many_times("red")
how_many_times("GREEN")