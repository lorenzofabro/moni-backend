from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ObtenerTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(ObtenerTokenSerializer, cls).get_token(user)

        token['username'] = user.username
        return token
