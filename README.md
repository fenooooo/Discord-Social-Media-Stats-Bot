
# Discord Social Media Stats Bot

This bot provides real-time statistics from YouTube, Twitch, and Twitter for specified users or channels. It allows users to retrieve data such as the number of subscribers, followers, and view counts.

## Features

- Retrieves YouTube subscriber and view counts
- Retrieves Twitch follower and view counts
- Retrieves Twitter follower count

## Setup

1. Clone the repository.
2. Install dependencies:

   ```
   pip install discord.py python-dotenv requests
   ```

3. Create a `.env` file and add your API keys and Discord bot token:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   YOUTUBE_API_KEY=your_youtube_api_key
   TWITCH_CLIENT_ID=your_twitch_client_id
   TWITCH_CLIENT_SECRET=your_twitch_client_secret
   TWITTER_BEARER_TOKEN=your_twitter_bearer_token
   ```

4. Run the bot:

   ```
   python bot.py
   ```

## Commands

- `!ytstats <channel_id>`: Fetch YouTube statistics for a given channel.
- `!twitchstats <username>`: Fetch Twitch statistics for a given user.
- `!twstats <username>`: Fetch Twitter statistics for a given user.

## Requirements

- Python 3.6 or higher
- discord.py
- python-dotenv
- requests
