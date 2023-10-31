from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('myapp.urls')),  # Rota do seu aplicativo
    path('admin/', admin.site.urls),  # Rota do painel de administração
    path('', RedirectView.as_view(url='musics/'))  # Rota padrão para redirecionar para 'musics/'
]