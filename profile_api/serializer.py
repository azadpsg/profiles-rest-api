from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializer name field for testing"""
    name = serializers.CharField(max_length=10)
