from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from materials.models import Material, Category
from users.models import User


class MaterialTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        """Создание и авторизация тестового пользователя"""
        self.user = User.objects.create(id=1, email='user@test.ru',
                                        password='12345', )
        self.client.force_authenticate(user=self.user)

        """Создание тестового материала"""
        self.material = Material.objects.create(name='test_name',
                                                content='test_content')

        """Создание тестового раздела"""
        self.category = Category.objects.create(title='test_title',
                                                description=' description')

    def test_create_category(self):
        """Тестирование создания раздела"""

        data = {'title': 'create_test', 'description': 'create_test_description'}
        path = reverse('materials:category_create')
        response = self.client.post(path=path, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Category.objects.filter(title=data['title']).exists())

    def test_detail_category(self):
        """Тестирование просмотра информации о разделе"""
        path = reverse('materials:category_detail', [self.category.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "title": "test_title",
            "description": "test_description",
            "material_list": [
                {"title": "test_title",
                 "content": "test_content"}
            ]
        })

    def test_update_category(self):
        """Тестирование редактирования раздела"""
        path = reverse('materials:category_update', [self.category.id])
        data = {'title': 'update_test', 'description': 'update_test_description'}
        response = self.client.patch(path, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.title, data['title'])

    def test_delete_category(self):
        """Тестирование удаления раздела"""
        path = reverse('materials:category_delete', [self.category.id])
        response = self.client.delete(path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())

    def test_create_material(self):
        """Тестирование создания материала"""
        path = reverse('materials:material_create')
        response = self.client.post(path,
                                    {'title': 'test_title', 'content': 'test_content', 'category': self.category.pk})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_material(self):
        """Тестирование просмотра материала"""
        path = reverse('materials:material_view', [self.material.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_material(self):
        """Тестирование редактирования материала"""
        path = reverse('materials:material_update', [self.material.id])
        response = self.client.patch(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.material.refresh_from_db()

    def test_delete_material(self):
        """Тестирование удаления материала"""
        self.client.force_authenticate(user=self.user)
        path = reverse('materials:material_delete', [self.material.id])
        response = self.client.delete(path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Material.objects.filter(id=self.material.id).exists())
