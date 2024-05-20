class UCException(Exception):
    """UI Core exception"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)
