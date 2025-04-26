from rest_framework import serializers
from .models import Tree, TreeNames, Taxonomy, EcologicalBackground, TreePhoto, TreeModel

class TreeNamesSerializer(serializers.ModelSerializer):
    otherNames = serializers.SerializerMethodField()

    class Meta:
        model = TreeNames
        fields = ['otherNames', 'nativeName', 'scientificName']

    def get_otherNames(self, obj):
        return obj.get_other_names()

class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = ['family', 'genus', 'species']

class EcologicalBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcologicalBackground
        fields = ['habitatType', 'nativeLocation', 'system', 'climate', 'endemicity']

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
    ecology = EcologicalBackgroundSerializer(read_only=True)
    photos = TreePhotoSerializer(many=True, read_only=True)
    models = TreeModelSerializer(many=True, read_only=True)

    class Meta:
        model = Tree
        fields = ['id', 'description', 'uses', 'qrCode', 
                  'names', 'taxonomy', 'ecology', 'photos', 'models',
                  'createdAt', 'updatedAt']