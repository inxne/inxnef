import soupsieve

f = open('lyrics.txt', 'r', encoding="utf8")
TOKEN = open('token.txt','r', encoding="utf8").read()

c = f.read()
import discord
import random
import requests
from discord.ext import commands
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='!')  # инициализируем бота с префиксом '!'
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

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
    print(arg)
@bot.command(pass_context=True)

async def maf(ctx):
    emb = discord.Embed(title=f'С',
                        description='Ну привет',
                        colour=discord.Color.purple())

    message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    await message.add_reaction('⏭')
@bot.command(pass_context=True)
async def lyrics(ctx,arg):
    if arg == "kizaru на моём аккаунте":




      url = "https://l-hit.com/ru/148095"
    page = requests.get(url, headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "cookie": "PHPSESSID=c6081a4da970200ac94c45547252aa80; __gads=ID=aa56ae6d6d8817fb-22231a239ed300b4:T=1657520484:RT=1657520484:S=ALNI_Mavd9O5D12ubyxKnZoYDTFVJBGZgg; __gpi=UID=00000883963321f1:T=1657520484:RT=1657520484:S=ALNI_MbVc_XBLSBztGp5kwhCTGeH-IeVGQ"
})
# print(page.content)

    selector = "body > div > div > div.wrapper > div.proper-content > div > div > div > div.span8 > article > div:nth-child(2)"

    soup = BeautifulSoup(page.text, "html.parser")
    l = soup.select(selector)
    get_text = l[0].get_text(separator="\n")
    # soup.select_one("body > div > div > div.wrapper > div.proper-content > div > div > div > div.span8 > article > h1 > a").attrs["href"]


    await ctx.send(get_text)
    embed = discord.Embed(color=0xf00c89, title=arg, type='rich', description="kizaru-На моём аккаунте"+get_text)
    await ctx.send(embed=embed)
bot.run(TOKEN)
