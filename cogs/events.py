#
# Copyright (C) 2022 lifehackerhansol
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

from utils.utils import simple_embed


class Events(commands.Cog):
    """
    Handles server events
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await member.send(embed=simple_embed("""
                                            You can download the patch for the latest version from <#409838466512191490>.
                                            You can use the `!patchguide` command for a tutorial on patching the ROM hack.
                                            DO NOT share the rom file or download pre-patched rom files, even in DMs! This will be a ban on sight.
                                            """, title="Welcome to the Pokémon Moon Black 2 server!"))


async def setup(bot):
    await bot.add_cog(Events(bot))
