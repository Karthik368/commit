from django.contrib import admin
from firstapp.models import happi
# Register your models here.
class happy(admin.ModelAdmin):
    list_display=['id','hid','hname','contact','salary','address']

admin.site.register(happi,happy)