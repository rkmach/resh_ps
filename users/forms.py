from django.contrib.auth import forms
#estou usando o meu User, não o do django. (sobrescrevendo atributos da classe pronta!)
from .models import MyUser
from django import forms as forms_fields
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.renderers import TemplateHTMLRenderer

class UserChangeForm(forms.UserChangeForm):
    username = forms_fields.CharField(label="Nome de Usuário", max_length=50, widget=forms_fields.TextInput(attrs={'class': 'form-control'}))
    first_name = forms_fields.CharField(label="Primeiro Nome", max_length=50, widget=forms_fields.TextInput(attrs={'class': 'form-control'}))
    last_name = forms_fields.CharField(label="Último Nome", max_length=50, widget=forms_fields.TextInput(attrs={'class': 'form-control'}))
    email = forms_fields.EmailField(label="Email", max_length=50, widget=forms_fields.EmailInput(attrs={'class': 'form-control'}))
    password = None
    class Meta(forms.UserChangeForm.Meta):
        model = MyUser 
        fields = ('email', 'username', 'first_name', 'last_name')


class UserCreationForm(forms.UserCreationForm): 
    username = forms_fields.CharField(label="Nome de Usuário", max_length=50, widget=forms_fields.TextInput(attrs={'class': 'form-control'}))
    first_name = forms_fields.CharField(label="Primeiro Nome", max_length=50, widget=forms_fields.TextInput(attrs={'class': 'form-control'}))
    last_name = forms_fields.CharField(label="Último Nome", max_length=50, widget=forms_fields.TextInput(attrs={'class': 'form-control'}))
    email = forms_fields.EmailField(label="Email", max_length=50, widget=forms_fields.EmailInput(attrs={'class': 'form-control'}))
    phone = forms_fields.CharField(label="Telefone", max_length=50, widget=forms_fields.TextInput(attrs={'class': 'form-control'}))
    password1 = forms_fields.CharField(label="Nova Senha", max_length=50, widget=forms_fields.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    password2 = forms_fields.CharField(label="Confirme a Nova Senha", max_length=50, widget=forms_fields.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    class Meta(forms.UserCreationForm.Meta): 
        model = MyUser
        fields = ['email', 'username', 'first_name', 'last_name', 'phone']

class UserChangePasswordForm(forms.PasswordChangeForm):     #descobri quais são os campos do formulário olhando o código fonte. Posso colocar css aqui também!
    old_password = forms_fields.CharField(label="Senha Antiga", max_length=50, widget=forms_fields.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms_fields.CharField(label="Nova Senha", max_length=50, widget=forms_fields.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms_fields.CharField(label="Confirme a Nova Senha", max_length=50, widget=forms_fields.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    class Meta:
        model = MyUser
        fields = ('old_password', 'new_password1', 'new_password2')

class RegisterAPIRenderer(BrowsableAPIRenderer):
    def get_context(self, *args, **kwargs):
        context = super(RegisterAPIRenderer, self).get_context(*args, **kwargs)
        context['display_edit_forms'] = True
        form = UserCreationForm()
        context['post_form'] = form 
        return context 