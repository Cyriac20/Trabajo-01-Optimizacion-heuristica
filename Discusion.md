# Discusión: descenso por gradiente vs. métodos heurísticos

Para la optimización numérica se seleccionaron las funciones de Rosenbrock y Schwefel, evaluadas en dos y tres dimensiones. La primera exige precisión local dentro de un valle estrecho y curvo; la segunda exige exploración global porque contiene múltiples mínimos locales.

## Aporte del descenso por gradiente

El descenso por gradiente aportó una referencia determinista y fácil de interpretar. Su trayectoria permite ver, paso a paso, cómo se explota la información local de la pendiente. En Rosenbrock puede acercarse al óptimo cuando la tasa de aprendizaje y la condición inicial son favorables, aunque suele avanzar lentamente por el valle curvo.

Su limitación aparece con fuerza en Schwefel: al depender de información local, queda atrapado en mínimos locales y no cuenta con un mecanismo natural de escape. En términos de evaluaciones, puede ser competitivo cuando converge pronto, pero en paisajes multimodales muchas evaluaciones no garantizan mejor calidad final.

## Aporte de los métodos heurísticos

Los métodos heurísticos aportaron exploración global. AE, PSO y DE trabajan con poblaciones de soluciones, por lo que no dependen de una única condición inicial. Esto les permite cubrir regiones distintas del dominio, comparar candidatos y escapar con mayor frecuencia de mínimos locales.

En Schwefel, DE y PSO fueron los métodos más robustos: alcanzaron valores finales cercanos al óptimo global con menor variabilidad entre corridas. En Rosenbrock, DE también destacó porque combina exploración poblacional con pasos diferenciales que se comportan como una aproximación adaptativa de dirección de mejora.

## Lectura comparativa

El descenso por gradiente es valioso como método de explotación local: muestra la geometría del problema, usa pocas ideas algorítmicas y puede ser eficiente cerca del óptimo. Los heurísticos son más costosos en número de evaluaciones porque cada iteración evalúa una población, pero compensan ese costo con robustez frente a condiciones iniciales desfavorables y paisajes multimodales.

La conclusión principal es que no hay un único algoritmo superior. La topología del problema decide: para superficies suaves y bien condicionadas, el gradiente es una herramienta precisa; para superficies rugosas, multimodales o combinatorias, las heurísticas aportan diversidad, exploración y estabilidad estadística.
