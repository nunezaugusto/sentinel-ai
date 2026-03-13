import discord
from discord.ext import commands
import os
import joblib  # <--- Importante para cargar la IA
from dotenv import load_dotenv

# Cargamos el Token desde el archivo .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# --- NUEVA RUTA AQUÍ ---
# Como movimos el modelo a la carpeta /models, indicamos la ruta
MODELO_PATH = 'models/modelo_sentinel.pkl'
modelo_ia = joblib.load(MODELO_PATH) 
# -----------------------

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

# Ejemplo de cómo usarías la IA en un comando
@bot.command()
async def analizar(ctx, IP):
    # Aquí usarías modelo_ia para predecir si la IP es peligrosa
    await ctx.send(f"Analizando la IP {IP} con el modelo en {MODELO_PATH}...")

# Arrancar el bot
if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ ERROR: No se encontró el TOKEN en el archivo .env")