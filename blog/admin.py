from django.contrib import admin

# то что будет отображаться в панели управления

from .models import Post #импортируем модуль пост

admin.site.register(Post) #Регистрируем модель нашего поста
