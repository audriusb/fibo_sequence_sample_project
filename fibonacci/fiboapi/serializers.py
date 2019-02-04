"""
App serializers
"""

import copy
from rest_framework import serializers

from fibonacci.settings import MAX_SEQUENCE_LENGTH

class SeqenceSerializer(serializers.BaseSerializer):
    """
    Simple serializer.
    """
    def to_representation(self, obj):
        """
        Object representation dictionary
        """
        return {
            'length': obj['length'],
            'sequence': obj['sequence'],
        }