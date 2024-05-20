import pytest
from content.objects.user import User


@pytest.fixture
def create_user_by_ui() -> User:
    def _create_user_by_ui():
        user = User().create_user()
        email = user.user_data.email
        password = user.user_data.password
        return email, password

    # Запуск теста
    yield _create_user_by_ui()
