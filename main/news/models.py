from django.db import models as m


# Модели таблиц в базе данных
class News(m.Model):
    title = m.CharField(max_length=50, verbose_name='Наиминование')
    content = m.TextField(blank=True, verbose_name='Контент')
    created_at = m.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    update_at = m.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = m.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = m.BooleanField(default=True, verbose_name='Опубликовано')
    category = m.ForeignKey('Category', on_delete=m.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'My News'
        verbose_name_plural = 'List of news'
        ordering = ['-created_at']


class Category(m.Model):
    title = m.CharField(max_length=50, db_index=True,
                        verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
