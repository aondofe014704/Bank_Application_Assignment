class Invalid_Amount_Exception (BaseException):
    def __init__(self, response):
        super().__init__(response)

