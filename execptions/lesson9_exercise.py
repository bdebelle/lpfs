"""
Exception Handling exercise

Create a dictionary 'car'
creat 3 keys
    -make
    -model
    -year

try to access the color key. remember, we never create the color key, so its going
to throw and exception. You need to handle the exception using the try except and finally block
"""
def colorKey():
    car = {'make': 'bmw' , 'model': '550i' , 'year': '2018'}
    try:
        print(car['color'])
    except:
        print("that key does not exist")
    finally:
        print("Please try a different key")

colorKey()