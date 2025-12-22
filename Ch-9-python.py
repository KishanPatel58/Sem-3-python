# CH (9) Advance Oop Concept :-

# single or simple level inheritance.
# class Parent:
#     def f1 (self):
#         print("This is parent class.")
# class Child (Parent): 
#     def f2 (self):
#         print("This is child class.")
# ob = Child()
# ob.f2()
# ob.f1()

# multi level inheritance.
# class grandparent:
#     def gp (self):
#         print("This is Grand Parent.")
# class Parent (grandparent):
#     def f1 (self):
#         print("This is parent class.")
# class Child (Parent):
#     def f2 (self):
#         print("This is child class.")
# ob = Child()
# ob.f2()
# ob.f1()
# ob.gp()

# class grandparent:
#     def gp (self):
#         print("This is Grand Parent.")
# class Parent (grandparent):
#     def f1 (self):
#         print("This is parent class.")
# class Child (Parent):
#     def f2 (self):
#         print("This is child class.")
# ob = Parent()
# ob.f2()
# ob.f1()
# ob.gp()

# class grandparent:
#     def gp (self):
#         print("This is Grand Parent.")
# class Parent (grandparent):
#     def f1 (self):
#         print("This is parent class.")
# class Child (Parent):
#     def f2 (self):
#         print("This is child class.")
# ob = grandparent()
# ob.f2() # give error
# ob.f1() # give error
# ob.gp()

