def sum():
    while True:
        try:
            num_1=int(input('Please enter the first number'))
            num_2=int(input('Please enter the second number'))
            return num_1/num_2
        except ValueError as error:
            print(f'Please enter a valid number ! {error}')
            continue
        except ZeroDivisionError as error:
            print(f'Please enter value greater then 0 {error}')
            break
        except:
            print('something went wrong')
        else:
            print('Thanks you very much !')
        finally:
            print('We are done here')
        print('Nothing went wrong!')

if __name__ == '__main__':
    print(sum())