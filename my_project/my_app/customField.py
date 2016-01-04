import base64
from rest_framework import serializers

# Custom image field - handles base 64 encoding/decoding
class Base64Field(serializers.Field):
    def get_attribute(self, obj):
        image = getattr(obj, 'image')
        obj = image
        return obj

    def to_internal_value(self, obj):
        return base64.b64decode(obj)

    def to_representation(self, obj):
        return base64.b64encode(obj)


