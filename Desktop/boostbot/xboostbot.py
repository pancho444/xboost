import asyncio, discord, json, requests, os, httpx, base64, time, subprocess, fade, colorama, string, http, sys, threading
from discord.ext import commands
from threading import Thread
from email.mime import application
from http import client
from colorama import Fore
import os.path
import platform
import random
import hashlib
from time import sleep
from datetime import datetime
sys.path.insert(0, sys.path[0]+'\\modules')
# from keyauth import api


bot = commands.Bot(intents=discord.Intents.all(), command_prefix='.')
settings = json.load(open("config.json", encoding="utf-8"))

emoji = ""


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Discord.gg/xboost"))
    def logo():
        colorama.deinit()
    print(sex)
    for char in cum:
        time.sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()
boostgem = ""
sex=fade.purpleblue("""
    __    __   ____                  _     ____        _   
    \ \  / /  |  _ \                | |   |  _ \      | |  
     \ \/ /   | |_) | ___   ___  ___| |_  | |_) | ___ | |_      ━━━━━━━━━━━━━━━━━━━━━━━━
     | _ |    |  _ < / _ \ / _ \/ __| __| |  _ < / _ \| __|        discord.gg/xboost
    / / \ \   | |_) | (_) | (_) \__ \  |  | |_) | (_) | |_      ━━━━━━━━━━━━━━━━━━━━━━━━
   |_/   \_|  |____/ \___/ \___/|___/\__| |____/ \___/ \__|

""")

cum=fade.pinkred(f"""
                [-] Bot Status {Fore.GREEN} [Online]
                [-] All Services up
                [-] Stocks Loaded
""")

def is_licensed(target):
    try:
        open(f"Stocks/{target}.txt", "r")
        return True
    except FileNotFoundError:
        return False


def Owner(ctx):
    return str(ctx.author.id) in settings["owner"]


def isAdmin(ctx):
    return str(ctx.author.id) in settings["bot_admin"]


def iswhitelisted(ctx):
    return str(ctx.author.id) in settings["whitelisted"]

def removeToken(user, token: str):
    with open(f'Stocks/{user}.txt', "r") as f:
        Tokens = f.read().split("\n")
        for t in Tokens:
            if len(t) < 5 or t == token:
                Tokens.remove(t)
        open(f'Stocks/{user}.txt', "w").write("\n".join(Tokens))


