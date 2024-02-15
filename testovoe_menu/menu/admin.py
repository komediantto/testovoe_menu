from django.contrib import admin
from menu.models import MenuItem, Menu


class MenuItemAdmin(admin.ModelAdmin):
    # form = MenuItemForm
    list_display = ('name', 'menu_name', 'parent', 'url')
    list_filter = ('menu_name', 'parent',)
    prepopulated_fields = {'url': ('name',)}

    def save_model(self, request, obj, form, change):
        obj.url = '/' + obj.menu_name.name + '/' + obj.url + '/'
        obj.save()


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu)
