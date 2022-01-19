# CODE ON REPLIT
# the os module helps us access environment variables
# i.e., our API keys
import os
import discord
import requests
from bs4 import BeautifulSoup # Beautiful Soup is a Python library for pulling data out of HTML and XML files. i.e., WebScraping
from keep_alive import keep_alive

client = discord.Client()

def live_score():
  # This function is used to get the Live Score of the matches
  # The bot gets it's output by WebScraping from 'https://www.cricbuzz.com/'
  url='https://www.cricbuzz.com/'
  page = requests.get(url)
  soup = BeautifulSoup(page.text,'html.parser')
  team_1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
  team_2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
  team_1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
  team_2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
  # to print Team Names and Scores
  s=team_1+" : "+team_1_score+"\n"+team_2+" : "+team_2_score+"\n"+"*This command might not work properly, when there are no ongoing matches.*"
  return(s)


def recent_score():
  # this function is used to get the Scores of Matches which have already completed
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
  # this function is called whenever the bot sees a message in a channel
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


