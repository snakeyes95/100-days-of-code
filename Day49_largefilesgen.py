def file_gen(filepath):
    for row in open(filepath,'r',encoding='utf-8'):
        print('------- --------')
        yield row


if __name__ == "__main__":
    result=file_gen('./sample.txt')
    print(result)
    for row in result:
        print(row)