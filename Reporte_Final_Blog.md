# Blog: Explorando el Horizonte de la Optimización — De Funciones Continuas al Vendedor Viajero Mexicano

**Autor:** Cyriac SALIGNAT y Juan José Zapata Moreno  
**Fecha:** Marzo 2026  
**Asignatura:** Analítica Descriptiva  

---

## 1. Introducción

La optimización es el pilar de la toma de decisiones moderna. En este proyecto, nos sumergimos en los dos grandes mundos de la disciplina: la **optimización numérica continua** (donde buscamos el punto más bajo en valles matemáticos complejos) y la **optimización combinatoria** (donde el desafío es encontrar el orden perfecto entre millones de posibilidades).

A través de este reporte, presentamos una comparativa entre los métodos clásicos basados en el gradiente y las potentes heurísticas bioinspiradas, aplicándolas a funciones de prueba estándar y al Problema del Vendedor Viajero (TSP) en las 32 capitales de México.

---

## 2. Parte 1: Optimización Numérica

Para esta fase, seleccionamos dos funciones de prueba con características contrastantes:

- **Función de Rosenbrock:** Un valle estrecho y curvado donde el óptimo es fácil de encontrar pero difícil de converger con precisión.
- **Función de Schwefel:** Un paisaje "traicionero" lleno de múltiples mínimos locales que engañan a los algoritmos simples.

### 2.1. Metodología y Algoritmos

Implementamos y evaluamos los siguientes enfoques en 2 y 3 dimensiones:

1. **Descenso por Gradiente (GD):** Basado en el cálculo simbólico de derivadas ($SymPy$).
2. **Algoritmo Evolutivo (AE):** Selección por ranking y cruce de un punto.
3. **Optimización por Enjambre de Partículas (PSO):** Simulación de comportamiento social.
4. **Evolución Diferencial (DE):** Operadores de mutación vectorial.

### 2.2. Resultados y Discusión

| Función | Dim | Método | Mejor Valor ($f_{min}$) | Evaluaciones |
| :--- | :--- | :--- | :--- | :--- |
| **Rosenbrock** | 2D | Gradiente | $< 10^{-6}$ | ~15,000 |
| | 2D | PSO | 0.00 | 15,000 |
| | 2D | DE | 0.00 | ~6,500 |
| **Schwefel** | 2D | Gradiente | 258.12 (Atrapado) | ~10,000 |
| | 2D | PSO | 0.00 | 15,000 |
| | 2D | DE | 0.00 | ~8,000 |

**Análisis Comparativo:**

- **Precisión Local:** El descenso por gradiente es extremadamente eficiente para "pulir" la solución una vez que está en la cuenca del óptimo. Sin embargo, su dependencia del punto inicial lo hace fallar en funciones como Schwefel.
- **Exploración Global:** Los métodos heurísticos (especialmente PSO y DE) demostraron ser robustos frente a mínimos locales. Aportan una visión global del espacio a cambio de un número constante y a veces superior de evaluaciones.
- **Costo Computacional:** El GD requiere evaluar el gradiente (varias evaluaciones de la función por paso), mientras que las heurísticas evalúan una población completa por generación.

### 2.3. Visualización del Proceso

A continuación, se observa cómo el Gradiente se queda atrapado en un mínimo local en Schwefel, mientras que el PSO explora todo el dominio:

