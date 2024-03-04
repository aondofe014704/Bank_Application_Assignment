class SoftwareEngineer:
    alias = "Keyboard Magician"
    def __init__(self, position, name, age, level, salary):
        self.position = position
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code...")


    def code_language(self, language):
        print(f"{self.name} is writing code in {language}...")


    def information(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

   def __str__(self):
         information = f"name = {self.name}, age = {self.age}, level = {self.level}"
            return information





software = SoftwareEngineer("Software Engineer","Jack Songu", 30, "Junior Developer", 500000)


print(software.position, software.name, software.age, software.level, software.salary)
print(SoftwareEngineer.alias)
software.code()
software.code_language("python")
print(software.information())
