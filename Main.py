import random
import discord
import datetime
from discord.ext import commands, tasks
from itertools import cycle
from keep_alive import keep_alive
import os

client = commands.Bot(command_prefix=".")
status = cycle([".help"])

client.remove_command("help")
foot = "\".help\" para todos los comandos"


# Startup
@client.event
async def on_ready():
    change_status.start()
    print("Bot ready!")


@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name=(next(status))))

# EasterEggs
# joya
@client.command()
async def joya(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        description=member.mention + "** está joya**",
        color=discord.Colour.random(),
    )
    embed.set_image(
        url=
        "https://i.pinimg.com/originals/31/6b/3c/316b3cd3d0c2522a3c9580cc74ba6ea7.jpg"
    )
    embed.set_footer(text=foot)
    await ctx.send(embed=embed)


@joya.error
async def joya_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            f"Necesitas introducir el usuario que está joya {ctx.author.mention}"
        )


# Public
# info
@client.command()
async def info(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f"**{ctx.guild.name}**",
                          description=f"**Bienvenidos al servidor!!!**\n"
                          f"**Miembros:** {ctx.guild.member_count}"
                          f"\n**Servidor creado el: "
                          f"\n**{ctx.guild.created_at}\n",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Colour.green())
    embed.set_footer(text=foot)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)


# random
@client.command()
async def random10(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="**Número al azar del 0 al 10**",
                          description=f"__El bot ha elegido:__"
                          f"\n`{random.randint(0, 11)}`",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Colour.blurple())
    embed.set_thumbnail(url="https://pngimg.com/uploads/dice/dice_PNG49.png")
    embed.set_footer(text=foot)
    await ctx.send(embed=embed)


@client.command()
async def random100(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="**Número al azar del 0 al 100**",
                          description=f"__El bot ha elegido:__"
                          f"\n`{random.randint(0, 101)}`",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Colour.blurple())
    embed.set_thumbnail(url="https://pngimg.com/uploads/dice/dice_PNG49.png")
    embed.set_footer(text=foot)
    await ctx.send(embed=embed)


# help
@client.command()
async def help(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title="**###𝐇𝐄𝐋𝐏###**",
        description=
        "**Comandos**\n.help (Todos los comandos en el servidor)"
        "\n.info (Información del servidor)\n.ppt (Piedra, Papel, Tijeras)"
        "\n.random10 (Número al azar del 0 al 10)\n.random100 (Número al azar del 0 al 100)"
        "\n.repe (El bot repite lo que escribas)\n.didyouknow (Did You Know?)\n.mongollland (Información de MongollLand)",
        timestamp=datetime.datetime.utcnow(),
        color=discord.Colour.dark_blue())
    embed.add_field(
        name="**Info extra**",
        value=">Bot creado por Tupei#0001\n"
        ">Disfrutad el bot!!!\n>Hay comandos secretos escondidos en el bot!\n"
              ">Si quieres una versión mejoradao la versión para moderar de este bot, contacta con Tupei",
        inline=True)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    embed.set_footer(text="Creado por Tupei con amor")
    await ctx.send(embed=embed)


# ppt
@client.command()
async def ppt(ctx, *, args):
    await ctx.channel.purge(limit=1)
    var = ["`Piedra`", "`Papel`", "`Tijeras`"]
    embed = discord.Embed(title="**Piedra, Papel, Tijeras**",
                          description="El bot ha elegido: " +
                          random.choice(var) + "\nTú has elegido: " + "`" +
                          args + "`",
                          color=discord.Colour.blurple(),
                          timestamp=datetime.datetime.utcnow())
    embed.set_author(
        name=f"{ctx.author.name}"
    )
    embed.set_thumbnail(
        url=
        "https://e7.pngegg.com/pngimages/243/115/png-clipart-rock-paper-scissors-scissors-stone.png"
    )
    embed.set_footer(text=foot)
    await ctx.send(embed=embed)


@ppt.error
async def ppt_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: Necesitas introducir un objeto con el que jugar")


# repetidor
@client.command()
async def repe(ctx, *, args):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{ctx.author.mention}: " + args)


@repe.error
async def repe_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":x: Necesitas introducir un mensaje")


# mongollland
@client.command()
async def mongollland(ctx):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f"**Invitación para MongollLand**",
                          description="**Discord**: https://discord.gg/UcW5cc37Ad\n**Página Web**: Próximamente",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Colour.dark_green())
    embed.set_footer(text=foot)
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/762689124855447572/a_6766e912c05dbc60db79e8437727edd5.webp?size=128")
    await ctx.send(embed=embed)


# did you know?
@client.command()
async def didyouknow(ctx):
	await ctx.channel.purge(limit=1)
	embed = discord.Embed(
		title="Did You Know?",
		description="Discord added a cool new way to use bot commands!\n一款默认表情符号。您可以在 Discord 的任意地方使用它",
		timestamp=datetime.datetime.utcnow(),
		color=discord.Colour.light_grey()
	)
	embed.set_footer(text=foot)
	await ctx.send(embed=embed)

# Music
# join
# leave
# play
# next
# stop
# resume
# BackUp
keep_alive()
client.run(os.getenv('TOKEN'))
