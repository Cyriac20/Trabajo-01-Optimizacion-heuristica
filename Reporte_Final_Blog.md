# Explorando el Horizonte de la Optimización: De los Valles Matemáticos al Relieve de México

**Autores:** Cyriac SALIGNAT y Juan José Zapata Moreno  
**Fecha:** Marzo 2026 | **Asignatura:** Analítica Descriptiva  

---

## 1. Introducción

La optimización es el motor invisible que impulsa la toma de decisiones en el mundo moderno moderno. Desde el diseño de redes neuronales hasta la planificación de rutas logísticas, encontrar el "mejor" resultado bajo un conjunto de restricciones es un arte y una ciencia. 

En este reporte (presentado en formato de blog), te invitamos a acompañarnos en un viaje iterativo. Exploraremos dos de los dominios más fascinantes de esta disciplina: la **o**ptimización numérica continua**, donde el desafío es navegar valles matemáticos traicioneros para encontrar el punto más bajo; y la **optimización combinatoria**, donde el reto consiste en descifrar el orden perfecto oculto entre millones de permutaciones (aplicado al Problema del Vendedor Viajero en México).

---

## 2. Planteamiento del Problema

Para poner a prueba nuestras estrategias, dividimos el proyecto en dos partes fundamentales:

1. **Optimización Numérica Continua:**
   Enfrentamos a nuestros algoritmos a dos topologías clásicas:
   - *Función de Rosenbrock:* Un valle estrecho, pronunciado y en forma de parábola. Encontrar el valle es sencillo, pero converger al óptimo global (0,0) exige alta precisión.
   - *Función de Schwefel:* Un terreno sinuoso, repleto de múltiples cerros y mínimos locales profundos. Ideal para causar que algoritmos simples queden "atascados".

2. **Optimización Combinatoria (TSP Mexicano):**
   Un viajero de negocios debe partir de su ciudad natal, recorrer las otras 31 capitales de México y volver a casa obteniendo el costo económico mínimo. ¿Cómo trazamos la ruta perfecta en un país tan extenso sin evaluar millones de años de combinaciones?

---

## 3. Metodología

Nuestra estrategia computacional sigue un enfoque progresivo:

- **Algoritmos Basados en Gradiente:** Utilizamos el Descenso por Gradiente (GD) apoyándonos en el cálculo simbólico mediante `SymPy` para obtener la dirección más pronunciada.
- **Heurísticas y Bioinspiración:** Para lidiar con la complejidad (y los mínimos locales), implementamos Algoritmos Evolutivos (AE), Optimización por Enjambre de Partículas (PSO), Evolución Diferencial (DE) y Optimización por Colonias de Hormigas (ACO).
- **Herramientas de Programación:** Base en `Python` empleando `NumPy` para operaciones vectorizadas rápidas, y `Matplotlib`/`ImageIO` para la visualización dinámica de la convergencia de las soluciones.

---

## 4. Experimentación y Resultados: Numérica Continua

### 4.1 Evaluación Clásica (2D y 3D)

Sometimos el GD, AE, PSO y DE a pruebas rigurosas. La **Tabla 1** resume el rendimiento obtenido en los escenarios bidimensionales clásicos. 

**Tabla 1:** *Métricas de rendimiento de algoritmos en funciones de prueba 2D.*

| Función | Método | Mejor Valor ($f_{min}$) | Evaluaciones |
| :--- | :--- | :--- | :--- |
| **Rosenbrock** | Gradiente | $< 10^{-6}$ | ~15,000 |
| | PSO | 0.00 | 15,000 |
| | DE | 0.00 | ~6,500 |
| **Schwefel** | Gradiente | 258.12 (Atrapado) | ~10,000 |
| | PSO | 0.00 | 15,000 |
| | DE | 0.00 | ~8,000 |

Como se ilustra en la **Tabla 1**, el Descenso por Gradiente es extremadamente rápido y preciso cuando las condiciones son convexas o lisas (Rosenbrock). Sin embargo, al enfrentar Schwefel, queda completamente engañado por el primer mínimo local.

