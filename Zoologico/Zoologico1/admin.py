from django.contrib import admin
from .models import (
    Cliente,
    Empleado,
    Animal,
    Veterinario,
    Cuidador,
    Guia,
    PersonalLimpieza,
    PersonalAdministrativo,
    Boleto,
)

admin.site.register(Boleto)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'cedula']  # Campos de búsqueda
    list_filter = ['genero', 'edad']  # Filtros por género y edad
    list_display = ['nombre', 'apellido', 'cedula', 'edad', 'telefono']  # Información en lista

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    search_fields = ['nombre',  'nombre_cientifico']  # Campos de búsqueda
    list_filter = ['tipo_dieta', 'estado', 'edad']  # Filtros personalizados
    list_display = ['nombre',  'nombre_cientifico', 'tipo_dieta', 'estado', 'edad']  # Información en lista

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'cedula', 'identificacion']  # Campos de búsqueda
    list_filter = ['genero', 'edad', 'salario']  # Filtros personalizados
    list_display = ['nombre', 'apellido', 'cedula', 'identificacion', 'salario']  # Información en lista

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'cedula', 'especialidad']  # Campos de búsqueda
    list_filter = ['especialidad']  # Filtro por especialidad
    list_display = ['nombre', 'apellido', 'cedula', 'especialidad', 'salario']

@admin.register(Cuidador)
class CuidadorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'cedula']  # Campos de búsqueda
    list_filter = ['edad', 'genero']  # Filtros por edad y género
    list_display = ['nombre', 'apellido', 'cedula', 'edad', 'salario']

@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'cedula']  # Campos de búsqueda
    list_filter = ['genero']  # Filtro por género
    list_display = ['nombre', 'apellido', 'cedula', 'edad', 'salario']

@admin.register(PersonalLimpieza)
class PersonalLimpiezaAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'cedula']  # Campos de búsqueda
    list_display = ['nombre', 'apellido', 'cedula', 'edad', 'salario']

@admin.register(PersonalAdministrativo)
class PersonalAdministrativoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'cedula']  # Campos de búsqueda
    list_filter = ['edad']  # Filtros por edad
    list_display = ['nombre', 'apellido', 'cedula', 'edad', 'salario']