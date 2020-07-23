from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from shop import views


urlpatterns = [
    path('', views.base_view, name='base_view'),
    path('phone/<int:item_id>', views.phone_view, name='phone_view'),
    path('empty_section/', views.empty_view, name='empty_section'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)