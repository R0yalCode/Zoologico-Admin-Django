
# Zoológico Royal

Este es un proyecto de un **Zoológico** implementado con **Django**. Permite gestionar diversas entidades relacionadas con el zoológico, como animales, empleados, jaulas, boletos, y más. La aplicación incluye funcionalidades como filtros, búsqueda avanzada y formularios de relación de uno a muchos.

## Funcionalidades Principales

### 1. **Filtros**
La aplicación permite aplicar filtros para buscar animales, empleados o personas por diferentes criterios. Por ejemplo:

- **Animales**: Nombre, tipo de dieta, estado (como "Comiendo", "Dormido", etc.), edad mínima y máxima.
#### Ejemplo de búsqueda de animales:

![BusquedaAnimales](https://github.com/user-attachments/assets/3b807352-bf0a-458a-a92e-18faef047cd9)
> Ejemplo donde se puede buscar a los animales registrados implementando filtros
  
- **Empleados**: Nombre, edad, género. 
#### Ejemplo de búsqueda de Empleados:
![BusquedaEmpleados](https://github.com/user-attachments/assets/4b63954a-bab2-475b-92d2-25f05de2a6cf)
> Ejemplo donde se puede buscar a los empleados registrados implementando filtros
  
- **Personas**: Nombre, apellido, cedula, telefono, género y edad.
#### Ejemplo de búsqueda de Clientes:
![BusquedaClientes](https://github.com/user-attachments/assets/e6213a0a-4cb5-48e4-ae3a-16424ea28aa4)
> Ejemplo donde se puede buscar a los Clientes registrados implementando filtros

La lógica de filtrado se realiza mediante la clase `BusquedaManager`, que proporciona métodos de búsqueda flexible.

### 2. **Presentación de Diferentes Tipos de Datos (Columnas)**
En las vistas de administración, se presentan las entidades (animales, empleados, clientes, etc.) en tablas, con columnas que incluyen información relevante, como:

- **Animales:** Nombre, edad, peso, tipo de dieta, tipo de cuerpo y estado.
![image](https://github.com/user-attachments/assets/663f10f4-04f2-4d5a-bceb-076c4d06a25c)


- **Empleados:** Nombre, apellido, cedula, edad, tipo de empleado, salario (si aplica).
![image](https://github.com/user-attachments/assets/2352ee12-f01b-4ee8-a6c8-ec3679262c9f)


- **Clientes:** Nombre, edad, correo electrónico, boletos comprados.
![image](https://github.com/user-attachments/assets/4a58858e-b595-43cb-b7fb-b226085c059d)


### 3. Relación de Uno a Muchos (Formulario Padre-Hijo)
En la relación de uno a muchos, puedes registrar un "padre" (por ejemplo, un zoológico o una jaula) y asociar múltiples "hijos" (animales que pertenecen a esa jaula). Este tipo de relación está implementado usando los campos ForeignKey y ManyToManyField.


### 4. Otras Funcionalidades
- Historial médico para cada animal, con un historial de diagnósticos y tratamientos.
- Manejo de empleados, incluyendo cuidadores, veterinarios, personal de limpieza, y guías turísticos.
- Boletos de entrada para clientes, que almacenan información como la fecha de la visita, el número de boleto y su valor.

#### Modelos en el Proyecto
- **Zoologico:** Almacena la información básica del zoológico, como nombre, capacidad y teléfono.
- **Animal:** Representa a los animales del zoológico, con campos como nombre, edad, tipo de dieta, estado de salud, etc.
-** Empleado:** Hereda de Persona y tiene clases específicas como Cuidador, Veterinario, etc.

# Instalación y Configuración
## Requisitos
- Python 3.8+
- Django 3.x o superior
- Base de datos: SQLite (por defecto) o puedes configurar PostgreSQL/MySQL

### **Paso 1: Clonar el repositorio**

    git clone https://github.com/R0yalCode/Zoologico-Admin-Django.git
    cd zoologico

### **Paso 2: Configurar la base de datos**
Si usas SQLite, no es necesario hacer configuraciones adicionales. Si usas otra base de datos (como PostgreSQL o MySQL), asegúrate de configurar correctamente las opciones en el archivo settings.py.

### **Paso 3: Ejecutar migraciones**
    python manage.py migrate

### Paso 4: Crear un superusuario
    python manage.py createsuperuser

###     Paso 6: Iniciar el servidor de desarrollo
    python manage.py runserver

Ahora puedes acceder al panel de administración de Django en http://localhost:8000/admin.
