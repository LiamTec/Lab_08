from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet
from categories.views import CategoryViewSet, TagViewSet, CategoryDeleteView, TagDeleteView, CategoryUpdateView, TagUpdateView

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = [
    path('api/category/<int:id>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('api/tag/<int:id>/', TagDeleteView.as_view(), name='tag-delete'),
    path('api/category/update/<int:id>/', CategoryUpdateView.as_view(), name='category-update'),
    path('api/tag/update/<int:id>/', TagUpdateView.as_view(), name='tag-update' )

]

urlpatterns = [
    path('', include(router.urls)),
]