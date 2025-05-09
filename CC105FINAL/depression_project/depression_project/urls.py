from django.contrib import admin
from django.urls import path
from predictor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('predict/', views.predict_view, name='predict'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # ✅ Add this
]
