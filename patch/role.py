role = discord.utils.get(message.guild.roles, id="<id роли>")
await message.author.add_roles(role)