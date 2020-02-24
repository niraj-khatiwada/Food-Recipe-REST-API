from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class TestAdmin(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'niraj@admin.com',
            username= 'niraj',
            password= 'nepal123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email= 'niraj@gmail.com',
            username= 'niraj',
            password= 'nepal123'
        )

    def test_users_are_listed_in_admin(self):
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.email)
        self.assertContains(response, self.user.username)