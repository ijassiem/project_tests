

class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, telno):
        self.first = first
        self.last = last
        self.telno = telno
        self.email = self.first + '.' + self.last + '@gmail.com'

    def set_firstname(self, name):
        self.first = name
        self.email = self.first + '.' + self.last + '@gmail.com'

    def get_firstname(self):
        return self.first

    def get_lastname(self):
        return self.last

    def set_lastname(self, name):
        self.last = name
        self.email = self.first + '.' + self.last + '@gmail.com'
        
    def set_telno(self, num):
        self.telno = num
        return self.telno

    def get_telno(self):
        return self.telno

    def display_all(self):
        print("-----------------")
        print("First name:", self.first)
        print("Last name:", self.last)
        print("Tel no:", self.telno)
        print("Email:", self.email)
        print("-----------------")

#########################################################################################################################################        

x = Employee("Janet","Jackson","021")

y = Employee("Tom","Cruise","011")

x.display_all()
y.display_all()

x.set_firstname("Alan")
x.set_telno("031")

y.set_firstname("Bill")
y.set_lastname("Gates")
y.set_telno("083")

print(x.get_lastname())
print(y.get_lastname())
print(y.get_telno())

x.display_all()
y.display_all()

 