### 4.2 Visualización Espacial

El comportamiento de estos agentes puede observarse vívidamente cuando proyectamos los datos en 3D. A continuación, el carrusel de imágenes muestra el abismo de comportamiento entre utilizar derivadas y utilizar inteligencia de enjambre:

````carousel
![Figura 1: Convergencia del Gradiente Descendente (GD) en la función de Rosenbrock (3D). Nótese cómo la trayectoria fluye por el valle hacia el óptimo en un rastro continuo.](./resultados/gd_rosenbrock_3D.gif)
<!-- slide -->
![Figura 2: Comportamiento del Optimización por Enjambre de Partículas (PSO) en la función de Schwefel (3D). Las partículas exploran todo el panorama superando los trampas locales.](./resultados/pso_schwefel_3D.gif)
````

### 4.3 Robustez a través de Múltiples Corridas

La optimización estocástica puede variar según la semilla aleatoria inicial. Para validarlo, realizamos 30 corridas independientes. 

![Figura 3: Gráfica de caja (Boxplot) de 30 corridas independientes midiendo la estabilidad de los algoritmos heurísticos.](./resultados/boxplot_multiples_corridas.png)

Como se describe en la **Figura 3**, observamos que la Evolución Diferencial (DE) y el Enjambre de Partículas (PSO) mantienen en todas las corridas una dispersión casi nula respecto al óptimo global, demostrando alta robustez estadística frente a las variaciones del espacio de convergencia.

---

## 5. Experimentación y Resultados: Vendedor Viajero Mexicano

Luego de dominar el relieve matemático continuo, pasamos a las rutas logísticas y a problemas discretos, intentando crear la ruta menos costosa para recorrer las capitales de México.

### 5.1 Justificación Técnica del Costo

Nuestra función objetivo no minimiza la distancia, minimiza los **pesos mexicanos (MXN)**. Tomando decisiones realistas apoyadas por literatura:

- **Vehículo y Combustible:** Suponemos un Nissan Versa, líder de mercado (INEGI, 2017), rindiendo 7 L / 100km. A un costo estimado de \$26 MXN por litro (CRE, 2023), da como resultado un estimado de **\$1.82 MXN / km**.
- **Peajes y Caminos:** Con base en promedios del tabulador oficial (CAPUFE, 2023), agregamos **\$4.00 MXN / km**.
- **Costo de Oportunidad (Salario):** Un salario general de \$10,000 MXN / mes (Secretaría del Trabajo, 2023), equivale a \$333 MXN / día. Suponiendo una capacidad de conducir 800 km / día, nos refleja un factor de **\$0.42 MXN / km**.

Este modelo de costos agrega un alto realismo al problema TSP.

### 5.2 Evolución de la Heurística: Hormigas vs. Genética

Modelamos la solución desde dos trincheras: el Rastro de Feromonas (ACO) y la Supervivencia del más apto (Generación). 

![Figura 4: Curva comparativa de convergencia del Algoritmo Genético frente al método de Colonia de Hormigas (ACO) minimizando el costo total en MXN.](./resultados/convergencia_ag_vs_aco.png)

Tal y como se observa en la **Figura 4**, el Algoritmo Genético encuentra un régimen de alto descenso inicial y estabiliza a un costo inferior de forma constante en contraste con las colonias de hormigas que rápidamente estancan sin alcanzar un valle profundo.

### 5.3 Animación de las Rutas Óptimas

A continuación, exponemos la animación iteración por iteración de cómo los algoritmos van encontrando el arreglo perfecto en el mapa nacional:

````carousel
![Figura 5: Animación del Algoritmo Genético (AG). El cableado cruza gradualmente menos, logrando desenredarse de forma magistral hasta crear el circulo óptimo.](./resultados/gif_ruta_ag.gif)
<!-- slide -->
![Figura 6: Evolución dinámica generada por el optimizador por Colonias de Hormigas (ACO) sobre el mapa de las 32 capitales de México.](./resultados/gif_ruta_aco.gif)
````

