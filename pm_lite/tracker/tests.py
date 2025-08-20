from django.test import TestCase
from django.urls import reverse
from .models import Project

class ProjectViewTests(TestCase):
    def setUp(self):
        """
        Create a sample project for testing.
        """
        self.project = Project.objects.create(
            name='Test Project',
            description='A test project for the unit tests.',
            project_type='Construction',
            status='In Progress'
        )

    def test_project_list_view(self):
        """
        Test that the project list view returns a 200 OK status code
        and contains the test project's name.
        """
        url = reverse('tracker:project_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.name)
        self.assertTemplateUsed(response, 'tracker/project_list.html')

    def test_project_detail_view(self):
        """
        Test that the project detail view returns a 200 OK status code
        for a valid project and contains the project's details.
        """
        url = reverse('tracker:project_detail', args=[self.project.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.name)
        self.assertContains(response, self.project.description)
        self.assertTemplateUsed(response, 'tracker/project_detail.html')

    def test_project_detail_view_not_found(self):
        """
        Test that the project detail view returns a 404 Not Found
        for an invalid project ID.
        """
        url = reverse('tracker:project_detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
