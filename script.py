import requests
import datetime

# Credenciales de Pushover
PUSHOVER_USER_KEY = "unojfi8ecu7p8tz5qha34v486fo4zd"
PUSHOVER_API_TOKEN = "acmzo9fnvaadcpo4kiaqbocspj8fid"

# Datos de la cuenta
INSTAGRAM_HANDLE = "ideastudio.jyb"

def check_instagram_and_notify():
    # 1. Simulación o check de Instagram (puedes usar instaloader o scraping)
    subio_contenido = False  # Cambiar por la lógica real de scraping
    
    if not subio_contenido:
        # 2. Generar idea de contenido (vía Gemini/OpenAI API)
        idea = "💡 Reel de 15s: Mostrá un proceso rápido de trabajo y usá el audio en tendencia."
        
        # 3. Mandar notificación crítica a Pushover
        url_atajo = "shortcuts://run-shortcut?name=PublicarEnInstagram"
        
        payload = {
            "token": PUSHOVER_API_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "title": "🚨 ¡SUBÍ ALGO A INSTAGRAM!",
            "message": f"Todavía no publicaste hoy.\n\nIdea rápida:\n{idea}",
            "priority": 2,        # Priority 2 = Alerta crítica/emergencia (suena en bucle)
            "retry": 60,          # Reintentar cada 60 segundos si no la confirmás
            "expire": 3600,       # Expira en 1 hora
            "sound": "persistent", # Sonido continuo de alarma
            "url": url_atajo,     # URL scheme que abre el Atajo al tocar la notificación
            "url_title": "Abrir Instagram / Ver Idea"
        }
        
        requests.post("https://api.pushover.net/1/messages.json", data=payload)

if __name__ == "__main__":
    check_instagram_and_notify()