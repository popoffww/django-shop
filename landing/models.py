from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя и фамилия')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    password = models.CharField(max_length=100, unique=True, verbose_name='Пароль')
    confirm_password = models.CharField(max_length=100, unique=True, verbose_name='Потвердить пароль')

    def __str__(self):
            return 'Пользователь %s, email: %s' % (self.name, self.email)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
        ordering = ['name']