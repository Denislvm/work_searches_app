from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

#**********
#4 Startup
# title
# about_yourself
# about_prj
# contact
# file_field


class Vacancy(models.Model):
    class Rating(models.TextChoices):
        INTERN = 'Intern', _('Intern')
        JUNIOR = 'Junior', _('Junior')
        MIDDLE = 'Middle', _('Middle')
        SENIOR = 'Senior', _('Senior')

    years_in_work = models.CharField(
        max_length=50,
        choices=Rating.choices,
        default=Rating.JUNIOR,
        blank=True,
        null=True,
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    content = models.TextField()
    about_company = models.CharField(max_length=255, null=True)

    ELEMENTARY = 'Elementary'
    PRE_INTERMEDIATE = 'Pre-Intermediate'
    INTERMEDIATE = 'Intermediate'
    UPPER_INTERMEDIATE = 'Upper-Intermediate'
    ADVANCED = 'Advanced'
    PROFICIENCY = 'Proficiency'
    LEVEL_ENGLISH = [
        (ELEMENTARY, 'Elementary'),
        (PRE_INTERMEDIATE, 'Pre-Intermediate'),
        (INTERMEDIATE, 'Intermediate'),
        (UPPER_INTERMEDIATE, 'Upper-Intermediate'),
        (ADVANCED, 'Advanced'),
        (PROFICIENCY, 'Proficiency'),
    ]
    level_english = models.CharField(
        max_length=50,
        choices=LEVEL_ENGLISH,
        default=ELEMENTARY,
        blank=True,
        null=True,
    )

    mail_address = models.EmailField(max_length=254, null=True)
    site_company = models.CharField( max_length=255, null=True)
    site_in_dou = models.CharField(max_length=255, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ['-time_created', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

class Startup(models.Model):
    name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(verbose_name='About startup')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    mail_address = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('startup_post', kwargs={'startup_slug': self.slug})






