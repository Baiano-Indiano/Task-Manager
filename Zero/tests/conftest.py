import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user():
    """Create a test user."""
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )

@pytest.fixture
def task():
    """Create a test task."""
    from tasks.models import Task
    return Task.objects.create(
        title='Test Task',
        description='This is a test task',
        status='P'
    )
