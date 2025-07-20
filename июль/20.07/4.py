class Parent1:
    def say(self):
        print("Hello from Paren1")

class Parent2:
    def sleep(self):
        print("Zzzzzz")

class Child(Parent1, Parent2):
    pass

c = Child()

c.say()
c.sleep()