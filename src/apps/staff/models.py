from django.db import models
from django.db.models.functions import Length
models.CharField.register_lookup(Length)

from utils.str_utils import gen_hash_from_str
# Create your models here.

class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Должность')
    short_name = models.CharField(max_length=200, default='',null=True, blank=True,  verbose_name='Сокращенная версия')
    note = models.CharField(max_length=200, default='', null=True, blank=True, verbose_name='Дополнительная информация')
    sort = models.CharField(max_length=5, default=0, blank=True,  verbose_name='Позиция при сортировке')
    hash = models.CharField(max_length=200, default='', blank=True, verbose_name='Hash')
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        constraints = [
            models.UniqueConstraint(
                name="%(app_label)s_%(class)s_hash_unique",
                fields=["hash"],
            ),
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_name_not_empty",
                check=models.Q(name__length__gt=0),
            ),
        ]
    def __str__(self):
        return f"{self.short_name}"
    def save(self, *args, **kwargs):
        if not self.hash:
            self.hash = gen_hash_from_str(self.name)
        super(Position, self).save(*args, **kwargs)