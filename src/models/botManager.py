from models.kokoro import Kkr
from models.bot import Bot

class BotManager:
    _instance = None

    @classmethod
    def get_instance(cls, bot=None):
        print(cls._instance)
        if cls._instance is None:
            cls._instance = Kkr(bot)
        print(cls._instance)
        return cls._instance

def initialize_manager(bot):
    return KkrManager.get_instance(bot)