from vkbottle.bot import Bot, Message
from vkbottle import BaseMiddleware
import helper
from loguru import logger

logger.disable("vkbottle")
bot = Bot(token="vk1.a.ASL_RbsdqEYCsgqFCRruLvgZl8uZX1EPYoSEqDwyxSeqXoP6c5CXlFh7lhoYiwj9Utx0EhowlyQ5RN3Egu15CFFzmCAZih-1u3Qoe2X3EK4O5Bo6eCtV1qDm1e2kdXpw0Rv4eRYD716DiZjk2v9USuA-7u44Jbtt3qeyyHYTlWTKOyjNmrAIVgBIeOqr_oGb")
users = "users.json"

class InfoMiddleware(BaseMiddleware[Message]):
    async def pre(self):
        user = helper.find("id", self.event.from_id, users)
        users_info = await bot.api.users.get(self.event.from_id)
        if not user:
            helper.push(users, {
                "id": self.event.from_id,
                "uid": helper.maxuId(users),
                "nick": users_info[0].first_name,
                "balance": 1000,
                "message": 1
            })
            await self.event.answer
@bot.on.message(text=["проф", "профиль"])
async def handler(ans: Message):
    user = helper.find("id", ans.from_id, users)
    text = f"{user['nick']}, ну ты конечно прокаченый тип:\n"
    text += f"твой ид: {user['uid']}"
    text += f"твой кровный балик: {user['balance']}"
    text += f"скок ты настрочил смск: {user['message']}"
    return text

bot.labeler.message_view.register_middleware(InfoMiddleware)
bot.run_forever()