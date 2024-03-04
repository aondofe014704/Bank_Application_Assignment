class InvalidPinException(BaseException):

    def __init__(self, response):
        super().__init__(response)
