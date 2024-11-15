import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(name="barlasis_fikri")
async def barlasis_fikri(ctx):
    ideas = [
        "Eski plastik şişelerden saksı yapabilirsiniz.",
        "Plastik kapaklardan küçük süs eşyaları yapabilirsiniz.",
        "Boş deterjan kutularını kullanarak saklama kutusu yapabilirsiniz.",
        "Plastik kaşık ve çatallardan dekoratif çerçeveler oluşturabilirsiniz."
    ]
    await ctx.send(f"İşte bir el işi fikri: {random.choice(ideas)}")

    @bot.command(name="barlasis bunu yap")
    async def barlasis_fikri(ctx):
        yapi = [
            "Bulduğun pilleri pil dönüşüm kutusuna koy.",
            "bulduğun şişeleri geri dönüşüm kutusuna at.",
            "yerde bulduğun sepetleri al."
        
        ]

@bot.command(name="barlasis bunlar sebepler ")
async def barlasis_fikri(ctx):
        sonuçlari = [
            "Yerde bulduğun poşetleri atmassan martılar ve kuşlar büyük tehlike altına düşer.",
            "Bir sigarayı yere atarsan çıkan gas raddioksit olduğu için atmosfer incelir.",
            "Bir pil gibi tür enerjileri yere atarsak pillerde bulunan kimyasal maddeler çevreyi kötü etkiler."
        ]
