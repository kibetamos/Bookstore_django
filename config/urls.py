from django.conf import settings # new
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),

    # User management
    # path('accounts/', include('django.contrib.auth.urls')),


    #local apps
    path('accounts/', include('allauth.urls')),
    
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
