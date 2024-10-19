from django.test import TestCase
from django.urls import reverse
from .models import Menu

class MenuModelTest(TestCase):
    def setUp(self):
        # Create sample menu items to test the model
        self.menu_item1 = Menu.objects.create(
            name="Spaghetti",
            description="Delicious spaghetti with marinara sauce",
            price=12.50
        )
        self.menu_item2 = Menu.objects.create(
            name="Caesar Salad",
            description="Crisp romaine lettuce with Caesar dressing",
            price=8.00
        )

    def test_menu_item_creation(self):
        # Check if the menu items were created and fields are correct
        self.assertEqual(self.menu_item1.name, "Spaghetti")
        self.assertEqual(self.menu_item1.price, 12.50)
        self.assertEqual(self.menu_item2.description, "Crisp romaine lettuce with Caesar dressing")

    def test_menu_str_method(self):
        # Test the __str__ method of the Menu model
        self.assertEqual(str(self.menu_item1), "Spaghetti")
        self.assertEqual(str(self.menu_item2), "Caesar Salad")


class MenuViewsTest(TestCase):
    def setUp(self):
        # Create menu items for testing the view
        self.menu_item1 = Menu.objects.create(
            name="Spaghetti",
            description="Delicious spaghetti with marinara sauce",
            price=12.50
        )

    def test_home_view_status_code(self):
        # Test if the home page loads correctly
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/home.html')

    def test_menu_view_status_code(self):
        # Test if the menu page loads correctly
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu.html')

    def test_menu_view_content(self):
        # Test if the menu page returns the correct menu item
        response = self.client.get(reverse('menu'))
        self.assertContains(response, 'Spaghetti')
        self.assertEqual(len(response.context['menu_list']), 1)

