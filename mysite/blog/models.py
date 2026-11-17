from django.db import models

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    body = models.TextField("Текст")
    author = models.CharField("Автор", max_length=100, default="Суркин Илья")
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=True)
    
    def __str__(self):
        return self.title
