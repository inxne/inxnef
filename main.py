import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!')  # инициализируем бота с префиксом '!'


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент


@bot.command(pass_context=True)
async def info(ctx):
    await ctx.send("""1:!music-проигрывает музыку
    2:!lyrics-скидывает текст песни
    """)


@bot.event
async def on_message(message):
    if "лох" in message.content and message.author.id != 994160883720781904:
        print(message.author.id)
        await message.channel.send(f"{message.author}, сам лох")

TOKEN = "OTk0MTYwODgzNzIwNzgxOTA0.GIpHyt.JwP2xVMvF0wLj3cCn-nsB7bCy8rvdHZ-MMiWDc"

bot.run(TOKEN)
