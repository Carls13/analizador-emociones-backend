# Proyecto Flask

Este proyecto es una aplicación web sencilla construida con [Flask](https://flask.palletsprojects.com/).

## Requisitos previos

- Tener instalado **Python 3.8** o superior.  
  Puedes verificar si tienes Python instalado ejecutando:

  ```bash
  python --version
  ```

  o, dependiendo de tu sistema operativo:

  ```bash
  python3 --version
  ```

- Tener **pip** instalado (normalmente viene junto con Python).

## Instalación de Python

Si no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/downloads/).

Recuerda marcar la opción **"Add Python to PATH"** al momento de instalar.

---

## Instrucciones para correr el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2. Crear un entorno virtual

Crear un entorno virtual es una buena práctica para mantener las dependencias organizadas.

- En Windows:

  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

- En MacOS/Linux:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar dependencias

Una vez activado el entorno virtual, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

> **Nota:** Si no existe un archivo `requirements.txt`, puedes instalar Flask directamente:

```bash
pip install Flask
```

Y luego generar el archivo de dependencias:

```bash
pip freeze > requirements.txt
```

### 4. Configurar variables de entorno (opcional)

Si tu aplicación necesita variables de entorno como `FLASK_APP` o `FLASK_ENV`, puedes configurarlas así:

- En Windows (cmd):

  ```bash
  set FLASK_APP=app.py
  set FLASK_ENV=development
  ```

- En Windows (PowerShell):

  ```bash
  $env:FLASK_APP = "app.py"
  $env:FLASK_ENV = "development"
  ```

- En MacOS/Linux:

  ```bash
  export FLASK_APP=app.py
  export FLASK_ENV=development
  ```

### 5. Correr la aplicación

Finalmente, corre la aplicación localmente:

```bash
flask run
```

La aplicación estará disponible en [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Estructura típica del proyecto

```plaintext
/tu-repo
│
├── app.py
├── requirements.txt
├── /templates
│   └── index.html
├── /static
│   ├── style.css
│   └── script.js
└── README.md
```

---

## Comandos útiles

- Salir del entorno virtual:

  - Windows:

    ```bash
    deactivate
    ```

  - MacOS/Linux:

    ```bash
    deactivate
    ```

- Actualizar dependencias:

  ```bash
  pip freeze > requirements.txt
  ```
