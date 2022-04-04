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

from discord.ext import commands
from utils.sql import get_guild_config


class XYDMaps(commands.Cog):
    """
    Map commands
    """
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        if not await get_guild_config(ctx.guild.id, "xyd"):
            raise commands.CheckFailure()
        return True

    async def mapembed(self, ctx, location, title=""):
        embed = discord.Embed(title=title)
        embed.set_image(url=f"https://raw.githubusercontent.com/lifehackerhansol/sycamore-assets/master/maps/{location}")
        await ctx.send(embed=embed)

    @commands.command()
    async def kalos(self, ctx):
        """Kalos map"""
        await self.mapembed(ctx, "kalos.png", "Kalos Region Map")

    @commands.command()
    async def r1(self, ctx):
        """Route 1"""
        await self.mapembed(ctx, "r1.png", "Route 1")

    @commands.command()
    async def r2(self, ctx):
        """Route 2"""
        await self.mapembed(ctx, "r2.png", "Route 2")

    @commands.command()
    async def r3(self, ctx):
        """Route 3"""
        await self.mapembed(ctx, "r3.png", "Route 3")

    @commands.command()
    async def r4(self, ctx):
        """Route 4"""
        await self.mapembed(ctx, "r4.png", "Route 4")

    @commands.command()
    async def r5(self, ctx):
        """Route 5"""
        await self.mapembed(ctx, "r5.png", "Route 5")

    @commands.command()
    async def r6(self, ctx):
        """Route 6"""
        await self.mapembed(ctx, "r6.png", "Route 6")

    @commands.command()
    async def r7(self, ctx):
        """Route 7"""
        await self.mapembed(ctx, "r7.png", "Route 7")

    @commands.command()
    async def r8(self, ctx):
        """Route 8"""
        await self.mapembed(ctx, "r8.png", "Route 8")

    @commands.command()
    async def r9(self, ctx):
        """Route 9"""
        await self.mapembed(ctx, "r9.png", "Route 9")

    @commands.command()
    async def r10(self, ctx):
        """Route 10"""
        await self.mapembed(ctx, "r10.png", "Route 10")

    @commands.command()
    async def r11(self, ctx):
        """Route 11"""
        await self.mapembed(ctx, "r11.png", "Route 11")

    @commands.command()
    async def r12(self, ctx):
        """Route 12"""
        await self.mapembed(ctx, "r12.png", "Route 12")

    @commands.command()
    async def r13(self, ctx):
        """Route 13"""
        await self.mapembed(ctx, "r13.png", "Route 13")

    @commands.command()
    async def r14(self, ctx):
        """Route 14"""
        await self.mapembed(ctx, "r14.png", "Route 14")

    @commands.command()
    async def r15(self, ctx):
        """Route 15"""
        await self.mapembed(ctx, "r15.png", "Route 15")

    @commands.command()
    async def r16(self, ctx):
        """Route 16"""
        await self.mapembed(ctx, "r16.png", "Route 16")

    @commands.command()
    async def r17(self, ctx):
        """Route 17"""
        await self.mapembed(ctx, "r17.png", "Route 17")

    @commands.command()
    async def r18(self, ctx):
        """Route 18"""
        await self.mapembed(ctx, "r18.png", "Route 18")

    @commands.command()
    async def r19(self, ctx):
        """Route 19"""
        await self.mapembed(ctx, "r19.png", "Route 19")

    @commands.command()
    async def r20(self, ctx):
        """Route 20"""
        await self.mapembed(ctx, "r20.png", "Route 20")

    @commands.command()
    async def r21(self, ctx):
        """Route 21"""
        await self.mapembed(ctx, "r21.png", "Route 21")

    @commands.command()
    async def r22(self, ctx):
        """Route 22"""
        await self.mapembed(ctx, "r22.png", "Route 22")

    @commands.command()
    async def vaniville(self, ctx):
        """Vaniville Town"""
        await self.mapembed(ctx, "vaniville.png", "Vaniville Town")

    @commands.command()
    async def aquacorde(self, ctx):
        """Aquacorde Town"""
        await self.mapembed(ctx, "aquacorde.png", "Aquacorde Town")

    @commands.command()
    async def santalune(self, ctx):
        """Santalune City"""
        await self.mapembed(ctx, "santalune.png", "Santalune City")

    @commands.command()
    async def lumiosesouth(self, ctx):
        """Lumiose City South"""
        await self.mapembed(ctx, "lumiosesouth.png", "Lumiose City - South Boulevard")

    @commands.command()
    async def lumiosenorth(self, ctx):
        """Lumiose City North"""
        await self.mapembed(ctx, "lumiosenorth.png", "Lumiose City - North Boulevard")

    @commands.command()
    async def camphrier(self, ctx):
        """Camphrier Town"""
        await self.mapembed(ctx, "camphrier.png", "Camphrier Town")

    @commands.command()
    async def cyllage(self, ctx):
        """Cyllage City"""
        await self.mapembed(ctx, "cyllage.png", "Cyllage City")

    @commands.command()
    async def ambrette(self, ctx):
        """Ambrette Town"""
        await self.mapembed(ctx, "ambrette.png", "Ambrette Town")

    async def geosenge(self, ctx):
        """Geosenge Town"""
        await self.mapembed(ctx, "geosenge.png", "Geosenge Town")

    @commands.command()
    async def shalour(self, ctx):
        """Shalour City"""
        await self.mapembed(ctx, "shalour.png", "Shalour City")

    @commands.command()
    async def coumarine(self, ctx):
        """Coumarine City"""
        await self.mapembed(ctx, "coumarine.png", "Coumarine City")

    @commands.command()
    async def laverre(self, ctx):
        """Laverre City"""
        await self.mapembed(ctx, "laverre.png", "Laverre City")

    @commands.command()
    async def dendemille(self, ctx):
        """Dendemille Town"""
        await self.mapembed(ctx, "dendemille.png", "Dendemille Town")

    @commands.command()
    async def anistar(self, ctx):
        """Anistar City"""
        await self.mapembed(ctx, "anistar.png", "Anistar City")

    @commands.command()
    async def couriway(self, ctx):
        """Couriway Town"""
        await self.mapembed(ctx, "couriway.png", "Couriway Town")

    @commands.command()
    async def kiloude(self, ctx):
        """Kiloude City"""
        await self.mapembed(ctx, "kiloude.png", "Kiloude City")


async def setup(bot):
    await bot.add_cog(XYDMaps(bot))
