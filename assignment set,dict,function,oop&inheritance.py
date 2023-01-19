#01. A = { ? } , B = { ? } apply  set union:

setA = {55, 6, 8, 9, 11}
setB = {44, 55, 89,54}
x = setA.union(setB)
print(x)



#02. Which data type not allow duplicate item.Give an example:
# Basically Set & Dictionery data types are not allow duplicate values.
# But now I will give example of sets:

user_command = int(input("How much element you want to add: "))

setX = set({})
for i in range(user_command):
    set_ele = input("Enter Set Element: ")
    setX.add(set_ele)
print("This is Your set ",setX)




#03. Print Dictionary Keys:
st_detais = {
    "Name": "Md Naism",
    "Id No": "AP10",
    "University": "South East University",
    "Dept": "CSE"
}

st_detais["Field"] = "Machine Learning"
st_detais["Result"] = ["Passed, CGPA- 3.75"]
st_detais.update({"Id No":"AP11"})
print(st_detais.keys())





#04. Create a function & call the function:
def f_function(x,y):

    print("this is result",x+y)

def addTownumber(x, y):
    sum = x + y
    print(sum)

def subTownumber(x, y):
    sub = x - y
    print(sub)

def message():
    print("No Parameter")

f_function(5,10)
addTownumber(10,100)
subTownumber(40,15)
message()






#05. Create Class & Object:

class Student:

    def __init__(self,id,gpa):
        self.id = id
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.id}, GPA: {self.gpa}")


obj1 = Student(1015,5.00)
obj1.display()






#06. Example of Inheritance:

class Mainclass:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

    def area(self):
        pass

class Triangle(Mainclass):
    def area(self):
        area = 0.5 * self.value1 * self.value2
        print("this is triangle area: ",area)

class Rectangel(Mainclass):
    def area(self):
        area = self.value1 * self.value2
        print("thid is rectangle area: ",area)


obj1 = Triangle(5,6)
obj1.area()

obj2 = Rectangel(10,5)
obj2.area()



#Thanks for read my code patiently.If You notice any mistake>
#plaease inform me i will solve as soon as possible.

