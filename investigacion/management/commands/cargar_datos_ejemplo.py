from django.core.management.base import BaseCommand
from investigacion.models import Investigacion, Noticia, Destacado
from datetime import date


class Command(BaseCommand):
    help = 'Carga datos de ejemplo basados en los HTMLs originales'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Cargando datos de ejemplo...'))
        
        # Limpiar datos existentes (opcional)
        # Investigacion.objects.all().delete()
        # Noticia.objects.all().delete()
        # Destacado.objects.all().delete()
        
        # Crear Destacados para el carrusel
        self.stdout.write('Creando destacados...')
        destacados = [
            {
                'titulo': 'Innovación en Sistemas de Riego Inteligente',
                'descripcion': 'Explorando nuevas fronteras tecnológicas para la optimización del recurso hídrico en cultivos de la Sabana de Bogotá.',
                'orden': 1,
            },
            {
                'titulo': 'Agricultura de Precisión con Drones',
                'descripcion': 'Implementación de tecnología de sensores remotos para el monitoreo de cultivos en tiempo real.',
                'orden': 2,
            },
            {
                'titulo': 'Sostenibilidad en Poscosecha',
                'descripcion': 'Nuevas técnicas para reducir pérdidas y mejorar la calidad de productos agrícolas.',
                'orden': 3,
            },
        ]
        
        for dest_data in destacados:
            Destacado.objects.get_or_create(
                titulo=dest_data['titulo'],
                defaults=dest_data
            )
        
        # Crear Investigaciones
        self.stdout.write('Creando investigaciones...')
        investigaciones = [
            {
                'titulo': 'Optimización de Riego por Goteo en Cundinamarca',
                'autores': 'García, J. et al.',
                'tags': 'Riego y Drenaje',
                'descripcion': 'Estudio integral sobre la eficiencia del uso del agua en cultivos de hortalizas bajo condiciones controladas en la sabana de Bogotá. Se evaluaron diferentes sistemas de riego por goteo y su impacto en el rendimiento de los cultivos.',
                'fecha_publicacion': date(2023, 5, 15),
            },
            {
                'titulo': 'Diseño de Cosechadora de Café de Bajo Costo',
                'autores': 'Rodríguez, M. & López, D.',
                'tags': 'Maquinaria Agrícola',
                'descripcion': 'Desarrollo de un prototipo funcional diseñado específicamente para pequeños productores, utilizando materiales locales y ergonomía adaptada. El diseño busca reducir costos de producción y mejorar la eficiencia en la cosecha.',
                'fecha_publicacion': date(2022, 8, 20),
            },
            {
                'titulo': 'Tratamiento para Aguacate de Exportación',
                'autores': 'Martínez, A.',
                'tags': 'Poscosecha',
                'descripcion': 'Análisis de metodologías innovadoras para mantener la cadena de frío y la calidad organoléptica del fruto durante trayectos largos. Se estudiaron diferentes tratamientos postcosecha y su efecto en la vida útil del aguacate.',
                'fecha_publicacion': date(2023, 3, 10),
            },
            {
                'titulo': 'Mecanización de Cultivos de Palma Africana',
                'autores': 'Pérez, F. et al.',
                'tags': 'Mecanización',
                'descripcion': 'Investigación sobre el impacto ambiental y la eficiencia energética del uso de tractores autónomos en el campo colombiano. Se evaluó la viabilidad económica y técnica de la mecanización en diferentes tipos de terreno.',
                'fecha_publicacion': date(2021, 11, 5),
            },
            {
                'titulo': 'Sensores Remotos en Agricultura de Precisión',
                'autores': 'Gómez, S.',
                'tags': 'Tecnología',
                'descripcion': 'Implementación de drones equipados con cámaras multiespectrales para el monitoreo en tiempo real de deficiencias de nitrógeno en cultivos de maíz. Los resultados muestran una mejora significativa en la detección temprana de problemas.',
                'fecha_publicacion': date(2023, 1, 18),
            },
            {
                'titulo': 'Gestión de Recursos Hídricos en el Valle',
                'autores': 'Sánchez, R.',
                'tags': 'Hídrica',
                'descripcion': 'Modelado hidrológico avanzado para la planificación de la sostenibilidad de la cuenca del Río Cauca frente al cambio climático. Se desarrollaron modelos predictivos para optimizar el uso del agua en agricultura.',
                'fecha_publicacion': date(2022, 6, 25),
            },
            {
                'titulo': 'Monitoreo con Drones y Sensores Multiespectrales',
                'autores': 'Torres, L. & Vargas, M.',
                'tags': 'Tecnología',
                'descripcion': 'Implementación de vehículos aéreos no tripulados para el diagnóstico temprano de deficiencias nutricionales en palma de aceite. El sistema permite identificar problemas antes de que sean visibles al ojo humano.',
                'fecha_publicacion': date(2023, 9, 12),
            },
            {
                'titulo': 'Modelado Termodinámico de Secado de Granos',
                'autores': 'Herrera, C. & Jiménez, P.',
                'tags': 'Agroindustria',
                'descripcion': 'Estudio de la eficiencia energética en procesos de secado de café mediante el uso de energías renovables y control digital. Se logró reducir el consumo energético en un 30% manteniendo la calidad del producto.',
                'fecha_publicacion': date(2023, 7, 8),
            },
        ]
        
        for inv_data in investigaciones:
            Investigacion.objects.get_or_create(
                titulo=inv_data['titulo'],
                defaults=inv_data
            )
        
        # Crear Noticias
        self.stdout.write('Creando noticias...')
        noticias = [
            {
                'titulo': 'Participación en el V Congreso Panamericano de Ingeniería Agrícola',
                'categoria': 'CONGRESO 2024',
                'descripcion': 'Nuestros investigadores presentaron los avances en teledetección aplicada a cultivos de papa en Cundinamarca. Los resultados fueron muy bien recibidos por la comunidad científica internacional y se establecieron nuevas colaboraciones.',
                'fecha_publicacion': date(2024, 10, 15),
            },
            {
                'titulo': 'Inauguración de la Nueva Planta de Procesamiento de Biomasa',
                'categoria': 'INFRAESTRUCTURA',
                'descripcion': 'Un hito para la Facultad de Ingeniería. El nuevo laboratorio cuenta con equipos de última generación para bioprocesos y permitirá realizar investigaciones de punta en el área de energías renovables.',
                'fecha_publicacion': date(2024, 9, 28),
            },
            {
                'titulo': 'Taller Práctico de Maquinaria Agrícola de Precisión',
                'categoria': 'ACADÉMICO',
                'descripcion': 'Estudiantes de pregrado tuvieron la oportunidad de operar tractores autónomos guiados por GPS en la sede Palmira. La actividad práctica complementó la formación teórica y permitió comprender mejor las tecnologías de agricultura de precisión.',
                'fecha_publicacion': date(2024, 9, 10),
            },
        ]
        
        for not_data in noticias:
            Noticia.objects.get_or_create(
                titulo=not_data['titulo'],
                defaults=not_data
            )
        
        self.stdout.write(self.style.SUCCESS('✓ Datos cargados exitosamente!'))
        self.stdout.write(self.style.SUCCESS(f'  - {Destacado.objects.count()} destacados'))
        self.stdout.write(self.style.SUCCESS(f'  - {Investigacion.objects.count()} investigaciones'))
        self.stdout.write(self.style.SUCCESS(f'  - {Noticia.objects.count()} noticias'))
        self.stdout.write('')
        self.stdout.write(self.style.WARNING('NOTA: Las imágenes y PDFs deben ser cargados manualmente desde el panel de administración.'))
        self.stdout.write(self.style.WARNING('Accede a http://127.0.0.1:8000/admin/ para agregar los archivos.'))
