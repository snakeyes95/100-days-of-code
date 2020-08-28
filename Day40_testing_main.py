def divide(arg1,arg2):
    try:
        total=int(arg1)/int(arg2)
        return total
    except ValueError as err:
        return err
    except ZeroDivisionError as err:
        return err
        

if __name__ == '__main__':
    print(divide('12',10))