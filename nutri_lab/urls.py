from django.contrib import admin
from django.urls import path, include

import autenticacao

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')  )
]
