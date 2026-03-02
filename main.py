import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import re

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

secret_role = "Gamer"
WEBHOOK_URL_BALLLAIR = "https://discord.com/api/webhooks/1478155291148292329/qxZsCT-PqiHthzQ2xO4ODtahmvv194QVn36zmRF4JfuBlLk3qFZs2BfE5EYHtlbyMCN6"
WEBHOOK_URL_GCN_memes = "https://discord.com/api/webhooks/1478156710245040312/-QVDXUmAUvF2Hp4j59ynwqO6rOlwxd_JpPzf2D30Q8wsTbYFhJeBMM9Vu-r2ce-5YBkf"
WEBHOOK_URL_GCN_gachaning = "https://discord.com/api/webhooks/1478166149425533103/19A7Z-u7Exgn2oOurxSers_3VGmE5G_w20z-QIyBH2LVYgHGEpo1x7vx6-_saLAHNnKn"
WEBHOOK_URL_GCN_armychannel = "https://discord.com/api/webhooks/1478166809638207509/RtDKq1WgvBEGH2pp585pmDzxaE71ld-175-CHjA3D5mtznGh84m5E0KvI0M9Zo4YWPzU"
WEBHOOK_URL_GCN_raidinfo = "https://discord.com/api/webhooks/1478166942836592861/bqhX7E4NflXb0hJ4cADRWwu4Jprx8HXLNmyblQC9aO3-5cqyI-hpNxLbkIGvDf1zqNOE"
WEBHOOK_URL_dripper = "https://discord.com/api/webhooks/1478167205165138035/NGQIowFwwVCVBVwopjxTtAJ0cIRlxlsDdTZ4UdH-e4SkYQv2r6WVEF8ylSXcXSZyGA0L"
WEBHOOK_URL_gamer = "https://discord.com/api/webhooks/1478167391056822273/TfiNUT94ISmPl_O3ut7-zPVZzNJL90Pev5z5XMbA35zUb_kWc3L7-qT_WC6KZWdtP7tO"

async def get_channel_webhook(channel):
    webhooks = await channel.webhooks()

    if webhooks:
        return webhooks[0]

    # Create webhook if none exists
    return await channel.create_webhook(name="BotWebhook")

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")
    #bot.webhook = discord.Webhook.from_url(
    #    WEBHOOK_URL_BALLLAIR,
    #    session=bot.http._HTTPClient__session
    #)
    #print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if ("https://x.com/" in message.content.lower()):# and (message.channel.id == 730425091212705952):
        
        """ Temporarily keeing them just in case
        if message.channel.id == 730425091212705952:
            bot.webhook = discord.Webhook.from_url(
                WEBHOOK_URL_GCN_memes,
                session=bot.http._HTTPClient__session
            )
            print(f"Logged in as {bot.user}")
        if message.channel.id == 1428088708934008945:
            bot.webhook = discord.Webhook.from_url(
                WEBHOOK_URL_GCN_gachaning,
                session=bot.http._HTTPClient__session
            )
            print(f"Logged in as {bot.user}")
        if message.channel.id == 689197397045149749:
            bot.webhook = discord.Webhook.from_url(
                WEBHOOK_URL_GCN_armychannel,
                session=bot.http._HTTPClient__session
            )
            print(f"Logged in as {bot.user}")
        if message.channel.id == 1046107492154884136:
            bot.webhook = discord.Webhook.from_url(
                WEBHOOK_URL_GCN_raidinfo,
                session=bot.http._HTTPClient__session
            )
            print(f"Logged in as {bot.user}")
        if message.channel.id == 1236908537825984513:
            bot.webhook = discord.Webhook.from_url(
                WEBHOOK_URL_dripper,
                session=bot.http._HTTPClient__session
            )
            print(f"Logged in as {bot.user}")
        if message.channel.id == 1447659465670267002:
            bot.webhook = discord.Webhook.from_url(
                WEBHOOK_URL_gamer,
                session=bot.http._HTTPClient__session
            )
            print(f"Logged in as {bot.user}")
        """
        
        channel = bot.get_channel(message.channel.id)
        webhook = await get_channel_webhook(channel)

        #await webhook.send("Hello world!")
        
        await message.delete()
        new_content = message.content.replace(
            "https://x.com/",
            "https://fixupx.com/"
        )

        #webhook = await message.channel.create_webhook(name="TempWebhook")
        
        await webhook.send(
        content=new_content,
        username=f"{message.author.display_name} (link fixed)",
        avatar_url=message.author.display_avatar.url
        )

    await bot.process_commands(message)
    #https://x.com/DOAAOQ/status/2027488828731101500?s=20
    
bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "kekw" in message.content():
        await message.delete()
        await message.channel.send(f"{message.author.mention}")

@bot.command()
async def fake(ctx, name, *, text):
    webhook = await ctx.channel.create_webhook(name="TempWebhook")
    
    await webhook.send(
        content=text,
        username=name
    )
    
    await webhook.delete()

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned to {role}")
    else:
        await ctx.send("Role doesn't exist")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has had the {role} role removed")
    else:
        await ctx.send("Role doesn't exist")

@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send("welcome to the club!")

@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have permission to do that!")


@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"You said {msg}")

@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to your message")


@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="New Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)