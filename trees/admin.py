from django.contrib import admin
from .models import Tree, TreeNames, Taxonomy, EcologyHabitat, TreePhoto, TreeModel

class TreeNamesInline(admin.StackedInline):
    model = TreeNames

class TaxonomyInline(admin.StackedInline):
    model = Taxonomy

class EcologyHabitatInline(admin.StackedInline):
    model = EcologyHabitat

class TreePhotoInline(admin.TabularInline):
    model = TreePhoto
    extra = 3

class TreeModelInline(admin.TabularInline):
    model = TreeModel
    extra = 1

@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_name', 'status', 'qrCode')
    search_fields = ('qrCode', 'names__name', 'names__scientificName')
    inlines = [TreeNamesInline, TaxonomyInline, EcologyHabitatInline, 
               TreePhotoInline, TreeModelInline]
    
    def get_name(self, obj):
        if hasattr(obj, 'names'):
            return obj.names.name
        return "-"
    get_name.short_description = 'Name'

@admin.register(TreePhoto)
class TreePhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_tree_name', 'caption', 'isPrimary')
    list_filter = ('isPrimary',)
    
    def get_tree_name(self, obj):
        if hasattr(obj.tree, 'names'):
            return obj.tree.names.name
        return f"Tree #{obj.tree.id}"
    get_tree_name.short_description = 'Tree'

@admin.register(TreeModel)
class TreeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_tree_name', 'fileFormat')
    
    def get_tree_name(self, obj):
        if hasattr(obj.tree, 'names'):
            return obj.tree.names.name
        return f"Tree #{obj.tree.id}"
    get_tree_name.short_description = 'Tree'