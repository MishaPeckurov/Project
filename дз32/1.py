class A:
    def method_a(self):
        print("Метод класса A")

class B:
    def method_b(self):
        print("Метод класса B")

class C(A, B):
    def method_c(self):
        print("Метод класса C")

obj = C()
obj.method_a()
obj.method_b()
obj.method_c()