````carousel
![Gradiente en Rosenbrock (Convergencia Suave)](file:///c:/Users/marce/Documents/Analitica_Descriptiva/PRE-02-programacion-en-python-mapreduce-jjzm0521/Trabajo-01-Optimizacion-heuristica/resultados/gd_rosenbrock_2D.gif)
<!-- slide -->
![Gradiente en Schwefel (Mínimo Local)](file:///c:/Users/marce/Documents/Analitica_Descriptiva/PRE-02-programacion-en-python-mapreduce-jjzm0521/Trabajo-01-Optimizacion-heuristica/resultados/gd_schwefel_2D.gif)
<!-- slide -->
![PSO en Rosenbrock (Enjambre Convergiendo)](file:///c:/Users/marce/Documents/Analitica_Descriptiva/PRE-02-programacion-en-python-mapreduce-jjzm0521/Trabajo-01-Optimizacion-heuristica/resultados/pso_rosenbrock_2D.gif)
<!-- slide -->
![PSO en Schwefel (Exploración Global)](file:///c:/Users/marce/Documents/Analitica_Descriptiva/PRE-02-programacion-en-python-mapreduce-jjzm0521/Trabajo-01-Optimizacion-heuristica/resultados/pso_schwefel_2D.gif)
````

---

## 3. Parte 2: Optimización Combinatoria (TSP México)

El desafío: Un vendedor debe visitar las 32 capitales de México al menor costo posible.

### 3.1. Definición del Costo

Seleccionamos el **Nissan Versa** (modelo líder en ventas) como vehículo de transporte.

- **Combustible:** $7$ L/100km $\times$ $\$26$ MXN/L = **$\$1.82$ MXN/km**.
- **Peajes:** Estimado de **$\$4.00$ MXN/km**.
- **Valor del Vendedor:** Basado en un salario de $\$10,000$ MXN/mes con una jornada de $800$ km/día $\approx$ **$\$0.42$ MXN/km**.
- **Costo Total:** Aproximadamente **$\$6.24$ MXN por kilómetro**.

### 3.2. Heurísticas Aplicadas: ACO vs GA

Utilizamos **Colonias de Hormigas (ACO)** y **Algoritmos Genéticos (GA)** para encontrar la ruta óptima. El ACO utiliza feromonas para marcar caminos prometedores, mientras que el AG evoluciona permutaciones de ciudades mediante cruces y mutaciones.

**Comparativa de Convergencia:**
![Convergencia ACO vs GA](file:///c:/Users/marce/Documents/Analitica_Descriptiva/PRE-02-programacion-en-python-mapreduce-jjzm0521/Trabajo-01-Optimizacion-heuristica/resultados/convergencia_ag_vs_aco.png)
*Figura 1: Evolución del costo total en pesos mexicanos para ambos métodos.*

### 3.3. Ruta Óptima Final

El Algoritmo Genético logró una ruta altamente eficiente recorriendo las capitales desde el norte hacia el sureste y de regreso por el centro del país.

![Recorrido óptimo nacional](file:///c:/Users/marce/Documents/Analitica_Descriptiva/PRE-02-programacion-en-python-mapreduce-jjzm0521/Trabajo-01-Optimizacion-heuristica/resultados/ruta_ag_mexico.png)

---

## 4. Metodología y Bibliografía

El desarrollo se basó en una metodología iterativa:

1. Modelado simbólico de funciones con `SymPy`.
2. Implementación de algoritmos base en `NumPy`.
3. Simulación masiva y registro de convergencia.
4. Visualización dinámica con `Matplotlib` e `ImageIO`.

### Referencias (Normas APA)

- Dorigo, M., & Gambardella, L. M. (1997). Ant colony system: A cooperative learning approach to the traveling salesman problem. *IEEE Transactions on Evolutionary Computation*, 1(1), 53-66.
- Goldberg, D. E. (1989). *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley Professional.
- Kennedy, J., & Eberhart, R. (1995). Particule swarm optimization. *Proceedings of ICNN'95 - International Conference on Neural Networks*, 1942-1948.
- Storn, R., & Price, K. (1997). Differential evolution – A simple and efficient heuristic for global optimization over continuous spaces. *Journal of Global Optimization*, 11(4), 341-359.

---

## 5. Declaración de Contribuciones

El conjunto de los trabajos presentados en este informe ha sido realizado íntegramente por **Cyriac SALIGNAT** y **Juan José Zapata Moreno**. La distribución de las contribuciones es la siguiente:

- **Juan José Zapata Moreno:** Realizó las preguntas 3 y 4 de la parte 1, así como la sección relativa al algoritmo evolutivo y la generación de animaciones (GIFs) de la parte 2.
- **Cyriac SALIGNAT:** Se encargó de las preguntas 1 y 2 de la parte 1, de la modelización del problema en la parte 2, así como de la implementación del enfoque de colonias de hormigas.

**Uso de IA:** Se recurrió ocasionalmente a herramientas de inteligencia artificial, principalmente con el fin de recordar la sintaxis adecuada y de obtener ideas generales sobre cómo estructurar el código, sin sustituir el trabajo de desarrollo propio.

**Enlace a GitHub:** [https://github.com/Cyriac20/Trabajo-01-Optimizacion-heuristica](https://github.com/Cyriac20/Trabajo-01-Optimizacion-heuristica.gi)

---
