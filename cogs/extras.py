#
# Copyright 2021 Nintendo Homebrew
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# about command and membercount command from extras.py
#

import discord
from discord.ext import commands


class Extras(commands.Cog):
    """
    Extra things.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def klefki(self, ctx):
        """Information on the bot Klefki"""
        embed = discord.Embed(title="Klefki")
        embed.set_author(name="lifehackerhansol")
        embed.url = "https://github.com/lifehackerhansol/Klefki"
        embed.set_thumbnail(url="https://archives.bulbagarden.net/media/upload/thumb/0/04/707Klefki.png/240px-707Klefki.png")
        embed.description = "ROM hacking Discord server bot"
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    async def membercount(self, ctx):
        """Prints the member count of the server."""
        await ctx.send(f"{ctx.guild.name} has {ctx.guild.member_count:,} members!")


async def setup(bot):
    await bot.add_cog(Extras(bot))
