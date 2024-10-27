from django.contrib import admin  
from .models import Shop  
from django.utils.text import slugify 

class ShopAdmin(admin.ModelAdmin):  
    list_display = ('title', 'owner', 'phone', 'created_at', 'updated_at')  
    search_fields = ('title', 'owner__username', 'phone')  
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('owner', 'created_at')  
    ordering = ('-created_at',)  

    def save_model(self, request, obj, form, change):  
        if not obj.slug:  # Ensure slug is generated if not provided  
            obj.slug = slugify(obj.title, allow_unicode=True)  
        super().save_model(request, obj, form, change)  

admin.site.register(Shop, ShopAdmin)