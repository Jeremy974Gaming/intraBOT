# bot.py
import os
from queue import Empty

import discord
from dotenv import load_dotenv
from discord.ext import commands
from pyparsing import empty

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix="$", activity = discord.Game(name="Better than the Books !"))
#client = discord.Client()

@client.command()
async def examshell(ctx):
    await ctx.send(
        'You are starting examshell.\n'
        'Are you sure you want to start an exam session ?\n'
        'There is no Practice mode available, you\'ll be in real mode for this session.\n'
        ' \n'
        'During this exam you\'ll receive multiple exercises, get as many aswers correct as possible,\n'
        'getting points helps you progress further in your exam, though, don\'t panic if you don\'t \n'
        'have the same exercise as your neighbors, life\'s unfair. Deal with it.\n'
        ' \n'
        'For more information on how to use examshell, please type README, you\'ll be DMed the Instructions manual.\n')

@client.command()
async def start(ctx):
    await ctx.send(
        'Welcome to the exam, please sign-in using your intranet account to proceed to the exam session.\n'
        ' \n'
        'REMINDER There is NO practice mode available, REAL mode only, your grade will be counted on the intranet.\n'
        'By the grace of REZNET, may your exam be good and DON\'T PANIC.\n'
        ' \n'
        'Normally, exams should be silent, though, as we don\'t have any physical campuses... Listening to music is OK.\n'
    )

@client.command()
async def grademe(ctx):
    await ctx.send(
        'Are you SURE you really FINISHED your exercise and that it\'s PUSHED ?'
    )

@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title = name + "Server Info",
        description = description,
        color = discord.Color.default()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

@client.command()
async def userinfo(ctx, *, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    name = str(ctx.guild.name)
    id = str(member.id)
    nickname = str(member.display_name)
    discriminator = str(member.discriminator)
    icon = str(ctx.guild.icon_url)
    ucreation = str(member.created_at)
    ujoined = str(member.joined_at)

    embed = discord.Embed(
        title = name + " | User Info",
        color = discord.Color.dark_red(),
    )
    
    embed.set_thumbnail(url=icon)
    embed.set_author(name=str(member), icon_url=member.default_avatar_url)
    embed.add_field(name="Display Name", value=nickname, inline=True)
    embed.add_field(name="User Discrim.", value=discriminator, inline=True)
    embed.add_field(name="User ID", value=id, inline=True)
    embed.add_field(name="Created on", value=ucreation, inline=True)
    embed.add_field(name="Joined on", value=ujoined, inline=True)

    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send('Response Time : {0}ms'.format(round(client.latency, 1)))

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

@client.command()
async def helpme(ctx):
    name = str("Help Dialog")
    description = str("Do you need help ? Then you're at the right place !")
    examsh = "Students and Deep Divers",
    kickuser = "Used to kick members.",
    banuser = "Used to ban members.",
    muteuser = "Used to mute members.",
    userinfo = "Get Somebody\'s info.",
    pinginf = "Get the bot\'s response time.",
    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title = name + " - Get Help here !",
        description = description,
        color = discord.Color.green(),
    )

    embed.set_thumbnail(url=icon)
    embed.add_field(name="examshell", value=examsh, inline=True)
    embed.add_field(name="kick", value=kickuser, inline=True)
    embed.add_field(name="ban", value=banuser, inline=True)
    embed.add_field(name="mute", value=muteuser, inline=True)
    embed.add_field(name="userinfo", value=userinfo, inline=True)
    embed.add_field(name="ping", value=pinginf, inline=True)

    await ctx.send(embed=embed)

@client.command()
async def repeat(ctx, *args):
    for arg in args:
        await ctx.send(arg)

@client.event()
async def on_message_delete(message):

    deleted = discord.Embed(
        description=f"Message deleted in {message.channel.mention}", color=0x4040EC
    ).set_author(name=message.author, url=empty, icon_url=message.author.avatar_url)

    deleted.add_field(name="Message", value=message.content)
    deleted.timestamp = message.created_at
    await channel.send(embed=deleted)

@client.event()
async def on_channel_create(channel):
    channel=client.get_channel(559373100978929684)
    created = discord.Embed(
        description=f"Channel created ! {channel.mention}", color=0x256340
    ).set_author(name=message.author, url=empty, icon_url=message.author.avatar_url)

    created.add_field(name="Channel", value=channel.name)
    created.timestamp = channel.created_at
    await channel.send(embed=created)

@client.event()
async def on_role_create(role):
    
    created = discord.Embed(
        description=f"Role created : {role.mention}", color = 0x422100
    ).set_author(name=message.author, url=empty, icon_url=message.author.avatar_url)

    created.add_field(name="Role", value=role.name)
    created.timestamp = role.created_at
    await channel.send(embed=created)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord !')

@client.event
async def on_member_join(member, guild):
    await guild.name(guild)
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to {guild.name} !'
    )

client.run(TOKEN)