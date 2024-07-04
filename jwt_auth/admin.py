from django.contrib import admin
from django.contrib.auth import get_user_model # A function ghat gets whichever model we set as the AUTH_USER_MODEL is in the project/settings.py

User = get_user_model()
admin.site.register(User)
