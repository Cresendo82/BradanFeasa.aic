import discord
import os
import random
import time
import feedparser
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel.name == '남태령':
            time.sleep(1)
            embed=discord.Embed(title=f"환영합니다! " + member.name + "님!", description="SCP 세계관 공식 한국어 사이트 대화방에 오신걸 환영합니다!", color=0x00ff56)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/715122773298511922/715410982901514271/sh.png")
            embed.add_field(name="일단,", value=f"member 권한이 없으신 분들께서 껐다 키면 로그가 안 보이는 불편을 겪으실 수 있습니다. <#563173658231701507>, <#556145244832530433>외의 다른 방에 못 들어가는 불편 역시 겪으실 수 있습니다. (<#563173658231701507>에 들어가시면 자세히 보실 수 있습니다).", inline=True)
            embed.add_field(name="그리고,", value="위키닷에 가입하신후, 재단 위키에 가입 신청을 해서 합격하면 member 권한을 얻으실 수 있습니다. http://ko.scp-wiki.net/system:join 이 링크로 들어가시면 됩니다. 가입 신청을 넣을 때에는 신입안내를 반드시 처음부터 끝까지 꼼꼼히 읽으셔야 합니다.", inline=True)
            embed.add_field(name="주의하셔야 할점이 있는데,", value="만약 가입 절차 내용을 누설 시 __***즉시 밴 처리 될 수 있습니다.***__ 또한 __***비회원은 경고시 즉시 밴***__임을 숙지해주시길 부탁드립니다. 더 많은 규칙을 위해 http://ko.scp-wiki.net/chat-guide 이걸 읽어주세요.", inline=True)
            embed.add_field(name="멤버 확인을 위해서,", value="관리자가 가입 신청을 수락하면 위키닷 닉네임과 디코 닉네임을 동일하게 바꾸어 주세요. 이 디스코드 서버에서만 바꾸시면 됩니다. 완료되면 스태프 분들을 호출하세요. 스태프 분이 확인 뒤 멤버 권한을 드릴겁니다.", inline=True)
            embed.set_footer(text="수동이라서 느릴 수 있는 점, 양해 부탁드립니다. 다시 한번 SCP 세계관 공식 한국어 사이트 대화방에 오신 것을 환영합니다.")
            await channel.send(embed=embed)          
    
