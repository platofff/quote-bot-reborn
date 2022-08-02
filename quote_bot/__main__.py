import os
from vkbottle import load_blueprints_from_package
from vkbottle.bot import Bot

from . import config
from .database.cache import bp as db_cache_bp

bot = Bot(token=config["quote"]["vk_token"])

for bp in load_blueprints_from_package(os.path.normcase("quote_bot/commands")):
    bp.load(bot)
db_cache_bp.load(bot)

bot.run_forever()
