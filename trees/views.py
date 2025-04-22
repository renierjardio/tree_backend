from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tree
from .serializers import TreeSerializer

class TreeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows trees to be viewed or edited.
    """
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

@api_view(['GET'])
def getTreeByQr(request, qrCode):
    """
    API endpoint to get tree information by QR code
    """
    try:
        tree = Tree.objects.get(qrCode=qrCode)
        serializer = TreeSerializer(tree)
        return Response(serializer.data)
    except Tree.DoesNotExist:
        return Response({"error": "Tree not found"}, status=404)