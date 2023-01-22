from dataclasses import dataclass

@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f'Name {self.name}, GPA: {self.gpa}'

def main():
    alex = Student('Alex', 'abcdef', 3.6)
    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student('Sam', 'qwerty', 3.8)
    print(sam)

if __name__ == '__main__':
    main()