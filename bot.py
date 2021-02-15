import discord
import os
import random
import asyncio
import feedparser
import requests
from bs4 import BeautifulSoup

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="남태령—여우고개")
    if channel:
        await asyncio.sleep(1)
        embed=discord.Embed(title=f"환영합니다! {member.name}님!", description="SCP 세계관 공식 한국어 사이트 대화방에 오신걸 환영합니다!", color=0x00ff56)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/715122773298511922/715410982901514271/sh.png")
        embed.add_field(name="일단,", value=f"member 권한이 없으신 분들께서 껐다 키면 로그가 안 보이는 불편을 겪으실 수 있습니다. <#563173658231701507>, <#563278103951179786>외의 다른 방에 못 들어가는 불편 역시 겪으실 수 있습니다. (<#563173658231701507>에 들어가시면 자세히 보실 수 있습니다).", inline=True)
        embed.add_field(name="그리고,", value="위키닷에 가입하신후, 재단 위키에 가입 신청을 해서 합격하면 member 권한을 얻으실 수 있습니다. http://scpko.wikidot.com/system:join 이 링크로 들어가시면 됩니다. 가입 신청을 넣을 때에는 신입안내를 반드시 처음부터 끝까지 꼼꼼히 읽으셔야 합니다.", inline=True)
        embed.add_field(name="주의하셔야 할점이 있는데,", value="만약 가입 절차 내용을 누설 시 __***즉시 밴 처리 될 수 있습니다.***__ 또한 __***비회원은 경고시 즉시 밴***__임을 숙지해주시길 부탁드립니다. 더 많은 규칙을 위해 http://scpko.wikidot.com/chat-guide 이걸 읽어주세요.", inline=True)
        embed.add_field(name="멤버 확인을 위해서,", value="관리자가 가입 신청을 수락하면 위키닷 닉네임과 디코 닉네임을 동일하게 바꾸어 주세요. 이 디스코드 서버에서만 바꾸시면 됩니다. 완료되면 @unterstaff로 스태프분들을 호출하세요. 스태프 분이 확인 뒤 멤버 권한을 드릴겁니다.", inline=True)
        embed.set_footer(text="수동이라서 느릴 수 있는 점, 양해 부탁드립니다. 다시 한번 SCP 세계관 공식 한국어 사이트 대화방에 오신 것을 환영합니다.")
        await channel.send(embed=embed)         
        
