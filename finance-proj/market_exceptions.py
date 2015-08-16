class AccessTokenError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class BadRequestError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidEndpointError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
