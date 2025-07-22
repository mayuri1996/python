from custom_exception import checkNumCustomException


def devide(num):
    result = None
    try:
        result = 100/num
        if num < 20 :
            raise checkNumCustomException(num) # use raise for custom exception
    except ZeroDivisionError :
        print(f"divide by 0 not allow")
    except checkNumCustomException as e:
        print(f"{e}")
        result = None
    finally:
       print(f"result is = {result}")