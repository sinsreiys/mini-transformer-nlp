# 🚀 Mini Transformer NLP

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

**Implementación técnica de un modelo Transformer desarrollado desde cero con PyTorch para procesamiento de lenguaje natural y generación de texto.**

</div>

---

<div align="center">

[![🚀 Demo en Vivo](https://img.shields.io/badge/🚀%20Demo%20en%20Vivo-Probar%20Ahora-brightgreen?style=for-the-badge)](https://TU-URL-AQUI.com)

</div>

---

## 🎯 Descripción

**Mini Transformer NLP** es un proyecto que demuestra capacidades avanzadas en el procesamiento de lenguaje natural (NLP) y el despliegue de aplicaciones web mediante **Flask**. Ofrece una herramienta eficiente para la **generación y predicción de texto**, construida sobre una arquitectura Transformer personalizada implementada íntegramente desde cero con PyTorch.

---

## ✨ Características Técnicas

- **⚙️ Motor de Inferencia:** Arquitectura Transformer personalizada para procesamiento de secuencias.
- **🔥 Backend de Alta Eficiencia:** API robusta construida en Flask para una respuesta rápida y escalable.
- **🎨 Interfaz de Usuario (UI/UX):** Diseño minimalista y moderno basado en *Glassmorphism* para una experiencia de usuario intuitiva.
- **🧹 Desarrollo Limpio:** Código estructurado profesionalmente, facilitando su integración en arquitecturas más complejas.

---

## 🛠️ Stack Tecnológico

| Área | Tecnologías |
|------|-------------|
| **IA / ML** | PyTorch, Python |
| **Backend** | Flask |
| **Frontend** | HTML5, CSS3, JavaScript (Fetch API) |
| **Entorno** | Git, GitHub |

---

## 📁 Estructura del Proyecto

```
mini-transformer-nlp/
├── model/
│   ├── transformer.py        # Arquitectura Transformer
│   └── train.py              # Entrenamiento del modelo
├── static/
│   ├── css/
│   │   └── style.css         # Estilos Glassmorphism
│   └── js/
│       └── main.js           # Lógica frontend (Fetch API)
├── templates/
│   └── index.html            # Interfaz de usuario
├── app.py                    # Servidor Flask
├── requirements.txt
└── README.md
```

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/mini-transformer-nlp.git
cd mini-transformer-nlp
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
# .\venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

### 3. Ejecutar la aplicación

```bash
python app.py
```

Abre tu navegador en `http://127.0.0.1:5000/`

---

## 📦 Dependencias Principales

```txt
torch>=2.0.0
flask>=3.0.0
numpy>=1.24.0
```

---

## 🧠 Arquitectura del Modelo

El modelo implementa los componentes fundamentales de la arquitectura Transformer original:

- **Multi-Head Self-Attention** — mecanismo de atención con múltiples cabezas.
- **Positional Encoding** — codificación posicional para preservar el orden secuencial.
- **Feed-Forward Layers** — capas densas con activación no lineal.
- **Layer Normalization** — normalización por capas para estabilizar el entrenamiento.

---

## 🖥️ Interfaz de la Aplicación

La UI presenta un diseño **Glassmorphism** con:

- Campo de entrada de texto para el prompt inicial.
- Control de longitud de la secuencia generada.
- Visualización en tiempo real de la predicción mediante llamadas asíncronas (Fetch API).

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* antes de enviar un *pull request* para discutir los cambios propuestos.

1. Haz un fork del repositorio.
2. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`.
3. Confirma tus cambios: `git commit -m 'Add nueva funcionalidad'`.
4. Sube la rama: `git push origin feature/nueva-funcionalidad`.
5. Abre un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">
  Hecho con ❤️ y PyTorch
</div>
