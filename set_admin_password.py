from django.contrib.auth import get_user_model

User = get_user_model()
try:
    user = User.objects.get(username='admin')
    user.set_password('password123')
    user.save()
    print("Password for user 'admin' set successfully.")
except User.DoesNotExist:
    print("User 'admin' not found.")
