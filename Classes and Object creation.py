class Dog:
    attr1="mammal"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("bark")

obj = Dog("pappu")
print(obj.attr1)
print(f"the name of the dog is {obj.name}")
obj.speak()
