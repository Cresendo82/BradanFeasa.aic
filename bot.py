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

    if scp.content.startswith('!핑'):

        await scp.channel.send('퐁')

    if scp.content.startswith('!환영'):

        embed=discord.Embed(title="환영합니다!", description="한국 지부 scp 챗방에 오신걸 환영합니다.", color=0x00ff56)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/556145244832530433/715391771051556905/logo_white.png")
        embed.add_field(name="일단,", value="member 권한이 없으신 분들께서 껐다 키면 로그가 안 보이는 불편을 겪으실 수 있습니다. #숯례문, #월대 외의 다른 방에 못 들어가는 불편 역시 겪으실 수 있습니다. (#숯례문에 들어가시면 자세히 보실 수 있습니다).", inline=True)
        embed.add_field(name="그리고,", value="위키닷에 가입하신후, 재단 위키에 가입신청을 해주시면 member 권한을 얻으실 수 있습니다. http://ko.scp-wiki.net/system:join 이 링크로 들어가시면 됩니다. 가입 신청을 넣을 때에는 신입안내를 반드시 처음부터 끝까지 꼼꼼히 읽으셔야 합니다.", inline=True)
        embed.add_field(name="주의하셔야 할점이 있는데,", value="만약 가입 절차 내용을 누설 시 경고 이후 밴 처리 될 수 있습니다.", inline=True)
        embed.add_field(name="멤버 확인을 위해서,", value="관리자가 가입 신청을 수락하면 위키닷 닉네임과 디코 닉네임을 동일하게 바꾸어 주세요. 재단 디코 채널에서만 바꾸시면 됩니다. 게 완료되면 스태프 분들을 호출하세요. 스태프 분이 확인 뒤 멤버 권한을 드릴겁니다.", inline=True)
        embed.set_footer(text="수동이라서 느릴 수 있는 점, 양해 부탁드립니다. 다시 한번 재단 디코방에 오신 것을 환영합니다.")
        await scp.channel.send(embed=embed)   
        
    if scp.content.startswith('!검색'):
        info = scp.content.split(" ")[1]
        embed=discord.Embed(title= f"http://ko.scp-wiki.net/search:site/a/pf/q/" + info, description=f"", color=0x23bb76)
        await scp.channel.send(embed=embed)       
        
    if scp.content.startswith('!도움'):

        embed=discord.Embed(title= f"!핑으로 핑 확인, !도움으로 도움말 보기, !scp로 엣씨피 검색, !환영으로 환영하기, !검색으로 페이지 및 포럼 검색.", description=f"!secret", color=0x23bb76)
        await scp.channel.send(embed=embed)
        
    if scp.content.startswith('!secret'):

        await scp.channel.send('well, revealed in 2021. about author of this bot')

    if scp.content.startswith('!scp'):
        
        try:
            info = scp.content.split(" ")[1]
            region = scp.content.split(" ")[2]
            lfo = len(info)
            
            if region != 'en':
                
                if lfo == 1:
                    embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp-00" + info + "-" + region, description=f"", color=0x23bb76)
                    await scp.channel.send(embed=embed)

                if lfo == 2:
                    embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp-0" + info + "-" + region, description=f"", color=0x23bb76)
                    await scp.channel.send(embed=embed)

                if lfo == 3 or lfo == 4:
                    embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp-" + info + "-" + region, description=f"", color=0x23bb76)
                    await scp.channel.send(embed=embed)
                    
            if region == 'en':
            
                if lfo == 1:
                    embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp-00" + info, description=f"", color=0x23bb76)
                    await scp.channel.send(embed=embed)

                if lfo == 2:
                    embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp-0" + info, description=f"", color=0x23bb76)
                    await scp.channel.send(embed=embed)

                if lfo == 3 or lfo == 4:
                    embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp-" + info, description=f"", color=0x23bb76)
                    await scp.channel.send(embed=embed)

        except IndexError:
            embed=discord.Embed(title= f"뒤에 검색할 내용을 적어주세요.", description=f"예를 들어, !scp 300 ko 이렇게 말이죠.", color=0xf3bb76)
            await scp.channel.send(embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
