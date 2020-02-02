import discord
import random
import datetime

class MyClient(discord.Client):
    #Einlogen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beed bop")
        self.vorzeichen = "$"

    #Wenn Nachricht geposted wird
    async def on_message(self, message):
        #Wenn die nachricht von dem bot selber ist dann wird es ignoriert
        if message.author != client.user:
            print("Nachricht von " + str(message.author) + " enthält " + str(message.content))
            open("logs/log " + str(datetime.date.today()) + ".txt", "a").write("Nachricht von: " + str(message.author) + ". Enthält: " + str(message.content) + "\n")

        #Sende Nachricht
        if message.author != client.user:
            if message.content.startswith("Hallo bot") or message.content.startswith("hallo bot"):
                #await message.channel.send("Hallo " + str(message.author)[:5])
                await message.author.send("Hallo " + str(message.author).split("#")[0])
            elif message.content.startswith("Nein ich habs zu erst gesagt"):
                await message.author.send("Nope")
            elif message.content.startswith("Doch"):
                await message.author.send("Nope")

        #help
        if message.author != client.user:
            if str(message.content).lower() == self.vorzeichen + "help":
                await message.channel.send("$roulette für roulette parameter: black/red number")

        #roulette
        if message.author != client.user:
            if str(message.content).lower().split()[0] == self.vorzeichen + "roulette":
                try:
                    bid = message.content.split()[1].lower()
                except:
                    await message.channel.send("Es wurden kein parameter angegeben")
                    return
                bid_param = -3
                if bid == "black":
                    bid_param = -1
                elif bid == "red":
                    bid_param = -2
                else:
                    try:
                        if int(bid) < 36 and int(bid) > 0:
                            bid_param = int(bid)
                        else:
                            await message.channel.send("Die angegebene zahl ist zu groß/zu klein")
                            return
                    except:
                        bid_param = -3
                if bid_param == -3:
                    await message.channel.send("Ungültige eingabe")
                    return
                result = random.randint(0, 36)
                if bid_param == -1:
                    won = result%2 == 0 and not result == 0
                elif bid_param == -2:
                    won = result%2 >= 1
                else:
                    won = result == bid_param
                if won:
                    await message.channel.send(self.vorzeichen*3 + " Du hast Gewonnen " + self.vorzeichen*3)
                elif not won:
                    await message.channel.send(self.vorzeichen*3 + " Leider verloren " + self.vorzeichen*3)

try:
    client = MyClient()
    client.run("")
except KeyboardInterrupt:
    print("Exiting ...")
    client.f.close()
    exit()
