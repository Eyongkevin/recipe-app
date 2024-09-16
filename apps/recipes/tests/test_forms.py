from django.test import TestCase
from .forms import RecipeForm, RecipeSearch

class RecipeSearchFormTest(TestCase):
    def setUp(self):
        self.recipe1 = Recipe.objects.create(name='Recipe 1', ingredients='salt', cooking_time=10, directions='Cook it')
        self.recipe2 = Recipe.objects.create(name='Recipe 2', ingredients='sugar', cooking_time=20, directions='Mix it')

    def test_search_form_validity(self):
        form_data = {'searching_by': 'name', 'search_term': 'Recipe 1'}
        form = RecipeSearch(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_search_form(self):
        form = RecipeSearch(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # Adjust if the number of fields changes

    def test_search_results(self):
        response = self.client.get(reverse('recipe:search'), {'searching_by': 'name', 'search_term': 'Recipe 1'})
        self.assertContains(response, 'Recipe 1')
        self.assertNotContains(response, 'Recipe 2')

class RecipeSearchFormTest(TestCase):
    def test_search_form_validity(self):
        form_data = {'searching_by': 'name', 'search_term': 'Test Recipe'}
        form = RecipeSearch(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_search_form(self):
        form = RecipeSearch(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # Number of required fields
