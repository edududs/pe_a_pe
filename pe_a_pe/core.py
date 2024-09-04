from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.response import Response
from rest_framework import status
import requests


class JWTRefreshMiddleware(MiddlewareMixin):

    def process_request(self, request):
        authorization_header = request.headers.get("Authorization")

        if authorization_header is not None:
            try:
                # Extrair o token do header Authorization
                token = authorization_header.split(" ")[1]
                access_token = AccessToken(token)

                # Verifica se o token está expirado
                if access_token.is_valid():
                    return None  # Token é válido, segue com a requisição

            except (TokenError, InvalidToken):
                # Se o token é inválido ou expirado, tentamos renovar
                refresh_token = request.COOKIES.get("refresh_token")

                if refresh_token:
                    try:
                        new_access_token = self.get_new_access_token(refresh_token)
                        if new_access_token:
                            # Substituir o token antigo pelo novo na requisição
                            request.META["HTTP_AUTHORIZATION"] = (
                                f"Bearer {new_access_token}"
                            )
                        else:
                            return Response(
                                {"error": "Unable to refresh token."},
                                status=status.HTTP_401_UNAUTHORIZED,
                            )

                    except TokenError:
                        return Response(
                            {"error": "Refresh token expired."},
                            status=status.HTTP_401_UNAUTHORIZED,
                        )

        return None

    def get_new_access_token(self, refresh_token):
        """Envia uma requisição POST para obter um novo access token usando o refresh token"""
        refresh_token = RefreshToken(refresh_token)
        try:
            new_access_token = refresh_token.access_token
            return str(new_access_token)
        except TokenError:
            return None
