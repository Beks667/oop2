class Human:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан Human: {0})'.format(self.name))
    def tell(self):
        
        print('Имя:{0} Возраст:{1}'.format(self.name, self.age))

class Teacher(Human):
    
    def __init__(self, name, age,speciality, salary,favorite_lesson):
        Human.__init__(self, name, age)
        self.speciality = speciality
        self.salary = salary
        self.favorite_lesson =favorite_lesson
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        Human.tell(self)
        print('speciality:"{0}"'.format(self.speciality))
        print('Зарплата: "{0}"'.format(self.salary))
        print('favorite lesson:{0}'.format(self.favorite_lesson))
        

class Student(Human):
    
    def __init__(self, name, age, grade,favorite_lesson):
        Human.__init__(self, name, age)
        self.grade = grade
        self.favorite_lesson = favorite_lesson
        print('(Создан Student: {0})'.format(self.name))

    def tell(self):
        Human.tell(self)
        print('Оценки: "{0:d}"'.format(self.grade))
        print("favorite lesson:{0}".format(self.favorite_lesson))

t = Teacher("Sergey",40,"pyThon", 30000,'Python')
s = Student('Swaroop', 25, 75,"python")

print() # печатает пустую строку
t.tell()
s.tell()

