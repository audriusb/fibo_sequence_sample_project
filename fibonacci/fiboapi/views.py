"""
REST api views
"""
import coreapi
import coreschema
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.schemas import SchemaGenerator
from rest_framework import response, schemas
from rest_framework.schemas import AutoSchema
from rest_framework import status

from fibonacci.fiboapi.generators import Fibonacci_Sequence
from fibonacci.fiboapi.serializers import SeqenceSerializer

from fibonacci.settings import MAX_SEQUENCE_LENGTH, DEFAULT_SEQUENCE_START


class FiboSeqView(ViewSet):
    """
    Generates fibonnaci sequence with requested legth starting with 0
    Currently limited to 5000 numbers due to size of response. Change it in settings.py
    """
    schema = AutoSchema( #Describe schema for swagger
            manual_fields=[
                coreapi.Field(
                    name='length',
                    location='query',
                    schema=coreschema.Integer(description='How long the sequence has to be produced. Max ' + str(MAX_SEQUENCE_LENGTH)),
                    required=True
                ),
            ],

        )
    def list(self, request):
        """
        Get the sequence
        """
        start = DEFAULT_SEQUENCE_START #currently api requirements only need to start from 0
        try:
            end = int(request.query_params['length'])
        except:
            return Response({'error': 'Invalid range requested'}, status=status.HTTP_400_BAD_REQUEST)
        if start < 0 or end > MAX_SEQUENCE_LENGTH or end < 0:
            return Response({'error': 'Invalid range requested'}, status=status.HTTP_400_BAD_REQUEST)
        result = Fibonacci_Sequence.generate_fibonnaci_seq(start,end)
        serializer = SeqenceSerializer(result)
        return Response(serializer.data)

