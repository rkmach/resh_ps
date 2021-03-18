from .models import MyUser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

#serializers tem funções importantes, como criar, atualizar, validar, serializar, além de propriedades para forms
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="Nome de Usuário", max_length=50)
    first_name = serializers.CharField(label="Primeiro Nome", max_length=50)
    last_name = serializers.CharField(label="Último Nome", max_length=50)
    email = serializers.EmailField(label="Email", max_length=50)
    phone = serializers.CharField(label="Telefone", max_length=15)
    password = serializers.CharField(label="Senha", write_only=True, required=True, validators=[validate_password], style={'input_type': 'password', 'placeholder': '8+ caracteres'})
    password2 = serializers.CharField(label="Confirme sua Senha",write_only=True, required=True, style={'input_type': 'password', 'placeholder': ''})

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'phone', 'first_name', 'last_name', 'password', 'password2']

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.password = validated_data.get('password', instance.password)
        return instance

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="Email ou Nome de Usuário", max_length=50)
    password = serializers.CharField(label="Senha", write_only=True, required=True, validators=[validate_password], style={'input_type': 'password', 'placeholder': 'Password'})
    class Meta:
        model = MyUser
        fields = ['username', 'password']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(label="Senha Antiga", write_only=True, required=True, validators=[validate_password], style={'input_type': 'password'})
    new_password = serializers.CharField(label="Nova Senha",write_only=True, required=True, style={'input_type': 'password', 'placeholder': '8+ caracteres'})
    class Meta:
        model = MyUser
        fields = ['old_password', 'new_password']

class UserChangeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="Nome de Usuário", max_length=50, required=True)
    first_name = serializers.CharField(label="Primeiro Nome", max_length=50, required=True)
    last_name = serializers.CharField(label="Último Nome", max_length=50, required=True)
    email = serializers.EmailField(label="Email", max_length=50, required=True)
    phone = serializers.CharField(label="Telefone", max_length=15, required=True)

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'phone', 'first_name', 'last_name']

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.phone = validated_data.get('phone', instance.phone)
        return instance

class MyUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="Nome de Usuário", max_length=50)
    first_name = serializers.CharField(label="Primeiro Nome", max_length=50)
    last_name = serializers.CharField(label="Último Nome", max_length=50)
    email = serializers.EmailField(label="Email", max_length=50)
    phone = serializers.CharField(label="Telefone", max_length=15)
    

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'phone', 'first_name', 'last_name']
