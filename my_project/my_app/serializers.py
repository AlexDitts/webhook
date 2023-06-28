from rest_framework import serializers


class VarEnvSerializer(serializers.Serializer):
    var = serializers.CharField()


class HookSerializer(serializers.Serializer):
    hook = serializers.CharField(required=False)
    push_event = serializers.CharField(required=False)
    event_name = serializers.CharField(required=False)
    object_kind = serializers.CharField(required=False)
