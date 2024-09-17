
import os
import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX", "!")

# Set up the bot
bot = commands.Bot(command_prefix=PREFIX)

# YouTube stats function
def get_youtube_stats(channel_id):
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        stats = data["items"][0]["statistics"]
        return stats
    else:
        return None

# Twitch stats function
def get_twitch_stats(user_login):
    url = f"https://api.twitch.tv/helix/users?login={user_login}"
    headers = {
        'Client-ID': TWITCH_CLIENT_ID,
        'Authorization': f'Bearer {get_twitch_oauth_token()}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"][0]
    else:
        return None

# Get Twitch OAuth token
def get_twitch_oauth_token():
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": TWITCH_CLIENT_ID,
        "client_secret": TWITCH_CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, params=params)
    return response.json()["access_token"]

# Twitter stats function
def get_twitter_stats(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["data"]
    else:
        return None

@bot.event
async def on_ready():
    print(f"Logged in as {{bot.user}}")

@bot.command(name='ytstats', help="Get YouTube channel statistics.")
async def youtube_stats(ctx, channel_id):
    stats = get_youtube_stats(channel_id)
    if stats:
        await ctx.send(f"YouTube Channel Stats: 
Subscribers: {stats['subscriberCount']}, Views: {stats['viewCount']}")
    else:
        await ctx.send("Could not retrieve YouTube stats.")

@bot.command(name='twitchstats', help="Get Twitch user statistics.")
async def twitch_stats(ctx, user_login):
    stats = get_twitch_stats(user_login)
    if stats:
        await ctx.send(f"Twitch User Stats: 
Followers: {stats['view_count']}")
    else:
        await ctx.send("Could not retrieve Twitch stats.")

@bot.command(name='twstats', help="Get Twitter user statistics.")
async def twitter_stats(ctx, username):
    stats = get_twitter_stats(username)
    if stats:
        await ctx.send(f"Twitter User Stats: 
Username: {stats['name']}, Followers: {stats['public_metrics']['followers_count']}")
    else:
        await ctx.send("Could not retrieve Twitter stats.")

bot.run(TOKEN)
