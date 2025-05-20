from rest_framework import serializers
from .models import Tree

class TreeSerializer(serializers.ModelSerializer):
    nativeName = serializers.CharField(source='names.nativeName', read_only=True)
    scientificName = serializers.CharField(source='names.scientificName', read_only=True)
    otherNames = serializers.SerializerMethodField()

    family = serializers.CharField(source='taxonomy.family', read_only=True)
    genus = serializers.CharField(source='taxonomy.genus', read_only=True)

    nativeLocation = serializers.CharField(source='ecology.nativeLocation', read_only=True)
    climate = serializers.CharField(source='ecology.climate', read_only=True)
    system = serializers.CharField(source='ecology.system', read_only=True)
    habitatType = serializers.CharField(source='ecology.habitatType', read_only=True)
    endemicity = serializers.CharField(source='ecology.endemicity', read_only=True)

    class Meta:
        model = Tree
        fields = [
            'nativeName',
            'scientificName',
            'description',
            'otherNames',
            'family',
            'genus',
            'nativeLocation',
            'climate',
            'system',
            'habitatType',
            'endemicity',
            'uses',
        ]

    def get_otherNames(self, obj):
        if hasattr(obj.names, 'get_other_names'):
            return obj.names.get_other_names()
        return []