from telebot.types import Message

def start(message: Message):
    """Maneja el comando /start"""
    return (
        "💰 ¡Bienvenido al Bot de Tasas Informales de Cuba! 🇨🇺\n\n"
        "🔍 Tu guía personal para el cambio de divisas en Cuba\n\n"
        "Comandos disponibles:\n"
        "• /tasas - Ver las tasas más recientes\n"
        "• /help - Descubre todos los secretos del bot\n\n"
        "💡 Tip: Usa /tasas para obtener las tasas más actualizadas\n"
        "✨ Actualizadas diariamente para ti\n"
    )