def runBoostshit(user, invite: str, amount: int):  #, expires: bool
    if amount % 2 != 0:
        amount += 1

    tokens = get_all_tokens(f'Stocks/{user}.txt')
    all_data = []
    tokens_checked = 0
    actually_valid = 0
    boosts_done = 0
    for token in tokens:
        s, headers = get_headers(token)
        profile = validate_token(s, headers)
        tokens_checked += 1

        if profile != False:
            actually_valid += 1
            data_piece = [s, token, headers, profile]
            all_data.append(data_piece)
            print(fade.pinkred(f"[-] {profile}"))
        else:
            pass
    for data in all_data:
        if boosts_done >= amount:
            return
        s, token, headers, profile = get_items(data)
        boost_data = s.get(f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots", headers=headers)
        if boost_data.status_code == 200:
            if len(boost_data.json()) != 0:
                join_outcome, server_id = do_join_server(s, token, headers, profile, invite)
                if join_outcome:
                    for boost in boost_data.json():

                        if boosts_done >= amount:
                            removeToken(user, token)
                        boost_id = boost["id"]
                        bosted = do_boost(s, token, headers, profile, server_id, boost_id)
                        if bosted:
                            print(fade.pinkred(f"[+] {profile} {Fore.GREEN}[SUCCESS] Boosted {Fore.RESET}> discord.gg/{invite}"))
                            boosts_done += 1
                        else:
                            print(fade.pinkred(f"[-] {profile} {Fore.YELLOW}[INFO] {Fore.RESET} Boost already used - {invite}"))
                    removeToken(user, token)
                else:
                    print(fade.pinkred(f"{Fore.RED} [-] {profile} {Fore.RED}[ERROR] Couldnt Join - {invite}"))

            else:
                removeToken(user, token)
                print(fade.pinkred(f"[-] {profile} {Fore.RED}[ERROR] Kein Nitro?"))


def getRandomString(length):
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return "".join(random.choice(pool) for i in range(length))


@bot.command(name="payments", description="Zeigt alle Bezahlungsmethoden an")
async def payments(ctx):
    embed = discord.Embed(title='Bezahlungsarten',       description="**Alle unten aufgeführten Zahlungsmethoden**",       color=0x7532f0)
    embed.add_field(name="**<:Paypal:1010907418911314002> Paypal**",
        value="``panchoh895@gmail.com`` **⚠️ Solo F&F, o no recibirás tu pedido ⚠️**",
        inline=False)
   
    await ctx.reply(embed=embed, mention_author=True)


@bot.slash_command(name="methods", description="Muestra todos los métodos de pago")
async def payments(ctx: discord.ApplicationContext):
    embed = discord.Embed(title='Métodos de pago',       description="**Todos los métodos de pago enumerados a continuación**",       color=0x7532f0)
    embed.add_field(name="**Paypal**",
        value=
		f"``panchoh895@gmail.com``**⚠️ Solo F&F, o no recibirás tu pedido ⚠️**",
        inline=False)
  

    return await ctx.respond(embed=embed)


gift = "https://discord.gift/"


@bot.slash_command(name="nitrogen", description="bruteforces nitros 💀")
async def nitrogen(ctx, amount: discord.Option(int, "amount") = 10):
    if amount > 10000:
        embed = discord.Embed(description="**⚠️ Solo puedes generar un máximo de 10.000 ⚠️**", color=0x7532f0)
        return await ctx.respond(embed=embed)
    num = int(amount)
    with open(f'Data/{amount}.txt', 'w+') as f:
        for x in range(num):
            char = getRandomString(16)
            f.write(f"{gift}{char}\n")

    await ctx.respond(file=discord.File(f'Data/{amount}.txt'))
    os.remove(f'Data/{amount}.txt')
    print(f"\n\n   [-] {amount} Nitros gened gen used by {ctx.author.name}")


@bot.command(name="nitrogen", description="unchecked nitros 💀")
async def nitrogen(ctx, amount=10):
    if amount > 10000:
        embed = discord.Embed(description="**⚠️ Solo puedes generar un máximo de 10.000⚠️**",           color=0x7532f0)
        return await ctx.reply(embed=embed, mention_author=True)
    num = int(amount)
    with open(f'Data/{amount}.txt', 'w+') as f:
        for x in range(num):
            char = getRandomString(16)
            f.write(f"{gift}{char}\n")

    await ctx.reply(file=discord.File(f'Data/{amount}.txt'), mention_author=True)
    os.remove(f'Data/{amount}.txt')
    print(f"\n\n   [-] {amount} Nitros gened gen used by {ctx.author.name}")


@bot.command(name="clear", description="Elimina su Boost Stock")
async def clear(ctx):
    if not is_licensed(ctx.author.id):
        return await ctx.reply("**⚠️ Solo los compradores pueden eliminar su propio stock.**",            mention_author=True)
    embed = discord.Embed(description=
        f"<:boost:1000475220504760330> **Exitosamente despejado {len(open(f'Stocks/{ctx.author.id}.txt', encoding='utf-8').read().splitlines())} nitro tokens ({len(open(f'Stocks/{ctx.author.id}.txt', encoding='utf-8').read().splitlines()) * 2}) Boosts from the stock**",
        color=0x7532f0)
    await ctx.reply(embed=embed, mention_author=True)
    f = open(f'Stocks/{ctx.author.id}.txt', 'r+')
    f.truncate(0)


@bot.slash_command(name="clear", description="Elimina su Boost Stock")
async def clear(ctx: discord.ApplicationContext):
    if not is_licensed(ctx.author.id):
        return await ctx.respond("**⚠️ Nur Käufer können ihren eigenen Stock löschen**"
                                 )
    embed = discord.Embed(description=
        f"<:boost:1000475220504760330> **Exitosamente despejado {len(open(f'Stocks/{ctx.author.id}.txt', encoding='utf-8').read().splitlines())} nitro tokens ({len(open(f'Stocks/{ctx.author.id}.txt', encoding='utf-8').read().splitlines()) * 2}) Boosts from the stock**",
        color=0x7532f0)
    await ctx.respond(embed=embed)
    f = open(f'Stocks/{ctx.author.id}.txt', 'r+')
    f.truncate(0)


@bot.command(name="stock", description="Muestra el stock del propietario del servidor si el usuario no tiene licencia, pero si el usuario tiene licencia, se mostrará su propio stock, o puede verificar el stock de otra persona\nSi el objetivo no tiene licencia, no hará nada")
async def stock(ctx: discord.ApplicationContext, userID=None):
    if not is_licensed(ctx.author.id):
        embed = discord.Embed(title=f"**{emoji} Shop Stock**",
        description=
        f"**{emoji} .gg/xboost Stock is Shown Below. \n{emoji} Shop Currently Has {len(open(f'Stocks/{534446328302927882}.txt', encoding='utf-8').read().splitlines())} Nitro Tokens ({len(open(f'Stocks/{534446328302927882}.txt', encoding='utf-8').read().splitlines()) * 2}) Boosts Left**",
        color=0x7532f0).set_image(url="https://cdn.discordapp.com/attachments/935427336327790632/1016955238072205363/xboost.gif").set_footer(text="discord.gg/xboost")
        return await ctx.reply(embed=embed, mention_author=True)
    if userID == None:
        embed = discord.Embed(title=f"**{boostgem} Your Stock**",
            description=
            f"**{boostgem} Stock is Shown Below. \n{boostgem} Your Stock Currently Has {len(open(f'Stocks/{ctx.author.id}.txt', encoding='utf-8').read().splitlines())} Nitro Tokens ({len(open(f'Stocks/{ctx.author.id}.txt', encoding='utf-8').read().splitlines()) * 2}) Boosts Left**",
            color=0x7532f0
        ).set_image(    url=
            "https://cdn.discordapp.com/attachments/935427336327790632/1016955238072205363/xboost.gif"
        ).set_footer(text="discord.gg/xboost")
        return await ctx.reply(embed=embed)

    embed = discord.Embed(title=f"**{boostgem} Stock**",
        description=
        f"**{boostgem} El stock del usuario se muestra a continuación. \n{boostgem} <@{userID}> tiene actualmente {len(open(f'Stocks/{userID}.txt', encoding='utf-8').read().splitlines())} Nitro Tokens ({len(open(f'Stocks/{userID}.txt', encoding='utf-8').read().splitlines()) * 2}) Boosts**",
        color=0x7532f0).set_image(url="https://cdn.discordapp.com/attachments/935427336327790632/1016955238072205363/xboost.gif").set_footer(text="discord.gg/xboost")

    await ctx.reply(embed=embed, mention_author=True)

@bot.slash_command(name="stock",
                   description="Le permite ver su propio stock actual.")
async def stock(ctx: discord.ApplicationContext):
    if not is_licensed(ctx.author.id):
        embed = discord.Embed(title=f"**{emoji} XBoost Stock**",
        description=
        f"**{emoji} .gg/xboost Stock se muestra a continuación. \n{emoji} La tienda actualmente tiene {len(open(f'Stocks/{995730637627596891}.txt', encoding='utf-8').read().splitlines())} Nitro Tokens ({len(open(f'Stocks/{995730637627596891}.txt', encoding='utf-8').read().splitlines()) * 2}) Boosts**",
        color=0x7532f0).set_image(url="https://media.discordapp.net/attachments/999633042513592352/999995247817928765/standard_2.gif").set_footer(text="discord.gg/xboost")
        return await ctx.reply(embed=embed, mention_author=True)

    embed = discord.Embed(title=f"**{boostgem} XBoost Stock**",
        description=
        f"**{boostgem} El inventario se muestra a continuación. \n{boostgem} Usted actualmente tiene {len(open(f'Stocks/{ctx.author.id}.txt', encoding='utf-8').read().splitlines())} Nitro Tokens ({len(open(f'Stocks/{ctx.author.id}.txt', encoding='utf-8').read().splitlines()) * 2}) Boosts**",
        color=0x7532f0).set_image(url="https://cdn.discordapp.com/attachments/935427336327790632/1016955238072205363/xboost.gif").set_footer(text="discord.gg/xboost")

    await ctx.respond(embed=embed)


@bot.command(name="restock", description="Restock mit pastebin (RAW ONLY)")
async def restock(ctx: discord.ApplicationContext, pastebin):
    if not is_licensed(ctx.author.id):
        embed = discord.Embed(    description="**⚠️ Solo los clientes pueden recargar su stock ⚠️**",
            color=0x7532f0)
        return await ctx.reply(embed=embed, mention_author=True)
    emoji = ""
    tokens = httpx.get(pastebin).text.splitlines()
    embed = discord.Embed(title=f"**{emoji} Success {emoji}**",
        description=
        f"** Successfully Added {str(len(tokens))} nitro tokens ({str(len(tokens)*2)}) boosts in stock**",
        color=0x7532f0).set_footer(text="discord.gg/xboost").set_image(url="https://media.discordapp.net/attachments/999633042513592352/1000708072982982686/standard_3.gif")
    with open(f"Stocks/{ctx.author.id}.txt", "a", encoding="utf-8") as file:
        for token in tokens:
            file.write(f"{token}\n")

    return await ctx.reply(embed=embed, mention_author=True)


@bot.slash_command(name="restock", description="Permite la recarga de Nitro Tokens.")
async def restock(ctx: discord.ApplicationContext,
                  pastebin: discord.Option(str,                        "pastebin_url (RAW)",                        required=True)):
    if not is_licensed(ctx.author.id):
        embed = discord.Embed(description="**⚠️ Solo los clientes pueden recargar su stock ⚠️**",
            color=0x7532f0)
        return await ctx.respond(embed=embed)
    emoji = ""
    tokens = httpx.get(pastebin).text.splitlines()
    embed = discord.Embed(title=f"**{emoji} Exitoso {emoji}**", description=f"** Agregado exitosamente {str(len(tokens))} nitro tokens ({str(len(tokens)*2)}) boosts in stock**", color=0x7532f0).set_footer(text="discord.gg/xboost").set_image(url="https://media.discordapp.net/attachments/999633042513592352/1000708072982982686/standard_3.gif")
    with open(f"Stocks/{ctx.author.id}.txt", "a", encoding="utf-8") as file:
        for token in tokens:
            file.write(f"{token}\n")

    return await ctx.respond(embed=embed)

@bot.slash_command(name="admin", description="Agrega un administrador al bot (solo unos pocos cmds más que puede usar))")
async def admin(ctx: discord.ApplicationContext, user: discord.Option(discord.Member, "user", required=True)):
    if not isAdmin(ctx):
        return await ctx.respond("*Solo los administradores de bots pueden usar este comando.*")

    settings["bot_admin"].append(str(user.id))
    json.dump(settings, open("config.json", "w", encoding="utf-8"), indent=4)

    return await ctx.respond(f"{user.mention} has been added to admin.")

@bot.command(name="admin", description="Agrega un administrador al bot (solo unos pocos cmds más que puede usar))")
async def admin(ctx: discord.ApplicationContext, user):
    if not isAdmin(ctx):
        return await ctx.reply("*❌ Solo los administradores de bots pueden usar este comando.*")

    settings["bot_admin"].append(str(user.id))
    json.dump(settings, open("config.json", "w", encoding="utf-8"), indent=4)

    return await ctx.reply(f"{user.mention} has been added to admin.")


@bot.slash_command(name="license",
                   description="Agrega una licencia a un ID de usuario especificado.")
async def add_license(ctx: discord.ApplicationContext, userid: discord.Option(str, "Target ID.", required=True)):
    if not isAdmin(ctx):
        return await ctx.respond("*⚠️ Solo los propietarios/administradores pueden usar este comando*")
    if isAdmin(ctx):
        if not is_licensed(userid):
            open(f"Stocks/{userid}.txt", "w")
            embed = discord.Embed(description=f"✅ User <@!{userid}> fue autorizado.", color=0x7532f0)
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(description=f"⚠️ *User <@!{userid}> ya tiene licencia*", color=0x7532f0)
            await ctx.respond(embed=embed)


@bot.command(name="license",    
             description="Agrega una licencia a un ID de usuario especificado")
async def add_license(ctx: discord.ApplicationContext, userid=None):
    if not isAdmin(ctx):
        await ctx.reply("*⚠️ Nur Eigentümer/Administratoren können diesen Befehl verwenden*")
    if isAdmin(ctx):
        if not is_licensed(userid):
            open(f"Stocks/{userid}.txt", "w")
            embed = discord.Embed(        description=f"✅ User <@!{userid}> fue autorizado.",
                color=0x7532f0)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(        description=f"⚠️ *User <@!{userid}> ya tiene licencia*",
                color=0x7532f0)
            await ctx.send(embed=embed)


@bot.slash_command(name="unlicense",
    description="Elimina una licencia/acceso de un usuario específico.")
async def unlicense(ctx: discord.ApplicationContext, targetid: discord.Option(str, "User ID.",                          required=True)):
    if isAdmin(ctx):
        if is_licensed(ctx.author.id):
            os.remove(f"Stocks/{targetid}.txt")
            embed = discord.Embed(        description=f"✅ *User <@!{targetid}> Se ha eliminado la licencia*",
                color=0x7532f0)
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(        description=f"*⚠️ User <@!{targetid}> no tiene licencia*",
                color=0x7532f0)
            await ctx.respond(embed=embed)


@bot.command(name="unlicense",
             description="Elimina una licencia/acceso de un usuario específico.")
async def unlicense(ctx, targetid=None):
    if isAdmin(ctx):
        if targetid == None:
            await ctx.reply("*⚠️ Benutzer-ID nicht angegeben*")
        if is_licensed(ctx.author.id):
            os.remove(f"Stocks/{targetid}.txt")
            embed = discord.Embed(        description=f"✅ *User <@!{targetid}> Se ha eliminado la licencia",
                color=0x7532f0)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(    description=f"*⚠️ User <@!{targetid}> no tiene licencia*",
            color=0x7532f0)
        await ctx.send(embed=embed)


@bot.slash_command(name="activity", description="cambia el nombre de la actividad del bot")
async def activity(ctx,
                   activity: discord.Option(str,                         "cambia el nombre de la actividad del bot",                         required=True)):
    if not Owner(ctx):
        embed = discord.Embed(    description="*⚠️ Solo los propietarios de bots pueden usar este comando*",
            color=0x7532f0)
        return await ctx.respond(embed=embed)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{activity}"))
    embed = discord.Embed(description=f"*✅ Bot activity changed to *``{activity}``",
        color=0x7532f0)
    await ctx.respond(embed=embed)


@bot.command(name="activity", description="cambia el nombre de la actividad del bot")
async def activity(ctx, activity):
    if not Owner(ctx):
        embed = discord.Embed(    description="*⚠️ Solo los propietarios de bots pueden usar este comando*",
            color=0x7532f0)
        return await ctx.reply(embed=embed)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"{activity}"))
    embed = discord.Embed(description=f"*✅ Bot activity changed to*   ``{activity}``",
        color=0x7532f0)
    await ctx.reply(embed=embed)


