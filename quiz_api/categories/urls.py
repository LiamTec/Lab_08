from django.urls import path, include
from .views import CategoryDeleteView, TagDeleteView, CategoryUpdateView, TagUpdateView

urlpatterns = [
    path('api/category/<int:id>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('api/tag/<int:id>/', TagDeleteView.as_view(), name='tag-delete'),
    path('api/category/update/<int:id>/', CategoryUpdateView.as_view(), name='category-update'),
    path('api/tag/update/<int:id>/', TagUpdateView.as_view(), name='tag-update' ),

]