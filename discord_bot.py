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
    try:
        if modelo_ia is None:
            await ctx.send("❌ El motor de IA no está cargado.")
            return

        # Convertimos a formato que entiende Scikit-Learn
        dato_entrada = [[int(intentos)]]
        
        # Hacemos la predicción
        prediccion = modelo_ia.predict(dato_entrada)
        
        if prediccion[0] == 1:
            await ctx.send(f"🚨 **ALERTA**: `{ip}` es un **ATAQUE**.")
        else:
            await ctx.send(f"✅ `{ip}` es **NORMAL**.")

    except Exception as e:
        # Esto nos dirá el error exacto en la terminal de VS Code
        print(f"⚠️ Error dentro de !analizar: {e}")
        await ctx.send(f"Hubo un error interno al analizar: {e}")
# Arrancar el bot
if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ ERROR: No se encontró el TOKEN en el archivo .env")