import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def entrenar_si_no_existe():
    # Solo entrenamos si no tenemos ya el modelo guardado
    if not os.path.exists('modelo_sentinel.pkl'):
        print("📊 IA: Entrenando modelo por primera vez...")
        # Cargamos el CSV que me habéis enseñado antes
        df = pd.read_csv('datos_logins.csv')
        
        # X son las pistas, y es la respuesta
        X = df[['intentos', 'usa_vpn', 'pais_sospechoso']]
        y = df['es_ataque']
        
        modelo = RandomForestClassifier(n_estimators=100)
        modelo.fit(X, y)
        
        # Guardamos el cerebro
        joblib.dump(modelo, 'modelo_sentinel.pkl')
        print("✅ IA: Modelo guardado como 'modelo_sentinel.pkl'")

def analizar_login(intentos, vpn, pais):
    # Cargamos el cerebro y predecimos
    modelo = joblib.load('modelo_sentinel.pkl')
    prediccion = modelo.predict([[intentos, vpn, pais]])
    
    # 1 significa Ataque, 0 significa Normal
    return prediccion[0]

if __name__ == "__main__":
    # Esto es para probar que funciona solo este archivo
    entrenar_si_no_existe()
    test = analizar_login(30, 1, 1)
    print(f"Prueba de detección: {'🚨 ATAQUE' if test == 1 else '✅ NORMAL'}")