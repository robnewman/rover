from django.contrib import admin

# Models
from dog.models import Breed, Dog, DogPhoto, Owner

"""
Custom actions
"""

class DogPhotoInline(admin.TabularInline):
    model = DogPhoto
    extra = 1

"""
Customize admin
"""
class DogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = (
        DogPhotoInline,
    )

class OwnerAdmin(admin.ModelAdmin):
    exclude = ('full_name',)

"""
Registration
"""
admin.site.register(Breed)
admin.site.register(Dog, DogAdmin)
admin.site.register(DogPhoto)
admin.site.register(Owner, OwnerAdmin)

