from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe       

class RecipeListViewTests(TestCase):
    def setUp(self):
        for i in range(10):
            Recipe.objects.create(
                name=f"Test Recipe {i}",
                ingredients="ingredient1, ingredient2, ingredient3",
                cooking_time=20,
                directions="Test directions"
            )

    def test_no_recipes(self):
        Recipe.objects.all().delete()  # Ensure no recipes
        response = self.client.get(reverse('recipe:home'))
        self.assertContains(response, "There are no recipes in the database yet")
        self.assertNotContains(response, "Recipe of the Day")

    def test_recipes_list(self):
        recipe = Recipe.objects.create(
            name="Test Recipe",
            ingredients="ingredient1, ingredient2, ingredient3",
            cooking_time=20,
            directions="Test directions"
        )
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertContains(response, recipe.name)

    def test_pagination(self):
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe 0')
        self.assertContains(response, 'Test Recipe 9')
        self.assertContains(response, 'Next')

class RecipeDetailViewTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name="Test Recipe",
            ingredients="ingredient1, ingredient2, ingredient3",
            cooking_time=20,
            directions="Test directions"
        )

    def test_valid_recipe(self):
        response = self.client.get(reverse('recipe:recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.recipe.name)

    def test_invalid_recipe(self):
        response = self.client.get(reverse('recipe:recipe_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_permissions(self):
        self.client.logout()
        response = self.client.get(reverse('recipe:recipe_detail', args=[self.recipe.id]))
        self.assertRedirects(response, f'/login/?next=/recipes/{self.recipe.id}/')

class AddRecipeViewTests(TestCase):
    def setUp(self):
        self.client.login(username='testuser', password='testpassword')

    def test_valid_form(self):
        with open('test_image.jpg', 'wb') as f:
            f.write(b'test_image_content')
        with open('test_image.jpg', 'rb') as f:
            data = {
                'name': 'Test Recipe',
                'ingredients': 'ingredient1, ingredient2, ingredient3',
                'cooking_time': 20,
                'directions': 'Test directions',
                'image': f
            }
            response = self.client.post(reverse('recipe:add_recipe'), data)
            self.assertRedirects(response, reverse('recipe:recipe_list'))
            self.assertEqual(Recipe.objects.count(), 1)

    def test_invalid_form(self):
        data = {
            'name': '',
            'ingredients': '',
            'cooking_time': -10,
            'directions': ''
        }
        response = self.client.post(reverse('recipe:add_recipe'), data)
        self.assertContains(response, 'This field is required.')
        self.assertEqual(Recipe.objects.count(), 0)

class RecipeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.recipe = Recipe.objects.create(
            name='Test Recipe',
            ingredients='flour, sugar, butter',
            cooking_time=15,
            directions='Mix ingredients and bake.',
            image='recipe_images/tea.jpg'
        )

    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_list.html')
        self.assertContains(response, 'Test Recipe')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe:recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_detail.html')
        self.assertContains(response, 'Test Recipe')

    def test_login_protection(self):
        response = self.client.get(reverse('recipe:add_recipe'))
        self.assertRedirects(response, '/login/?next=/recipes/add/')

    def test_pagination(self):
        for i in range(15):
            Recipe.objects.create(
                name=f'Test Recipe {i}',
                ingredients='flour, sugar, butter',
                cooking_time=15,
                directions='Mix ingredients and bake.',
                image='recipe_images/tea.jpg'
            )
        response = self.client.get(reverse('recipe:recipe_list'))
        self.assertContains(response, 'Test Recipe 0')
        self.assertContains(response, 'Test Recipe 14')
        self.assertContains(response, 'Next')

    def test_search_functionality(self):
        response = self.client.get(reverse('recipe:search'), {'searching_by': 'name', 'search_term': 'Test Recipe'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')

