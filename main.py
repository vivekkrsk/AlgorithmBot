import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands,tasks
from algoDataBase import add_algo,clear_db

#bot
bot = commands.Bot(command_prefix = '?')

#hello command:
@bot.command(name = "hello")
async def hello(ctx):
  await ctx.send("Hello {}".format(ctx.author))

  
#algo list string:
algo_list = ""
j = 1
for i in db.keys():
  algo_list += str(j) + ". " + i + "\n"
  j += 1

  
#algolist command:
@bot.command(name = "algolist", aliases = ["alglist"], help = "Displays the list of algorithms")
async def algolist(ctx):
  await ctx.send(">>> " + algo_list)


#pseudo-code command:
@bot.command(name = "sudocode", aliases = ["sdc"], help = "Displays the pseudo code of algorithms")
async def sudocode(ctx, *args):
  if len(args) == 0:
    await  ctx.send("**" + "Usage : " +"**" + "`sudocode <algorithm>`" )
    return
    
  algo_name = (' '.join(args)).lower()

  if len(db.prefix(args[0])) == 0:
    await ctx.send(file=discord.File('kyakr.gif'))
    return
  
  if algo_name not in db.keys():
    suggestion = ">>> "+ "_" + "Did you mean: " + "_"
    for i in db.prefix(args[0]):
      suggestion += "**" + i + "**" + "\n"
      
    await ctx.send(suggestion)
    return
    
  sudo_code = db[algo_name][0]
  await ctx.send("```" + sudo_code + "```")

#time complexity command
@bot.command(name = "timecomplex", aliases = ["tc"], help = "Displays the time complexity")
async def timecomplex(ctx, *args):
  if len(args) == 0:
    await  ctx.send("**" + "Usage : " +"**" + "`timecomplex <algorithm>`" )
    return
  algo_name = (' '.join(args)).lower()

  if len(db.prefix(args[0])) == 0:
    await ctx.send(file=discord.File('kyakr.gif'))
    return
    
  if algo_name not in db.keys():
    suggestion = ">>> "+ "_" + "Did you mean: " + "_"
    for i in db.prefix(args[0]):
      suggestion += "**" + i + "**" + "\n"
      
    await ctx.send(suggestion)
    return
  time_complex = db[algo_name][1]
  await ctx.send("```" + "Time Complexity : " + time_complex + "```")

#space complexity command
@bot.command(name = "spacecomplex", aliases = ["sc"], help = "Display the space complexity")
async def spacecomplex(ctx, *args):
  #empty tuple
  if len(args) == 0:
    await  ctx.send("**" + "Usage : " +"**" + "`spacecomplex <algorithm>`" )
    return
  algo_name = (' '.join(args)).lower()

  if len(db.prefix(args[0])) == 0:
    await ctx.send(file=discord.File('kyakr.gif'))
    return

  #matching algos
  if algo_name not in db.keys():
    suggestion = ">>> "+ "_" + "Did you mean: " + "_"
      
    for i in db.prefix(args[0]):
      suggestion += "**" + i + "**" + "\n"
      
    await ctx.send(suggestion)
    return
  space_complexity = db[algo_name][2]
  await ctx.send("```"+"Space Complexity : "+ space_complexity + "```"  )

#flask app
keep_alive() 
bot.run(os.getenv('TOKEN'))