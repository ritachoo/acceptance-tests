from acceptance_core.helpers import env


class UTException(Exception):
    """UI Test exception"""

    def __init__(self, message):
        self.message = message
        self.test_name = env.get_test_name_with_path()

    def __str__(self):
        return (
            str(self.message) + f"\n From test: {self.test_name}"
            if self.test_name
            else ""
        )
