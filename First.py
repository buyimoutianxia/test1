class Base(object):
    def __init__(self):
        print('Base create');
class childA(Base):
    def __init__(self):
        print('enter A ');
        # Base.__init__(self)
        super(childA, self).__init__()
        print('leave A');
class childB(Base):
    def __init__(self):
        print('enter B ');
        # Base.__init__(self)
        super(childB, self).__init__()
        print('leave B');
class childC(childA, childB):
    pass
c = childC()