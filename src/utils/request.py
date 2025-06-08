import requests
from typing import TypedDict


class Tasas(TypedDict):
    TRX: float
    USDT_TRC20: float
    BTC: float
    MLC: float
    USD: float
    EUR: float  # La tasa de EUR se devuelve como ECU


class DataDict(TypedDict):
    tasas: Tasas
    date: str  # Formato 'YYYY-MM-DD'
    hour: int
    minutes: int
    seconds: int


def get_data_from_api(api_token) -> DataDict:
    url = "https://tasas.eltoque.com/v1/trmi"
    headers = {
        "accept": "*",
        "Authorization": f"Bearer {api_token}"
    }

    data = requests.get(url, headers=headers).json()
    data["tasas"]["EUR"] = data["tasas"].pop("ECU")  # Rename ECU to EUR
    return data