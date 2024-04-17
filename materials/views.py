from rest_framework import generics
from materials.models import Material
from materials.paginators import MaterialsPaginator
from materials.serializers import MaterialSerializer


class MaterialListView(generics.ListAPIView):
    """Контроллер просмотра списка опубликованых материалов"""
    serializer_class = MaterialSerializer
    pagination_class = MaterialsPaginator

    def get_queryset(self):
        """Фильтруем подборку по признаку публикации"""
        return Material.objects.filter(is_published=True)


class MaterialCreateView(generics.CreateAPIView):
    """Контроллер создания материалов"""
    serializer_class = MaterialSerializer

    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемому объекту"""
        new_material = serializer.save()
        new_material.user = self.request.user
        new_material.save()


class MaterialDetailView(generics.RetrieveAPIView):
    """Контроллер просмотра материалов"""
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialUpdateView(generics.UpdateAPIView):
    """Контроллер редактирования материалов"""
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialDeleteView(generics.DestroyAPIView):
    """Контроллер удаления материалов"""
    queryset = Material.objects.all()
