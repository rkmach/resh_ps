from users.models import MyUser
from rest_framework import viewsets, serializers
from users.serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, UserChangeSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from users.backends import EmailOrUsernameModelBackend
from django.http import HttpResponse
from rest_framework import status

from django.core import serializers as core_serializers


class HomePageView(TemplateView, APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    template_name = "home.html"

class RegisterView(APIView):
    model = MyUser
    serializer_class = RegisterSerializer
    renderer_classes = [TemplateHTMLRenderer]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    template_name = "register.html"

    def get(self, request):     #método get simplismente renderiza o formulário. Os campos foram definidos no serializer.
        serializer = RegisterSerializer()
        return render(request, "register.html", {"serializer": serializer})

    def post(self, request):    #trata dos dados vindos do formulário
        serializer = RegisterSerializer(data=request.data)      #serializando os dados
        if(serializer.is_valid()):
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            if MyUser.objects.filter(email=email).exists() or MyUser.objects.filter(username=username).exists():    #email e username são chaves primárias.
                return redirect("pages:register")
            if serializer.validated_data['password'] == serializer.validated_data['password2']:     #se as senhas não forem iguais só recarrega a página.
                serializer.validated_data.pop("password2")  
                new_user = serializer.create(serializer.validated_data) #função definida no serializer que retorna um usuário com os campos preenchidos.
                new_user.set_password(serializer.validated_data['password'])
                new_user.save() #novo usuário salvo no bd
                login(request, new_user)    #novo usuário é loggado automaticamente.
                return redirect("pages:home")
            else:
                return redirect("pages:register")
        return render(request, "register.html", {"serializer": serializer})

    def put(self, request):     #trata dos dados vindos pela API(json)
        serializer = RegisterSerializer(data=request.data)
        if(serializer.is_valid()):
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            if MyUser.objects.filter(email=email).exists() or MyUser.objects.filter(username=username).exists():
                return HttpResponse("Nome de Usuário ou email informado já existe! Escolha outro.\n")
            if serializer.validated_data['password'] == serializer.validated_data['password2']:
                serializer.validated_data.pop("password2")
                new_user = serializer.create(serializer.validated_data)
                new_user.set_password(serializer.validated_data['password'])
                new_user.save()
                login(request, new_user)
                return HttpResponse("Registro criado com sucesso!\n")
            else:
                return HttpResponse("Senhas informadas não são iguais!\n")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class MyUserLoginView(APIView):
    model = MyUser
    serializer_class = LoginSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "login.html"

    def get(self, request):
        serializer = LoginSerializer()
        return render(request, "login.html", {"serializer": serializer})

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if(serializer.is_valid()):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = EmailOrUsernameModelBackend.authenticate(self, request, username=username, password=password)    #essa linha garante que a autenticação pode ser
            if user is not None and user.is_active:                                                                 # feita por email ou username
                login(request, user)
                return redirect("pages:home")
            else:
                return redirect("pages:login")
        return render(request, "login.html", {"serializer": serializer})

class LogoutPageView(LogoutView):       #View de logout padrão do django
    pass

class ChangePasswordView(APIView):
    model = MyUser
    serializer_class = ChangePasswordSerializer
    renderer_classes = [TemplateHTMLRenderer]
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    template_name = "change_password.html"
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = ChangePasswordSerializer()
        return render(request, "change_password.html", {"serializer": serializer})

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = MyUser.objects.get(username=request.user)
            if not user.check_password(serializer.validated_data.get("old_password")):
                return redirect("pages:change_password")
            
            user.set_password(serializer.validated_data.get("new_password"))    #settando a nova senha(essa função cuida das hashes)
            user.save() #salvando as mudanças no bd
            login(request, user)    #logando com o usuário atualizado
            return render(request, 'senha_alterada.html', {})   #página de confirmação de senha alterada

    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = MyUser.objects.get(username=request.user)
            if not user.check_password(serializer.validated_data.get("old_password")):
                return HttpResponse("Senha Atual não é a senha que foi digitada!\n")
            
            user.set_password(serializer.validated_data.get("new_password"))
            user.save()
            return HttpResponse("Senha Atualizada com Sucesso!\n")
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteAccountView(APIView):
    model = MyUser
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = MyUser.objects.get(username=request.user)
        user.is_active = False      #pelo browser, simplismente desativa a conta
        user.save()
        logout(request)

        return redirect("pages:login")

    def delete(self, request):
        try :
            request.user.delete()   #pela API, exclui o user do bd
            return HttpResponse("Usuário removido com sucesso!\n")
        except:
            return HttpResponse("Não foi possível remover o usuário!\n")

class ChangeUserInfoView(generics.UpdateAPIView, APIView):
    model = MyUser
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = UserChangeSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        serializer = UserChangeSerializer()
        return render(request, "change_info.html", {"serializer": serializer})

    def post(self, request):
        serializer = UserChangeSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']     #o usuário não pode mudar seu username e email para o de outro usuário mas pode manter o seu atual.
            if (MyUser.objects.filter(email=email).exists() and MyUser.objects.get(email=email).email != request.user.email) or (MyUser.objects.filter(username=username).exists() and MyUser.objects.get(username=username) != request.user):
                return redirect("pages:change_info")
            user = MyUser.objects.get(username=request.user)
            
            updated_user = serializer.update(user, serializer.validated_data)   #função de atualização no serializer, precisa de todos os campos preenchidos corretamente!
            updated_user.save()     #salva alterações no bd
        else:
            redirect("pages:change_info")

        return redirect("pages:home")

    def put(self, request):
        serializer = UserChangeSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            if (MyUser.objects.filter(email=email).exists() and MyUser.objects.get(email=email).email != request.user.email) or (MyUser.objects.filter(username=username).exists() and MyUser.objects.get(username=username) != request.user):
                return HttpResponse("Nome de usuário ou email já em uso!\n")
            user = MyUser.objects.get(username=request.user)
            updated_user = serializer.update(user, serializer.validated_data)
            updated_user.save()
            return HttpResponse("Dados atualizados com sucesso!\n")
        else:
           return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

