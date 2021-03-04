from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
          path('',views.home,name='home'),
                  path('details', views.details, name='details'),
                  path('email/', views.send_email.as_view(), name='send_email'),

    ]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)