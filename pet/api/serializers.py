from rest_framework.serializers import ModelSerializer
from pet.models import Dog, Cat


class DogSerializer(ModelSerializer):

    class Meta:
        model = Dog
        fields = ('owner', 'name', 'birthday')
        extra_kwargs = {
            'owner': {
                'read_only': True
            }
        }


class CatSerializer(ModelSerializer):

    class Meta:
        model = Dog
        fields = ('owner', 'name', 'birthday')
        extra_kwargs = {
            'owner': {
                'read_only': True
            }
        }
