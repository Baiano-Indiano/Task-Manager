import pytest
from django.test import TestCase
from tasks.models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        """Test creating a new task"""
        task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            status='P'
        )
        self.assertEqual(str(task), 'Test Task')
        self.assertEqual(task.status, 'P')
        self.assertEqual(task.get_status_display(), 'Pendente')
