from ant import Flow, Node, IfNode, StartNode, StopNode, Client

if __name__ == '__main__':
    e = StopNode(None, None)

    n4 = Node(Client('IF_FALSE'), e)
    n3 = Node(Client('IF_TRUE'), e)
    n2 = IfNode(Client('IF'), [('=', 'true', n3), ('!=', 'true', n4)])
    n1 = Node(Client('BASE', context={'c': 'bbb'}), n2)
    s = StartNode(None, n1)

    f = Flow(s, ctx={'c': 'ccc'})
    f.run()
