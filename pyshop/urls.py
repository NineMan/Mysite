from django.urls import path

from . import views

app_name = 'pyshop'
urlpatterns = [
    # ex: /pyshop/
    path('', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='index'),
    # ex: /pyshop/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
