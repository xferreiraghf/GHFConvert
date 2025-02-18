import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from waitress import serve  # Ou outro servidor WSGI de sua escolha

# Configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ghfconverter.settings")  # Substitua 'seu_projeto' pelo nome real do seu projeto

# Configurar o WSGI do Django
application = get_wsgi_application()
application = WhiteNoise(application, root="staticfiles")  # Configurando o WhiteNoise para servir arquivos estáticos

if __name__ == "__main__":
    serve(application, host="0.0.0.0", port=8007)
