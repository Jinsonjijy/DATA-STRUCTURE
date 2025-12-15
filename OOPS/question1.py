class calculation:
    res=0

    def add(self,a,b):
        self.sum=a+b
        self.res=self.sum




    def sub(self,a,b):
        self.subs=a-b
        self.res=self.subs
    def get_res(self):
        print(self.res)
        print(self.subs)

obj=calculation
obj.add(obj,2,7)
obj.sub(obj,4,5)

obj.get_res(obj)