@client.event
async def on_message(scp):
    if scp.author == client.user:
        return
    
    if scp.content.startswith('!업데이트'):
        await scp.channel.send('업데이트 내역: 자동 경연 및 스레드 홍보')
        
    elif scp.content.startswith('!버전'):
        await scp.channel.send('버전 3.0, 가입 안내 메세지 생성!')  
        
    elif scp.content.startswith('!경고'):
        await scp.channel.send('경고입니다. 비회원은 경고시 즉시 밴임을 알아두시기 바랍니다.')  
        
    elif scp.content.startswith('!가입'):
        await scp.channel.send('위키닷만 가입하신 것 같은데, 재단 위키에도 따로 가입을 해야합니다. 그러니까 네이버와 네이버 카페 같은 거죠. 신청서를 내시고 승인받으면 재단 위키 가입 완료입니다. 링크는 http://scpko.wikidot.com/guide-for-newbies 여기서 해주세요!')         
        
    elif scp.content.startswith('!최근'):  
        f = feedparser.parse('http://scpko.wikidot.com/feed/pages/pagename/most-recently-created/category/_default/order/created_at+desc/limit/1/t/%EC%B5%9C%EA%B7%BC+%EC%83%9D%EC%84%B1%EB%90%9C+%ED%8E%98%EC%9D%B4%EC%A7%80')
        
        if len(f['entries']):
            feed = list(f['entries'])[0]
            embed=discord.Embed(title= f"최근 페이지", description="", color=0x23bb76)
            embed.add_field(name="최근 페이지 결과", value=f'[{feed.title}](<{feed.link}>)', inline=False)
            await scp.channel.send(embed=embed)
    
    elif scp.content.startswith('!샌박'):
        info = scp.content[4:]
        repl= info.replace(" ","-")
        n_link = "http://scpkosb.wikidot.com/portal:" + repl
        o_link = "http://sandbox.scp-wiki.kr/" + repl
        
        embed=discord.Embed(title= f"{info} 검색 결과", description="", color=0x23bb76)
        embed.add_field(name="구 샌박: " + info, value=f'[{info}](<{o_link}>)', inline=False)
        embed.add_field(name="신 샌박: " + info, value=f'[{info}](<{n_link}>)', inline=False)
        await scp.channel.send(embed=embed)
        
    elif scp.content.startswith('!구글'):
        info = scp.content[4:]
        repl= info.replace(" ","+") 
        link = "https://www.google.com/search?q=" + repl
        embed=discord.Embed(title= f"{info} 검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name=f"'{info}'의 구글 검색 결과", value=f'[{info}](<{link}>)', inline=False)
        await scp.channel.send(embed=embed)    
        
    elif scp.content.startswith('!유저'):
        info = scp.content[4:]
        repl= info.replace(" ","_") 
        link = "http://www.wikidot.com/user:info/" + repl
        embed=discord.Embed(title= f"{info} 검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name=f"'{info}'의 유저 검색 결과", value=f'[{info}](<{link}>)', inline=False)
        await scp.channel.send(embed=embed)  

    elif scp.content.startswith('!태그'):
        info = scp.content[4:]
        repl= info.replace(" ","+") 
        link = "http://scpko.wikidot.com/system:page-tags/tag/" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name=f"'{info}'의 태그 검색 결과", value=f'[{info}](<{link}>)', inline=False)
        await scp.channel.send(embed=embed)  
        
    elif scp.content.startswith('!위백'):
        info = scp.content[4:]
        repl= info.replace(" ","_") 
        link = "https://ko.wikipedia.org/wiki/" + repl
        embed=discord.Embed(title= f"{info} 검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name=f"'{info}'의 검색 결과", value=f'[{info}](<{link}>)', inline=False)
        await scp.channel.send(embed=embed)  
        
    elif scp.content.startswith('!명령어'): 
        embed=discord.Embed(title=f"도와드릴까요?", description="명령어 목록", color=0x00ff56)
        embed.add_field(name="검색기능", value="!구글, !위백, !scp, !태그, !샌박, !랜덤, !라틴", inline=True)
        embed.add_field(name="관리기능", value="!경고, !가입, !투표, 자동 ", inline=True)
        embed.add_field(name="부가기능", value="!명령어, !환영, !업데이트, !핑, !브라단, !경연, !최근, !버전", inline=True)
        await scp.channel.send(embed=embed)
        
    elif scp.content.startswith('!환영'): 
        embed=discord.Embed(title=f"환영합니다!", description="SCP 세계관 공식 한국어 사이트 대화방에 오신걸 환영합니다!", color=0x00ff56)
        embed.set_thumbnail(url="http://scpko.wdfiles.com/local--files/dinodon-s-hand/SH-KO.png")
        embed.add_field(name="일단,", value=f"member 권한이 없으신 분들께서 껐다 키면 로그가 안 보이는 불편을 겪으실 수 있습니다. <#563173658231701507>, <#563278103951179786>외의 다른 방에 못 들어가는 불편 역시 겪으실 수 있습니다. (<#563173658231701507>에 들어가시면 자세히 보실 수 있습니다).", inline=True)
        embed.add_field(name="그리고,", value="위키닷에 가입하신후, 재단 위키에 가입 신청을 해서 합격하면 member 권한을 얻으실 수 있습니다. http://scpko.wikidot.com/system:join 이 링크로 들어가시면 됩니다. 가입 신청을 넣을 때에는 신입안내를 반드시 처음부터 끝까지 꼼꼼히 읽으셔야 합니다.", inline=True)
        embed.add_field(name="주의하셔야 할점이 있는데,", value="만약 가입 절차 내용을 누설 시 __***즉시 밴 처리 될 수 있습니다.***__ 또한 __***비회원은 경고시 즉시 밴***__임을 숙지해주시길 부탁드립니다. 더 많은 규칙을 위해 http://scpko.wikidot.com/chat-guide 이걸 읽어주세요.", inline=True)
        embed.add_field(name="멤버 확인을 위해서,", value="관리자가 가입 신청을 수락하면 위키닷 닉네임과 디코 닉네임을 동일하게 바꾸어 주세요. 이 디스코드 서버에서만 바꾸시면 됩니다. 완료되면 스태프 분들을 호출하세요. 스태프 분이 확인 뒤 멤버 권한을 드릴겁니다.", inline=True)
        embed.set_footer(text="수동이라서 느릴 수 있는 점, 양해 부탁드립니다. 다시 한번 SCP 세계관 공식 한국어 사이트 대화방에 오신 것을 환영합니다.")
        await scp.channel.send(embed=embed)

    elif scp.content.startswith('!경연'):
        embed=discord.Embed(title=f"현재 진행중인 경연 목록", description="", color=0x23bb76)
        embed.add_field(name="http://scpko.wikidot.com/samcheonri-contest#toc2")
        embed.add_field(name="http://scpko.wikidot.com/2g3a-contest-hub")
        await scp.channel.send(embed=embed)
            
    elif scp.content.startswith('!핑'):  
        await scp.channel.send('퐁')

    elif scp.content.startswith('!투표'):  
        await scp.add_reaction('a:voteup:723564695579000903')
        await scp.add_reaction('a:voteno:723564695755162065')
        await scp.add_reaction('a:votedown:723564695486988319')
        
    elif scp.content.startswith('!브라단'):  
        i = random.randint(1,2)
        
        if i == 1:
            await scp.channel.send('지혜의 연어, 브라단입니다.')
            
        else:
            await scp.channel.send('Made by Cresendo, 이용해주셔서 감사합니다!')

    elif scp.content.startswith('!scp'):
        info = scp.content[5:]
        repl= info.replace(" ","-")  
        link = "http://scpko.wikidot.com/scp-" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name=f"'SCP-{repl}'의 검색 결과", value=f'[{info}](<{link}>)', inline=False)
        await scp.channel.send(embed=embed) 
        
    elif scp.content.startswith('!라틴'):
        info = scp.content[4:]
        repl = info.replace(" ","+")
        link = "https://latina.bab2min.pe.kr/xe/?vid=xe&mid=latina&act=IS&where=&search_target=title_content&is_keyword=" + repl
        embed=discord.Embed(title= f"검색 결과", description=f"", color=0x23bb76)
        embed.add_field(name=f"'{info}'의 검색 결과", value=f'[{info}](<{link}>)', inline=False)
        await scp.channel.send(embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    Channel = discord.utils.get(client.guild.channels, name="섭스크라이버-등록")
    if reaction.channel.id != Channel:
        return
    if reaction.emoji == '👍':
        async def _Sub(ctx, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="subscriber"))

              
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
