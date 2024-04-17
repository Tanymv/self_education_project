from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from materials.models import Material
from users.models import User


class MaterialTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        """Создание и авторизация тестового пользователя"""
        self.user = User.objects.create(id=1, email='user@test.ru',
                                        password='12345', )
        self.client.force_authenticate(user=self.user)

        """Создание тестового материала"""
        self.material = Material.objects.create(name='test_material',
                                                content='test_content')


    def test_create_habit(self):
        """Тестирование создания материала"""


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