@client.event
async def on_message(scp):
    if scp.author == client.user:
        return

    if scp.content.startswith('!업데이트'):

        await scp.channel.send('업데이트 내역: 가입 안내 메세지 생성!')
        
    if scp.content.startswith('!버전'):

        await scp.channel.send('버전 2.2.7, 가입 안내 메세지 생성!')  
        
    if scp.content.startswith('!경고'):

        await scp.channel.send('경고입니다. 비회원은 경고시 즉시 밴임을 알아두시기 바랍니다.')  
        
    if scp.content.startswith('!가입'):

        await scp.channel.send('위키닷만 가입하신 것 같은데, 재단 위키에도 따로 가입을 해야합니다. 그러니까 네이버와 네이버 카페 같은 거죠. 신청서를 내시고 승인받으면 재단 위키 가입 완료입니다. 링크는 http://ko.scp-wiki.net/guide-for-newbies 여기서 해주세요!')         
        
    if scp.content.startswith('!os'):

        await scp.channel.send(os.getcwd())    
        
    if scp.content.startswith('!최근'):
        
        i = 0
        
        f = feedparser.parse('http://ko.scp-wiki.net/feed/pages/pagename/most-recently-created/category/_default/order/created_at+desc/limit/1/t/%EC%B5%9C%EA%B7%BC+%EC%83%9D%EC%84%B1%EB%90%9C+%ED%8E%98%EC%9D%B4%EC%A7%80')
 
        for feed in f['entries']:
            i = i+1
            embed=discord.Embed(title= f"최근 페이지", description=f"", color=0x23bb76)
            embed.add_field(name="최근 페이지 결과", value='[{0}](<{1}>)'.format(feed.title, feed.link), inline=False)
            await scp.channel.send(embed=embed)
            if i == 1:
                break
    
    if scp.content.startswith('!샌박'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","-")
        link = "http://sandbox.scp-wiki.kr/" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name="'" + info + "'" + "의 샌드박스 페이지", value='[{0}](<{1}>)'.format(info, link), inline=False)
        await scp.channel.send(embed=embed)          
        
    if scp.content.startswith('!구글'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","+") 
        link = "https://www.google.com/search?q=" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name="'" + info + "'" + "의 구글 검색 결과", value='[{0}](<{1}>)'.format(info, link), inline=False)
        await scp.channel.send(embed=embed)    
        
    if scp.content.startswith('!유저'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","_") 
        link = "http://www.wikidot.com/user:info/" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name="'" + info + "'" + " 유저 검색 결과", value='[{0}](<{1}>)'.format(info, link), inline=False)
        await scp.channel.send(embed=embed)  

    if scp.content.startswith('?유저'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","_") 
        link = "http://www.wikidot.com/user:info/" + repl
        req = requests.get(link)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        my = soup.find_all("a",{"href":"http://ko.scp-wiki.net"})
        
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name="'" + info + "'" + " 유저 검색 결과", value='[{0}](<{1}>)'.format(info, link), inline=False)   
        embed.add_field(name='유저 가입 현황', value='{0}'.format(my), inline=False)
            
        await scp.channel.send(embed=embed)
        
    if scp.content.startswith('!태그'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","+") 
        link = "http://ko.scp-wiki.net/system:page-tags/tag/" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name="'" + info + "'" + " 태그 검색 결과", value='[{0}](<{1}>)'.format(info, link), inline=False)
        await scp.channel.send(embed=embed)  
        
    if scp.content.startswith('!위백'):
        info = scp.content[4:len(scp.content)]
        repl= info.replace(" ","_") 
        link = "https://ko.wikipedia.org/wiki/" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name="'" + info + "'" + "  검색 결과", value='[{0}](<{1}>)'.format(info, link), inline=False)
        await scp.channel.send(embed=embed)  
        
    if scp.content.startswith('!명령어'):
        
        embed=discord.Embed(title=f"도와드릴까요?", description="명령어 목록", color=0x00ff56)
        embed.add_field(name="검색기능", value="!구글, !위백, !scp, !태그, !샌박, !랜덤, !라틴", inline=True)
        embed.add_field(name="부가기능", value="!명령어, !환영, !업데이트, !핑, !브라단, !경연, !최근, !버전, !경고, !가입", inline=True)
        await scp.channel.send(embed=embed)
        
    if scp.content.startswith('!환영'): 
        
        embed=discord.Embed(title=f"환영합니다!", description="SCP 세계관 공식 한국어 사이트 대화방에 오신걸 환영합니다!", color=0x00ff56)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/715122773298511922/715410982901514271/sh.png")
        embed.add_field(name="일단,", value=f"member 권한이 없으신 분들께서 껐다 키면 로그가 안 보이는 불편을 겪으실 수 있습니다. <#563173658231701507>, <#556145244832530433>외의 다른 방에 못 들어가는 불편 역시 겪으실 수 있습니다. (<#563173658231701507>에 들어가시면 자세히 보실 수 있습니다).", inline=True)
        embed.add_field(name="그리고,", value="위키닷에 가입하신후, 재단 위키에 가입 신청을 해서 합격하면 member 권한을 얻으실 수 있습니다. http://ko.scp-wiki.net/system:join 이 링크로 들어가시면 됩니다. 가입 신청을 넣을 때에는 신입안내를 반드시 처음부터 끝까지 꼼꼼히 읽으셔야 합니다.", inline=True)
        embed.add_field(name="주의하셔야 할점이 있는데,", value="만약 가입 절차 내용을 누설 시 __***즉시 밴 처리 될 수 있습니다.***__ 또한 __***비회원은 경고시 즉시 밴***__임을 숙지해주시길 부탁드립니다. 더 많은 규칙을 위해 http://ko.scp-wiki.net/chat-guide 이걸 읽어주세요.", inline=True)
        embed.add_field(name="멤버 확인을 위해서,", value="관리자가 가입 신청을 수락하면 위키닷 닉네임과 디코 닉네임을 동일하게 바꾸어 주세요. 이 디스코드 서버에서만 바꾸시면 됩니다. 완료되면 스태프 분들을 호출하세요. 스태프 분이 확인 뒤 멤버 권한을 드릴겁니다.", inline=True)
        embed.set_footer(text="수동이라서 느릴 수 있는 점, 양해 부탁드립니다. 다시 한번 SCP 세계관 공식 한국어 사이트 대화방에 오신 것을 환영합니다.")
        await scp.channel.send(embed=embed)
        
    if scp.content.startswith('!랜덤'):
        embed=discord.Embed(title= f"랜덤 scp", description=f"", color=0x23bb76)
        embed.add_field(name="", value='[랜덤!](<{0}>)'.format(info, 'http://ko.scp-wiki.net/random:random-scp'), inline=False)
        await scp.channel.send(embed=embed)
        
    if scp.content.startswith('!경연'):
        
        info = scp.content[4:len(scp.content)]
        
        if info == '1':
            embed=discord.Embed(title= f"**성탄절 경연 결과가 나왔습니다.**", description=f"우승자는 Crislr님, ZachRobinson님입니다! 상품은... 호주산 살치살입니다! 대박", color=0x23bb76)        
            await scp.channel.send(embed=embed)
            
        elif info == '2':
            embed=discord.Embed(title= f"**경연 검색 결과 없음**", description=f"", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '3':
            embed=discord.Embed(title= f"**나무 경연 투고 기간입니다.**", description=f"이미 지났네요. 아쉽다", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '4':
            embed=discord.Embed(title= f"**나무 경연 결과가 나왔습니다.**", description=f"우승자는 thd-glasses님입니다! 상품은 BBQ 황금올리브치킨 반반입니다.", color=0x23bb76)      
            await scp.channel.send(embed=embed)
            
        elif info == '5':
            embed=discord.Embed(title= f"**열쇠 경연 투고 기간입니다.**", description=f"이미 지나가버린 경연입니다. 아쉽당", color=0x23bb76)        
            await scp.channel.send(embed=embed)
            
        elif info == '6':
            embed=discord.Embed(title= f"**열쇠 경연 결과가 나왔습니다.**", description=f"우승자는 Nareum님, Profound Kaye님입니다! 상품은 등킨 도나쓰 20개입니다.", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '7':
            embed=discord.Embed(title= f"**물고기 경연 투고 기간입니다.**", description=f"우리 모두 다 같이 투고해요!", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '8':
            embed=discord.Embed(title= f"**물고기 경연 결과가 나왔습니다.**", description=f"우승자는 [편집됨]님, [편집됨]님입니다! 상품은 [데이터 말소]입니다!", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '9':
            embed=discord.Embed(title= f"**언어 경연 투고 기간입니다.**", description=f"우리 모두 투고하고 우승해요!", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '10':
            embed=discord.Embed(title= f"**언어 경연 결과가 나왔습니다.**", description=f"우승자는 [편집됨]님, [편집됨]님입니다! 상품은 [데이터 말소]입니다!", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '11':
            embed=discord.Embed(title= f"**성탄절 경연 투고 기간입니다.**", description=f"우리 모두 투고하고 상품받아요!", color=0x23bb76)
            await scp.channel.send(embed=embed)
            
        elif info == '12':
            embed=discord.Embed(title= f"**성탄절 경연 결과가 나왔습니다.**", description=f"우승자는 [편집됨]님, [편집됨]님입니다! 상품은 [데이터 말소]입니다!", color=0x23bb76) 
            await scp.channel.send(embed=embed)
            
        else:
            embed=discord.Embed(title= f"**http://ko.scp-wiki.net/bimonthly-contests-2020#toc4**", description=f"", color=0x23bb76)                      
            await scp.channel.send(embed=embed)
            
    if scp.content.startswith('!핑'):
        
        await scp.channel.send('퐁')

    if scp.content.startswith('?반응'):  
        
        await scp.add_reaction(🐟)
        
    if scp.content.startswith('!브라단'):
        
        i = random.randint(1,3)
        
        if i == 1:
            await scp.channel.send('지혜의 연어, 브라단입니다.')
            
        if i == 2:
            await scp.channel.send('Made by Cresendo, 이용해주셔서 감사합니다!')
            
        if i == 3:
            await scp.channel.send('SH-KO 에서 일하게 된게 영광인 연어, 브라단입니다.')

    if scp.content.startswith('!scp'):
        info = scp.content[5:len(scp.content)]
        repl= info.replace(" ","-")  
        link = "http://ko.scp-wiki.net/scp-" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name="'" + info + "'" + "의 검색 결과", value='[{0}](<{1}>)'.format(info, link), inline=False)
        await scp.channel.send(embed=embed) 
        
    if scp.content.startswith('!라틴'):
        info = scp.content[4:len(scp.content)]
        repl = info.replace(" ","+")
        link = "https://latina.bab2min.pe.kr/xe/?vid=xe&mid=latina&act=IS&where=&search_target=title_content&is_keyword=" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name="'" + info + "'" + "의 검색 결과", value='[{0}](<{1}>)'.format(info, link), inline=False)
        await scp.channel.send(embed=embed)            

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
