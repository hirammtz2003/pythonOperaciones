import pandas as pd
# Funcion que recibe una lista y regresa la sumatoria
def sumar(numeros:list[float]) -> float:
    res=sum(numeros)
    return res

# Funcion ue recibe una lista y regresa su promedio
def promediar(numeros:list[float]) -> float:
    if( len(numeros)==0):
        return 0
    prom=sum(numeros) / len(numeros)
    return prom

# Contar las organizaiones en el archivo CSV
def contar_org(ruta):
    datos=pd.read_csv(ruta, encoding="latin-1")
    conteo= len(datos)
    return conteo

datos=[10, 20, 35, 1.5, 70.2]
s = sumar(datos)
print("Sumatoria ", s)

p=promediar(datos)
print("Promedio", p)

cant=contar_org("Organization_v3.csv")
print("Cantidad de organizaciones ",cant)