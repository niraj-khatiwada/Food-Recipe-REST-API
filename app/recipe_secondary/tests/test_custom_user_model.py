from django.test import TestCase
from django.contrib.auth import get_user_model

class TestCustomeUserModel(TestCase):

    def test_custom_user_model(self):
        email = 'niraj@gmail.com'
        password = 'nepal123'
        username = 'niraj'
        user = get_user_model().objects.create_user(
            email = email,
            username = username,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_is_normalized(self):
        email = 'niraj@NEPAL.gmail.com'
        password= 'nepal123'
        username = 'niraj'
        user = get_user_model().objects.create_user(
            email= email,
            username= username,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_email_value_error(self):
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(
                email = None,
                username = 'niraj',
                password = 'nepal123'
            )

    # def test_create_superuser(self):
    #     user = get_user_model().objects.create_superuser(
    #         email = 'niraj@gmail.com',
    #         username = 'niraj',
    #         password = 'nepal123'
    #     )
    #     self.assertTrue(user.is_admin)
    #     self.assertTrue(user.is_staff)