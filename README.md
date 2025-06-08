# Tasas de Cuba Bot 🇨🇺

Bot de Telegram para consultar las tasas de cambio informales en Cuba de manera rápida y precisa: [https://t.me/tasacubot](https://t.me/tasacubot)

## Funcionalidades 🚀

- 📊 Consulta instantánea de tasas de cambio
- ⏱️ Actualización automática cada hora
- 📱 Interfaz amigable y fácil de usar
- 📈 Datos precisos de ElToque
- 📖 Guía de ayuda completa
- 🔄 Tasas en CUP y MLC
- 🤖 Respuestas rápidas y eficientes
- 🔄 Caché local para respuestas más rápidas
- 🛠️ Manejo de errores robusto

## Requisitos Previos

- Python 3.10 o superior
- Git
- Entorno virtual (recomendado)

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Angelito91/TasaCuBot.git
cd TasaCuBot
```

2. Crea un entorno virtual y actívalo:
```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate     # En Windows
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Configura las variables de entorno:
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```
BOT_TOKEN_API=tu_token_del_bot_de_telegram
TOQUE_TOKEN_API=tu_token_de_la_api_de_eltoque
```

## Estructura del proyecto 📁

```
TasaCuBot/
├── .env
├── .git/
├── .gitignore
├── README.md
├── requirements.txt
└── src/
    ├── config.py           # Configuración de la aplicación
    ├── main.py             # Punto de entrada de la aplicación
    └── bot/                # Módulo principal del bot
    │   ├── __init__.py     # Inicialización del bot
    │   ├── bot.py          # Configuración y manejo del bot
    │   └── commands/       # Comandos del bot
    │       ├── __init__.py
    │       ├── start.py    # Comando /start
    │       ├── tasas.py    # Comando /tasas
    │       └── help.py     # Comando /help
    └── utils/              # Utilidades
        ├── __init__.py
        ├── request.py      # Manejo de peticiones a la API
        └── cache.py        # Sistema de caché para datos
```

## Variables de entorno 🔄

El proyecto requiere las siguientes variables de entorno:

1. `BOT_TOKEN_API`: Token de la API de Telegram (obtenido de @BotFather)
2. `TOQUE_TOKEN_API`: Token de la API de ElToque (obtenido de ElToque.com)

## Uso 🚀

1. Configura las variables de entorno en el archivo `.env`
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta el bot:
```bash
python -m src.main
```

## Comandos disponibles

- `/start` - Inicia el bot y muestra un mensaje de bienvenida
- `/tasas` - Muestra las tasas de cambio actuales
- `/help` - Muestra la ayuda y los comandos disponibles

## Contribución 🤝

Las contribuciones son bienvenidas. Por favor, crea un issue antes de enviar un pull request.

## Licencia 📄

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
