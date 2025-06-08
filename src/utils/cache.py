from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from utils.request import get_data_from_api

class APICache:
    def __init__(self, update_interval: int = 3600):  # 1 hora por defecto
        self._data: Optional[Dict[str, Any]] = None
        self._last_update: Optional[datetime] = None
        self._update_interval = timedelta(seconds=update_interval)

    def get_cached_data(self, api_token: str) -> Dict[str, Any]:
        """Obtiene datos de la API usando caché"""
        # Si no hay datos o han expirado
        if self._data is None or self._should_update():
            self._update_cache(api_token)
        
        return self._data

    def _should_update(self) -> bool:
        """Verifica si es necesario actualizar los datos"""
        if self._last_update is None:
            return True
        
        return datetime.now() - self._last_update > self._update_interval

    def _update_cache(self, api_token: str):
        """Actualiza los datos en caché"""
        try:
            self._data = get_data_from_api(api_token)
            self._last_update = datetime.now()
        except Exception as e:
            print(f"❌ Error al actualizar caché: {str(e)}")
            # Mantener los datos anteriores si hay error

# Instancia global del caché
api_cache = APICache(update_interval=3600)  # Actualizar cada hora
