
def count_items():
   
    counter = 1
    counter += 1
    print("Inside the function:", counter)

count_items()

print("Trying to use counter outside the function:")
try:
    print(counter)
except NameError:
    print("counter does not exist outside the function.")


