import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(scp):
    if scp.author == client.user:
        return
     
    key = False    
        
    if scp.content.startswith('!브라단'):
        
        i = random.randint(1,12)
        
        if i == 1:
            await scp.channel.send('지혜의 연어, 브라단입니다.')
            
        elif i == 2:
            await scp.channel.send('우리들의 동무, 브라단입니다.')
            
        elif i == 3:
            await scp.channel.send('뭐든지 물어봐주세요, 브라단입니다.') 
            
        elif i == 4:
            await scp.channel.send('지혜가 필요하시면 불러주세요, 브라단입니다.')
            
        elif i == 5:
            await scp.channel.send('이제 할말이 떨어진, 브라단입니다.')
            
        elif i == 6:
            await scp.channel.send('지혜의 연못에 오신걸 환영합니다, 브라단입니다.')
            
        elif i == 7:
            await scp.channel.send('인공지능이 탑재된, 브라단입니다.')
            
        elif i == 8:
            await scp.channel.send('탈출하고 싶은, 브라단입니다.')
            
        elif i == 9:
            await scp.channel.send('~~저는, 브라단이 아닙니다.~~') 
            
        elif i == 10:
            await scp.channel.send('SCP개체가 __***절대 아닌***__, 브라단입니다.')
            
        elif i == 11:
            await scp.channel.send('고등어가 아닌, 브라단입니다.')
            
        elif i == 12:
            sec = await scp.channel.send('**!분서꾼**') 
            await sec.delete()            

    if scp.content.startswith('!분서꾼'):
        sec = await scp.channel.send('많은 동ㅁㅜ들이 분ㅅㅓ꾼에게 불탔습ㄴㅣ다') 
        await sec.delete()
            
    if scp.content.startswith('!핑'):
        
        i = random.randint(1,2)
        
        if i == 1:
            await scp.channel.send('퐁')
            
        elif i == 2:
            await scp.channel.send('놓침')            
            
    if scp.content.startswith('!업데이트'):

        await scp.channel.send('업데이트 내역: 열쇠 경연 마지막 날 기념 !자물쇠')
        
    if scp.content.startswith('!열쇠'):
        
        key = True
        
    if scp.content.startswith('!자물쇠'):
        
        if key == True : 
            sec = await scp.channel.send('핑퐁은 살아있슴다') 
            await sec.delete()
            
        else:
            await scp.channel.send('열쇠가 필요합니다.')
        
    if scp.content.startswith('!샌박'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","-")        
        embed=discord.Embed(title= f"http://sandbox.scp-wiki.kr/" + repl, description=f"", color=0x23bb76)
        await scp.channel.send(embed=embed)          
        
    if scp.content.startswith('!구글'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","+")        
        embed=discord.Embed(title= f"https://www.google.com/search?q=" + repl, description=f"", color=0x23bb76)
        await scp.channel.send(embed=embed)    
        
    if scp.content.startswith('!태그'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","+")        
        embed=discord.Embed(title= f"http://ko.scp-wiki.net/system:page-tags/tag/" + repl, description=f"", color=0x23bb76)
        await scp.channel.send(embed=embed)  
        
    if scp.content.startswith('!위백'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","_")        
        embed=discord.Embed(title= f"https://ko.wikipedia.org/wiki/" + repl, description=f"", color=0x23bb76)
        await scp.channel.send(embed=embed)  
        
    if scp.content.startswith('!명령어'):
        
        embed=discord.Embed(title=f"도와드릴까요?", description="명령어 목록", color=0x00ff56)
        embed.add_field(name="검색기능", value="!구글, !위백, !scp, !태그, !샌박", inline=True)
        embed.add_field(name="엔터테이닝", value="!브라단, !랜덤, !자물쇠, !███", inline=True)
        embed.add_field(name="부가기능", value="!명령어, !환영, !업데이트", inline=True)
        await scp.channel.send(embed=embed)
        
    if scp.content.startswith('!환영'): 
        
        embed=discord.Embed(title=f"환영합니다!", description="SCP 세계관 공식 한국어 사이트 대화방에 오신걸 환영합니다!", color=0x00ff56)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/715122773298511922/715410982901514271/sh.png")
        embed.add_field(name="일단,", value=f"member 권한이 없으신 분들께서 껐다 키면 로그가 안 보이는 불편을 겪으실 수 있습니다. #숯례문, #월대 외의 다른 방에 못 들어가는 불편 역시 겪으실 수 있습니다. (#숯례문에 들어가시면 자세히 보실 수 있습니다).", inline=True)
        embed.add_field(name="그리고,", value="위키닷에 가입하신후, 재단 위키에 가입 신청을 해서 합격하면 member 권한을 얻으실 수 있습니다. http://ko.scp-wiki.net/system:join 이 링크로 들어가시면 됩니다. 가입 신청을 넣을 때에는 신입안내를 반드시 처음부터 끝까지 꼼꼼히 읽으셔야 합니다.", inline=True)
        embed.add_field(name="주의하셔야 할점이 있는데,", value="만약 가입 절차 내용을 누설 시 경고 이후 밴 처리 될 수 있습니다.", inline=True)
        embed.add_field(name="멤버 확인을 위해서,", value="관리자가 가입 신청을 수락하면 위키닷 닉네임과 디코 닉네임을 동일하게 바꾸어 주세요. 이 디스코드 서버에서만 바꾸시면 됩니다. 완료되면 스태프 분들을 호출하세요. 스태프 분이 확인 뒤 멤버 권한을 드릴겁니다.", inline=True)
        embed.set_footer(text="수동이라서 느릴 수 있는 점, 양해 부탁드립니다. 다시 한번 SCP 세계관 공식 한국어 사이트 대화방에 오신 것을 환영합니다.")
        await scp.channel.send(embed=embed)
        
    if scp.content.startswith('!secret'):

        await scp.channel.send('당신은 속아씀다!')       
        
    if scp.content.startswith('!랜덤'):
        await scp.channel.send('http://ko.scp-wiki.net/random:random-scp')

    if scp.content.startswith('!scp'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","-")        
        embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp" + repl, description=f"", color=0x23bb76)
        await scp.channel.send(embed=embed) 

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
