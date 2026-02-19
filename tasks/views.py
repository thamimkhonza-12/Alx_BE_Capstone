from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # FIXED: use user instead of owner
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # FIXED: use user instead of owner
        serializer.save(user=self.request.user)


class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # FIXED: use user instead of owner
        return Task.objects.filter(user=self.request.user)
