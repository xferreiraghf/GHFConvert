import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from waitress import serve 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ghfconverter.settings") 

application = get_wsgi_application()
application = WhiteNoise(application, root="staticfiles") 

if __name__ == "__main__":
    serve(application, host="0.0.0.0", port=8007)
