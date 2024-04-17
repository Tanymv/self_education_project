from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from materials.models import Category, Material


class CategorySerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели разделов"""

    class Meta:
        model = Category
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели материалов"""

    class Meta:
        model = Material
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра информации о разделах, включает в себя
       поля количества материала, списка материалов этого раздела"""
    materials_count = SerializerMethodField()
    materials_list = SerializerMethodField()

    def user_(self):
        """Получаем текущего пользователя"""
        request = self.context.get('request', None)
        if request:
            return request.user
        return None

    @staticmethod
    def get_materials_count(course):
        """Получаем количество материалов для данного раздела"""
        return Material.objects.filter(category=category).count()

    @staticmethod
    def get_materials_list(course):
        """Получаем список материалов для данного раздела"""
        return MaterialSerializer(Material.objects.filter(category=category),
                                many=True).data

    class Meta:
        model = Category
        fields = '__all__'


class MaterialDetailSerializer(serializers.ModelSerializer):
    """Cериализатор для просмотра информации о материале,
       где для раздела выводится его наименование"""
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Material
        fields = '__all__'
