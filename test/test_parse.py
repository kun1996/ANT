from ant.parse import Parse


if __name__ == '__main__':
    s = '''>>>ips:123456<<<
    >>>asd:asdadasf
<<<
    >>>asd:asdadasf
asd s 
<<<
    '''
    p = Parse(s)
    d = p.parse()
    print(d)