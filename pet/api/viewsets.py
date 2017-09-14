from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .permissions import AccessOwnPet
from .serializers import DogSerializer, CatSerializer
from pet.models import Dog, Cat


class DogViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, AccessOwnPet)
    serializer_class = DogSerializer
    queryset = Dog.objects.all()

    def perform_create(self, serializer):
        'sets the owner to logged in user'
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CatViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, AccessOwnPet)
    serializer_class = CatSerializer
    queryset = Cat.objects.all()

    def perform_create(self, serializer):
        'sets the owner to logged in user'
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class LoginViewSet(ViewSet):
    '''Check email and password and returns an auth token'''

    serializer_class = AuthTokenSerializer

    def create(self, request):
        '''use ObtainAuthToken APIView to validate and create a token'''
        return ObtainAuthToken().post(request)
