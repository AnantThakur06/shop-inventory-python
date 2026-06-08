try:
    number = int(input(f"Enter a number :  "))
    result = 100 / number 

except ValueError:
    print(f"Please enter a valid number.")

except ZeroDivisionError:
    print(f"Error: cannot divide by zero.")

else:
    print(f"Result: {result}")
    
# 2nd 

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Index does not exist")
except ValueError:
    print("Wrong value")
finally:
    print("Done")

# this is a index error not a value one so "index does not exist" and finally will execute so done will also print 

