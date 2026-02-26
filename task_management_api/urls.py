from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({
        "message": "Welcome to the Task Management API",
        "status": "running",
        "endpoints": {
            "admin": "/admin/",
            "tasks": "/api/tasks/",
            "users": "/api/users/",
            "login": "/api-auth/login/",
            "logout": "/api-auth/logout/"
        },
        "description": "This API allows users to manage their tasks with full CRUD functionality."
    })

urlpatterns = [
    path('', api_home),  # professional API root
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),
    path('api/users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
