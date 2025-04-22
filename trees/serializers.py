from rest_framework import serializers
from .models import Tree, TreeNames, Taxonomy, EcologyHabitat, TreePhoto, TreeModel

class TreeNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeNames
        fields = ['name', 'nativeName', 'scientificName']

class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = ['family', 'genus', 'species']

class EcologyHabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcologyHabitat
        fields = ['habitat', 'location', 'climate']

class TreePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreePhoto
        fields = ['id', 'image', 'caption', 'isPrimary']

class TreeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeModel
        fields = ['id', 'modelFile', 'description', 'fileFormat']

class TreeSerializer(serializers.ModelSerializer):
    names = TreeNamesSerializer(read_only=True)
    taxonomy = TaxonomySerializer(read_only=True)
    ecology = EcologyHabitatSerializer(read_only=True)
    photos = TreePhotoSerializer(many=True, read_only=True)
    models = TreeModelSerializer(many=True, read_only=True)
    
    class Meta:
        model = Tree
        fields = ['id', 'description', 'benefits', 'status', 'qrCode', 
                  'names', 'taxonomy', 'ecology', 'photos', 'models',
                  'createdAt', 'updatedAt']