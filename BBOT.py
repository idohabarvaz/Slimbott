import discord
from discord.ext import commands
import random
print(discord.__version__)
from discord.utils import get
bot = commands.Bot(command_prefix='$')







@bot.command()
async def h(ctx):
 embed=discord.Embed(title="MarsBoat Help", color=0xe124d3)
 embed.set_author(name="MarsBoat Commands ")
 embed.set_thumbnail(url="https://res.cloudinary.com/teepublic/image/private/s--PSVQzzUf--/t_Preview/b_rgb:5e366e,c_limit,f_jpg,h_630,q_90,w_630/v1525073416/production/designs/2640845_0.jpg")
 embed.add_field(name="$h", value="See this message", inline=True)
 embed.add_field(name="$feedback", value="Write Feedback on The channel you are using", inline=False)
 embed.add_field(name="$feedbot" , value="Write a feeback about my bot", inline=False)
 embed.add_field(name="$iq", value="Shows someone's iq", inline=True)
 embed.add_field(name='$slap', value='slap someone', inline=True)
 embed.add_field(name='$clear', value='Clear amount of messages', inline=True)
 embed.add_field(name='$echo', value='Send what you send', inline=True)
 embed.add_field(name='$owner', value='Shows The guild owner', inline=True)
 embed.add_field(name='$invite', value='Invite the bot to your server', inline=True)
 embed.set_footer(text="IDO#6999")
 await ctx.send(embed=embed)





  




@bot.command()
async def invite(ctx):
  await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=561278229177171972&permissions=8&scope=bot")
  

    


@bot.command()
async def feedbot(ctx, *, text):
   ido = bot.get_user(427841299920453634)
   author = ctx.message.author
   await ido.send(f"{author} sent you a feedbot: {text}")
   await ctx.message.delete()

@bot.command()
async def owner(ctx):
    owner = ctx.guild.owner
    owner_id = ctx.guild.owner.id
    await ctx.send(f"The Guild's owner is {owner} and his id is {owner_id}")

       
      
      
      
@bot.command()
async def feedback(ctx, *, text):
    
    channel = discord.utils.get(ctx.guild.channels, name="feedbacks")
    slimbo = ctx.guild.owner
    author = ctx.message.author
    if ctx.channel.id == channel.id:
         await slimbo.send(f"{author} send you a feedback: {text}")
         await ctx.message.delete()
         await ctx.author.send("Thank You.")
         await asyncio.sleep(2)
         await ctx.message.delete()
    else:
         await ctx.message.delete()
    await ctx.send(f"sorry {author} but you can't use the command here, try to use it in feedback channel.")





@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))






@bot.command()
async def join(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()



@bot.command()
async def leave(ctx):
        await ctx.voice_client.disconnect()
  
  
  
  @bot.command()
async def bigorsmall(ctx, *, thing):
    thingy = random.randint(1, 2)
    if thingy == 1:
        await ctx.send(f"{thing} is  small")
    if thingy == 2:
        await ctx.send(f"{thing} is  huge")

    
   




@bot.command()
async def guess(ctx, num):
    random_num = random.randint(1, 10)
    await ctx.send("1 - 10")
    if num == random_num:
        await ctx.send("Good Job!")
    else:
        await ctx.send(f"{num} to {random_num} sooo close")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  



@bot.command()
async def iq(ctx,members: commands.Greedy[discord.Member]):
  His_iq = ", ".join(x.name for x in members)
  author = ctx.message.author
  IQ = random.randint(0,200)
  await ctx.send(f"{His_iq} has {IQ} IQ")



@bot.command()
async def war(ctx):
    author = ctx.message.author
    pc = random.randint(1, 13)
    bot = random.randint(1, 13)
    if pc == bot:
        bot = random.randint(1, 13)
        pc = random.randint(1, 13)
        await ctx.send("its a draw")
        await ctx.send("1 2 3 ")
        if bot > pc:
            await ctx.send("bot  won")
        if pc > bot:
            await ctx.send("You are the winner")
    if pc > bot:
        await ctx.send(f"{author} = {pc} and bot = {bot}")
        await ctx.send("You are the winner")
    if pc < bot:
        await ctx.send(f"{author} = {pc} and bot = {bot}")
        await ctx.send('You are the loser')
  
  
  
  
  
  
  
  
  
  
  
  
  
@bot.command()
async def clear(ctx, amount: int):
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"Deleted {len(deleted)} messages")




@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)
    


bot.run('NTYxMjc4MjI5MTc3MTcxOTcy.XLYrqA.bBMIN7_dNBsEsGfvd6oNUu562to')
