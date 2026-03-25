"""
El salario medio en Mexico es de 10 000 MXN al mes.
El caro mas vendido en Mexico en 2017 era la Nissan Versa.


Entonces supondremos que el vendedor tiene un Nissan Versa para moverse y que el vendedor gana 10 000MXN al mes (333 MXN al dia)

El peaje costa 4 MXN al km
El caro consume 7L al 100km y el precio al litro de la gasolina 26MXN litro

Supongamos que podemos hacer 800km al dia
"""
import numpy as np
from AntColonyOptimizer import AntColonyOptimizer
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import imageio.v2 as imageio
import os

os.makedirs('../resultados', exist_ok=True)


ciudades = np.array([
    [21.8818, -102.2958],     # Aguascalientes
    [32.6278, -115.4545],     # Mexicali
    [24.1426, -110.3132],     # La Paz
    [19.8444, -90.5349],      # San Francisco de Campeche
    [16.7597, -93.1131],      # Tuxtla Gutierrez
    [28.6329, -106.0691],     # Chihuahua
    [25.4232, -101.0053],     # Saltillo
    [19.2452, -103.7241],     # Colima
    [24.0277, -104.6546],     # Victoria de Durango
    [21.0194, -101.2574],     # Guanajuato
    [17.5507, -99.5010],      # Chilpancingo
    [20.1160, -98.7335],      # Pachuca
    [20.6597, -103.3496],     # Guadalajara
    [19.2892, -99.6557],      # Toluca
    [19.7008, -101.1844],     # Morelia
    [18.9242, -99.2216],      # Cuernavaca
    [21.5045, -104.8964],     # Tepic
    [25.6866, -100.3161],     # Monterrey
    [17.0677, -96.7226],      # Oaxaca de Juarez
    [19.0439, -98.2005],      # Puebla de Zaragoza
    [20.5881, -100.3881],     # Santiago de Queretaro
    [18.5141, -88.2948],      # Chetumal
    [22.1565, -100.9855],     # San Luis Potosi
    [24.8075, -107.3928],     # Culiacan
    [29.0988, -110.9548],     # Hermosillo
    [17.9869, -92.9303],      # Villahermosa
    [23.7461, -99.1462],      # Ciudad Victoria
    [19.3175, -98.2386],      # Tlaxcala
    [19.5430, -96.9052],      # Xalapa
    [20.9754, -89.6169],      # Merida
    [22.7709, -102.5833],     # Zacatecas
    [19.4326, -99.1332]       # Ciudad de Mexico
]) * np.pi / 180




def distancia(ciudad_1, ciudad_2): 

    """
    uso de la formula de Harvenstine
    """
    lat_1, long_1 = ciudad_1[0], ciudad_1[1]
    lat_2, long_2 = ciudad_2[0], ciudad_2[1]

    delta_lat = lat_2 - lat_1
    delta_long = long_2 - long_1

    a = np.sin(delta_lat/2)**2 + np.cos(lat_1)*np.cos(lat_2)* ( np.sin(delta_long/2)**2 )  
    c = 2 * np.atan2( np.sqrt(a), np.sqrt(1 - a) )

    R = 6371

    factor_coreccion = 1.2

    return factor_coreccion*R*c


def precio_viaje(ciudad_1 , ciudad_2 ):

    precio_gasolina = 7*26/100  # MXN / km
    precio_peaje = 4    # MXN / km
    kilometros_al_dia = 800     #km
    salario_diario = 333    # MXN

    d = distancia(ciudad_1, ciudad_2) 
    gasolina = d * precio_gasolina
    peaje = d * precio_peaje
    salario_perdido = (d / kilometros_al_dia) * salario_diario
    
    return gasolina + peaje + salario_perdido




precio_matrice = np.zeros(shape = (32,32))


for i in range(32):
    for j in range(32):
        
        precio_matrice[i][j] = precio_viaje(ciudades[i], ciudades[j])



optimizer = AntColonyOptimizer(ants=32, evaporation_rate=.1, intensification=2, alpha=1, beta=1,
                               beta_evaporation_rate=0, choose_best=.1)

best = optimizer.fit(precio_matrice, 200)

print(optimizer.best_path)

ciudades_plano = ciudades.copy()
ciudades_plano[:,0] = ciudades[:,1] * 6371
ciudades_plano[:,1] = np.log( np.tan( (np.pi/4) + ciudades[:,0]/2 )) * 6371


img = mpimg.imread('../data/mexico.jpg')

