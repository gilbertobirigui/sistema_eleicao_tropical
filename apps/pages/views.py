from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


"""
def: Palavra-chave usada para definir uma função em Python.

index: Nome da função.

request: Parâmetro que representa o objeto de solicitação HTTP. Este objeto 
contém dados sobre a solicitação feita pelo cliente (navegador).
    
return: Palavra-chave que indica o valor que a função deve retornar.

render: Função do Django usada para renderizar um template HTML.

request: O objeto de solicitação HTTP passado como argumento para a função 
        render.

'index.html': Nome do template HTML que será renderizado e enviado como
              resposta ao cliente.


"""