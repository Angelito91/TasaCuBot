from telebot.types import Message

def help(message: Message) -> str:
    """Genera un mensaje de ayuda detallado"""
    return (
        "💡 ** Guía de uso del Bot de Tasas de Cuba ** 🇨🇺\n\n"
        "**Comandos disponibles:**\n"
        "• /tasas - Ver las tasas de cambio actuales\n"
        "• /help - Mostrar esta guía de ayuda\n\n"
        
        "**Información sobre las tasas:**\n"
        "• Las tasas se actualizan automáticamente cada hora\n"
        "• Se muestran en CUP y su equivalente en MLC\n"
        "• Datos proporcionados por ElToque\n\n"
        
        "**Monedas disponibles:**\n"
        "• 💵 USD (Dólar Estadounidense)\n"
        "• 💶 EUR (Euro)\n"
        "• 🏦 MLC (Moneda Libre Convertible)\n"
        "• 💰 USDT (TRC20)\n"
        "• ₿ Bitcoin\n"
        "• 🔺 TRX (Tron)\n\n"
        
        "**¿Cómo usar el bot?**\n"
        "1. Escribe /tasas para ver las tasas actuales\n"
        "2. Las tasas se muestran en CUP y su equivalente en MLC\n"
        "3. Los valores se actualizan automáticamente\n\n"
        
        "**Información adicional:**\n"
        "• El bot se mantiene actualizado con las tasas más recientes\n"
        "• Los datos son obtenidos de fuentes confiables\n"
        "• Si encuentras algún error, por favor reportarlo\n\n"
        
        "**Soporte y contacto:**\n"
        "• Para sugerencias o reportar problemas:\n"
        "• Escribir al administrador del bot\n\n"
        
        "✨ Mantente informado con las tasas más recientes\n"
        "🔄 Actualizado automáticamente cada hora\n"
        "💰 Tasas de cambio informales en Cuba"
    )
