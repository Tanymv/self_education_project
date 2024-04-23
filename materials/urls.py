from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import MaterialListView, MaterialCreateView, MaterialDetailView, \
    MaterialUpdateView, MaterialDeleteView, CategoryListView, CategoryCreateView, CategoryDetailView, \
    CategoryUpdateView, CategoryDeleteView

app_name = MaterialsConfig.name

urlpatterns = [
    path('', MaterialListView.as_view(), name='material_list'),
    path('create/', MaterialCreateView.as_view(), name='material_create'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='material_view'),
    path('update/<int:pk>/', MaterialUpdateView.as_view(), name='material_update'),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='material_delete'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
