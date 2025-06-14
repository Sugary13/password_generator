# 🔐 Password Manager (Tkinter App)

Aplicación de escritorio desarrollada con **Python** y **Tkinter** que permite generar, guardar y gestionar contraseñas de forma segura y rápida. Ideal para mejorar tu productividad y mantener tus credenciales organizadas.

---

## 🧩 Funcionalidades

- ✅ **Generador de contraseñas seguras** con letras, números y símbolos
- ✅ **Autocompletado de email/usuario**
- ✅ **Copia automática al portapapeles**
- ✅ **Guardado en archivo local (`data.txt`)**
- ✅ Validación de campos vacíos y confirmación previa al guardado
- ✅ Interfaz amigable y sencilla con `Tkinter`

---

## 🚀 Cómo usarlo

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener **Python 3.x** instalado.
3. Instala la librería `pyperclip` si no la tienes:

```bash
pip install pyperclip
python main.py
```

.

├── main.py          # Código principal de la app

├── data.txt         # Archivo donde se guardan las contraseñas (generado en ejecución)

├── logo.png         # Imagen del logo usada en el encabezado

└── README.md        # Este archivo

💡 Ejemplo de uso

Escribe el nombre del sitio web.

Ingresa tu correo o nombre de usuario.

Haz clic en Generate Password (o escribe uno propio).

Haz clic en Add para guardar.

El password se copiará automáticamente al portapapeles.

🔐 Seguridad

Este gestor guarda las contraseñas en texto plano (data.txt). No es recomendado para producción sin cifrado. Para mejorar la seguridad podrías:

Usar cifrado con cryptography o fernet

Guardar datos en archivos .json estructurados

Agregar protección con clave maestra

🛠 Tecnologías utilizadas
Python 3

Tkinter – Interfaz gráfica

random – Generación aleatoria de contraseñas

pyperclip – Copiar contraseñas al portapapeles

messagebox – Alertas de confirmación
