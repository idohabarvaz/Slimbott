import discord
from discord.ext import commands
import random
print(discord.__version__)

bot = commands.Bot(command_prefix='$')





@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.idle, activity=game, )
  print('bot is ready')







  







    
    





@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="$help"))
        print('bot is ready')
      
      
      
      
      
@bot.command()
async def feedback(ctx, *, text):
    slimbo = ctx.guild.owner.id
    author = ctx.message.author
    if ctx.channel.id == 568518780146286602:
         await ctx.message.delete()
         await ctx.author.send("Sending the feedback to slimbo.....")
         await asyncio.sleep(2)
         await bot.message.delete()
         await slimbo.send(f"{author} send you a feedback: {text}")
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
async def iq(ctx,members: commands.Greedy[discord.Member]):
  His_iq = ", ".join(x.name for x in members)
  author = ctx.message.author
  IQ = random.randint(0,200)
  await ctx.send(f"{His_iq} has {IQ} IQ")





@bot.command()
async def clear(ctx, amount: int):
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"Deleted {len(deleted)} messages")




@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)
    


bot.run('NTYxMjc4MjI5MTc3MTcxOTcy.XLYrqA.bBMIN7_dNBsEsGfvd6oNUu562to')
