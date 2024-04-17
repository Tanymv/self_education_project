from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import MaterialListView, MaterialCreateView, MaterialDetailView, \
    MaterialUpdateView, MaterialDeleteView

app_name = MaterialsConfig.name

urlpatterns = [
    path('', MaterialListView.as_view(), name='material_list'),
    path('create/', MaterialCreateView.as_view(), name='material_create'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='material_view'),
    path('update/<int:pk>/', MaterialUpdateView.as_view(), name='material_update'),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='material_delete'),
]