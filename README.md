# 🧠 Datagen Segmentators

**Datagen Segmentators** es una herramienta web para segmentación de imágenes que permite a los usuarios subir imágenes, ejecutar diferentes algoritmos segmentadores (como SAM o YOLO), y visualizar resultados como **cajas delimitadoras** (bounding boxes) y **polígonos de segmentación** en una interfaz amigable.

Este proyecto forma parte del ecosistema **Datagen**, una plataforma SaaS enfocada en la **generación, anotación y visualización de datasets para entrenamiento de modelos de machine learning**.

---

## ✨ Funcionalidades

* Subida de imágenes desde la interfaz web.
* Segmentación automática utilizando distintos motores (SAM, YOLO, etc.).
* Visualización en tiempo real de:

  * **Cajas delimitadoras (Bounding Boxes)**.
  * **Polígonos de segmentación**.
* Backend basado en **FastAPI**.
* Frontend web embebido con HTML, CSS y JavaScript.
* Soporte modular para incorporar nuevos segmentadores fácilmente.

---

## 🧰 Requisitos previos

* Tener instalado **Docker**.
* (Opcional para desarrollo local) Tener **Python 3.10+** y `pip`.

---

## ⚙️ Instalación y ejecución con Docker

1. Clonar el repositorio:

   ```bash
   git clone <repository_url>
   cd datagen-segmentators
   ```

2. Construir la imagen Docker:

   ```bash
   docker build -t datagen_segmentators .
   ```

3. Ejecutar el contenedor:

   ```bash
   docker run -p 8000:8000 datagen_segmentators
   ```

La aplicación estará disponible en `http://localhost:8000`.

---

## 👨‍💻 Uso en desarrollo local (sin Docker)

1. Crear un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Iniciar el servidor FastAPI:

   ```bash
   uvicorn main:app --reload
   ```

4. Acceder a la aplicación:

   ```bash
   http://127.0.0.1:8000
   ```

---

## 🗂️ Estructura del proyecto

```
datagen-segmentators/
│
├── main.py                  # Punto de entrada del servidor FastAPI
├── segmentators/            # Lógica de segmentación (SAM, YOLO, etc.)
├── static/                  # Frontend web (HTML, CSS, JS)
├── Dockerfile               # Configuración para Docker
├── requirements.txt         # Dependencias de Python
└── README.md
```

---

## 🧪 Uso de la herramienta

1. Accede a `http://localhost:8000`.
2. Sube una imagen en formato `.jpg`, `.png` o similar.
3. Visualiza los resultados:

   * Cajas delimitadoras en el canvas de **Bounding Boxes**.
   * Polígonos en el canvas de **Segmentations**.

---

## 🧩 Integración con Datagen

Este servicio se integra con otros componentes del ecosistema Datagen:

| Proyecto                 | Descripción                                                                |
| ------------------------ | -------------------------------------------------------------------------- |
| **Datagen Backend**      | API REST para gestión de datasets, imágenes, etiquetas, anotaciones y más. |
| **Datagen Frontend**     | Interfaz web construida con React + Vite + Tailwind.                       |
| **Datagen Orchestrator** | CLI para generación automática de datasets a través de pipelines.          |
| **Datagen Segmentators** | Este proyecto: servicio web de segmentación de imágenes.                   |

---

## 🛠️ Problemas comunes

### ❌ Error: `libGL.so.1: cannot open shared object file`

Este error ocurre cuando OpenCV necesita bibliotecas de OpenGL. Solución en Docker:

```bash
apt-get install -y libgl1 libglib2.0-0
```

Luego reconstruir la imagen:

```bash
docker build -t datagen_segmentators .
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!
Puedes forquear el repositorio, crear una rama y enviar una Pull Request con tus cambios. Asegúrate de seguir las buenas prácticas y pasar los chequeos de estilo si aplican.

---

## 🙏 Agradecimientos

* [FastAPI](https://fastapi.tiangolo.com/) – framework backend moderno y asíncrono.
* [Ultralytics](https://ultralytics.com/) – proveedores de modelos como YOLO.
* [Segment Anything Model (SAM)](https://segment-anything.com/) – modelo de segmentación avanzada.
* Comunidad open-source y colaboradores de Datagen.



## Contact

For any inquiries or support, please contact [your_email@example.com].

