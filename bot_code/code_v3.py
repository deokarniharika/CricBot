import discord
import os
import requests
from bs4 import BeautifulSoup
from keep_alive import keep_alive

client = discord.Client()

def live_score():
  url='https://www.cricbuzz.com/'
  page = requests.get(url)
  soup = BeautifulSoup(page.text,'html.parser')
  team_1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
  team_2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
  team_1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
  team_2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
  # print team names and scores
  s=team_1+" : "+team_1_score+"\n"+team_2+" : "+team_2_score+"\n"+"*This command might not work properly, when there are no ongoing matches.*"
  return(s)


def recent_score():
  results=requests.get("https://www.cricbuzz.com/cricket-match/live-scores/recent-matches")
  src=results.content
  soup=BeautifulSoup(src,'html.parser')
  score=soup.find("div",class_='cb-scr-wll-chvrn cb-lv-scrs-col')
  s2="Recent Match:\n"
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

  if message.content.startswith('!recent'):
    s1=recent_score()
    await message.channel.send(s1)
  
  if message.content.startswith('!live'):
    s=live_score()
    await message.channel.send(s)
  
 
my_secret = os.environ['TOKEN']   

keep_alive()
client.run(my_secret)


