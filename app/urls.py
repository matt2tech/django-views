from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # path('', views.create, name='create'),
    # path('link/<short_code>/', views.show, name='show'),
    # path('<short_code>/', views.goto, name='goto')
    path('', views.Create.as_view(), name='create'),
    path('link/<short_code>/', views.Show.as_view(), name='show'),
    path('<short_code>/', views.Goto.as_view(), name='goto')
]
