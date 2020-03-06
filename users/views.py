from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action

import re

from utils import get_or_none

from .models import ModifiedUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """API endpoints pertaining to users.

    GET /users                  Get list of all users.
    GET /users/<id>             Get information of a single user.
    PUT /users/<id>             Update user information.

    POST /users/login           Login user.
    POST /users/create-account  Create user account.
    """
    
    queryset = ModifiedUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    @action(detail=False, url_path='create-account')
    @csrf_exempt
    def create_account_view(self, request):
        """Verify a user's entered email and password while creating account.

        POST data --
            'email': string
            'password': string

        Returns --
            'success': boolean
            'message': string
            'user': int // None if account creation unsuccessful
        """

        input_email = request.POST.get('email')
        input_password = request.POST.get('password')

        message = 'Email already exists'

        user = get_or_none(ModifiedUser, email=input_email)
        if not user:
            if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", input_password):
                user = get_user_model().objects.create_user(email=input_email, password=input_password)
                return JsonResponse({'success': True, 'message': 'Account creation successful', 'user': user.id})
            else:
                message = 'Invalid password. Must have at least 8 characters, at least 1 uppercase letter, at least 1 lowercase letter and at least 1 number'

        return JsonResponse({'success': False, 'message': message, 'user': None})

    @action(detail=False, url_path='login')
    @csrf_exempt
    def login_view(self, request):
        """Verify a user's entered email and password while logging in.

        POST data --
            'email': string
            'password': string

        Returns --
            'success': boolean
            'message': string
            'user': int // only if login successful
        """
        input_email = request.POST.get('email')
        input_password = request.POST.get('password')

        message = 'Email not found'

        user = get_or_none(ModifiedUser, email=input_email)
        if user:
            if user.check_password(input_password):
                return JsonResponse({'success': True, 'message': 'Login successful', 'user': user.id})
            else:
                message = 'Wrong password'
        
        return JsonResponse({'success': False, 'message': message, 'user': None})