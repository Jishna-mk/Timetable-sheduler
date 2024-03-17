
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Student

class ApprovalBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        user = super().authenticate(request, username=username, password=password, **kwargs)

        if user and user.is_superuser:
            
            try:
                teacher = user.teacher
                if not teacher.is_approved:
                    
                    return None
            except Student.DoesNotExist:
                pass 

        return user
