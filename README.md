# Trabajo 01 – Optimización Heurística

**Asignatura:** Analítica Descriptiva (Programación en Python / MapReduce)  
**Repositorio:** `PRE-02-programacion-en-python-mapreduce-jjzm0521`

---

## Descripción

Este trabajo implementa y compara métodos de optimización numérica y combinatoria:

- **Parte 1:** Optimización de funciones de prueba continuas (Rosenbrock y Schwefel) con descenso por gradiente y métodos heurísticos (AE, PSO, DE).  
- **Parte 2:** Problema del Vendedor Viajero por las 32 capitales de los estados de México, resuelto con Colonias de Hormigas (ACO) y Algoritmo Genético (AG).

---

## Estructura del repositorio

```
Trabajo-01-Optimizacion-heuristica/
│
├── data/
│   └── mexico.jpg                        # Mapa base de México
│
├── notebooks/
│   └── Parte1_Optimizacion_Heuristica.ipynb   # Parte 1 completa (AE, PSO, DE, GD, GIFs)
│
├── scripts/
│   ├── AntColonyOptimizer.py             # Clase ACO (implementación base)
│   ├── descenso_gradiente.py             # Descenso por gradiente simbólico (sympy)
│   ├── evolucion_differencial.py         # Operadores DE (mutación, cruce)
│   ├── vendedor_mexicano.py              # TSP México – Colonia de Hormigas (ACO)
│   └── genetico_vendedor.py             # TSP México – Algoritmo Genético (AG) + GIF
│
├── resultados/
│   ├── superficies_2D.png               # Superficies de Rosenbrock y Schwefel
│   ├── convergencia_heuristica.png      # Convergencia AE / PSO / DE (Parte 1)
│   ├── gd_rosenbrock_2D.gif             # GIF: descenso por gradiente – Rosenbrock 2D
│   ├── gd_schwefel_2D.gif               # GIF: descenso por gradiente – Schwefel 2D
│   ├── pso_rosenbrock_2D.gif            # GIF: PSO – Rosenbrock 2D
│   ├── pso_schwefel_2D.gif              # GIF: PSO – Schwefel 2D
│   ├── ruta_vendedor_mexicano.png       # Mapa final – ruta óptima ACO
│   ├── ruta_ag_mexico.png               # Mapa final – ruta óptima AG
│   ├── gif_ruta_ag.gif                  # GIF: evolución de la ruta AG en el mapa
│   └── convergencia_ag_vs_aco.png       # Comparativa de convergencia AG vs ACO
│
├── Discusion.md                          # Análisis: gradiente vs heurísticos
├── requirements.txt                      # Dependencias Python
└── README.md                             # Este archivo
```

---

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

Las dependencias son: `numpy`, `matplotlib`, `scipy`, `imageio`, `sympy`.

---

## Cómo ejecutar

### Parte 1 – Optimización numérica (notebook)

```bash
cd notebooks
jupyter notebook Parte1_Optimizacion_Heuristica.ipynb
```

El notebook ejecuta todas las celdas en orden y guarda los resultados en `resultados/`.

### Parte 2 – TSP México

#### Colonias de Hormigas (ACO)
```bash
cd scripts
python vendedor_mexicano.py
```
Genera `resultados/ruta_vendedor_mexicano.png`.

#### Algoritmo Genético (AG) + GIF animado
```bash
cd scripts
python genetico_vendedor.py
```
Genera:
- `resultados/ruta_ag_mexico.png`
- `resultados/gif_ruta_ag.gif`
- `resultados/convergencia_ag_vs_aco.png`

---

## Metodología

### Parte 1 – Funciones de prueba elegidas

| Función | Dimensiones | Óptimo global |
|---------|-------------|---------------|
| **Rosenbrock** | 2D y 3D | f(1,…,1) = 0 |
| **Schwefel**   | 2D y 3D | f(420.97,…) ≈ 0 |

**Métodos aplicados:**
1. Descenso por gradiente (sympy + gradiente numérico, condición inicial aleatoria)
2. Algoritmo Evolutivo (AE) — selección por ranking, cruce de un punto, mutación uniforme
3. PSO — peso de inercia, componente cognitiva y social
4. Evolución Diferencial (DE) — usando `scipy.optimize.differential_evolution`

### Parte 2 – TSP México

**Costo de desplazamiento entre ciudades** (por km):

| Concepto | Valor |
|----------|-------|
| Vehículo | Nissan Versa (modelo más vendido en México, 2017) |
| Combustible | 7 L/100 km × 26 MXN/L = **1.82 MXN/km** |
| Peajes | **4 MXN/km** |
| Hora del vendedor | 10,000 MXN/mes → 333 MXN/día; a 800 km/día = **0.42 MXN/km** |
| **Total aprox.** | **~6.24 MXN/km** |

Las distancias se calculan con la fórmula de Haversine × 1.2 (factor de corrección de ruta real).

**ACO:** 32 hormigas, 200 iteraciones, evaporación 0.1, intensificación 2.

**AG:** 100 individuos, 500 generaciones, cruce OX1, mutación swap (p=0.05), elitismo k=5.

---

## Resultados principales

> Los valores exactos se obtienen al ejecutar los scripts. A modo de referencia:

- **Rosenbrock 2D:** PSO y DE encuentran valores cercanos a 0 (óptimo global), GD queda atrapado en mínimos locales con puntos iniciales desfavorables.
- **Schwefel 2D:** Los métodos heurísticos (especialmente DE y PSO) superan claramente al gradiente gracias a su capacidad de exploración global.
- **TSP México:** Ambos métodos (ACO y AG) encuentran rutas competitivas; el GIF `gif_ruta_ag.gif` muestra la convergencia generación a generación.

Ver `Discusion.md` para el análisis completo.

---

## Animaciones

| Archivo | Descripción |
|---------|-------------|
| `gd_rosenbrock_2D.gif` | Trayectoria del gradiente sobre el contorno de Rosenbrock |
| `gd_schwefel_2D.gif`   | Trayectoria del gradiente sobre Schwefel (se queda en mínimo local) |
| `pso_rosenbrock_2D.gif`| Nube de partículas PSO en Rosenbrock |
| `pso_schwefel_2D.gif`  | Nube de partículas PSO en Schwefel |
| `gif_ruta_ag.gif`      | Evolución de la ruta del vendedor (AG) sobre el mapa de México |

---

## Referencias

Ver bibliografía completa en el reporte técnico (blog). Principales fuentes:

- Kennedy, J., & Eberhart, R. (1995). Particle swarm optimization. *Proceedings of ICNN*.
- Storn, R., & Price, K. (1997). Differential evolution. *Journal of Global Optimization*, 11(4), 341–359.
- Dorigo, M., & Gambardella, L. M. (1997). Ant colony system. *IEEE Transactions on Evolutionary Computation*, 1(1), 53–66.
- Goldberg, D. E. (1989). *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley.