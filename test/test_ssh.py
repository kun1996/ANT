from ant import Client

if __name__ == '__main__':
    data = Client('BASE').exec()
    print(data)
