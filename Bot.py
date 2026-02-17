import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Бот {bot.user} запущен!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'🏓 Понг! {round(bot.latency * 1000)} мс')

@bot.command()
async def hello(ctx):
    await ctx.send(f'👋 Привет, {ctx.author.name}!')

# Flask сервер для Render (чтоб не вырубался)
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

bot.run(os.getenv('BOT_TOKEN'))
