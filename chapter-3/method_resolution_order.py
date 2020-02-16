class A:
    def which_class(self):
        print('A')


class B(A):
    def which_class(self):
        print('B')


class C(B, A):
    def which_class(self):
        # super().which_class() # will call 'which_class' method from class B
        B.which_class(self)
        A.which_class(self)
        print('C')


print(C.mro())
c = C()
c.which_class()
