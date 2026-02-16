from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Crea el superusuario por defecto con credenciales admin/admin'

    def handle(self, *args, **options):
        User = get_user_model()
        
        username = 'admin'
        email = 'julianrf527@gmail.com'
        password = 'admin'
        
        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'El usuario "{username}" ya existe.')
            )
            
            # Preguntar si quiere actualizar la contraseña
            user = User.objects.get(username=username)
            user.email = email
            user.set_password(password)
            user.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'✓ Contraseña actualizada para "{username}"')
            )
        else:
            # Crear el superusuario
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'✓ Superusuario creado exitosamente!')
            )
        
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('Credenciales de acceso:'))
        self.stdout.write(f'  Usuario: {username}')
        self.stdout.write(f'  Contraseña: {password}')
        self.stdout.write(f'  Email: {email}')
        self.stdout.write('')
        self.stdout.write('Accede al panel de administración en:')
        self.stdout.write('  http://127.0.0.1:8000/admin/')
        self.stdout.write('')
