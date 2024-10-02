import pandas as pd

# Dataframe es la informacion básica con el nombre de las piezas y centrimetos para poder armar el Excel

data = {
    "Piezas" : ["Pata", "Tablero", "Puerta", "Estante", "Panel lateral"],
    "Centimetros" : [40, 120, 60, 30, 180]
} 

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel

df.to_excel("muebles_medidas.xlsx", index=False)