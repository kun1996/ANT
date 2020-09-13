if __name__ == '__main__':
    print(str(bytes('''\r\n
    123'''.replace('\r\n','\n'), encoding='utf-8'), encoding='utf-8'))