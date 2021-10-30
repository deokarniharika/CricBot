import discord
import os
import requests
from bs4 import BeautifulSoup
from keep_alive import keep_alive

client = discord.Client()

def score_gen():
  page = requests.get(url)
  soup = BeautifulSoup(page.text,'html.parser')
  team_1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
  team_2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
  team_1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
  team_2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
# print team names and scores
  s=team_1+" : "+team_1_score+"\n"+team_2+" : "+team_2_score
  return(s)

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


