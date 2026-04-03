from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token


class CookieTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        token_key = request.COOKIES.get('token')

        if not token_key:
            return None
            
        return self.authenticate_credentials(token_key)
