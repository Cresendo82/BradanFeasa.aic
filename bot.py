import discord
import os
import random
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(scp):
    if scp.author == client.user:
        return

    if scp.content.startswith('!업데이트'):

        await scp.channel.send('업데이트 내역: !')
        
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
        embed.add_field(name="검색기능", value="!구글, !위백, !scp, !태그, !샌박, !랜덤, !라틴", inline=True)
        embed.add_field(name="부가기능", value="!명령어, !환영, !업데이트, !핑, !브라단, !경연", inline=True)
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
        
    if scp.content.startswith('!랜덤'):
        await scp.channel.send('http://ko.scp-wiki.net/random:random-scp')
        
    if scp.content.startswith('!경연'):
        
        info = scp.content[4:len(scp.content)]
        
        if info == '1':
            embed=discord.Embed(title= f"**성탄절 경연 결과가 나왔습니다.**" + repl, description=f"우승자는 Crislr님, ZachRobinson님입니다! 상품은... 호주산 살치살입니다! 대박", color=0x23bb76)        
            await scp.channel.send(embed=embed)
            
        elif info == '2':
            embed=discord.Embed(title= f"**경연 검색 결과 없음**" + repl, description=f"", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '3':
            embed=discord.Embed(title= f"**나무 경연 투고 기간입니다.**" + repl, description=f"이미 지났네요. 아쉽다", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '4':
            embed=discord.Embed(title= f"**나무 경연 결과가 나왔습니다.**" + repl, description=f"우승자는 thd-glasses님입니다! 상품은 BBQ 황금올리브치킨 반반입니다.", color=0x23bb76)      
            await scp.channel.send(embed=embed)
            
        elif info == '5':
            embed=discord.Embed(title= f"**열쇠 경연 투고 기간입니다.**" + repl, description=f"이미 지나가버린 경연입니다. 아쉽당", color=0x23bb76)        
            await scp.channel.send(embed=embed)
            
        elif info == '6':
            embed=discord.Embed(title= f"**열쇠 경연 결과가 나왔습니다.**" + repl, description=f"우승자는 Nareum님, Profound Kaye님입니다! 상품은 등킨 도나쓰 20개입니다.", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '7':
            embed=discord.Embed(title= f"**물고기 경연 투고 기간입니다.**" + repl, description=f"우리 모두 다 같이 투고해요!", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '8':
            embed=discord.Embed(title= f"**물고기 경연 결과가 나왔습니다.**" + repl, description=f"우승자는 [편집됨]님, [편집됨]님입니다! 상품은 [데이터 말소]입니다!", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '9':
            embed=discord.Embed(title= f"**언어 경연 투고 기간입니다.**" + repl, description=f"우리 모두 투고하고 우승해요!", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '10':
            embed=discord.Embed(title= f"**언어 경연 결과가 나왔습니다.**" + repl, description=f"우승자는 [편집됨]님, [편집됨]님입니다! 상품은 [데이터 말소]입니다!", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '11':
            embed=discord.Embed(title= f"**성탄절 경연 투고 기간입니다.**" + repl, description=f"우리 모두 투고하고 상품받아요!", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '12':
            embed=discord.Embed(title= f"**성탄절 경연 결과가 나왔습니다.**" + repl, description=f"우승자는 [편집됨]님, [편집됨]님입니다! 상품은 [데이터 말소]입니다!", color=0x23bb76) 
            await scp.channel.send(embed=embed)
            
        else:
            embed=discord.Embed(title= f"**http://ko.scp-wiki.net/bimonthly-contests-2020#toc2**" + repl, description=f"", color=0x23bb76)                      
            await scp.channel.send(embed=embed)
            
    if scp.content.startswith('!핑'):
        await scp.channel.send('퐁')   
        
    if scp.content.startswith('!브라단'):
        
        i = random.randint(1,3)
        
        if i == 1:
            await scp.channel.send('지혜의 연어, 브라단입니다.')
            
        if i == 2:
            await scp.channel.send('Made by Cresendo, 이용해주셔서 감사합니다!')
            
        if i == 3:
            await scp.channel.send('SH-KO 에서 일하게 된게 영광인 연어, 브라단입니다.')

    if scp.content.startswith('!scp'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","-")        
        embed=discord.Embed(title= f"http://ko.scp-wiki.net/scp" + repl, description=f"", color=0x23bb76)
        await scp.channel.send(embed=embed) 
        
    if scp.content.startswith('!라틴'):
        info = scp.content[4:len(scp.content)]
        repl = info.replace(" ","+")
        link = "https://latina.bab2min.pe.kr/xe/?vid=xe&mid=latina&act=IS&where=&search_target=title_content&is_keyword=" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name=info, value='[{0}](<{1}>)'.format(info, link), inline=False)
        await scp.channel.send(embed=embed)                

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
