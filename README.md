````markdown
# La Caffettiera

## Descripción

**La Caffettiera** es un sitio web didáctico de cafetería, construido con Django. Demuestra buenas prácticas en arquitecturas multi‑sección: página de inicio, servicios, blog, páginas informativas y formulario de contacto.

## Tecnologías

- **Python 3 & Django**  
- **SQLite** (desarrollo)  
- **HTML5, CSS3 & Bootstrap 4**  
- **JavaScript & jQuery**  
- **Django CKEditor**  
- **Font Awesome**  
- **SMTP** para envío de correos

## Instalación

1. Clona el repositorio:  
   ```bash
   git clone <url>
   cd Cafeteria.py
````

2. Crea y activa un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```
4. Configura el correo (opcional):

   * Crea `email_settings.json` con credenciales SMTP o ajusta `settings.py`.
5. Ejecuta migraciones:

   ```bash
   python manage.py migrate
   ```
6. Crea superusuario (opcional):

   ```bash
   python manage.py createsuperuser
   ```
7. Inicia el servidor:

   ```bash
   python manage.py runserver
   ```

   Accede en `http://127.0.0.1:8000/` y al admin en `/admin/`.

## Funcionalidades

* **Inicio & páginas estáticas**: Historia, Visítanos.
* **Servicios**: CRUD de productos via modelo `Service`.
* **Blog**: Entradas con categorías (modelo `Post`).
* **Páginas dinámicas**: Modelo `Page` y CKEditor.
* **Contacto**: Formulario con envío SMTP.
* **Redes sociales**: Modelo `Link` para gestionar enlaces.
* **Admin**: Gestión completa de contenido sin tocar código.

## Créditos

Desarrollado por **Nassim Wessin** como ejercicio práctico. Basado en la plantilla “Business Casual” de Start Bootstrap (MIT).

```

**Explicación breve:**  
1. Estructuré secciones claras y concisas.  
2. Usé listados y comandos formateados.  
3. Ajusté tono profesional y directo.
```
