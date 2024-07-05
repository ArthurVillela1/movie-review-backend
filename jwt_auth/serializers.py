from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation # password_validation is the function that runs when we create a superuser
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # when a user is being converted back to JSON ready for teruning to the user, password & password confirmation are not going to be returned
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    
    # validate that the password and password_confirmation match
    # hash the password
    # add to the database
    def validate(self, data): # <-- data is going to come from the request.body
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'passwords do no match'})
        
        # validate the password meets the criterie
        try:
            password_validation.validate_password(password=password)
        except ValidationError as err:
            raise ValidationError({'password': err.messages})

        # hash the password
        data['password'] = make_password(password)

        return data

    class Meta:
        model = User
        fields = '__all__'