from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

User = get_user_model()

# we're going to extend the BasicAuthentication class, because it already has things like password and email validation

class JWTAuthentication(BasicAuthentication):
    def authenticate(self, request):
        header = request.headers.get('Authorization')
        print(header)
        # if there's no authentication headers, just return none to end the request
        if not header:
            return None
        
        # check if the token starts with Bearer (it is a jwt token)
        if not header.startswith('Bearer'):
            raise PermissionDenied(detail="Invalid Auth Token")
        
        # remove the Bearer part of the string and store the token as a variable called token
        token = header.replace('Bearer ', '')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            # find the user in the database using the sub from the token
            user = User.objects.get(pk=payload.get('sub'))

        # if the token has expired or has incorrect formatting - error
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied(detail="Invalid Token")
        
        # if the user doesn't exist - error
        except User.DoesNotExist:
            raise PermissionDenied(detail="User not found")

        # if everything checks out, return the user and the token
        return (user, token)