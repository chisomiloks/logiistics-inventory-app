from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from django.utils import timezone

from .models import Inventory


# Create your tests here.
class InventoryListPageTests(TestCase):

    def test_inventory_list_page_status_code(self):
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('inventory_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('inventory_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory_list.html')


class InventoryDetailPageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.inventory = Inventory.objects.create(
            title='test item',
            description='this is just a test item',
            specifications='test specs',
            merchant=self.user,
        )
        #  'manufacturer', 'quantity'

    def test_inventory_detail_page_status_code(self):
        response = self.client.get('/items/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('inventory_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('inventory_detail', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory_detail.html')


class InventoryDeletePageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.inventory = Inventory.objects.create(
            title='test item',
            description='this is just a test item',
            specifications='test specs',
            merchant=self.user,
        )
        #  'manufacturer', 'quantity'

    def test_inventory_delete_page_status_code(self):
        response = self.client.post('/items/1/delete/')
        self.assertEqual(response.status_code, 302)

    def test_view_url_by_name(self):
        response = self.client.post(reverse('inventory_delete', args='1'))
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        response = self.client.post(reverse('inventory_delete', args='1'))
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'inventory_delete.html')


class InventoryUpdatePageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.inventory = Inventory.objects.create(
            title='test item',
            description='this is just a test item',
            specifications='test specs',
            merchant=self.user,
        )
        #  'manufacturer', 'quantity'

        self.response = self.client.post('/items/1/edit/', {
            'title': 'updated test item',
            'description': 'updated this is just a test item',
            'specifications': 'updated test specs',
            'merchant': self.user.id,
        })

        self.response2 = self.client.post(reverse('inventory_edit', args='1'), {'title': 'another updated test item',})

    def test_inventory_delete_page_status_code(self):
        self.assertEqual(self.response.status_code, 302)

    def test_view_url_by_name(self):
        self.assertEqual(self.response2.status_code, 200)

    def test_view_uses_correct_template(self):
        self.assertEqual(self.response2.status_code, 200)
        self.assertTemplateUsed(self.response2, 'inventory_edit.html')


class InventoryCreatePageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.response = self.client.post('/items/new/', {
            'title':'test item',
            'description':'this is just a test item',
            'specifications':'test specs',
            'merchant':self.user,
        })

        self.response2 = self.client.post(reverse('inventory_new'), {
            'title':'test item',
            'description':'this is just a test item',
            'specifications':'test specs',
            'merchant':self.user,
        })

    def test_inventory_create_page_status_code(self):
        # response = self.client.get('/items/1/delete/')
        self.assertEqual(self.response.status_code, 200)

    def test_view_url_by_name(self):
        # response = self.client.get(reverse('inventory_delete', args='1'))
        self.assertEqual(self.response2.status_code, 200)

    def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('inventory_delete', args='1'))
        self.assertEqual(self.response2.status_code, 200)
        self.assertTemplateUsed(self.response2, 'inventory_new.html')

class InventoryModelTests(TestCase):
    """
    To be used if functions are added to the Model
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.inventory = Inventory.objects.create(
            title='test item',
            description='this is just a test item',
            specifications='test specs',
            merchant=self.user,
        )
    """


# use to test that views works
"""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.inventory = Inventory.objects.create(
            title='test item',
            description='this is just a test item',
            specifications='test specs',
            merchant=self.user,
        )
"""