import discord
from discord.ext import commands
import random
print(discord.__version__)

bot = commands.Bot(command_prefix='$')





@bot.event
async def on_ready():
   game = discord.Game("with the API")
   await client.change_presence(status=discord.Status.idle, activity=game)







  



@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="$help"))
    print("bot is readyy")




    
    





@bot.event
async def on_ready():
        print('bot is ready')
      
      
      
      
      
@bot.command()
async def feedback(ctx, *, text):
    slimbo = bot.get_user(180927756761169920)
    author = ctx.message.author
    if ctx.channel.id == 568518780146286602:
         await ctx.message.delete()
         await ctx.author.send("Sending the feedback to slimbo.....")
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
async def iq(ctx):
    author = ctx.message.author
    IQ = random.randint(0,200)
    await ctx.send(f"{author} has {IQ} IQ")




@bot.command()
async def h(ctx):
    channelvc = ctx.author.voice_channel
    await ctx.send("Someone need your help in {}".format(channelvc)) 


@bot.command()
async def clear(ctx, amount: int):
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"Deleted {len(deleted)} messages")




@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)
    


bot.run('NTYxMjc4MjI5MTc3MTcxOTcy.XLYrqA.bBMIN7_dNBsEsGfvd6oNUu562to')
