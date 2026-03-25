import numpy as np
import sympy as sym
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

iteraciones_max = 100000
tasa_de_aprendizaje = 0.0002

# %% 2D

x,y = sym.symbols('x y', real = True)

#### Rosenbrock ####
a, b = 1, 100

R_2D = (a-x)**2 + b*(y-x**2)**2

dRx_2D = sym.diff(R_2D, x)
dRy_2D = sym.diff(R_2D, y)

derivada_rosenbrock_2D_x = sym.lambdify((x,y),dRx_2D, 'numpy')
derivada_rosenbrock_2D_y = sym.lambdify((x,y),dRy_2D, 'numpy')

Rosenbrock_2D = sym.lambdify((x,y),R_2D, 'numpy')


#### Schwefel ####

a = 418.9829
d = 2

S_2D = a*d - x * sym.sin( sym.sqrt(sym.Abs(x)) ) - y * sym.sin( sym.sqrt(sym.Abs(y)) )

dSx_2D = sym.diff(S_2D, x)
dSy_2D = sym.diff(S_2D, y)

dSx_2D = sym.simplify(dSx_2D)
dSy_2D = sym.simplify(dSy_2D)

derivada_schwefel_2D_x = sym.lambdify((x,y),dSx_2D, 'numpy')
derivada_schwefel_2D_y = sym.lambdify((x,y),dSy_2D, 'numpy')

Schwefel_2D = sym.lambdify((x,y),S_2D, 'numpy')

### optimization

def optimization_2D(x_val, y_val, funcion , derivada_x , derivada_y, print_indice = True ):
    
    valores = np.zeros(shape=(iteraciones_max,3))

    for i in range(iteraciones_max):

        # Cálculo de los gradientes
        gradientes = [derivada_x(x_val, y_val),
                    derivada_y(x_val, y_val)]
        
        x_val = x_val - tasa_de_aprendizaje * gradientes[0]
        y_val = y_val - tasa_de_aprendizaje * gradientes[1]

        valores[i][0] = x_val
        valores[i][1] = y_val
        valores[i][2] = funcion(x_val, y_val)
    
    if print_indice:
        nb = np.arange(1, iteraciones_max + 1, 1)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        ax1.scatter(nb, valores[:,0], label = "convergencia de x")
        ax1.set_xlabel("Numero iteraciones")
        ax1.set_ylabel("Valor de x")
        ax1.legend()

        ax2.scatter(nb, valores[:,1], label = "convergencia de y")
        ax2.set_xlabel("Numero iteraciones")
        ax2.set_ylabel("Valor de y")
        ax2.legend()

        plt.savefig("descenso_gradiente.png")
        plt.close()
    
    return np.array([valores[-1][0], valores[-1][1]])

def different_values_2D(funcion , derivada_x , derivada_y):
    results = []
    for j in range(10):
        x_val = np.random.uniform(-5, 5)
        y_val = np.random.uniform(-5, 5)

        results.append(optimization_2D(x_val,y_val , funcion , derivada_x , derivada_y, False))
        results[j].append(x_val)
        results[j].append(y_val)

    return np.array(results)


optimization_2D(20,10,Schwefel_2D, derivada_schwefel_2D_x, derivada_schwefel_2D_y)

# %% 3D

x,y,z = sym.symbols('x y z', real = True)

### Rosenbrock ###

a, b = 1, 100

R_3D = (a-x)**2 + b*(y-x**2)**2 + (a-y)**2 + b*(z-y**2)**2 

dRx_3D = sym.diff(R_3D, x)
dRy_3D = sym.diff(R_3D, y)
dRz_3D = sym.diff(R_3D, z)

derivada_rosenbrock_3D_x = sym.lambdify((x,y,z),dRx_3D, 'numpy')
derivada_rosenbrock_3D_y = sym.lambdify((x,y,z),dRy_3D, 'numpy')
derivada_rosenbrock_3D_z = sym.lambdify((x,y,z),dRz_3D, 'numpy')

Rosenbrock_3D = sym.lambdify((x,y,z),R_3D, 'numpy')

#### Schwefel ####

a = 418.9829
d = 3

S_3D = a*d - x * sym.sin( sym.sqrt(sym.Abs(x)) ) - y * sym.sin( sym.sqrt(sym.Abs(y)) ) - z * sym.sin( sym.sqrt(sym.Abs(z)) )

dSx_3D = sym.diff(S_3D, x)
dSy_3D = sym.diff(S_3D, y)
dSz_3D = sym.diff(S_3D, z)

dSx_3D = sym.simplify(dSx_3D)
dSy_3D = sym.simplify(dSy_3D)
dSz_3D = sym.simplify(dSz_3D)

derivada_schwefel_3D_x = sym.lambdify((x,y,z),dSx_3D, 'numpy')
derivada_schwefel_3D_y = sym.lambdify((x,y,z),dSy_3D, 'numpy')
derivada_schwefel_3D_z = sym.lambdify((x,y,z),dSz_3D, 'numpy')

Schwefel_3D = sym.lambdify((x,y,z),S_3D, 'numpy')

### optimization

def optimization_3D(x_val, y_val, z_val, funcion , derivada_x , derivada_y, derivada_z, print_indice = True ):
    
    valores = np.zeros(shape=(iteraciones_max,4))

    for i in range(iteraciones_max):

        # Cálculo de los gradientes
        gradientes = [derivada_x(x_val, y_val, z_val),
                    derivada_y(x_val, y_val, z_val), derivada_z(x_val, y_val, z_val) ]
        
        x_val = x_val - tasa_de_aprendizaje * gradientes[0]
        y_val = y_val - tasa_de_aprendizaje * gradientes[1]
        z_val = z_val - tasa_de_aprendizaje * gradientes[2]

        valores[i][0] = x_val
        valores[i][1] = y_val
        valores[i][2] = z_val
        valores[i][3] = funcion(x_val, y_val, z_val)
    
    nb = np.arange(1, iteraciones_max + 1, 1)
    if print_indice:

        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 5))

        ax1.scatter(nb, valores[:,0], label = "convergencia de x")
        ax1.set_xlabel("Numero iteraciones")
        ax1.set_ylabel("Valor de x")
        ax1.legend()

        ax2.scatter(nb, valores[:,1], label = "convergencia de y")
        ax2.set_xlabel("Numero iteraciones")
        ax2.set_ylabel("Valor de y")
        ax2.legend()

        ax3.scatter(nb, valores[:,2], label = "convergencia de z")
        ax3.set_xlabel("Numero iteraciones")
        ax3.set_ylabel("Valor de z")
        ax3.legend()

        plt.savefig("descenso_gradiente.png")
        plt.close()
    
    return [valores[-1][0], valores[-1][1], valores[-1][2]]

def different_values_3D(funcion , derivada_x , derivada_y, derivada_z ):
    results = []
    for j in range(10):
        x_val = np.random.uniform(1, 10)
        y_val = np.random.uniform(1, 10)
        z_val = np.random.uniform(1, 10)

        results.append(optimization_3D(x_val ,y_val, z_val,funcion , derivada_x , derivada_y, derivada_z, False  ))
        results[j].append(x_val)
        results[j].append(y_val)
        results[j].append(z_val)

    return np.array(results)


