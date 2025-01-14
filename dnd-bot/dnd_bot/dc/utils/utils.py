from nextcord import User, NotFound

from dnd_bot.dc.ui.messager import Messager


async def get_user_name_by_id(user_id: int) -> str | None:
    bot = Messager.bot

    try:
        user: User = await bot.fetch_user(user_id)
    except NotFound:
        return None

    return user.name
