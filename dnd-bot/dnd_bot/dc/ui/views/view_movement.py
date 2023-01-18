import nextcord
from nextcord.ui import View

from dnd_bot.dc.ui.message_templates import MessageTemplates
from dnd_bot.logic.game.handler_movement import HandlerMovement


class ViewMovement(View):
    def __init__(self, token):
        super().__init__()
        self.value = None
        self.token = token

    @nextcord.ui.button(label='⬅️', style=nextcord.ButtonStyle.blurple)
    async def move_one_left(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await ViewMovement.move_one_tile('left', interaction.user.id, self.token)
        map_view_message = MessageTemplates.map_view_template(self.token)
        await interaction.response.send_message(map_view_message, view=ViewMovement(self.token))
        return

    @nextcord.ui.button(label='➡️', style=nextcord.ButtonStyle.blurple)
    async def move_one_right(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await ViewMovement.move_one_tile('right', interaction.user.id, self.token)
        return

    @nextcord.ui.button(label='⬆️', style=nextcord.ButtonStyle.blurple)
    async def move_one_up(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await ViewMovement.move_one_tile('up', interaction.user.id, self.token)
        return

    @nextcord.ui.button(label='⬇️', style=nextcord.ButtonStyle.blurple)
    async def move_one_down(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await ViewMovement.move_one_tile('down', interaction.user.id, self.token)
        return

    @staticmethod
    async def move_one_tile(direction, id_user, token):
        status = await HandlerMovement.handle_movement(direction, id_user, token)
