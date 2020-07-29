from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from . import views


urlpatterns = [
    path('', views.base_view, name='base_view'),
    path('empty_section/', views.empty_view, name='empty_section'),
    path('item/<int:item_id>', views.item_view, name='item_view'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.registration_view, name='registration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)