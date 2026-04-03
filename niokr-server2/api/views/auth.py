from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from ..models import User


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        external_id = request.data.get('external_id')
        if not external_id:
            return Response({'detail': 'Поле external_id обязательно.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(external_id=external_id)
        except User.DoesNotExist:
            return Response({'detail': 'Пользователь не найден.'}, status=status.HTTP_404_NOT_FOUND)
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        response = Response(status=status.HTTP_200_OK)
        response.set_cookie(
            key='token',
            value=token.key,
            httponly=True,
            samesite='Lax',
        )
        return response


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, _):
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('token')
        return response
