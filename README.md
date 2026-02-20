# 🧠 API Backend en Django para Predicción de Churn en Telecomunicaciones

Este proyecto implementa un **backend en Django** que expone una API para realizar predicciones de **churn de clientes** utilizando un modelo de Machine Learning previamente entrenado en un cuaderno Jupyter.  
El objetivo es ofrecer un servicio escalable que permita integrar el modelo en aplicaciones web, móviles o dashboards.

## 🚀 Funcionalidades principales

- API REST construida con **Django** y **Django REST Framework**.
- Endpoint para recibir datos de un cliente y devolver la predicción de churn.
- Carga del modelo de Machine Learning entrenado en el proyecto Jupyter.
- Preprocesamiento de datos antes de la predicción.
- Arquitectura modular para facilitar mantenimiento y escalabilidad.

## 📁 Estructura del proyecto

proyecto_telcom/
├── .venv/                      # Entorno virtual (aislamiento de librerías)
├── manage.py                   # Script de administración de Django
├── core/                       # Carpeta de configuración del proyecto
│   ├── __init__.py
│   ├── settings.py             # Configuración de JWT, CORS y Apps
│   ├── urls.py                 # Enrutador principal (Auth + Predictions)
│   └── wsgi.py
├── predictions/                # App de Machine Learning
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py               # Opcional: Para guardar históricos de predicciones
│   ├── serializers.py          # Validadores de entrada de datos (DRF)
│   ├── urls.py                 # Rutas específicas: api/predict/
│   ├── views.py                # Lógica de carga de modelo y predicción
│   ├── utils.py                # (Opcional) Funciones de apoyo para el mapeo de datos
│   └── ml_models/              # Carpeta para tus binarios (NO subir a Git si son pesados)
│       ├── modelo_churn_telmex.pkl
│       └── escalador_churn.pkl
├── static/                     # Archivos estáticos generales
├── templates/                  # (Opcional) Si decides servir Vue.js desde Django
└── requirements.txt            # Lista de dependencias (pip freeze)


> Nota: El archivo del modelo debe generarse desde el notebook del proyecto de churn y colocarse dentro de la carpeta `predictions/`.

---

## 🔗 Relación con el proyecto de Machine Learning

Este backend utiliza el modelo entrenado en el repositorio:

**ChurnTelco**  
- Notebook: `churn_prediction.ipynb`  
- Dataset: `Telco-Customer-Churn.csv`  

El modelo se entrena en Jupyter, se exporta como `.pkl` y luego se integra aquí para servir predicciones vía API.

---

## 🛠 Tecnologías utilizadas

- Python 3.x  
- Django  
- Django REST Framework  
- Scikit-learn  
- Pandas / NumPy  
- Pickle para serialización del modelo  

---

## 📡 Endpoints principales

### 🔍 Predicción de churn
**POST** `/api/predict/`

**Body (JSON):**
```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "InternetService": "Fiber optic",
  "MonthlyCharges": 89.5,
  "TotalCharges": 1080.5
}
