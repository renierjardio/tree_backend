from django.db import models
import json

class Tree(models.Model):
    description = models.TextField()
    uses = models.TextField()
    qrCode = models.CharField(max_length=100, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        if hasattr(self, 'names'):
            return f"{self.names.name} ({self.names.scientificName})"
        return f"Tree #{self.id}"

class TreeNames(models.Model):
    tree = models.OneToOneField(Tree, on_delete=models.CASCADE, related_name='names')
    otherNames = models.TextField(blank=True)
    nativeName = models.CharField(max_length=100)
    scientificName = models.CharField(max_length=100)

    def __str__(self):
        return self.scientificName

    def set_other_names(self, names_list):
        self.otherNames = json.dumps(names_list)

    def get_other_names(self):
        return json.loads(self.otherNames or "[]")

    def validate(self):
        if not self.scientificName or ' ' not in self.scientificName:
            return False
        return True

class Taxonomy(models.Model):
    tree = models.OneToOneField(Tree, on_delete=models.CASCADE, related_name='taxonomy')
    family = models.TextField()
    genus = models.TextField()
    species = models.TextField()

    def __str__(self):
        return f"{self.family} - {self.genus} - {self.species}"
    
class EcologicalBackground(models.Model):
    tree = models.OneToOneField(Tree, on_delete=models.CASCADE, related_name='ecology')
    habitatType = models.TextField()
    nativeLocation = models.TextField()
    system = models.TextField()
    climate = models.TextField()
    endemicity = models.TextField()
    
    def __str__(self):
        return f"Ecological background for {self.tree}"
    
class TreePhoto(models.Model):
    """Model for storing multiple photos per tree"""
    tree = models.ForeignKey(Tree, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='treePhotos/')
    caption = models.CharField(max_length=200, blank=True)
    isPrimary = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Photo for {self.tree}"

class TreeModel(models.Model):
    """Model for storing 3D model files for trees"""
    tree = models.ForeignKey(Tree, related_name='models', on_delete=models.CASCADE)
    modelFile = models.FileField(upload_to='treeModels/')
    description = models.CharField(max_length=200, blank=True)
    fileFormat = models.CharField(max_length=50)  # e.g., "glb", "obj", etc.
    
    def __str__(self):
        return f"3D Model for {self.tree}"
