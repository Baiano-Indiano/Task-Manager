from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task

class TaskViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            status='P'
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')
        self.assertTemplateUsed(response, 'tasks/task_list.html')

    def test_task_create_view(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'This is a new task',
            'status': 'P'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after POST
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_update_view(self):
        response = self.client.post(reverse('task_update', args=[self.task.id]), {
            'title': 'Updated Task',
            'description': 'This task has been updated',
            'status': 'C'
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.status, 'C')

    def test_task_delete_view(self):
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
