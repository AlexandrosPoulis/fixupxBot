import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import asyncio
import os
import re
import webserver

# to load the key
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding = 'utf-8', mode='w')
intents = discord.Intents.default()
# enable in developer site first and then here
intents.message_content = True
intents.members = True
intents.webhooks = True

bot = commands.Bot(command_prefix="!", intents=intents)


async def get_channel_webhook(channel):
    webhooks = await channel.webhooks()

    if webhooks:
        return webhooks[0]

    # Create webhook if none exists
    return await channel.create_webhook(name="BotWebhook")

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")


@bot.event
async def on_message(message):
    await asyncio.sleep(1)
    if message.author == bot.user:
        return
    
    if ("https://x.com/" in message.content.lower()):# and (message.channel.id == 730425091212705952):
        
        channel = bot.get_channel(message.channel.id)
        webhook = await get_channel_webhook(channel)
        
        await message.delete()
        new_content = message.content.replace(
            "https://x.com/",
            "https://fixupx.com/"
        )

        
        await webhook.send(
        content=new_content,
        username=f"{message.author.display_name} (link fixed)",
        avatar_url=message.author.display_avatar.url
        )

    await bot.process_commands(message)

webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)


