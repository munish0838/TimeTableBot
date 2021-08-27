import discord
import os
import json
import discord.ext
import datetime
from keep_alive import keep_alive
from days  import monday
from days  import tuesday
from days  import wednesday
from days  import thursday
from days  import friday
#from days import commands
#from days import classroom

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(activity = discord.Game('Your Class Schedule'))
  print('WE have looged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
   return
  #this is for curent day
  
  current = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
  
  day = current.weekday() 
  
  
  #commands list
  if message.content.startswith('.list commands'):
    await message.channel.send(embed=commands())
  
  
  
  '''#for subjects
  if message.content.startswith('.subjects'):
    await message.channel.send('https://cdn.discordapp.com/attachments/797750483250839583/828202806539845652/unknown.png')'''
  
    
  '''#gcr codes
  if message.content.startswith('.classroom'):
    await message.channel.send(embed=classroom())'''


  #function to print the curretn day time table
  if message.content.startswith('.today') or message.content.startswith('.aaj'):
    if day ==0:
      await message.channel.send  (embed=monday())
    elif day ==1:
      await message.channel.send  (embed=tuesday())
    elif day ==2:
      await message.channel.send(embed=   wednesday())
    elif day ==3:
      await message.channel.send  (embed=thursday())
    elif day ==4:
      await message.channel.send(embed =  friday())
    elif day ==5:
      await message.channel.send('https://cdn.discordapp.com/attachments/865954484244185152/880791466375536670/unknown.png')  
    else:
      await message.channel.send('NO CLASSES TODAY')          
  
  #command for next day time table
  if message.content.startswith('.tom') or message.content.startswith('.kal'):
    day+=1
    if day ==0:
      await message.channel.send  (embed=monday())
    elif day ==1:
      await message.channel.send  (embed=tuesday())
    elif day ==2:
      await message.channel.send(embed=   wednesday())
    elif day ==3:
      await message.channel.send  (embed=thursday())
    elif day ==4:
      await message.channel.send(embed =  friday())
    elif day ==5:
      await message.channel.send('https://cdn.discordapp.com/attachments/865954484244185152/880791466375536670/unknown.png')    
    elif day ==6:
      await message.channel.send('NO CLASSES TOMORROW')
    elif day>6:
      await message.channel.send(embed =monday())
  
  
  
  #making all commands for time tabel of all days
  if message.content.startswith('.monday'):
    await message.channel.send(embed=monday()) 

  if message.content.startswith('.tuesday'):
    await message.channel.send(embed=tuesday())

  if message.content.startswith('.wednesday'):
    await message.channel.send(embed=wednesday())

  if message.content.startswith('.thursday'):
    await message.channel.send(embed=thursday())

  if message.content.startswith('.friday'):
    await message.channel.send(embed=friday())      


keep_alive()
client.run(os.getenv('TOKEN')) 