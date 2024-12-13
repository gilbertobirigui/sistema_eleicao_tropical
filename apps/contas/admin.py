from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from contas.models import MyUser

class MyUserAdmin(UserAdmin): 
    # add_form = UserCreationForm
    model = MyUser
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    
    # 'email': Exibe o campo de email do registro.

    # 'first_name': Exibe o campo de primeiro nome do registro.

    # 'last_name': Exibe o campo de sobrenome do registro.

    # 'is_active': Exibe o campo que indica se o registro está ativo.

    # 'is_staff': Exibe o campo que indica se o registro pertence ao staff (equipe administrativa).
    
    
    
    
    
    
    
    list_filter = ('is_active', 'is_staff')
    
    # list_filter: Esta variável é uma tupla que define quais campos do modelo serão usados como filtros na barra lateral do Django Admin. Isso permite que os administradores filtrem os registros com base nos valores desses campos.

    # 'is_active': Adiciona um filtro para o campo que indica se o registro está ativo.

    # 'is_staff': Adiciona um filtro para o campo que indica se o registro pertence ao staff (equipe administrativa).
    
    
    
    
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined',)

admin.site.register(MyUser, MyUserAdmin)
