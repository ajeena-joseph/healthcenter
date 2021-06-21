from django.db import models


# Create your models here.
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='department', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def get_url(self):
        return reverse('departmentapp:doctors_by_department', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Doctor(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='doctor', blank=True)
    consultroom = models.IntegerField()
    phoneno=models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'

    def get_url(self):
        return reverse('departmentapp:docdepartmentdetail', args=[self.department.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
