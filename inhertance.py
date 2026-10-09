#pormophysim,,Encapsulpsion,,Abtsraction
class Animal:
# class can hae both variable and method
#the dog and cat inherts from class animal
    ismammal=True
    hasfur=True
class Dog(Animal):
    def bark(self):
        print("woof!!woof!!")
class cat(Animal):
    def meow(self):
        print("meows!!meow!!meow!!")
#object--variable
d = Dog()
d.bark()
print(d.ismammal)

c= cat()
c.meow()
print(c.ismammal)

