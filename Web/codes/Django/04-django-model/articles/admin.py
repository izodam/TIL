from django.contrib import admin
from .models import Article

# Register your models here.
# admin site에 Article 클래스 등록
admin.site.register(Article)