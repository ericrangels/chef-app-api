from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@github.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_mail_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test1@github.com'
        password = 'Test321'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email normalized for new users"""
        email = 'test2@GITHUB.COM'
        user = get_user_model().objects.create_user(email, 'test012345')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating new user with invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test012345')

    def test_create_superuser(self):
        """Test creating new super user"""
        user = get_user_model().objects.create_superuser(
            'super@github.com',
            'test012345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
