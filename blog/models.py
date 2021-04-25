from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _ 

#Create your models here.
class blog(models.Model):
    title = models.CharField(_("عنوان"),max_length=50)
    description = models.CharField(_("توضیحات"),max_length=100)
    content = models.TextField(_("متن"))
    created_at = models.DateTimeField(_("تاریخ انتشار"),default=timezone.now)
    author = models.ForeignKey(User,verbose_name=_("نویسنده"),on_delete = models.CASCADE)
    image = models.ImageField(_("تصویر"),upload_to = "blogs/",blank= True,null= True)
    Category = models.ForeignKey("category",related_name="blog",verbose_name =_("دسته بندی"),on_delete = models.CASCADE, blank= True , null= True )
    tags = models.ManyToManyField("tag",verbose_name=_("تگ ها"),related_name="blogs",blank= True,null= True)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
    def __str__(self):
        return self.title

class category(models.Model):
    title = models.CharField(_("عنوان"),max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"),auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    def __str__(self):
        return self.title

class tag(models.Model):
    title = models.CharField(_("عنوان"),max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"),auto_now=False , auto_now_add= True)
    updated_at = models.DateTimeField(_("تاریخ بروزرسانی"),auto_now=False , auto_now_add=True)

    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ ها"
    def __str__(self):
        return self.title

class comments(models.Model):
    Blog = models.ForeignKey("blog",verbose_name=_("مقاله"),related_name="Comments",on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"),max_length=100)
    email = models.EmailField(_("ایمیل کاربر"),max_length= 200)
    message = models.TextField(_("متن"))
    date = models.DateTimeField(_("تاریخ"),auto_now=False , auto_now_add=True)

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return self.email

