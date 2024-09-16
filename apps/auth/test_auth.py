from django.test import TestCase

class AuthTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        User.objects.create_user(username=self.username, password=self.password)

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertRedirects(response, reverse('recipe:recipe_list'))
        self.assertEqual(self.client.session['_auth_user_id'], str(User.objects.get(username=self.username).id))

    def test_login_protection(self):
        response = self.client.get(reverse('recipe:add_recipe'))
        self.assertRedirects(response, '/login/?next=/recipes/add/')

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_login_form_errors(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertContains(response, 'Your username and password didn’t match. Please try again.')
