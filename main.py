import os
import discord
from discord import app_commands

class PiyushDeveloperBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced!")

bot = PiyushDeveloperBot()

@bot.event
async def on_ready():
    print(f"🟢 {bot.user} is online!")

@bot.tree.command(
    name="hello",
    description="Check whether Piyush Developer Bot is online"
)
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🤖 Hello Piyush!\n"
        "Piyush Developer Bot is online 🟢"
    )

token = os.getenv("DISCORD_TOKEN")

if not token:
    raise RuntimeError("DISCORD_TOKEN is missing")

bot.run(token)