@bot.slash_command(name="sendtokens")
async def give_tokens(ctx: discord.ApplicationContext, amount: discord.Option(int, "Menge an Tokens.", required=True),
                      user: discord.Option(str, "User ID.", required=True)):
    if is_licensed(ctx.author.id):

        temp_tokens = open(f"Stocks/{ctx.author.id}.txt", encoding="UTF-8").read().splitlines()
        if len(temp_tokens) < amount:
            return await ctx.send("No tienes suficientes tokens en stock.")

        tokens_to_give = temp_tokens[0:amount]
        temp_tokens = temp_tokens[amount:]

        f = open(f"Stocks/temp.txt", "w", encoding="UTF-8")
        for tk in tokens_to_give:
            f.write(tk + "\n")
        f.close()

        f = open(f"Stocks/{ctx.author.id}.txt", "w", encoding="UTF-8")
        for tk in temp_tokens:
            f.write(tk + "\n")
        f.close()

        embed = discord.Embed(title=f"Nitro Tokens",
                              description=f"Sent {amount} tokens to user <@{user}>.",
                              color=0x7532f0)
        await ctx.send(embed=embed, file=discord.File("Stocks/temp.txt"))
        os.remove("Stocks/temp.txt")
    else:
        await ctx.send(f"You do not have an active subscription for the bot.")

