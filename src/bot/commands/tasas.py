import humanize
from datetime import datetime
from utils.request import DataDict
from pytz import timezone


def show_tasas(data: DataDict):
    """Genera un mensaje con las tasas de cambio actuales usando Markdown"""
    tasas = data["tasas"]

    # Hora actual en Cuba
    cuba_tz = timezone('America/Havana')
    now_cuba = datetime.now(cuba_tz).astimezone()

    # Convertir la fecha/hora a timezone-aware
    date_time_str = f"{data['date']} {data['hour']}:{data['minutes']}:{data['seconds']}"
    date_time = datetime.strptime(
        date_time_str, "%Y-%m-%d %H:%M:%S").astimezone()

    humanize.i18n.activate("es")
    time = humanize.naturaltime(
        now_cuba - date_time,
        when=now_cuba,
        months=True
    )

    # Crear el mensaje con todas las tasas en una tabla Markdown
    message = (
        f"📊 **Tasas de cambio** - Última actualización {time}\n\n"
        "```\n"
        "Moneda          |     CUP    |     MLC\n"
        "----------------|------------|-----------\n"
        f"💵 USD          | {tasas['USD']:.2f}     | {tasas['USD'] / tasas['MLC']:.2f}\n"
        f"💶 EUR          | {tasas['EUR']:.2f}     | {tasas['EUR'] / tasas['MLC']:.2f}\n"
        f"🏦 MLC          | {tasas['MLC']:.2f}     | 1.00\n"
        f"💰 USDT (TRC20) | {tasas['USDT_TRC20']:.2f}     | {tasas['USDT_TRC20'] / tasas['MLC']:.2f}\n"
        f"₿ Bitcoin       | {tasas['BTC']:.2f}     | {tasas['BTC'] / tasas['MLC']:.2f}\n"
        f"🔺 TRX          | {tasas['TRX']:.2f}     | {tasas['TRX'] / tasas['MLC']:.2f}\n"
        "```\n\n"
        "*🔄 Actualizadas diariamente para mantener siempre las tasas más precisas*\n\n"
        "💡 **Tip:** Las tasas se actualizan automáticamente cada hora\n"
        "✨ **Precisión garantizada por ElToque**"
    )

    return message
