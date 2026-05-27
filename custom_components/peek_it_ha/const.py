"""Constants for the Peek-it [HA] integration."""

DOMAIN = "peek_it_ha"
DEFAULT_PORT = 8081
CONF_IP_ADDRESS = "ip_address"
CONF_NAME = "name"
CONF_PORT = "port"
CONF_API_KEY = "api_key"
CONF_WEBHOOK_SECRET = "webhook_secret"

# Fixed identifier for receiving logs (must match the Android app code)
WEBHOOK_ID = "peek_it_debug"
# HTTP header the TV must send so the webhook accepts the call
WEBHOOK_SECRET_HEADER = "X-Peek-Secret"

# ADB (pour les boutons Assist/Overlay)
ADB_PORT = 5555
PEEKIT_PACKAGE = "net.jolabs40.peekit"
PEEKIT_ACCESSIBILITY_COMPONENT = f"{PEEKIT_PACKAGE}/{PEEKIT_PACKAGE}.MenuKeyService"
