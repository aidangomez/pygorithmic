def checkRequest(self, request):
    code = request.status_code
    if (code == 200):
        return request
    elif (code == 202):
        return request
    elif (code == 401):
        raise AccessTokenError("Bad access token.")
    elif (code == 400):
        raise BadRequestError("Bad request.")
    elif (code == 404):
        raise InvalidEndpointError("Invalid endpoint: " + request.url)
    elif (code == 429):
        raise LimitExceededError(
            "Too many requests. Reset in: " + str(request.headers["X-RateLimit-Reset"]))
    else:
        print("UNKNOWN ERROR: " + str(code))
        print(request.text)
        raise Exception


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


class LimitExceededError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
