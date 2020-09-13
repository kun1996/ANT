from ant import Flow

if __name__ == '__main__':
    f = Flow('BASE', 'BASE2', ctx={'c': 'ccc'})
    f.run()
