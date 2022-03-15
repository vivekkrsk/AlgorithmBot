import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands,tasks
from algoDataBase import *

#bot
bot = commands.Bot(command_prefix = '?')

#hello command:
@bot.command(name = "hello")
async def hello(ctx):
  await ctx.send("Hello {}".format(ctx.author))

  
#algolist command:
@bot.command(name = "algolist", help = "Displays the list of algorithms")
async def algolist(ctx):
  #algo list string:
  algo_list = ""
  j = 1
  for i in db.keys():
    algo_list += str(j).ljust(2) + '. ' + (i.capitalize()).ljust(25) + db[i]["time_complexity"].ljust(10) + db[i]["space_complexity"].ljust(10) +"\n"
    j += 1
    if j > 15:
      break
    
  await ctx.send(algo_list)


#display code command:
@bot.command(name = "code", help = "Displays the code of algorithms")
async def code(ctx, arg1, *args):
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

  filename = arg1 + ".txt"
  filepath = 'codes/{}/{}'.format(algo_name, filename)
  try:
    f = open(filepath, 'r')
    code = f.read()
    await ctx.send("```c++\n" + code + "```")
  except:
    await ctx.send("No such code available.")


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

  if len(db.prefix(args[0].lower())) == 0:
    await ctx.send(file=discord.File('kyakr.gif'))
    return

  #matching algos
  if algo_name not in db.keys():
    suggestion = ">>> "+ "_" + "Did you mean: " + "_"
      
    for i in db.prefix(args[0].lower()):
      suggestion += "**" + i + "**" + "\n"
      
    await ctx.send(suggestion)
    return
  space_complexity = db[algo_name][2]
  await ctx.send("```"+"Space Complexity : "+ space_complexity + "```"  )

@bot.command(name = "algo")
async def algo(ctx, *args):
  if len(args) == 0:
    await  ctx.send("**" + "Usage : " +"**" + "`algo <algorithm>`" )
    return
  algo_name = (' '.join(args)).lower()

  if len(db.prefix(args[0].lower())) == 0:
    await ctx.send(file=discord.File('kyakr.gif'))
    return

  #matching algos
  if algo_name not in db.keys():
    suggestion = ">>> "+ "_" + "Did you mean: " + "_"
      
    for i in db.prefix(args[0].lower()):
      suggestion += "**" + i + "**" + "\n"
      
    await ctx.send(suggestion)
    return

  algo_str = ">>> __" + algo_name.capitalize() + "__ \n" + "Time Complexity: " + db[algo_name]["time_complexity"] + "\n" + "Space Complexity: " + db[algo_name]["space_complexity"]

  await ctx.send(algo_str)
  return
  


#add algorithm
@bot.command(name = "add_algo", help="add new algorithm")
async def add_algo(ctx, algo_name):
  await ctx.send(addAlgo(algo_name))


@bot.command(name = "add_time_complexity", aliases = ["atc"], help = "add time complexity of algorithm")
async def add_time_complexity(ctx, algo_name, time_complexity):
  await ctx.send(addTimeComplexity(algo_name, time_complexity))

@bot.command(name = "add_space_complexity", aliases = ["asc"], help = "add space complexity")
async def add_space_complexity(ctx, algo_name, space_complexity):
  await ctx.send(addSpaceComplexity(algo_name, space_complexity))


#algorithm bot logo
@bot.command(name = "algo_bot_logo")
async def algo_bot_logo(ctx):
  await ctx.send(file=discord.File('DigitalFortress.gif'))
  
  
#developers help command
@bot.command(name = "dev_help")
async def dev_help(ctx):
  dev_str = ">>> ___Algorithm Bot___ " + "*Commands:*\n\n" + "Add a new Algorithm : " +'`add_algo "algo_name"`\n' + "Add time complexity : " + '`add_time_complexity "algo name" "time complexity"`\n'+"Add space complexity : " + '`add_space_complexity "algo name" "space complexity"`\n'+"Add space complexity : " + '`add_space_complexity "algo name" "space complexity"`\n'+ "\n*Developed by :* **DigitalFortress**\n\n"
  await ctx.send(file=discord.File('DigitalFortress.gif'))
  await ctx.send(dev_str)



@bot.command(name = "bot_help")
async def how_to_use_algo_bot(ctx):
  dev_str = ">>> ___Algorithm Bot___ " + "*Help Commands:*\n"+ "\n>>>___*Search Commands:*___\n" +"Search algorithm list : " + '` algolist`\n'+"Search pseudo code : " + '` sudocode <algo name>`\n'+"Search  time complexity : " + '` timecomplex <algo name>`\n'+"Search  space complexity : " + '` spacecomplex <algo name>`'+ "\n\n>>>___*Devloper Commands:*___\n"+"Add a new Algorithm : " +'`add_algo "algo_name"`\n' + "Add time complexity : " + '`add_time_complexity "algo name" "time complexity"`\n'+ "\n*Developed by :* **DigitalFortress**\n\n"
  await ctx.send(file=discord.File('DigitalFortress.gif'))
  await ctx.send(dev_str)



#flask app
keep_alive() 
bot.run(os.getenv('TOKEN'))