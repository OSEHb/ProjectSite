from django.db import models


class Problems(models.Model):
    title = models.CharField(max_length=120)  # заголовок CharField-для текстовых полей макс. 120 символов
    body = models.TextField()  # TextField-для текстовых полей c большим числом символов

    def __str__(self):  # для получения текста заголовка, а не объекта title класса Problems
        return self.title

