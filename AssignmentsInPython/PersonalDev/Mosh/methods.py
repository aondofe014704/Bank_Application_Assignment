class Method:
    def __init__(self):
        self.user_input = ""  # self.user_input

    def get_string(self):
        self.user_input = str(input("Enter a word"))

    def print_string(self):
        return self.user_input.upper()

    def __repr__(self):
         return f"{self.user_input.upper()}"
 methods = Method()
 methods.get_string()
 print(methods.print_string())
