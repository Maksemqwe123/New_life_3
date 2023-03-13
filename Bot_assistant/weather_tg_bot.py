from New_life_3.Bot_assistant.register_handlers_main import *

from New_life_3.Bot_assistant.config_bot.config import *

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


if __name__ == '__main__':

    dp.middleware.setup(AccessMiddleware())

    register_handlers_commands(dp)
    register_handlers_weather_house_street(dp)
    register_handlers_back_game(dp)
    register_handlers_eats_drinks(dp)
    register_handlers_film_book(dp)
    register_handlers_location_new_city(dp)
    register_handlers_admin(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
