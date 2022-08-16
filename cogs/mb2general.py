#
# Copyright (C) 2021-present lifehackerhansol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import discord

from inspect import cleandoc
from discord.ext import commands
from utils.sql import get_guild_config


class MB2General(commands.Cog):
    """
    General commands
    """

    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if not await get_guild_config(ctx.guild.id, "mb2"):
            raise commands.CheckFailure()
        return True

    async def simple_embed(self, ctx, text, *, title="", color=discord.Color.default()):
        embed = discord.Embed(title=title, color=color)
        embed.description = cleandoc(text)
        await ctx.send(embed=embed)

    @commands.command(aliases=["info"])
    async def information(self, ctx):
        """Moon Black 2 PokeCommunity post"""
        embed = discord.Embed(title="Pokemon Moon Black 2")
        embed.set_author(name="JrFort & Aster")
        embed.url = "https://www.pokecommunity.com/showthread.php?t=405031"
        embed.set_thumbnail(url="https://www.pokeharbor.com/wp-content/uploads/2021/07/wo44ltN.png")
        embed.description = "Pokemon Black 2 ROM hack"
        await ctx.send(embed=embed)

    @commands.command()
    async def patchguide(self, ctx):
        """How to patch a ROM"""
        await self.simple_embed(ctx, """
                                Here is a guide for how to patch using xDelta for Windows. (Unipatcher for Android uses the same layout)
                                <https://www.romulation.org/tutorials/using-xdelta-to-patch-roms>

                                **If you are using any other device**, use [kotcrab's web patcher](https://kotcrab.github.io/xdelta-wasm/) instead.
                                """, title="ROM hack patching guide")

    @commands.command()
    async def wiki(self, ctx):
        """Moon Black 2 Wiki"""
        await self.simple_embed(ctx, """
                                [Moon Black 2 Wiki](https://pokemon-moon-black-2.fandom.com/wiki/Pokemon_Moon_Black_2_Wiki)
                                """)

    @commands.command()
    async def wildpokemon(self, ctx):
        """Wild Pokemon location documentation"""
        await self.simple_embed(ctx, """
                                [Moon Black 2 Wild Pokemon List](https://cdn.discordapp.com/attachments/436652008196276224/663866369271529472/Moon_Black_2_-_Wild_List.pdf)
                                """)

    @commands.command()
    async def fairy(self, ctx):
        """Fairy type issues"""
        await self.simple_embed(ctx, """
                                The implementation of Fairy-type messed up the arm9, which is causing compatibility and other issues.
                                Currently, Fairy-types are displayed as Normal-types, but still function as a Fairy-type. While technically a bug, this fixed an issue with Summary crashes, so it is left as is.

                                Fairy-types will be completely removed in a future update to fix these problems.
                                """, title="Fairy-type issues")

    @commands.command(aliases=["hof"])
    async def halloffame(self, ctx):
        """Hall of Fame warning"""
        await self.simple_embed(ctx, """
                                A bug in Hall of Fame causes the entire game to crash if you bring any Fairy-type Pokemon. This may result in you ***losing your save file***.
                                It is known that the **Noibat evolution line**, as well as **Marshadow**, also causes this issue. There are other Pokemon as well but this is unconfirmed.

                                It is recommended to completely avoid using Fairy-types when challenging the Elite Four.
                                """, title="Do NOT bring a Pokémon with a primary typing of Fairy to the Hall of Fame.")

    @commands.command()
    async def compatibility(self, ctx):
        """Compatibility list"""
        await self.simple_embed(ctx, """
                                Moon Black 2 is confirmed to work on these platforms:
                                - [DeSmuME (official latest version)](http://desmume.org/download/)
                                - [melonDS (official latest version)](https://melonds.kuribo64.net/downloads.php)
                                - [melonDS Android (official latest beta version)](https://play.google.com/store/apps/details?id=me.magnum.melonds)
                                - [TWiLight Menu++/nds-bootstrap (official latest version)](https://wiki.ds-homebrew.com/twilightmenu/installing.html)
                                - R4i Gold 3DS Plus
                                - SuperCard DSONE SDHC/DSONEi
                                - SuperCard DSTWO Plus

                                Other emulators are not supported at this time. Other flashcarts *might* be supported, you can ping <@387858799198863361> if it does not work.
                                """, title="Which emulator or software works with Moon Black 2?")

    @commands.command()
    async def pokedex(self, ctx):
        """Pokedex entries"""
        await self.simple_embed(ctx, """
                                [Moon Black 2 Pokedex list](https://pastebin.com/TbxtwUYF)
                                """
                                )

    @commands.command()
    async def unovaforms(self, ctx):
        """Unova forms"""
        await self.simple_embed(ctx, """
                                [Moon Black 2 Unova forms](https://pastebin.com/cLQapvGh)
                                """
                                )


async def setup(bot):
    await bot.add_cog(MB2General(bot))
