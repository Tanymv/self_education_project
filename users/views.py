from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, UserDetailSerializer


class UserCreateView(generics.CreateAPIView):
    """Регистрация нового пользователя"""
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """Переопределение метода для сохранения хешированного пароля в бд (если пароль не хешируется -
        пользователь не считается активным и токен авторизации не создается)"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.is_active = True
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserDetailView(generics.RetrieveAPIView):
    """Просмотр профиля пользователя"""
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()


class UserUpdateView(generics.UpdateAPIView):
    """Редактирование профиля пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteView(generics.DestroyAPIView):
    """Удаление профиля пользователя"""
    queryset = User.objects.all()


class UserListView(generics.ListAPIView):
    """Просмотр списка зарегистрированных пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