# ── Mapa estatico con la mejor ruta final ──
fig, ax = plt.subplots(figsize=(10, 7))
ax.imshow(img, extent=[np.min(ciudades_plano[:,0])-300, np.max(ciudades_plano[:,0])+100,
                        np.min(ciudades_plano[:,1])-400, np.max(ciudades_plano[:,1])+200], aspect='auto')
ax.scatter(ciudades_plano[:,0], ciudades_plano[:,1], color='white', edgecolors='tomato', s=30, zorder=4)
ax.plot(ciudades_plano[optimizer.best_path,0], ciudades_plano[optimizer.best_path,1],
        '-o', color='tomato', linewidth=1.5, markersize=4, zorder=3)
ax.set_title(f'Mejor ruta - ACO  |  Costo: {best:,.0f} MXN', fontsize=11)
ax.axis('off')
plt.tight_layout()
plt.savefig("../resultados/ruta_vendedor_mexicano.png", dpi=150)
plt.close()
print("Mapa ACO guardado en resultados/ruta_vendedor_mexicano.png")


# ── GIF animado: evolucion de la mejor ruta ACO iteracion a iteracion ──
def crear_gif_aco(historia_pob, historia_best, ciudades_plano, img,
                  filename='../resultados/gif_ruta_aco.gif',
                  n_frames=60, duration=150):
    """
    Genera un GIF que muestra la mejor ruta ACO evolucionando
    sobre el mapa de Mexico, iteracion a iteracion.
    """
    print(f"Generando GIF ACO: {filename}...")
    total   = len(historia_pob)
    indices = np.unique(np.linspace(0, total - 1, n_frames, dtype=int))
    if indices[-1] != total - 1:
        indices = np.append(indices, total - 1)

    x_min = np.min(ciudades_plano[:, 0]) - 300
    x_max = np.max(ciudades_plano[:, 0]) + 100
    y_min = np.min(ciudades_plano[:, 1]) - 400
    y_max = np.max(ciudades_plano[:, 1]) + 200

    temp_files = []
    for k, i in enumerate(indices):
        ruta    = historia_pob[i]
        costo_i = historia_best[i]

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        fig.patch.set_facecolor('#1a1a2e')

        # Mapa con la ruta actual
        ax1.imshow(img, extent=[x_min, x_max, y_min, y_max], aspect='auto')
        idx_cierre = ruta + [ruta[0]]
        ax1.plot(ciudades_plano[idx_cierre, 0], ciudades_plano[idx_cierre, 1],
                 '-', color='tomato', linewidth=1.4, alpha=0.85)
        ax1.scatter(ciudades_plano[:, 0], ciudades_plano[:, 1],
                    color='white', edgecolors='tomato', s=20, zorder=4)
        ax1.set_title(f'Iteracion {i} | Costo: {costo_i:,.0f} MXN',
                      color='white', fontsize=10)
        ax1.axis('off')

        # Curva de convergencia
        ax2.set_facecolor('#16213e')
        ax2.plot(historia_best[:i+1], color='tomato', linewidth=1.8)
        ax2.set_xlim(0, total)
        y_lo = min(historia_best) * 0.98
        y_hi = max(historia_best) * 1.02
        ax2.set_ylim(y_lo, y_hi)
        ax2.set_xlabel('Iteracion', color='white')
        ax2.set_ylabel('Costo (MXN)', color='white')
        ax2.set_title('Convergencia ACO', color='white')
        ax2.tick_params(colors='white')
        ax2.spines[:].set_color('#444')
        ax2.grid(True, alpha=0.3)
        ax2.yaxis.get_major_formatter().set_scientific(False)

        plt.tight_layout()
        tmp = f'../resultados/_tmp_aco_{k}.png'
        plt.savefig(tmp, dpi=100, facecolor=fig.get_facecolor())
        plt.close(fig)
        temp_files.append(tmp)

    with imageio.get_writer(filename, mode='I', duration=duration) as writer:
        for f in temp_files:
            writer.append_data(imageio.imread(f))
    for f in temp_files:
        os.remove(f)
    print(f"GIF guardado: {filename}")


crear_gif_aco(
    optimizer.best_path_series,
    optimizer.best_series,
    ciudades_plano,
    img,
    filename='../resultados/gif_ruta_aco.gif',
    n_frames=60,
)

print("\nFin! Archivos generados:")
print("  resultados/ruta_vendedor_mexicano.png")
print("  resultados/gif_ruta_aco.gif")