Como evidencian las **Figuras 5 y 6**, las mejoras de la ruta iteración con iteración demuestran el intenso proceso de aprendizaje biológico. La ruta encontrada por el algoritmo genético es técnicamente válida y asombrosamente de bajo costo, bajando consistentemente y "desenredando" visualmente la red hasta quedar un círculo casi perfecto a lo largo de las fronteras de nuestro país.

---

## 6. Discusión

Si entrelazamos estos descubrimientos, nos percatamos que la naturaleza posee herramientas matemáticas muy valiosas:
1. Al contrastar iterativamente los resultados en escenarios espaciales, como lo revelado en las **Figuras 1 y 2**, notamos que un Gradiente Descendiente requiere condiciones inmaculadas para funcionar, sufriendo "miopía matemática". Las heurísticas, por otro lado, sacrifican elegancia simbólica por pragmatismo computacional.
2. La robustez demostrada en el Boxplot de la **Figura 3** nos da la tranquilidad de que tácticas como la Evolución Diferencial no son golpes de suerte.
3. Finalmente, como lo demuestran categóricamente las animaciones en el mapa de las **Figuras 5 y 6**, los algoritmos biológicos transforman el caos estructural en rutas altamente eficientes, permitiendo a empresas del mundo real ahorrar enormes montos operativos.

---

## 7. Conclusión

A través de rigurosos ejercicios que comprendieron simulaciones de funciones numéricas complejas y la optimización de gastos de viáticos a nivel nacional (TSP), hemos demostrado empíricamente el valor incomparable de la Optimización Computacional Heurística. 
Los métodos estocásticos, a pesar de sus pesados requerimientos de evaluaciones poblacionales, compensan con creces garantizando su escape de trampas locales y encontrando rumbos creativos (y validables) ante problemas masivos.

---

## 8. Bibliografía

- Caminos y Puentes Federales de Ingresos y Servicios Conexos (CAPUFE). (2023). *Tarifas vigentes de la red carretera*. Gobierno de México. Extraído de https://www.gob.mx/capufe
- Comisión Reguladora de Energía (CRE). (2023). *Precios promedios nacionales de combustibles*. Datos Abiertos del Gobierno de México.
- Dorigo, M., & Gambardella, L. M. (1997). Ant colony system: A cooperative learning approach to the traveling salesman problem. *IEEE Transactions on Evolutionary Computation*, 1(1), 53-66.
- Goldberg, D. E. (1989). *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley Professional.
- Instituto Nacional de Estadística y Geografía (INEGI). (2017). *Registro Administrativo de la Industria Automotriz de Vehículos Ligeros*.
- Kennedy, J., & Eberhart, R. (1995). Particule swarm optimization. *Proceedings of ICNN'95 - International Conference on Neural Networks*, 1942-1948.
- Secretaría del Trabajo y Previsión Social (STPS). (2023). *Estadísticas de la fuerza laboral y salarios promedios*. Gobierno de México.
- Storn, R., & Price, K. (1997). Differential evolution – A simple and efficient heuristic for global optimization over continuous spaces. *Journal of Global Optimization*, 11(4), 341-359.

---

## 9. Declaración de Contribuciones

El conjunto de los trabajos presentados en este informe ha sido realizado íntegramente por **Cyriac SALIGNAT** y **Juan José Zapata Moreno**. La distribución es la siguiente:

- **Juan José Zapata Moreno:** Realizó la parametrización de las preguntas 3 y 4 de la parte 1, así como el bloque robusto del algoritmo evolutivo y la generación de ricas animaciones visuales (como los GIFs).
- **Cyriac SALIGNAT:** Concluyó las preguntas de iniciación 1 y 2, formó el marco del costo y la teoría en la parte combinatoria (Parte 2), y programó con excelencia la técnica de Colonia de Hormigas.

**Uso de IA:** Se recurrió de forma productiva a la asistencia de LLMs para el refino estético, depuración de anomalías sintácticas y redacción de estilo-blog para una divulgación más atractiva.

🔗 **Enlace a GitHub:** [Repositorio Oficial Heurísticas](https://github.com/Cyriac20/Trabajo-01-Optimizacion-heuristica)
