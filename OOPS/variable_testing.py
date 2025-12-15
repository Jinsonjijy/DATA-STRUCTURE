class dog:
    species="canien"
    name="hello"
    def checking(self,age,name):
        self.age=age
        self.name=name
        if age<18:
            print("not valid")
        else:
            print("valid")
dog1=dog()
# dog.name="achu"
dog1.checking(18,"messi")
print(dog1.name)
print(dog1.age)