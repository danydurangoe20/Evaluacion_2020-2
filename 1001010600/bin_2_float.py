import numpy as np

#Para el codigo general debería pedir un b de la siguiente manera
#b = str(input('Ingrese un numero binario de 32-bits: '))
#Para efectos practicos dejo b asignado como el binario que se mostró
#durante la clase

b = '00111110001000000000000000000000'

b_list= [i for i in b][::-1]
b_array = np.array(b_list).astype(int) # arreglo de numpy con los caracteres 
#del numero en binario, en orden invertido para facilitar calculos

s = b_array[31] #signo
b_exp = b_array[23:31] #lista con los numeros asignados al exponente

#Sumatoria e 
i = np.arange(0,8)
e = sum((b_exp)*(2**i))
#===========

#Sumatoria para la fraccion
j = np.arange(0,23)
b_frac = sum((b_array[j])/(2**(23-j)))
#==========================

r_num = (((-1)**s)/(2**(127-e)))*(1+b_frac)
print(r_num)