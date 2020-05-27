import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(scp):
    if scp.author == client.user:
        return

    if scp.content.startswith('!ping'):

        await scp.channel.send('pong')

    if scp.content.startswith('!scp'):
        
        try:
            info = scp.content.split(" ")[1]
            region = scp.content.split(" ")[2]
            lfo = len(info)

            if lfo == 1:
                embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp-00" + info + "-" + region, description=f"", color=0x23bb76)
                await scp.channel.send(embed=embed)

            if lfo == 2:
                embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp-0" + info + "-" + region, description=f"", color=0x23bb76)
                await scp.channel.send(embed=embed)

            if lfo == 3 or lfo == 4:
                embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp-" + info + "-" + region, description=f"", color=0x23bb76)
                await scp.channel.send(embed=embed)

        except IndexError:
            embed=discord.Embed(title= f"뒤에 검색할 내용을 적어주세요.", description=f"예를 들어, !scp 300 ko 이렇게 말이죠.", color=0xf3bb76)
            await scp.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
