class SchoolMember:
    '''Represents any school member.'''
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print 'Initialized schoolmember: {}'.format(self.name)
        
    def tell(self):
        '''Tell my details.'''
        print 'Name: {}, Age: {},'.format(self.name, self.age),
                
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print 'Initialized teacher: {}'.format(self.name)
        
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: {:d}'.format(self.salary)
    
        
class Student(SchoolMember):
    '''Represents a student.'''
    
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print 'Initialized student: {}'.format(self.name)
        
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: {:d}'.format(self.marks)

t = Teacher('Dr. X', 44, 134000)
s = Student('DG', 24, 70)

# prints a blank line
print

members = [t, s]

for member in members:
    member.tell()

