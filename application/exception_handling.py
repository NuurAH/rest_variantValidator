#Define my custom error
class myZeroDivisionError(Exception):
    pass

#Use an exception block to capture a known error
try:
    print(1/0)
except ZeroDivisionError as e:
    """"Once the exception is caught, the custom exception is caught
    this can be raised with a better value"""""
    error = "The warning is trying to tell you that is illegal to divide something by zero" % str(e)
    raise myZeroDivisionError(error)