import discord
from discord.ext import commands
import os
import joblib 
from dotenv import load_dotenv

# Cargamos el Token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Carga del modelo con manejo de errores básico
MODELO_PATH = 'models/modelo_sentinel.pkl'
try:
    modelo_ia = joblib.load(MODELO_PATH)
    print("✅ Cerebro de IA cargado con éxito.")
except Exception as e:
    print(f"❌ Error crítico: No se pudo cargar el modelo. {e}")
    modelo_ia = None

# Configuramos el bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} está conectado y vigilando.')

@bot.command()
async def estado(ctx):
    await ctx.send("🛡️ Sentinel activo. Sistema de IA analizando logs...")

# --- EL COMANDO DE LA IA MEJORADO ---
@bot.command()
async def analizar(ctx, ip: str, intentos: int):
    """
    Uso: !analizar 192.168.1.1 15
    """
    if modelo_ia is None:
        await ctx.send("❌ Error: El motor de IA no está cargado.")
        return

    # 1. Preparamos el dato para la IA (debe ser una lista de listas: [[valor]])
    # Nota: Asegúrate de que tu IA se entrenó solo con 'intentos_fallidos'
    dato_entrada = [[intentos]]
    
    # 2. La IA hace la predicción
    prediccion = modelo_ia.predict(dato_entrada) # Devuelve [0] o [1]
    
    # 3. Respondemos según el resultado
    if prediccion[0] == 1:
        await ctx.send(f"🚨 **ALERTA DE SEGURIDAD** 🚨\nLa IP `{ip}` muestra un patrón de **ATAQUE** ({intentos} intentos fallidos).")
    else:
        await ctx.send(f"✅ **IP Limpia**: El comportamiento de `{ip}` parece normal ({intentos} intentos).")

# Arrancar el bot
if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ ERROR: No se encontró el TOKEN en el archivo .env")