@bot.slash_command(name="givetokens",
    description="⚠️ Da X cantidad de tokens a un usuario dado")
async def give_tokens(ctx: discord.ApplicationContext,   amount: discord.Option(int, "Menge an Tokens.",required=True),   targetid: discord.Option(str, "User ID.", required=True)):
    if is_licensed(ctx.author.id):
        temp_tokens = open(f"Stocks/{ctx.author.id}.txt", encoding="UTF-8").read().splitlines()
        if len(temp_tokens) < amount:
            return await ctx.reply("*❌ No tienes suficientes tokens en stock*")
            
        tokens_to_give = temp_tokens[:amount]
        temp_tokens = temp_tokens[amount:]

        f = open(f"Stocks/{targetid}.txt", "w", encoding="UTF-8")
        for tk in tokens_to_give:
            f.write(tk + "\n")
        f.close()

        f = open(f"Stocks/{ctx.author.id}.txt", "w", encoding="UTF-8")
        for tk in temp_tokens:
            f.write(tk + "\n")
        f.close()

        embed = discord.Embed(title=f"Nitro Tokens", description= f"**✅ Sent {amount} nitro tokens ({amount * 2}) boosts to user <@!{targetid}>**", color=0x7532f0)
        await ctx.respond(embed=embed)
    else:
        await ctx.send(f"ℹ️ **You do not have an active subscription for the bot**")


