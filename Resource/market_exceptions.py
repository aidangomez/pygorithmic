def checkRequest(request):
    code = request.status_code
    if (code == 200):
        return request
    elif (code == 202):
        return request
    elif (code == 401):
        raise AccessTokenError("Bad access token.")
    elif (code == 400):
        raise BadRequestError(request)
    elif (code == 404):
        raise NotFoundError(request)
    elif (code == 413):
        raise LimitExceededError("Request too large.")
    elif (code == 429):
        raise LimitExceededError("Too many requests. Reset in: " +
                                 str(request.headers["X-RateLimit-Reset"]))
    elif (code in [500, 502, 503]):
        raise APIError("Questrade API failed.")
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
        try:
            code = value.json()["code"]
            if (code == 1002):
                self.value = "Invalid argument."
            elif (code == 1003):
                self.value = "Argument length exceeds limit."
            elif (code == 1004):
                self.value = "Missing required argument."
            elif (code == 1015):
                self.value = "Invalid argument."
        except ValueError:
            self.value = "Bad Request: " + str(value.headers)

    def __str__(self):
        return repr(self.value)


class NotFoundError(Exception):

    def __init__(self, value):
        try:
            code = value.json()["code"]
            if (code == 1001):
                self.value = "Invalid endpoint."
            elif (code == 1018):
                self.value = "Account number not found."
            elif (code == 1019):
                self.value = "Symbol not found."
            elif (code == 1020):
                self.value = "Order not found."
        except ValueError:
            self.value = "Not Found Error."

    def __str__(self):
        return repr(self.value)


class LimitExceededError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class APIError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
