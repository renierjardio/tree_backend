from django.contrib import admin
from .models import Tree, TreeNames, Taxonomy, EcologicalBackground, TreePhoto, TreeModel

class TreeNamesInline(admin.StackedInline):
    model = TreeNames

class TaxonomyInline(admin.StackedInline):
    model = Taxonomy

class EcologicalBackgroundInline(admin.StackedInline):
    model = EcologicalBackground

class TreePhotoInline(admin.TabularInline):
    model = TreePhoto
    extra = 3

class TreeModelInline(admin.TabularInline):
    model = TreeModel
    extra = 1

@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_name', 'qrCode')
    search_fields = ('qrCode', 'names__nativeName', 'names__scientificName')
    inlines = [TreeNamesInline, TaxonomyInline, EcologicalBackgroundInline, 
               TreePhotoInline, TreeModelInline]

    def get_name(self, obj):
        if hasattr(obj, 'names'):
            return obj.names.nativeName
        return "-"
    get_name.short_description = 'Native Name'

@admin.register(TreePhoto)
class TreePhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_tree_name', 'caption', 'isPrimary')
    list_filter = ('isPrimary',)

    def get_tree_name(self, obj):
        if hasattr(obj.tree, 'names'):
            return obj.tree.names.nativeName
        return f"Tree #{obj.tree.id}"
    get_tree_name.short_description = 'Tree'

@admin.register(TreeModel)
class TreeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_tree_name', 'fileFormat')

    def get_tree_name(self, obj):
        if hasattr(obj.tree, 'names'):
            return obj.tree.names.nativeName
        return f"Tree #{obj.tree.id}"
    get_tree_name.short_description = 'Tree'