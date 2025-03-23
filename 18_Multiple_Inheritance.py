#Multiple Inheritance
'''Real Life Example :

1. Create multiple inheritance on teacher,student and youtuber.
Q. if we have created teacher and now one student joins master degree with becoming teacher then what??

Ans :  just make subclass from  teacher so that student will become teacher'''
class teacher():
    def teach(self):
        print("teacher teach the students")
class student(teacher):
    def learn(self):
        teacher.teach(self)
        print("student learn from the teacher")
s= student()
s.learn()

'''2. Now student is teacher as well as youtuber then what???
-just use multiple inheritance for these three relations'''
class teacher():
    def teach(self):
        print("teacher teach the students")
class youtuber():
    def shoots(self):
        print("youtuber makes video that uploaled on the YT")
class student(teacher,youtuber):
    def learn(self):
        teacher.teach(self)
        youtuber.shoots(self)
        print("student learn from the teacher")
s= student()
s.learn()