import discord
from discord.ext import commands, tasks
import random
import asyncio
import praw
import os

Reddit = praw.Reddit(client_id = "U98c5LmcHr-Kkjjj3bz4-g",
                     client_secret = "hCDSnjq2OTJLYp23aGdY_YfLiTRKSw",
                     username = "TheHolyTachanka",
                     password = "Vasil@123",
                     user_agent = "StalinBot")


client = commands.Bot(command_prefix='S!')
client.remove_command("help")


@client.command()
async def meme(ctx):
    subreddit = Reddit.subreddit("Communism Memes")
    all_subs = ()

    for submission in reddit.subreddit('communism memes').hot(limit=50):
      all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url
 
    em = discord.embed(title = name)

    em.set_image(url = url)
    await ctx.send()

    


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print (f'(member) has become a communist. ')

@client.event
async def on_member_remove(member):
    print(f'(member) has become a capitalist.')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
@commands.has_permissions(kick_members=True)
async def deport(ctx, member : discord.Member,*, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} was deported out of Soviet Russia')

@client.command()
@commands.has_permissions(ban_members=True)
async def gulag(ctx, member : discord.Member,*, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} was sent to gulag')

@client.command()
async def hi(ctx):
    await ctx.send(f'Hello comrade!')

    



@client.command()
@commands.has_permissions(ban_members=True)
async def ungulag(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'**{user}** was freed from gulag')
            return
        






client.run('ODk3NDk1Njc3NDA2NDQxNTIy.YWWf_A.5T2eMUWwDOCzombEijqjXX7U5ng')

