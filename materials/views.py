from rest_framework import generics, permissions
from materials.models import Material, Category
from materials.paginators import MaterialsPaginator
from materials.serializers import MaterialSerializer, CategorySerializer, CategoryDetailSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListView(generics.ListAPIView):
    """Контроллер для просмотра списка разделов"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CategoryCreateView(generics.CreateAPIView):
    """Контроллер создания раздела"""
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDetailView(generics.RetrieveAPIView):
    """Контроллер просмотра раздела"""
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CategoryUpdateView(generics.UpdateAPIView):
    """Контроллер редактирования раздела"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class CategoryDeleteView(generics.DestroyAPIView):
    """Контроллер удаления раздела"""
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class MaterialListView(generics.ListAPIView):
    """Контроллер просмотра списка опубликованых материалов"""
    serializer_class = MaterialSerializer
    pagination_class = MaterialsPaginator
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('title',)
    ordering_fields = ('category',)

    def get_queryset(self):
        """Фильтруем подборку по признаку публикации"""
        return Material.objects.filter(is_published=True)


class MaterialCreateView(generics.CreateAPIView):
    """Контроллер создания материалов"""
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемому объекту"""
        new_material = serializer.save()
        new_material.user = self.request.user
        new_material.save()


class MaterialDetailView(generics.RetrieveAPIView):
    """Контроллер просмотра материалов"""
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class MaterialUpdateView(generics.UpdateAPIView):
    """Контроллер редактирования материалов"""
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class MaterialDeleteView(generics.DestroyAPIView):
    """Контроллер удаления материалов"""
    queryset = Material.objects.all()
    permission_classes = [permissions.IsAuthenticated]
