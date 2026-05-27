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

# Manufacturer / model labels exposed in the device registry
MANUFACTURER = "jolabs40"
MODEL = "peek-it"

# Coordinator polling
STATUS_SCAN_INTERVAL_SECONDS = 30
HTTP_TIMEOUT_SECONDS = 5
STATUS_TIMEOUT_SECONDS = 3
# Backoffs (seconds) between retry attempts for transient ClientError
RETRY_BACKOFFS = (1.0, 3.0)

# Repair issue keys
ISSUE_ANDROIDTV_MISSING = "androidtv_missing"

# ADB (pour les boutons Assist/Overlay)
ADB_PORT = 5555
PEEKIT_PACKAGE = "net.jolabs40.peekit"
PEEKIT_ACCESSIBILITY_COMPONENT = f"{PEEKIT_PACKAGE}/{PEEKIT_PACKAGE}.MenuKeyService"