@bot.slash_command(name="boost", description="boost server")
async def boost(ctx: discord.ApplicationContext, invitecode: discord.Option(str, "Discord-Einladungscode, um dem Server beizutreten (NUR CODE).", required=True),
                amount: discord.Option(int,                    "Número de boosts.",                    required=True)):
    if not is_licensed(ctx.author.id):
        embed = discord.Embed(    description="*⚠️ Solo los compradores pueden usar este comando ⚠️*",
            color=0x7532f0)
        return await ctx.respond(embed=embed)
    await ctx.respond(f"{boostgem} Iniciando Boosteo a discord.gg/{invitecode} {amount} Times")

    INVITE = invitecode.replace("//", "")
    if "/invite/" in INVITE:
        INVITE = INVITE.split("/invite/")[1]

    elif "/" in INVITE:
        INVITE = INVITE.split("/")[1]

    dataabotinvite = httpx.get(f"https://discord.com/api/v9/invites/{INVITE}").text

    if '{"message": "Unknown Invite", "code": 10006}' in dataabotinvite:
        print(    fade.pinkred(f"{Fore.RED}https://Discord.gg/{INVITE} is invalid"))
        return await ctx.edit("*Der Einladungslink ist ungültig*")
    else:
        print(    fade.pinkred(        f"https://Discord.gg/{INVITE} Selected, Starting Boosting it"))

    runBoostshit(ctx.author.id, INVITE, amount)
    return await ctx.respond(f"{boostgem} Finished boosting https://discord.gg/{invitecode} {amount} times")


