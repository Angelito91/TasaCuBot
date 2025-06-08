from telebot import TeleBot
from telebot.types import BotCommand
from utils.cache import api_cache

# Commands
from .commands.start import start
from .commands.tasas import show_tasas
from .commands.help import help


def init_bot(bot_token, api_token):

    bot = TeleBot(bot_token)

    # Configuración del bot
    bot.set_my_short_description(
        "💰 Tasas de cambio informales en Cuba 🇨🇺 - Actualizadas diariamente 🔄")
    bot.set_my_description(
        "🔍 Tu guía personal para el cambio de divisas en Cuba 🇨🇺\n\n"
        "💰 Consulta las tasas más recientes de:\n"
        "• USD 💵\n"
        "• MLC 🏦\n"
        "• TRX 🔺\n"
        "• Bitcoin ₿\n"
        "• USDT 💰 (TRC20)\n\n"
        "🔄 Actualizadas diariamente para mantenerte siempre informado\n\n"
        "📊 Usa /tasas para ver las tasas más recientes"
    )
    bot.set_my_commands([
        BotCommand("start", "🔹 Iniciar el bot y ver los comandos disponibles"),
        BotCommand("tasas", "📊 Ver las tasas de cambio más recientes"),
        BotCommand("help", "🤔 Ayuda y información sobre el bot"),
    ])

    # Manejadores de comandos
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, start(message))

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.reply_to(message, help(message), parse_mode="Markdown")

    @bot.message_handler(commands=['tasas'])
    def handle_tasas(message):
        # Mostrar mensaje de espera
        msg = bot.reply_to(message, "⏳ Obteniendo las tasas más recientes...")

        try:
            # Obtener datos de la API usando caché
            data = api_cache.get_cached_data(api_token)

            # Editar el mensaje con las tasas
            bot.edit_message_text(
                chat_id=msg.chat.id,
                message_id=msg.message_id,
                parse_mode="Markdown",
                text=show_tasas(data)
            )
        except Exception as e:
            # Si hay un error, mostrar mensaje de error
            bot.edit_message_text(
                chat_id=msg.chat.id,
                message_id=msg.message_id,
                text=f"❌ Error al obtener las tasas: {str(e)}\n\n"
                "🔄 Intenta nuevamente más tarde"
            )

    return bot
