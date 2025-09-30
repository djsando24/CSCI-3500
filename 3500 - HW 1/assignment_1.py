class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show(self):
        print(self.name, "-", self.grade)

#in this section I will make student objects
isaiah = Student("Isaiah", 85)
brandon = Student("Brandon", 90)
dj = Student("DJ", 78)

#call method
isaiah.show()
brandon.show()
dj.show()
