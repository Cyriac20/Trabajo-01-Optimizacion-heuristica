# Discusión: Descenso por Gradiente vs. Métodos Heurísticos

Para esta primera parte de optimización numérica, seleccionamos las funciones de **Rosenbrock** y **Schwefel**, probándolas en 2 y 3 dimensiones.

Al comparar el método de **descenso por gradiente** (con condición inicial aleatoria) con los métodos heurísticos o metaheurísticos (**Algoritmos Genéticos**, **Optimización por Enjambre de Partículas - PSO** y **Evolución Diferencial - DE**), pudimos notar varias diferencias en lo que aporta cada uno.

### ¿Qué aportó el método de descenso por gradiente?
El descenso por gradiente es muy bueno haciendo "sintonía fina" (explotación). Cuando logra caer en la cuenca del óptimo global (como nos pasó un par de veces con Rosenbrock), el valor final de la función objetivo suele ser bastante bueno. Sin embargo, su mayor problema es que es sumamente sensible al punto inicial. 
Por ejemplo, con la función de Schwefel (que tiene muchísimos mínimos locales), el descenso por gradiente se quedó atascado rápidamente en mínimos locales alejados del óptimo global, dándonos valores finales de la función muy altos (pobres).
En cuanto a las evaluaciones, el número de evaluaciones varió muchísimo. A veces convergía rápido en pocos pasos si el punto inicial ayudaba, pero si el paso o la tasa de aprendizaje requerían muchos ajustes finos, la cantidad de evaluaciones se disparaba, llegando en algunos casos a miles de iteraciones sin lograr el óptimo global.

### ¿Qué aportaron los métodos heurísticos?
Los métodos heurísticos (GA, PSO, DE) aportaron una gran capacidad de **exploración global**. Al no depender de derivadas ni de un solo punto inicial (sino de toda una población), lograron evadir los mínimos locales mucho mejor que el gradiente.
- En la función de **Schwefel**, que está llena de "trampas" (mínimos locales), los métodos heurísticos brillaron. PSO y Evolución Diferencial (DE) lograron acercarse al mínimo global (o llegar a él) con mucha consistencia.
- El número de evaluaciones con los métodos heurísticos es generalmente fijo por iteración (tamaño de la población $\times$ número de iteraciones). En nuestras pruebas corrimos con 30 individuos y 50 iteraciones, logrando unas 1500 evaluaciones fijas. Aunque a veces esto es más alto que una corrida rápida de gradiente, la calidad de la solución (el valor final de la función objetivo) fue muchísimo mejor y más confiable para funciones complejas como la de Schwefel.

### Conclusión general
El **descenso por gradiente aporta precisión local** rápida si ya estamos cerca de la solución, pero es ciego a nivel global. Los **métodos heurísticos aportan robustez y visión global**, permitiendo encontrar el vecindario del óptimo verdadero en problemas complejos (como Schwefel) a costa de un mayor y más constante número de evaluaciones de la función objetivo.

A continuación, puedes consultar los GIFs animados en el repositorio que muestran cómo el gradiente a veces sigue un solo camino local, mientras que heurísticas como PSO mandan "exploradores" por todo el espacio de búsqueda.