# -*- coding:utf-8 -*-


def fun(n):
    '''
    aaaa
     bbbb
     ccc
    '''
    def fun1(x):
        return x + n;
    return  fun1;

f = fun(40);

print(f(1))
print(fun.__doc__)

def f(ham:str , egg:str='egg')->str:
    print('Annotation:' , f.__annotations__);
    print('Arguments:',ham , egg);

f('spam')