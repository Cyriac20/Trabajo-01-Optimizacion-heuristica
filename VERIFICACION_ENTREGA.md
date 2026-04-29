# Verificación de entrega - Trabajo 01

Fecha de revisión local: 28 de abril de 2026.

## Resumen ejecutivo

El proyecto ya cubre la mayoría de observaciones realizadas en la corrección: la Parte 1 contiene experimentos en 2D y 3D para Rosenbrock y Schwefel, incluye métodos de descenso por gradiente, algoritmo evolutivo, PSO y evolución diferencial, y conserva GIFs/figuras en `resultados/`. La Parte 2 contiene implementaciones de colonia de hormigas y algoritmo genético para el TSP de las 32 capitales mexicanas, con mapas finales y GIFs de evolución.

El video "Reporte de contribución individual" fue entregado por separado, por lo que no se marca como pendiente dentro del repositorio.

## Checklist contra la retroalimentación

| Requisito / observación | Estado | Evidencia local |
|---|---:|---|
| Funciones de prueba seleccionadas | Cumple | Rosenbrock y Schwefel en `notebooks/Parte1_Optimizacion_Heuristica.ipynb` |
| Optimización en 2D y 3D con descenso por gradiente | Cumple | `gd_rosenbrock_2D.gif`, `gd_rosenbrock_3D.gif`, `gd_schwefel_2D.gif`, `gd_schwefel_3D.gif` |
| Optimización en 2D y 3D con AE, PSO y DE | Cumple | Notebook, `convergencia_heuristica.png`, GIFs AE/PSO y secciones de DE en el reporte |
| Varias corridas y comparación estadística | Cumple | `boxplot_multiples_corridas.png`; sección "Robustez Estadística" del HTML |
| Discusión de valor final y evaluaciones | Cumple | `Discusion.md`, notebook y tabla comparativa del reporte |
| TSP con colonia de hormigas | Cumple | `scripts/vendedor_mexicano.py`, `resultados/ruta_vendedor_mexicano.png`, `resultados/gif_ruta_aco.gif` |
| TSP con algoritmo genético | Cumple | `scripts/genetico_vendedor.py`, `resultados/ruta_ag_mexico.png`, `resultados/gif_ruta_ag.gif` |
| Modelo de costo con combustible, peajes y salario | Cumple | Fórmulas actualizadas en `scripts/vendedor_mexicano.py`, `scripts/genetico_vendedor.py` y reporte; fuentes Profeco/CRE, CAPUFE e INEGI |
| Animación geográfica sobre mapa de México | Cumple | `resultados/gif_ruta_ag.gif` y `resultados/gif_ruta_aco.gif` |
| Reporte en formato blog | Cumple | `reporte-tecnico-blog.html` |
| Figuras/tablas rotuladas y citadas | Cumple | El HTML tiene 25 figuras y 1 tabla; se corrigió numeración secuencial de leyendas |
| Bibliografía APA | Cumple | Se reforzó con fuentes oficiales para costos: Profeco/CRE, CAPUFE e INEGI |
| Uso de IA reportado | Cumple | Se documentó como soporte para estructura, planeación, plan de acción, revisión de requisitos, organización del repositorio y diseño del reporte HTML/blog |
| Video de contribución individual | Cumple por entrega externa | El equipo indicó que se entregó por separado |
| Repositorio Git referenciado | Cumple | Enlace a GitHub dentro del reporte HTML |

## Ajustes recomendados antes de entregar

1. Publicar `reporte-tecnico-blog.html` como entrada de blog o adjuntarlo como HTML final si la plataforma lo permite.
2. Publicar o adjuntar también `VERIFICACION_ENTREGA.md` si se desea mostrar explícitamente cómo se atendieron las observaciones del profesor.
