<div align="center">
  <h1>🧭 Optimización Heurística — Trabajo 01</h1>
  <p><em>Descenso por gradiente, metaheurísticas y TSP sobre las capitales de México</em></p>

<a href="https://cyriac20.github.io/Trabajo-01-Optimizacion-heuristica/reporte-tecnico-blog.html">
    <img src="https://img.shields.io/badge/Reporte_Técnico-Blog-0F172A?style=for-the-badge&logo=readthedocs&logoColor=white" alt="Reporte Técnico"/>
  </a>
  <a href="https://github.com/Cyriac20/Trabajo-01-Optimizacion-heuristica">
    <img src="https://img.shields.io/badge/Código-GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repositorio GitHub"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</div>

<br>

Proyecto desarrollado para el curso de **Redes Neuronales y Algoritmos Bioinspirados**, enfocado en comparar métodos de optimización numérica y combinatoria. En la primera parte se optimizan funciones benchmark en 2D y 3D; en la segunda se resuelve una variante del Problema del Vendedor Viajero con las 32 capitales de los estados de México.

## 🎯 Objetivo

Evaluar el comportamiento de métodos clásicos y heurísticos frente a problemas con distinta geometría: superficies continuas con mínimos locales y un problema combinatorio de rutas. La comparación considera valor final de la función objetivo, número de evaluaciones, múltiples corridas experimentales y visualizaciones animadas del proceso de optimización.

---

## 🚀 Entregables

1. **[📄 Reporte Técnico / Blog Post](PENDIENTE_PEGAR_LINK_DEL_BLOG)**: metodología, resultados, discusión, bibliografía APA y análisis de uso de IA.
2. **🧪 Notebook de Optimización Numérica**: experimentos en Rosenbrock y Schwefel con descenso por gradiente, algoritmo evolutivo, PSO y evolución diferencial.
3. **🗺️ TSP Mexicano**: solución con algoritmo genético y colonia de hormigas, incluyendo visualización sobre mapa de México.
4. **🎞️ Animaciones**: GIFs del proceso de optimización numérica y de la evolución de rutas para el TSP.

---

## 🧠 Metodología

### Parte 1: Optimización Numérica

Funciones seleccionadas:

- **Rosenbrock**: función de valle estrecho, útil para evaluar precisión local y estabilidad de convergencia.
- **Schwefel**: función multimodal, útil para probar exploración global y resistencia a mínimos locales.

Métodos comparados:

- Descenso por gradiente con condición inicial aleatoria.
- Algoritmo evolutivo.
- Optimización por enjambre de partículas (PSO).
- Evolución diferencial (DE).

### Parte 2: Optimización Combinatoria

Se modeló un recorrido por las 32 capitales mexicanas. El costo entre ciudades se calcula con:

- Distancia Haversine corregida por un factor de ruta.
- Costo de combustible.
- Costo de peajes.
- Costo del tiempo del vendedor.

El modelo de costos fue reforzado con fuentes para gasolina, peajes y salario.

---

## 🛠️ Instalación y Replicación

### 1. Requisitos previos

- Python 3.10 o superior.
- Git.

### 2. Configuración del entorno

```bash
# Clonar el repositorio
git clone https://github.com/Cyriac20/Trabajo-01-Optimizacion-heuristica.git
cd Trabajo-01-Optimizacion-heuristica

# Crear y activar entorno virtual en Windows
python -m venv .venv
.venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 3. Ejecutar experimentos

Parte 1:

```bash
jupyter notebook notebooks/Parte1_Optimizacion_Heuristica.ipynb
```

Parte 2 — Colonia de Hormigas:

```bash
cd scripts
python vendedor_mexicano.py
```

Parte 2 — Algoritmo Genético:

```bash
cd scripts
python genetico_vendedor.py
```

---

## 📂 Arquitectura del Repositorio

```text
|-- data/
|   `-- mexico.jpg
|
|-- notebooks/
|   `-- Parte1_Optimizacion_Heuristica.ipynb
|
|-- scripts/
|   |-- AntColonyOptimizer.py
|   |-- descenso_gradiente.py
|   |-- evolucion_differencial.py
|   |-- genetico_vendedor.py
|   `-- vendedor_mexicano.py
|
|-- resultados/
|   |-- gd_rosenbrock_2D.gif
|   |-- gd_rosenbrock_3D.gif
|   |-- gd_schwefel_2D.gif
|   |-- gd_schwefel_3D.gif
|   |-- ae_rosenbrock_2D.gif
|   |-- ae_schwefel_2D.gif
|   |-- pso_rosenbrock_2D.gif
|   |-- pso_rosenbrock_3D.gif
|   |-- pso_schwefel_2D.gif
|   |-- pso_schwefel_3D.gif
|   |-- gif_ruta_ag.gif
|   |-- gif_ruta_aco.gif
|   |-- ruta_ag_mexico.png
|   |-- ruta_vendedor_mexicano.png
|   |-- convergencia_ag_vs_aco.png
|   |-- convergencia_heuristica.png
|   `-- boxplot_multiples_corridas.png
|
|-- Reporte_Final_Blog.md
|-- Reporte_Final_Blog.html
|-- Reporte_Tecnico_v4_1.html
|-- VERIFICACION_ENTREGA.md
|-- PLAN_DE_ACCION_MEJORAS.md
|-- requirements.txt
`-- README.md
```

---

## 📊 Resultados Destacados

- En **Rosenbrock**, los métodos basados en gradiente pueden acercarse al óptimo, pero son sensibles a la tasa de aprendizaje y a la condición inicial.
- En **Schwefel**, los métodos heurísticos tienen ventaja clara por su capacidad de exploración global.
- En el **TSP mexicano**, el algoritmo genético mantuvo diversidad durante más generaciones, mientras que ACO converge rápido pero puede estancarse por concentración de feromonas.
- Las visualizaciones animadas permiten observar la diferencia entre explotación local y exploración poblacional.

---

## ✅ Verificación de Entrega

El archivo [`VERIFICACION_ENTREGA.md`](VERIFICACION_ENTREGA.md) resume cómo se atendieron las observaciones de la retroalimentación:

- Ejecución 2D y 3D.
- GIFs de descenso por gradiente y heurísticas.
- Múltiples corridas experimentales.
- Modelo de costos con fuentes.
- Figuras y tablas rotuladas.
- Bibliografía en formato APA.

El video de contribución individual fue entregado por separado.

---

## 📚 Bibliografía y Referencias Clave

- Dorigo, M., & Gambardella, L. M. (1997). *Ant colony system: A cooperative learning approach to the traveling salesman problem*. IEEE Transactions on Evolutionary Computation.
- Goldberg, D. E. (1989). *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley.
- Kennedy, J., & Eberhart, R. (1995). *Particle swarm optimization*. Proceedings of ICNN.
- Rosenbrock, H. H. (1960). *An automatic method for finding the greatest or least value of a function*. The Computer Journal.
- Storn, R., & Price, K. (1997). *Differential evolution: A simple and efficient heuristic for global optimization over continuous spaces*. Journal of Global Optimization.
