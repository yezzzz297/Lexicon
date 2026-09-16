
def show_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
        
show_profile(name="Ada", age=20, city="London")
