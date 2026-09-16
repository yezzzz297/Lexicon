
course_name = "Python Fundamentals"

def make_local_variable():
   
    course_name = "Python"
    print("Inside the function:", course_name)


print("Before calling the function:", course_name)
make_local_variable()
print("After calling the function:", course_name)

