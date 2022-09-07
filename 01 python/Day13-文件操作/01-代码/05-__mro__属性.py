class A(object):
    pass


class B(object):
    def foo(self):
        print('我是B类里的foo方法')


class C(A):
    def foo(self):
        print('我是C类里的foo方法')


class D(B):
    pass


class E(object):
    pass


class X(C, D, E):
    pass


x = X()
x.foo()
print(X.__mro__)
