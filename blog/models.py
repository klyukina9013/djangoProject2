from django.db import models


# этот файл отвечает за модель вносимых нами данных, импортируем методы модели, отвечающие за добавление порта

class Post(models.Model):
    title = models.CharField(max_length=450)  # заголовок поста
    author = models.ForeignKey(  # автор поста, которого выбираем в администр панели управления
        'auth.User',
        on_delete=models.CASCADE  # удаление поста
    )
    body = models.TextField()  # поле, в которое вводим текст поста

    def __str__(self):  # магический метод, возвращается ввиде строки
        return self.title
