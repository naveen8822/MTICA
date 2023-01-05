class A:
    def first_method(self):
        print('Method of class A...')
class B:
    def first_method(self):
        print('method of class B...')
class C(A,B):#B,A
    def third_method(self):
        print('method of class C...')


if __name__=='__main__':
    ob=C()
    ob.first_method()
    ob.third_method()
    #C().third_method()
