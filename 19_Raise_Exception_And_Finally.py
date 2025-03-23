#Raise Exception And Finally
class AdultException(Exception):
    pass
class person(Exception):
    def __init__(self, name, age):
        self.name= name
        self.age= age
        
    def get_minor_age(self):
        if int(self.age) >=18:
            print(f"{self.name} is major because his age is {self.age}" )
        else:
            print("raise exception ")
    def display(self):
          try:
            print(f"age -> {self.get_minor_age()}")
          except AdultException:
            print("Person is an adult")
          finally:
            print(f"name -> {self.name}")

person("Geetanshu", 18).display()
person("Gaurav", 17).display()

'''
#CodeBasic Code
# for making exception just make subclass of Exception
class AdultException(Exception):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if int(self.age) >= 18:
            raise AdultException
        else:
            return self.age

    def display(self):
        try:
            print(f"age -> {self.get_minor_age()}")
        except AdultException:
            print("Person is an adult")
        finally:
            print(f"name -> {self.name}")


# No exception
Person("Bhavin", 17).display()

# AdultException is raised
Person("Dhaval", 23).display()'''

#CHATGPT CODE
class AdultException(Exception):
    """Custom Exception to indicate a person is a minor."""
    pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        """Raises an exception if the person is an adult, otherwise returns the age."""
        if self.age >= 18:
            raise AdultException(f"{self.name} is major because their age is {self.age}")
        return self.age

    def display(self):
        """Displays the name and age, handling exceptions properly."""
        print(f"Name -> {self.name}")
        try:
            age = self.get_minor_age()  # Check if the person is a minor
            print(f"Age -> {age} (Minor)")
        except AdultException as e:
            print(e)
        finally:
            print("Execution completed.")

# Test Cases
try:
    Person("Geetanshu", 18).display()
except AdultException as e:
    print(f"Exception Caught: {e}")

try:
    Person("Gaurav", 17).display()
except AdultException as e:
    print(f"Exception Caught: {e}")