def get_super_properties():
    properties = '''{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-GB","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36","browser_version":"95.0.4638.54","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":102113,"client_event_source":null}'''
    properties = base64.b64encode(properties.encode()).decode()
    return properties


def get_fingerprint(s):
    try:
        fingerprint = s.get(f"https://discord.com/api/v9/experiments",         timeout=5).json()["fingerprint"]
        return fingerprint
    except Exception as e:
        # print(e)
        return "Error"


def get_cookies(s, url):
    try:
        cookieinfo = s.get(url, timeout=5).cookies
        dcf = str(cookieinfo).split('__dcfduid=')[1].split(' ')[0]
        sdc = str(cookieinfo).split('__sdcfduid=')[1].split(' ')[0]
        return dcf, sdc
    except:
        return "", ""


def get_proxy():
    return None  # can change if problems occur


def get_headers(token):
    while True:
        s = httpx.Client(proxies=get_proxy())
        dcf, sdc = get_cookies(s, "https://discord.com/")
        fingerprint = get_fingerprint(s)
        if fingerprint != "Error":  # Making sure i get both headers
            break

    super_properties = get_super_properties()
    headers = {
        'authority': 'discord.com',
        'method': 'POST',
        'path': '/api/v9/users/@me/channels',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US',
        'authorization': token,
        'cookie': f'__dcfduid={dcf}; __sdcfduid={sdc}',
        'origin': 'https://discord.com',
        'sec-ch-ua':
        '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-fingerprint': fingerprint,
        'x-super-properties': super_properties,
    }

    return s, headers


