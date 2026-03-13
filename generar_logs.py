import pandas as pd
import random

def crear_datos():
    data = []
    # Generamos 100 logins normales
    for _ in range(100):
        data.append([random.randint(1, 3), 0, 0]) # Pocos intentos, no VPN, Normal
    
    # Generamos 20 ataques de fuerza bruta
    for _ in range(20):
        data.append([random.randint(15, 50), 1, 1]) # Muchos intentos, VPN, Ataque
        
    df = pd.DataFrame(data, columns=['intentos', 'usa_vpn', 'pais_sospechoso'])
    # La columna 'es_ataque' es lo que la IA debe aprender a predecir
    df['es_ataque'] = [0]*100 + [1]*20 
    df.to_csv('datos_logins.csv', index=False)
    print("✅ Archivo 'datos_logins.csv' creado.")

if __name__ == "__main__":
    crear_datos()