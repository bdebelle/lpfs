'''
more exception errors
'''

def exceptionHandling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) / c
        print(d)
    except:
        print("in the except block")
        raise Exception("this is an exception")
    else:
        print("Because there was no exception, 'else' is executed")
    finally:
        print("Finally, always executed")

exceptionHandling()