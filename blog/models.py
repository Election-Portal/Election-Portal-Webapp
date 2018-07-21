from django.contrib.auth.models import User
from volunteers.models import Volunteer
from django.db import models, IntegrityError
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(Volunteer, on_delete = models.CASCADE)
    published_on = models.DateTimeField(auto_now_add = True)
    featured_image = models.ImageField(upload_to = 'blog_featued_image')
    #slug = models.SlugField(unique=True)
    time_read = models.IntegerField()
    summary = models.TextField(default="Write the executive summary ...")
    body = models.TextField()
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_more_on = models.BooleanField(default=False)
    is_most_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # override save method
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)

    #     while True:
    #         try:
    #             super().save()
    #         # Assuming the IntegrityError is due to a slug fight
    #         except IntegrityError:
    #             match_obj = re.match(r'^(.*)-(\d+)$', self.slug)
    #             if match_obj:
    #                 next_int = int(match_obj.group(2)) + 1
    #                 self.slug = match_obj.group(1) + '-' + str(next_int)
    #             else:
    #                 self.slug += '-2'
    #         else:
    #             break


class Category(models.Model):
    title = models.CharField(max_length = 100)
    #slug = models.SlugField(unique = True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)

    #     while True:
    #         try:
    #             super().save()
    #         # Assuming the IntegrityError is due to a slug fight
    #         except IntegrityError:
    #             match_obj = re.match(r'^(.*)-(\d+)$', self.slug)
    #             if match_obj:
    #                 next_int = int(match_obj.group(2)) + 1
    #                 self.slug = match_obj.group(1) + '-' + str(next_int)
    #             else:
    #                 self.slug += '-2'
    #         else:
    #             break
