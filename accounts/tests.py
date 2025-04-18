from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AccountsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = '123456'
        user_user = get_user_model().objects.create(username=self.username)
        user_user.set_password(self.password)
        user_user.save()

    def test_login(self):
        response = self.client.login(
            username=self.username,
            password=self.password,
        )
        self.assertTrue(response, True)

    def test_profile_view_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('accounts:profile')),
            'accounts/profile.html',
        )

    def test_signup_view_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('accounts:signup')),
            'accounts/signup.html',
        )

    def test_update_view_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('accounts:update')),
            'accounts/update.html',
        )
