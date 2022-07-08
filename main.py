f = open('lyrics.txt', 'r',encoding="utf8")
c = f.read()
import discord
import random
from discord.ext import commands
bot = commands.Bot(command_prefix='!')  # инициализируем бота с префиксом '!'


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    print(arg)
    await ctx.send(arg)  # отправляем обратно аргумент


@bot.command(pass_context=True)
async def info(ctx):
    await ctx.send("""1:!music-проигрывает музыку
    2:!lyrics-скидывает текст песни
    """)
s = c.split('$$$')


@bot.command(pass_context=True)
async def music(ctx,arg):

    if arg == "shadowraze":
        await ctx.send(s[2])


    if arg == "internet L0ve":
        await ctx.send(s[0])


    if arg == "jeep":
        await ctx.send(s[1])
    if arg == "unravel":
        await ctx.send(s[3])
    if arg == "deutschland":
        await ctx.send(s[4])

@bot.command(pass_context=True)
async def music_r(ctx):
    arg = random.randint(0,4)
    if arg == 0:
        await ctx.send(s[2])


    if arg == 1:
        await ctx.send(s[0])


    if arg == 2:
        await ctx.send(s[1])
    if arg == 3:
        await ctx.send(s[3])
    if arg == 4 :
        await ctx.send(s[4])




bot.run(TOKEN)
