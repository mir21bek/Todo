from rest_framework import serializers
from apptodo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ('id', 'status', 'priority', 'title', 'body', 'created', 'status')


class TodoStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title', 'body', 'created', 'status']
