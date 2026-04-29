"""
Algoritmo Genético para el Problema del Vendedor Viajero Mexicano.

Mismos parámetros de costo que en vendedor_mexicano.py:
  - Vendedor con Nissan Versa
  - Salario: 14,056 MXN/mes -> 468.53 MXN/dia (INEGI, Censos Economicos 2024)
  - Peaje: 4.00 MXN/km como parametro efectivo basado en tarifas CAPUFE por tramo
  - Gasolina: 7 L/100km x 23.96 MXN/L = 1.677 MXN/km (Profeco/CRE, nov. 2024)
  - Velocidad media: 800 km/día
  - Factor de corrección de ruta: ×1.2 (fórmula de Haversine)

Representación: permutación de índices de ciudades (0-31).
Operadores genéticos:
  - Selección por torneo binario
  - Cruce de orden (OX1)
  - Mutación por intercambio (swap mutation)
  - Elitismo: se preservan los k_elite mejores individuos
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

# ─── carpeta de resultados ───────────────────────────────────────────────────
os.makedirs('../resultados', exist_ok=True)

# ─── Coordenadas de las 32 capitales (lat, lon) en radianes ─────────────────
ciudades = np.array([
    [21.8818, -102.2958],     # 0  Aguascalientes
    [32.6278, -115.4545],     # 1  Mexicali
    [24.1426, -110.3132],     # 2  La Paz
    [19.8444,  -90.5349],     # 3  San Francisco de Campeche
    [16.7597,  -93.1131],     # 4  Tuxtla Gutiérrez
    [28.6329, -106.0691],     # 5  Chihuahua
    [25.4232, -101.0053],     # 6  Saltillo
    [19.2452, -103.7241],     # 7  Colima
    [24.0277, -104.6546],     # 8  Victoria de Durango
    [21.0194, -101.2574],     # 9  Guanajuato
    [17.5507,  -99.5010],     # 10 Chilpancingo
    [20.1160,  -98.7335],     # 11 Pachuca
    [20.6597, -103.3496],     # 12 Guadalajara
    [19.2892,  -99.6557],     # 13 Toluca
    [19.7008, -101.1844],     # 14 Morelia
    [18.9242,  -99.2216],     # 15 Cuernavaca
    [21.5045, -104.8964],     # 16 Tepic
    [25.6866, -100.3161],     # 17 Monterrey
    [17.0677,  -96.7226],     # 18 Oaxaca de Juárez
    [19.0439,  -98.2005],     # 19 Puebla de Zaragoza
    [20.5881, -100.3881],     # 20 Santiago de Querétaro
    [18.5141,  -88.2948],     # 21 Chetumal
    [22.1565, -100.9855],     # 22 San Luis Potosí
    [24.8075, -107.3928],     # 23 Culiacán
    [29.0988, -110.9548],     # 24 Hermosillo
    [17.9869,  -92.9303],     # 25 Villahermosa
    [23.7461,  -99.1462],     # 26 Ciudad Victoria
    [19.3175,  -98.2386],     # 27 Tlaxcala
    [19.5430,  -96.9052],     # 28 Xalapa
    [20.9754,  -89.6169],     # 29 Mérida
    [22.7709, -102.5833],     # 30 Zacatecas
    [19.4326,  -99.1332],     # 31 Ciudad de México
]) * np.pi / 180

nombres_ciudades = [
    "Aguascalientes", "Mexicali", "La Paz", "Campeche", "Tuxtla Gutiérrez",
    "Chihuahua", "Saltillo", "Colima", "Durango", "Guanajuato",
    "Chilpancingo", "Pachuca", "Guadalajara", "Toluca", "Morelia",
    "Cuernavaca", "Tepic", "Monterrey", "Oaxaca", "Puebla",
    "Querétaro", "Chetumal", "San Luis Potosí", "Culiacán", "Hermosillo",
    "Villahermosa", "Cd. Victoria", "Tlaxcala", "Xalapa", "Mérida",
    "Zacatecas", "CDMX",
]

N_CIUDADES = len(ciudades)


# ─── Funciones de costo (idénticas a vendedor_mexicano.py) ───────────────────

def distancia(ciudad_1, ciudad_2):
    """Distancia Haversine con factor de corrección 1.2 (carretera)."""
    lat_1, long_1 = ciudad_1[0], ciudad_1[1]
    lat_2, long_2 = ciudad_2[0], ciudad_2[1]
    delta_lat  = lat_2 - lat_1
    delta_long = long_2 - long_1
    a = np.sin(delta_lat / 2)**2 + np.cos(lat_1) * np.cos(lat_2) * np.sin(delta_long / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return 1.2 * 6371 * c


def precio_viaje(ciudad_1, ciudad_2):
    precio_gasolina    = 7 * 23.96 / 100  # MXN/km
    precio_peaje       = 4.00             # MXN/km
    kilometros_al_dia  = 800             # km/día
    salario_diario     = 14056 / 30      # MXN/día

    d = distancia(ciudad_1, ciudad_2)
    gasolina        = d * precio_gasolina
    peaje           = d * precio_peaje
    salario_perdido = (d / kilometros_al_dia) * salario_diario
    return gasolina + peaje + salario_perdido


# ─── Matriz de costos ────────────────────────────────────────────────────────
print("Construyendo matriz de costos...")
precio_matriz = np.zeros((N_CIUDADES, N_CIUDADES))
for i in range(N_CIUDADES):
    for j in range(N_CIUDADES):
        precio_matriz[i][j] = precio_viaje(ciudades[i], ciudades[j])


# ─── Utilidades del AG ───────────────────────────────────────────────────────

def costo_ruta(ruta, matriz):
    """Costo total (MXN) de una ruta circular (regresa al inicio)."""
    total = sum(matriz[ruta[i], ruta[i + 1]] for i in range(len(ruta) - 1))
    total += matriz[ruta[-1], ruta[0]]   # volver al punto de partida
    return total


def pob_inicial(N, n_ciudades):
    """Genera N permutaciones aleatorias."""
    return [np.random.permutation(n_ciudades).tolist() for _ in range(N)]


def seleccion_torneo(poblacion, costos, k=3):
    """Torneo de tamaño k: devuelve el índice del ganador (menor costo)."""
    candidatos = np.random.choice(len(poblacion), k, replace=False)
    mejor = candidatos[np.argmin([costos[c] for c in candidatos])]
    return mejor


def cruce_ox(padre1, padre2):
    """Order Crossover (OX1): produce un hijo válido."""
    n = len(padre1)
    a, b = sorted(np.random.choice(n, 2, replace=False))
    hijo = [-1] * n
    hijo[a:b+1] = padre1[a:b+1]
    ptr = (b + 1) % n
    for ciudad in padre2[b+1:] + padre2[:b+1]:
        if ciudad not in hijo:
            hijo[ptr] = ciudad
            ptr = (ptr + 1) % n
    return hijo


def mutacion_swap(ruta, prob_mut=0.05):
    """Intercambia dos ciudades al azar con probabilidad prob_mut."""
    ruta = ruta[:]
    if np.random.rand() < prob_mut:
        i, j = np.random.choice(len(ruta), 2, replace=False)
        ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta


# ─── Algoritmo Genético principal ────────────────────────────────────────────

def algoritmo_genetico(matriz, N=100, max_gen=500, prob_mut=0.05,
                        k_elite=5, k_torneo=3, semilla=42):
    """
    AG para TSP.

    Parámetros
    ----------
    matriz    : matriz de costos (N_ciud × N_ciud)
    N         : tamaño de la población
    max_gen   : número de generaciones
    prob_mut  : probabilidad de mutación por individuo
    k_elite   : número de élites que pasan sin cambios
    k_torneo  : tamaño del torneo de selección
    semilla   : semilla para reproducibilidad

    Retorna
    -------
    mejor_ruta    : lista con el orden óptimo de ciudades
    mejor_costo   : costo total en MXN
    historia_best : mejor costo por generación
    historia_pob  : lista de mejores rutas por generación (para GIF)
    """
    np.random.seed(semilla)
    n_ciudades = matriz.shape[0]

    poblacion     = pob_inicial(N, n_ciudades)
    historia_best = []
    historia_pob  = []          # guardamos la mejor ruta de cada generación
    mejor_ruta    = None
    mejor_costo   = np.inf

    for gen in range(max_gen):
        # Evaluar
        costos = [costo_ruta(r, matriz) for r in poblacion]

        # Actualizar mejor global
        idx_mejor = int(np.argmin(costos))
        if costos[idx_mejor] < mejor_costo:
            mejor_costo = costos[idx_mejor]
            mejor_ruta  = poblacion[idx_mejor][:]

        historia_best.append(mejor_costo)
        historia_pob.append(mejor_ruta[:])

        # Élite: los k_elite mejores pasan directamente
        orden   = np.argsort(costos)
        nueva_pob = [poblacion[i][:] for i in orden[:k_elite]]

        # Llenar el resto con cruce + mutación
        while len(nueva_pob) < N:
            p1 = seleccion_torneo(poblacion, costos, k_torneo)
            p2 = seleccion_torneo(poblacion, costos, k_torneo)
            hijo = cruce_ox(poblacion[p1], poblacion[p2])
            hijo = mutacion_swap(hijo, prob_mut)
            nueva_pob.append(hijo)

        poblacion = nueva_pob

    return mejor_ruta, mejor_costo, np.array(historia_best), historia_pob


# ─── Correr el AG ────────────────────────────────────────────────────────────
print("Ejecutando Algoritmo Genetico...")
mejor_ruta_ag, mejor_costo_ag, hist_best_ag, hist_pob_ag = algoritmo_genetico(
    precio_matriz, N=100, max_gen=500, prob_mut=0.05, k_elite=5, semilla=42
)

print(f"\nAG -> costo total: {mejor_costo_ag:,.0f} MXN")
print("Orden de ciudades:")
for idx in mejor_ruta_ag:
    print(f"  {idx:2d}. {nombres_ciudades[idx]}")


# ─── Proyección mercator para el mapa ────────────────────────────────────────
ciudades_plano           = ciudades.copy()
ciudades_plano[:, 0]     = ciudades[:, 1] * 6371                                 # x = lon × R
ciudades_plano[:, 1]     = np.log(np.tan(np.pi / 4 + ciudades[:, 0] / 2)) * 6371  # y = Mercator

import matplotlib.image as mpimg
img = mpimg.imread('../data/mexico.jpg')


# ─── Mapa con la mejor ruta del AG ───────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 7))
ax.imshow(img, extent=[
    np.min(ciudades_plano[:, 0]) - 300,
    np.max(ciudades_plano[:, 0]) + 100,
    np.min(ciudades_plano[:, 1]) - 400,
    np.max(ciudades_plano[:, 1]) + 200,
], aspect='auto')

idx_cierre = mejor_ruta_ag + [mejor_ruta_ag[0]]   # ruta cerrada
ax.plot(ciudades_plano[idx_cierre, 0], ciudades_plano[idx_cierre, 1],
        '-o', color='deepskyblue', linewidth=1.5, markersize=4, zorder=3)
ax.scatter(ciudades_plano[:, 0], ciudades_plano[:, 1],
           color='white', edgecolors='deepskyblue', s=30, zorder=4)

ax.set_title(f'Mejor ruta – Algoritmo Genético\nCosto total: {mejor_costo_ag:,.0f} MXN', fontsize=11)
ax.axis('off')
plt.tight_layout()
plt.savefig('../resultados/ruta_ag_mexico.png', dpi=150)
plt.close()
print("Mapa AG guardado en resultados/ruta_ag_mexico.png")


# ─── GIF animado: evolución de la ruta en el mapa ────────────────────────────
def crear_gif_ruta(historia_pob, historia_best, ciudades_plano, img,
                   filename='../resultados/gif_ruta_ag.gif',
                   n_frames=60, duration=150):
    """
    Genera un GIF que muestra cómo va mejorando la ruta del AG
    sobre el mapa de México, frame a frame.
    """
    print(f"Generando GIF: {filename}...")
    total        = len(historia_pob)
    indices      = np.unique(np.linspace(0, total - 1, n_frames, dtype=int))
    if indices[-1] != total - 1:
        indices = np.append(indices, total - 1)

    x_min = np.min(ciudades_plano[:, 0]) - 300
    x_max = np.max(ciudades_plano[:, 0]) + 100
    y_min = np.min(ciudades_plano[:, 1]) - 400
    y_max = np.max(ciudades_plano[:, 1]) + 200

    temp_files = []
    for k, i in enumerate(indices):
        ruta       = historia_pob[i]
        idx_cierre = ruta + [ruta[0]]
        costo_i    = historia_best[i]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.patch.set_facecolor('#1a1a2e')

        # ── Mapa con ruta ──
        ax1.imshow(img, extent=[x_min, x_max, y_min, y_max], aspect='auto')
        ax1.plot(ciudades_plano[idx_cierre, 0], ciudades_plano[idx_cierre, 1],
                 '-', color='deepskyblue', linewidth=1.4, alpha=0.85)
        ax1.scatter(ciudades_plano[:, 0], ciudades_plano[:, 1],
                    color='white', edgecolors='deepskyblue', s=20, zorder=4)
        ax1.set_title(f'Generación {i} | Costo: {costo_i:,.0f} MXN',
                      color='white', fontsize=10)
        ax1.axis('off')

        # ── Curva de convergencia ──
        ax2.set_facecolor('#16213e')
        ax2.plot(historia_best[:i+1], color='deepskyblue', linewidth=1.8)
        ax2.set_xlim(0, total)
        y_lo = min(historia_best) * 0.98
        y_hi = max(historia_best) * 1.02
        ax2.set_ylim(y_lo, y_hi)
        ax2.set_xlabel('Generación', color='white')
        ax2.set_ylabel('Costo (MXN)', color='white')
        ax2.set_title('Convergencia AG', color='white')
        ax2.tick_params(colors='white')
        ax2.spines[:].set_color('#444')
        ax2.grid(True, alpha=0.3)
        ax2.yaxis.get_major_formatter().set_scientific(False)

        plt.tight_layout()
        tmp = f'../resultados/_tmp_ag_{k}.png'
        plt.savefig(tmp, dpi=100, facecolor=fig.get_facecolor())
        plt.close(fig)
        temp_files.append(tmp)

    with imageio.get_writer(filename, mode='I', duration=duration) as writer:
        for f in temp_files:
            writer.append_data(imageio.imread(f))
    for f in temp_files:
        os.remove(f)
    print(f"GIF guardado: {filename}")


crear_gif_ruta(hist_pob_ag, hist_best_ag, ciudades_plano, img,
               filename='../resultados/gif_ruta_ag.gif', n_frames=60)


# ─── Convergencia comparativa: AG vs ACO ────────────────────────────────────
# Importar resultados del ACO desde vendedor_mexicano (reutilizamos la serie)
# Para no re-ejecutar el ACO costoso aquí, re-creamos el optimizer en silencio
print("\nEjecutando ACO para comparativa (puede tardar un poco)...")
from AntColonyOptimizer import AntColonyOptimizer

optimizer_cmp = AntColonyOptimizer(
    ants=32, evaporation_rate=0.1, intensification=2,
    alpha=1, beta=1, beta_evaporation_rate=0, choose_best=0.1
)
optimizer_cmp.fit(precio_matriz, 200, verbose=False)
hist_aco = optimizer_cmp.best_series

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hist_aco,      label='ACO',               color='tomato',      linewidth=1.8)
ax.plot(hist_best_ag,  label='AG (Gen.)',          color='deepskyblue', linewidth=1.8)
ax.set_xlabel('Iteración / Generación')
ax.set_ylabel('Mejor costo (MXN)')
ax.set_title('Convergencia comparativa – TSP México\nACO vs. Algoritmo Genético')
ax.legend()
ax.grid(True, alpha=0.4)
ax.yaxis.get_major_formatter().set_scientific(False)
plt.tight_layout()
plt.savefig('../resultados/convergencia_ag_vs_aco.png', dpi=150)
plt.close()
print("Gráfica de convergencia guardada en resultados/convergencia_ag_vs_aco.png")

print("\nFin! Archivos generados:")
print("  resultados/ruta_ag_mexico.png")
print("  resultados/gif_ruta_ag.gif")
print("  resultados/convergencia_ag_vs_aco.png")
