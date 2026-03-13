import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Cargamos el Token desde el archivo .env (Seguridad)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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

# Arrancar el bot
if __name__ == "__main__":
    bot.run(TOKEN)
