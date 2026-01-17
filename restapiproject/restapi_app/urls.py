from django.urls import path
from .import views


urlpatterns = [
    path('test/', views.TestView.as_view(), name='test'),
    path('test/update/<int:id>/', views.TestViewUpdate.as_view(), name='test_update'),
    path('test/delete/<int:id>/', views.TestViewDelete.as_view(), name='test_delete')
]