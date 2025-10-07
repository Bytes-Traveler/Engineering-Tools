# 🛠️ Engineering Tools

Una colección de **mini-aplicaciones de escritorio** creadas en **Python + Tkinter**, pensadas para resolver problemas prácticos de ingeniería, matemáticas y computación.  
Cada herramienta es **ligera, modular y fácil de usar**, con documentación y ejemplos incluidos.

---

## ✨ Herramientas incluidas

- 🔢 **Calculadora científica**  
  Funciones básicas y avanzadas: trigonometría, logaritmos, potencias.  

- 💻 **Conversores numéricos**  
  Conversión entre binario, decimal, hexadecimal y octal.  

- 📊 **Mini-plotter de funciones**  
  Ingresa una función matemática y visualízala con `matplotlib`.  

- 🔐 **Generador de contraseñas seguras**  
  Crea contraseñas aleatorias con opciones de longitud y complejidad.  

---

## 📂 Estructura del repositorio

```
engineering-tools/
├── apps/                                # Conjunto de aplicaciones modulares
│   │                      
│   ├── calculator/                      # App de calculadora
│   │   │
│   │   ├── logic/                       # Lógica matemática
│   │   │   │
│   │   │   ├── operations.py            # Funciones matemáticas principales
│   │   │   │
│   │   │   └── utils.py                 # Funciones auxiliares
│   │   │
│   │   ├── tests/                       # Pruebas unitarias de la app
│   │   │   │
│   │   │   └── test_operations.py       # Tests para verificar la lógica de operaciones
│   │   │
│   │   │
│   │   └── UI/                          # Interfaz gráfica de la calculadora
│   │       │
│   │       ├── events.py                # Manejo de eventos
│   │       │
│   │       └── calculator_ui.py         # Ventana principal de la calculadora
│   │   
│   ├── converters/                      # App de conversores
│   │
│   ├── password-generator/              # App generadora de contraseñas seguras 
│   │
│   └── plotter/                         # App para graficar funciones matemáticas  
│
├── assets/                              # Recursos estáticos
│   
├── core/                                # Núcleo del sistema   
│   │
│   ├── config.py                        # Configuración global 
│   │
│   └── main_windows.py                  # Ventana principal
│
├── docs/                                # Documentación del proyecto                
│   │
│   └── README.md
│   
├── .gitignore
│
├── LICENSE
│
├── main.py
│
├── Pipfile
│
└── requeriments.txt                     # Lista de dependencias para instalación con pip clásico
