from dotenv import load_dotenv
from os import getenv
from sys import exit
from time import sleep
from bot.bot import init_bot

# Cargar variables de entorno
load_dotenv()

if __name__ == "__main__":
    # Validar tokens
    bot_token = getenv("BOT_TOKEN_API")
    api_token = getenv("TOQUE_TOKEN_API")

    if not bot_token or not len(bot_token.strip()) > 0:
        print("❌ Error: No se encontró el token del bot de Telegram en el archivo .env")
        print(
            "💡 Asegúrate de tener una línea con 'BOT_TOKEN_API=tu_token' en tu archivo .env")
        exit(1)

    if not api_token or not len(api_token.strip()) > 0:
        print("❌ Error: No se encontró el token de la API de ElToque en el archivo .env")
        print("💡 Asegúrate de tener una línea con 'TOQUE_TOKEN_API=tu_token' en tu archivo .env")
        exit(1)

    # Bucle principal del bot con reinicio automático
    while True:
        try:
            print("🚀 Iniciando el bot...")
            bot = init_bot(bot_token, api_token)
            bot.polling(non_stop=True, timeout=60)
        except KeyboardInterrupt:
            print("👋 Adiós! Hasta pronto.")
            exit(0)
        except Exception as e:
            print(f"❌ Error crítico en el bot: {str(e)}")
            print("🔄 Intentando reiniciar el bot en 5 segundos...")
            sleep(5)
            print("🔄 Reiniciando el bot...")
