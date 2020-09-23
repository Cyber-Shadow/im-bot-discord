import discord
import asyncio
import re
from random import randint 
client = discord.Client()
global list_im
global list_your
list_im = ["I'm","i'm","im","Im","IM"]
list_your = ["youre", "your", "you're", "You're", "Your", "Youre"]

def exists(ind, lst):
  try:
    numb = lst.index(ind)
    return numb 
  except:
    return 99999
  

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print (str(message.content) + " " + str(message.author))
    
    mess = (message.content).split(" ")
    
    pos = []
    
    ap = []
    
    if any(y in list_im for y in mess):
      for x in list_im:
        pos.append(exists(x,mess))
        
      for x in mess:
         if int(mess.index(x)) > int(min(pos)):
           ap.append(x)
      
      sections = 0
      for x in list_im:
        sections += message.content.count(x)
      
      ap = []
      for x in range(sections):
        print (re.split("I'm","i'm","im","Im","IM",message.content)[1+x])
        ap.append("Hi, " + str(message.content.split("I'm","i'm","im","Im","IM")[1+x])) 
        
      await client.send_message(message.channel,  '<@%s>' % message.author.id + ' ' + str(" ".join(ap)) + "! I'm Bot")
    
    
    elif any(y in list_your for y in mess):
      for x in list_your:
        pos.append(exists(x,mess))
        
      for x in mess:
         if int(mess.index(x)) > int(min(pos)):
           ap.append(x)
      
      if randint(0,1) == 1:  
        await client.send_message(message.channel,  '<@%s>' % message.author.id + " No, I'm Bot")
      else:
        await client.send_message(message.channel,  '<@%s>' % message.author.id + ' NO U')
    




client.run('insert bot token here')
