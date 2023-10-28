

from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('register/',views.register_view,name="register"),
    path('logout/',views.logout_view,name="logout"),
    path('login/', views.login_view,name="login"),
    path('create/',views. create_view,name="create"),
]
