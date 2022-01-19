from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Inventory


# Create your tests here.
class InventoryListPageTests(TestCase):

    def test_inventory_list_page_status_code(self):
        response = self.client.get('/items/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        url = reverse('inventory_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse('inventory_list')
        response = self.client.get(url)
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
        url = reverse('inventory_detail', args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse('inventory_detail', args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory_detail.html')


class InventoryDeletePageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.client.login(username='testuser', password='secret')

        self.inventory = Inventory.objects.create(
            title='test item',
            description='this is just a test item',
            specifications='test specs',
            merchant=self.user,
        )
        #  'manufacturer', 'quantity'
    
    def test_inventory_delete_page_status_code(self):
        response = self.client.get('/items/1/delete/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        url = reverse('inventory_delete', args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        url = reverse('inventory_delete', args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory_delete.html')


class InventoryUpdatePageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.client.login(username='testuser', password='secret')

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
        self.assertEqual(self.response.status_code, 200)

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

        self.client.login(username='testuser', password='secret')

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
        self.assertEqual(self.response.status_code, 200)

    def test_view_url_by_name(self):
        self.assertEqual(self.response2.status_code, 200)

    def test_view_uses_correct_template(self):
        self.assertEqual(self.response2.status_code, 200)
        self.assertTemplateUsed(self.response2, 'inventory_new.html')


def createInventory(title, description, specifications, merchant):
    return Inventory.objects.create(
            title=title,
            description=description,
            specifications=specifications,
            merchant=merchant,
        )
class InventoryListViewTests(TestCase):
    def test_list_non_existent_inventory(self):
        url = reverse('inventory_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are currently no inventory items.")
        self.assertQuerysetEqual(response.context['latest_inventory_list'], [])

    def test_list_single_inventory(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )
        inventory = createInventory(title='test item', description='this is just a test item', specifications='test specs', merchant=self.user,)
        url = reverse('inventory_list')
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context['latest_inventory_list'],
            [inventory],
            ordered=False
        )

    def test_list_multiple_inventory(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@email.com', password='secret',)
        inventory = createInventory(title='test item', description='this is just a test item', specifications='test specs', merchant=self.user,)
        inventory2 = createInventory(title='test item 2', description='this is just a test item 2', specifications='test specs 2', merchant=self.user,)
        response = self.client.get(reverse('inventory_list'))
        self.assertQuerysetEqual(
            response.context['latest_inventory_list'],
            [inventory2, inventory],
            ordered=False
        )


class InventoryDetailViewTests(TestCase):
    def test_details_non_existent_inventory(self):
        url = reverse('inventory_detail', args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_details_existing_inventory(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@email.com', password='secret',)
        inventory = createInventory(title='test item', description='this is just a test item', specifications='test specs', merchant=self.user,)
        url = reverse('inventory_detail', args=(inventory.id,))
        response = self.client.get(url)
        self.assertContains(response, inventory.title)


class InventoryUpdateViewTests(TestCase):
    def test_update_non_existent_inventory(self):
        url = reverse('inventory_edit', args='1')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)

    def test_update_existing_inventory(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@email.com', password='secret',)
        self.client.login(username='testuser', password='secret')
        inventory = createInventory(title='test item', description='this is just a test item', specifications='test specs', merchant=self.user,)

        url = reverse('inventory_edit', args=(inventory.id,))
        response = self.client.post(url, {'title': 'updated test item','description': 'This description has been updated',})
        self.assertEqual(response.context['updated_inventory_list'].title, 'updated test item')


class InventoryDeleteViewTests(TestCase):
    def test_delete_non_existent_inventory(self):
        url = reverse('inventory_delete', args='1')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)

    def test_delete_existing_inventory(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@email.com', password='secret',)
        self.client.login(username='testuser', password='secret')
        inventory = createInventory(title='test item', description='this is just a test item', specifications='test specs', merchant=self.user,)
        inventory2 = createInventory(title='test item 2', description='this is just a test item 2', specifications='test specs 2', merchant=self.user,)
        
        response = self.client.post(reverse('inventory_delete', args=(inventory2.id,)))
        response = self.client.get(reverse('inventory_list'))
        self.assertQuerysetEqual(
            response.context['latest_inventory_list'],
            [inventory],
            ordered=False
        )