import os
import sys
from pathlib import Path

# Ensure project root is on sys.path so Django settings can be imported
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'semillero_project.settings')
import django
django.setup()

from investigacion.models import Investigacion, Noticia, Destacado

print('Investigacion', Investigacion.objects.count())
print('Noticia', Noticia.objects.count())
print('Destacado', Destacado.objects.count())
