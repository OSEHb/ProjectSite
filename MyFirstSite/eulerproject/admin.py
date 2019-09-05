from django.contrib import admin
from .models import Problems  # импортируем нашу таблице


admin.site.register(Problems)  # регистрируем наш класс в понели администратора

