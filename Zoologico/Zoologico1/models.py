from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Enumeraciones
class Estado(models.TextChoices):
    COMIENDO = 'COMIENDO', _('Comiendo')
    DORMIDO = 'DORMIDO', _('Dormido')
    ENFERMO = 'ENFERMO', _('Enfermo')
    ESTRESADO = 'ESTRESADO', _('Estresado')
    HAMBRIENTO = 'HAMBRIENTO', _('Hambriento')
    HERIDO = 'HERIDO', _('Herido')
    NORMAL = 'NORMAL', _('Normal')

class TipoDieta(models.TextChoices):
    CARNIVORO = 'CARNIVORO', _('Carnívoro')
    HERVIVORO = 'HERVIVORO', _('Hervívoro')
    OMNIVORO = 'OMNIVORO', _('Omnívoro')

class TipoCuerpo(models.TextChoices):
    INVERTEBRADO = 'INVERTEBRADO', _('Invertebrado')
    VERTEBRADO = 'VERTEBRADO', _('Vertebrado')

class Zona(models.TextChoices):
    ESTE = 'ESTE', _('Este')
    NORTE = 'NORTE', _('Norte')
    OESTE = 'OESTE', _('Oeste')
    SUR = 'SUR', _('Sur')

class TipoAlimento(models.TextChoices):
    CARNE = 'CARNE', _('Carne')
    PESCADO = 'PESCADO', _('Pescado')
    HIERBA = 'HIERBA', _('Hierba')
    FRUTA = 'FRUTA', _('Fruta')

# Modelos principales
class Zoologico(models.Model):
    capacidad = models.IntegerField()
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

class Direccion(models.Model):
    calle_principal = models.CharField(max_length=255)
    calle_secundaria = models.CharField(max_length=255)
    referencia = models.TextField()
    zoologico = models.OneToOneField(Zoologico, on_delete=models.CASCADE, related_name="direccion")

class SerVivo(models.Model):
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nombre = models.CharField(max_length=255)

    def calcular_edad(self):
        from datetime import date
        return date.today().year - self.fecha_nacimiento.year

class Animal(SerVivo):
    edad = models.IntegerField()
    nombre_cientifico = models.CharField(max_length=255)
    peso = models.FloatField()
    tipo_dieta = models.CharField(max_length=20, choices=TipoDieta.choices, default=TipoDieta.OMNIVORO)
    tipo_cuerpo = models.CharField(max_length=20, choices=TipoCuerpo.choices, default=TipoCuerpo.VERTEBRADO)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.NORMAL)

    def _str_(self):
        return f'Animal: {self.nombre}'

class HistorialMedico(models.Model):
    diagnostico = models.TextField()
    fecha = models.DateField()
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="historial_medico")

    def _str_(self):
        return f'Historial de {self.animal.nombre}'

class Jaula(models.Model):
    capacidad = models.IntegerField()
    esta_limpio = models.BooleanField(default=True)
    numero_jaula = models.CharField(max_length=20)
    zona = models.CharField(max_length=20, choices=Zona.choices, default=Zona.NORTE)
    animales = models.ManyToManyField(Animal, related_name="jaulas")

class Persona(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    apellido = models.CharField(max_length=255, null=True, blank=True)
    cedula = models.CharField(max_length=20)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15, null=True, blank=True)
    correo = models.CharField(max_length=50, null=True, blank=True)
    genero = models.CharField(max_length=10, choices=[('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino')], null=True, blank=True)

class Empleado(Persona):
    identificacion = models.IntegerField()
    salario = models.FloatField()

class Cuidador(Empleado):
    def cuidar_animal(self):
        pass

    def dar_comida(self):
        pass

class Veterinario(Empleado):
    especialidad = models.CharField(max_length=255)

    def realizar_diagnostico(self):
        pass

    def realizar_tratamiento(self):
        pass

    def verificar_especialidad(self):
        pass

class PersonalLimpieza(Empleado):
    def limpiar_jaula(self):
        pass

    def _str_(self):
        return f"Nombre del empleado: {self.nombre}"

class PersonalAdministrativo(Empleado):
    def gestionar_recursos(self):
        pass

class Guia(Empleado):
    clientes = models.ManyToManyField('Cliente', related_name="guias")

    def agregar_cliente(self, cliente):
        self.clientes.add(cliente)

    def establecer_recorrido(self):
        pass

    def mostrar_cliente(self):
        return self.clientes.all()

class Cliente(Persona):
    def comprar_boleto(self):
        pass

    def listar_informacion(self):
        pass

    def __str__(self):
        return self.nombre

class Boleto(models.Model):
    fecha_visita = models.DateField()
    numero = models.IntegerField()
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="boletos")

    def __str__(self):
        return f"Boleto: {self.numero}"

# Funciones de búsqueda
class BusquedaManager(models.Manager):
    def buscar_personas(self, nombre=None, genero=None, edad_min=None, edad_max=None, tipo_persona=None):
        query = Q()
        if nombre:
            query &= Q(nombre_icontains=nombre) | Q(apellido_icontains=nombre)
        if genero:
            query &= Q(genero=genero)
        if edad_min is not None:
            query &= Q(edad__gte=edad_min)
        if edad_max is not None:
            query &= Q(edad__lte=edad_max)
        if tipo_persona == 'cliente':
            query &= Q(cliente__isnull=False)
        elif tipo_persona == 'empleado':
            query &= Q(empleado__isnull=False)
        return self.filter(query)

    def buscar_animales(self, nombre=None, tipo_dieta=None, estado=None, edad_min=None, edad_max=None):
        query = Q()
        if nombre:
            query &= Q(nombre_icontains=nombre) | Q(apodo_icontains=nombre)
        if tipo_dieta:
            query &= Q(tipo_dieta=tipo_dieta)
        if estado:
            query &= Q(estado=estado)
        if edad_min is not None:
            query &= Q(edad__gte=edad_min)
        if edad_max is not None:
            query &= Q(edad__lte=edad_max)
        return self.filter(query)

    def buscar_empleados(self, tipo_empleado=None, **kwargs):
        query = self.buscar_personas(tipo_persona='empleado', **kwargs)
        if tipo_empleado == 'cuidador':
            query = query.filter(cuidador__isnull=False)
        elif tipo_empleado == 'veterinario':
            query = query.filter(veterinario__isnull=False)
        elif tipo_empleado == 'personal_limpieza':
            query = query.filter(personallimpieza__isnull=False)
        elif tipo_empleado == 'administrativo':
            query = query.filter(personaladministrativo__isnull=False)
        elif tipo_empleado == 'guia':
            query = query.filter(guia__isnull=False)
        return query

class EmpleadoManager(BusquedaManager):
    pass

class ClienteManager(BusquedaManager):
    pass

class AnimalManager(models.Manager):
    def buscar(self, **kwargs):
        return self.buscar_animales(**kwargs)

# Asignación de managers
Empleado.objects = EmpleadoManager()
Cliente.objects = ClienteManager()
Animal.objects = AnimalManager()