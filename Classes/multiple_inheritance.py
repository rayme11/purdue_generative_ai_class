class Base1:
    def method_base1(self):
        return "Method from Base1"  
class Base2:
    def method_base2(self):
        return "Method from Base2"
class Derived(Base1, Base2):
    def method_derived(self):
        return "Method from Derived"
obj = Derived()
print(obj.method_base1())  # Output: Method from Base1
print(obj.method_base2())  # Output: Method from Base2
print(obj.method_derived())  # Output: Method from Derived