def find_token(token):
    if ':' in token:
        token_chosen = None
        tokensplit = token.split(":")
        for thing in tokensplit:
            if '@' not in thing and '.' in thing and len(            thing
            ) > 30:  # trying to detect where the token is if a user pastes email:pass:token (and we dont know the order)
                token_chosen = thing
                break
        if token_chosen == None:
            print(f"Error finding token", Fore.RED)
            return None
        else:
            return token_chosen

    else:
        return token


def get_all_tokens(filename):
    all_tokens = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            token = line.strip()
            token = find_token(token)
            if token != None:
                all_tokens.append(token)

    return all_tokens


def validate_token(s, headers):
    check = s.get(f"https://discord.com/api/v9/users/@me", headers=headers)

    if check.status_code == 200:
        profile_name = check.json()["username"]
        profile_discrim = check.json()["discriminator"]
        profile_of_user = f"{profile_name}#{profile_discrim}"
        return profile_of_user
    else:
        return False


def do_member_gate(s, token, headers, profile, invite, server_id):
    outcome = False
    try:
        member_gate = s.get(    f"https://discord.com/api/v9/guilds/{server_id}/member-verification?with_guild=false&invite_code={invite}",
            headers=headers)
        if member_gate.status_code != 200:
            return outcome
        accept_rules_data = member_gate.json()
        accept_rules_data["response"] = "true"

        # del headers["content-length"] #= str(len(str(accept_rules_data))) #Had too many problems
        # del headers["content-type"] # = 'application/json'  ^^^^

        accept_member_gate = s.put(    f"https://discord.com/api/v9/guilds/{server_id}/requests/@me",
            headers=headers,
            json=accept_rules_data)
        if accept_member_gate.status_code == 201:
            outcome = True

    except:
        pass

    return outcome


def do_join_server(s, token, headers, profile, invite):
    join_outcome = False
    server_id = None
    try:
        # headers["content-length"] = str(len(str(server_join_data)))
        headers["content-type"] = 'application/json'

        for i in range(15):
            try:
                createTask = httpx.post(            "https://api.capmonster.cloud/createTask", json={
                        "clientKey": settings["capmonsterKey"],     "task": {
                            "type": "HCaptchaTaskProxyless",         "websiteURL": "https://discord.com/channels/@me",         "websiteKey":
                            "4c672d35-0701-42b2-88c3-78380b0db560"
                        }
                    }).json()["taskId"]

                print(fade.pinkred(f"Captcha Task: {createTask}"))

                getResults = {}
                getResults["status"] = "processing"
                while getResults["status"] == "processing":
                    getResults = httpx.post(                "https://api.capmonster.cloud/getTaskResult",     json={
                            "clientKey": settings["capmonsterKey"],         "taskId": createTask
                        }).json()

                    time.sleep(1)

                solution = getResults["solution"]["gRecaptchaResponse"]

                print(fade.pinkred(f"Captcha Solved"))

                join_server = s.post(            f"https://discord.com/api/v9/invites/{invite}", headers=headers, json={"captcha_key": solution})

                break
            except:
                pass

        server_invite = invite
        if join_server.status_code == 200:
            join_outcome = True
            server_name = join_server.json()["guild"]["name"]
            server_id = join_server.json()["guild"]["id"]
            print(        fade.pinkred(            f"[-] {profile} > https://Discord.gg/{server_invite}"))
        else:
            print(join_server.text)
    except:
        pass

    return join_outcome, server_id


