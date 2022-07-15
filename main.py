import soupsieve

f = open('lyrics.txt', 'r', encoding="utf8")
TOKEN = open('token.txt','r', encoding="utf8").read()
vc = None
c = f.read()
import discord
import random
import requests
from discord.ext import commands
from bs4 import BeautifulSoup
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
from youtube_dl import  YoutubeDL
from random import choice
from discord.utils import get
client = commands.Bot(command_prefix='!')  # инициализируем бота с префиксом '!'
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@client.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    print(arg)
    await ctx.send(arg)  # отправляем обратно аргумент


@client.command(pass_context=True)
async def info(ctx):
    await ctx.send("""1:!music-проигрывает музыку
    2:!lyrics-скидывает текст песни
    """)
s = c.split('$$$')


@client.command(pass_context=True)
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

@client.command(pass_context=True)
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
@client.command(pass_context=True)

async def maf(ctx):
    emb = discord.Embed(title=f'С',
                        description='Ну привет',
                        colour=discord.Color.purple())

    message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    await message.add_reaction('⏭')
@client.command(pass_context=True)
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
    youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

    #ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)




status = ['Jamming out to music!', 'Eating!', 'Sleeping!']
queue = []

@client.event
async def on_ready():
    print('Путя тут')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `?help` command for details!')





@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()


@client.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()


@client.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()


@client.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
        await ctx.send("Путин на связи")
    else:
        voice = await channel.connect()


@client.command()
async def quit(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send("Путин улетел")

YDL_OPTIONS = {'format': 'worstaudio/best', 'noplaylist': 'False', 'simulate': 'True',
               'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'}

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}



@client.command(pass_context=True, name='play', help='Запустить качево в войс ')
async def play(ctx, *, arg):
    global vc
    try:
        vc = await ctx.message.author.voice.channel.connect()
    except:
        await stop(ctx)
    with YoutubeDL(YDL_OPTIONS) as ydl:
        if 'https://' in arg:
            info = ydl.extract_info(arg, download=False)
        else:
            info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
    print(info["title"])
    url = info['formats'][0]['url']

    vc.play(discord.FFmpegPCMAudio(executable="bin\\ffmpeg\\bin\\ffmpeg.exe", source=url, **FFMPEG_OPTIONS))
    await ctx.send(f'Сейчас играет:\n'
                   f'{info["title"]}')


z = open('cityUk.txt', 'r', encoding="utf8")
x = z.read()
v = x.split('$$$')
@client.command(pass_context=True)
async def bomb(ctx):
    arg = random.randint(0,63)
    print(v)
    await ctx.send("город " + v[arg].strip() + " был забомбордирован")

client.run(TOKEN)
