import discord
import os
import requests
from bs4 import BeautifulSoup
from keep_alive import keep_alive

client = discord.Client()

def score_gen():
  results=requests.get("https://www.cricbuzz.com/cricket-match/live-scores/recent-matches")
  src=results.content
  soup=BeautifulSoup(src,'html.parser')
  score=soup.find("div",class_='cb-scr-wll-chvrn cb-lv-scrs-col')
  s2=""
  for s1 in score.text:
    s2=s2+s1
    if s1 == ')':
      s2=s2+"\n"
  return s2

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!livescore'):
    s=score_gen()
    await message.channel.send(s)
 
my_secret = os.environ['TOKEN']   

keep_alive()
client.run(my_secret)


