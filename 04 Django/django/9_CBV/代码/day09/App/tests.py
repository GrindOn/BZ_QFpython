from django.test import TestCase

# Create your tests here.

class Dog:
    name = '黑背'
    def run(self):
        print("run")


def go():
    print("GO")

dog = Dog()
# print(getattr(dog,'name'))
fun = getattr(dog,'run1',go)
fun()

# print(hasattr(dog,'nam2e'))