def do_boost(s, token, headers, profile, server_id, boost_id):
    boost_data = {"user_premium_guild_subscription_slot_ids": [f"{boost_id}"]}
    headers["content-length"] = str(len(str(boost_data)))
    headers["content-type"] = 'application/json'

    boosted = s.put(f"https://discord.com/api/v9/guilds/{server_id}/premium/subscriptions",
        json=boost_data,
        headers=headers)
    if boosted.status_code == 201:
        return True
    else:
        return False


def get_invite():
    while True:
        print(f"{Fore.CYAN}Server invite?", end="")
        invite = input(" > ").replace("//", "")

        if "/invite/" in invite:
            invite = invite.split("/invite/")[1]

        elif "/" in invite:
            invite = invite.split("/")[1]

        dataabotinvite = httpx.get(    f"https://discord.com/api/v9/invites/{invite}").text

        if '{"message": "Unknown Invite", "code": 10006}' in dataabotinvite:
            print(f"{Fore.RED}discord.gg/{invite} ist ungültig")
        else:
            print(        f"{Fore.GREEN}discord.gg/{invite} ausgewählt und wird geboostet"
            )
            break

    return invite


def get_items(item):
    s = item[0]
    token = item[1]
    headers = item[2]
    profile = item[3]
    return s, token, headers, profile

# print((f"{Fore.LIGHTBLUE_EX}Initializing"))
# def getchecksum():
# 	path = os.path.basename(__file__)
# 	if not os.path.exists(path):
# 		path = path[:-2] + "exe"
# 	md5_hash = hashlib.md5()
# 	a_file = open(path,"rb")
# 	content = a_file.read()
# 	md5_hash.update(content)
# 	digest = md5_hash.hexdigest()
# 	return digest

# keyauthapp = api(
# 	name = "boost bot",
# 	ownerid = "goIzKWsmR6",
# 	secret = "2b4d411892c96858b2cb6dc1c6dd4cff18d312d305fbf548e684c87de5349905",
# 	version = "1.0",
# 	hash_to_check = getchecksum()
# )

# print ("""
# 1.Login
# 2.Register
# 3.Already Regirested
# """)
# ans=input("Select Option: ") 
# if ans=="1": 
# 	user = input('Provide username: ')
# 	password = input('Provide password: ')
# 	keyauthapp.login(user,password)
# elif ans=="2":
# 	user = input('Provide username: ')
# 	password = input('Provide password: ')
# 	license = input('Provide License: ')
# 	keyauthapp.register(user,password,license)
# elif ans=="3":
#     user = settings["username"]
#     password = settings["password"]
#     keyauthapp.login(user,password)
# else:
# 	print("\nNot Valid Option") 
# 	sys.exit(5)

# subs = keyauthapp.user_data.subscriptions ## Get all Subscription names, expiry, and timeleft
# for i in range(len(subs)):
#   sub = subs[i]["subscription"] # Subscription from every Sub
#   expiry = datetime.utcfromtimestamp(int(subs[i]["expiry"])).strftime('%Y-%m-%d %H:%M:%S') ## Expiry date from every Sub


#   print(f"Subscription: {sub} - Expiry: {expiry}")

# sleep(3)
# os.system('cls')
bot.run(settings["bot_token"])