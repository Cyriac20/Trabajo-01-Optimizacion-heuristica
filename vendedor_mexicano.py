"""
El salario medio en México es de 10 000 MXN al mes.
El caro mas vendido en México en 2017 era la Nissan Versa.


Entonces supondremos que el vendedor tiene un Nissan Versa para movarse y que el vendedor gana 10 000MXN al mes (333 MXN al dia)

El peago costa 4 MXN al km
El caro consume 7L al 100km yel precio al litre del gasolina 26MXN litre

Supongamos que podemos hacer 800km al dia
"""
import numpy as np
from AntColonyOptimizer import AntColonyOptimizer
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


ciudades = np.array([
    [21.8818, -102.2958],     # Aguascalientes
    [32.6278, -115.4545],     # Mexicali
    [24.1426, -110.3132],     # La Paz
    [19.8444, -90.5349],      # San Francisco de Campeche
    [16.7597, -93.1131],      # Tuxtla Gutiérrez
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
    [17.0677, -96.7226],      # Oaxaca de Juárez
    [19.0439, -98.2005],      # Puebla de Zaragoza
    [20.5881, -100.3881],     # Santiago de Querétaro
    [18.5141, -88.2948],      # Chetumal
    [22.1565, -100.9855],     # San Luis Potosí
    [24.8075, -107.3928],     # Culiacán
    [29.0988, -110.9548],     # Hermosillo
    [17.9869, -92.9303],      # Villahermosa
    [23.7461, -99.1462],      # Ciudad Victoria
    [19.3175, -98.2386],      # Tlaxcala
    [19.5430, -96.9052],      # Xalapa
    [20.9754, -89.6169],      # Mérida
    [22.7709, -102.5833],     # Zacatecas
    [19.4326, -99.1332]       # Ciudad de México
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


img = mpimg.imread('mexico.jpg')

fig, ax = plt.subplots()
ax.imshow(img, extent=[np.min(ciudades_plano[:,0])-300, np.max(ciudades_plano[:,0])+100, np.min(ciudades_plano[:,1])-400, np.max(ciudades_plano[:,1])+200], aspect='auto')

ax.scatter(ciudades_plano[:,0], ciudades_plano[:,1])
ax.plot(ciudades_plano[optimizer.best_path,0],ciudades_plano[optimizer.best_path,1],'-r')
plt.savefig("graphique.png")
plt.close()






