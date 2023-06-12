import nextcord
import datetime
intents = nextcord.Intents.default()
intents.members = True
client = nextcord.Client(intents=intents)

@client.event
async def on_message(msg):
    if msg.content.startswith("!"):
        a = msg.content.split('!')
        command = a[1]
    if command == "내정보":
        user = msg.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        embed = nextcord.Embed(title='내정보',description=f"@{user}님의 정보:", color= 0x62c1cc)
        embed.add_field(name='가입일', value=f"{date.year}/{date.month}/{date.day}")
        embed.set_thumbnail(url=msg.author.avatar)
        await msg.channel.send(embed=embed)
client.run('ODc2ODAxODU4ODA1NTY3NTA5.GZd8ex.hiAAe-qK_FkkL0NOIoz-_yCGRvsycvyqIB-cmY')













