
class Person:
    pass


class Student(Person):
    pass


class GroupLeader(Student):
    pass


person = Person()
student = Student()
leader = GroupLeader()

pairs = [
    (person, Person),
    (person, Student),
    (person, GroupLeader),
    (student, Person),
    (student, Student),
    (student, GroupLeader),
    (leader, Person),
    (leader, Student),
    (leader, GroupLeader)
]

print("isinstance:")
for obj, cls in pairs:
    print(f"{obj.__class__.__name__} -> {cls.__name__}: {isinstance(obj, cls)}")

print("\nissubclass:")
classes = [Person, Student, GroupLeader]

for cls1 in classes:
    for cls2 in classes:
        print(f"{cls1.__name__} -> {cls2.__name__}: {issubclass(cls1, cls2)}")

print("\nMRO:")
print(GroupLeader.__mro__)
