# CLAUDE.md — peek-it-ha

> Custom component Home Assistant qui pilote l'app Android TV **peek-it**
> (`net.jolabs40.peekit`) via son serveur HTTP local (port 8081, header
> `X-API-Key`) et reçoit en retour ses callbacks (button presses, logs)
> via un webhook signé.
>
> Repo Android compagnon : `../peek-it/` (Java + Kotlin pour l'écran
> Settings). L'app TV est l'autorité du contrat API ; toute modification
> de payload doit être synchronisée des deux côtés.

---

## 1. Architecture

```
                          Home Assistant
┌─────────────────────────────────────────────────────────────┐
│  custom_components/peek_it_ha/                              │
│                                                             │
│   config_flow ──── zeroconf (_peekit._tcp) ── user form    │
│        │                                                    │
│        ▼                                                    │
│   ConfigEntry data: {ip, port, name, api_key,              │
│                      webhook_secret}                        │
│        │                                                    │
│        ▼                                                    │
│   PeekItCoordinator ── GET /api/status toutes les 30 s     │
│        │                                                    │
│   ┌────┼─────────────────────────────────────────────┐     │
│   │    │                                             │     │
│   │  binary_sensor  notify  button (×6)              │     │
│   │  - status       1× NotifyEntity                  │     │
│   │  - overlay      via http.async_post_json         │     │
│   │  - a11y                                          │     │
│   │  - micro                                         │     │
│   └─────────────────────────────────────────────────┘      │
│                                                             │
│   Services :  notify · tts · tts_stop · get_templates       │
│   Webhook  :  /api/webhook/peek_it_debug                    │
│                   ↑ exige header X-Peek-Secret              │
└─────────────────────────────────────────────────────────────┘
                ▲ HTTP local LAN
                │
          ┌─────┴─────┐
          │ peek-it   │  Android TV app
          │ port 8081 │  /api/{status,notify,tts,tts/stop,
          │           │      templates/list}
          └───────────┘
```

### Fichiers clés

| Fichier | Rôle |
|---|---|
| `__init__.py` | setup/unload entry, services (`notify`/`tts`/`tts_stop`/`get_templates`), webhook handler avec validation secret, migration auto du secret |
| `config_flow.py` | flow zeroconf + manual + options (Settings/Templates/Designer) |
| `coordinator.py` | `PeekItCoordinator` (DataUpdateCoordinator) — un seul GET `/api/status` toutes les 30 s, partagé par toutes les entités |
| `http.py` | helper `async_post_json` : session HA mutualisée (`async_get_clientsession`) + retry 2× (backoffs 1 s / 3 s) sur `ClientError` transitoire |
| `binary_sensor.py` | 4 capteurs `CoordinatorEntity` : status (connectivity) + overlay/accessibility/microphone |
| `notify.py` | `NotifyEntity` avec 3 modes (message simple, `elements` brut, `template_id`+`params`) |
| `button.py` | 6 boutons ADB (`EntityCategory.CONFIG`) : enable/disable Assist, Overlay, Accessibility — via `adb-shell` |
| `const.py` | toutes les constantes (CONF_*, intervalles, backoffs, repair keys) |
| `strings.json` + `translations/*.json` | EN / FR / DE / ES / PT / NL |
| `services.yaml` | schema UI des services |
| `manifest.json` | `version`, `zeroconf`, `iot_class=local_polling` |

---

## 2. Conventions Home Assistant — règles absolues

1. **Async partout** (`async def`, préfixe `async_*`). Jamais d'I/O dans
   un `@property`.
2. **Session aiohttp HA** : toujours `async_get_clientsession(hass)`,
   jamais `aiohttp.ClientSession()` ad-hoc.
3. **`DataUpdateCoordinator`** pour tout polling — `CoordinatorEntity`
   pour les entités. Pas de `async_update()` direct par entité.
4. **`DeviceInfo`** sur toutes les entités (mêmes `identifiers={(DOMAIN, ip)}`)
   pour qu'elles soient regroupées dans une seule device card.
5. **Type hints stricts** : `str | None = None`, jamais `str = None`.
6. **Pas de `print`** — toujours `_LOGGER`.
7. **Pas de blocking I/O** dans une coroutine — utiliser
   `hass.async_add_executor_job(...)` pour les libs sync (cf. `button.py`
   avec `adb-shell`).
8. **Strings UI** dans `strings.json` + `translations/*.json` synchronisés
   sur les 6 langues (EN, FR, DE, ES, PT, NL).
9. **Webhook** : toute requête entrante doit présenter le header
   `X-Peek-Secret` valide ; sinon 401 + log warning.
10. **Repair issues** plutôt que `persistent_notification` pour signaler
    une config incomplète.

---

## 3. Contrat API avec l'app peek-it (Android)

| Endpoint Android | Méthode | Usage HA |
|---|---|---|
| `/api/status` | GET | Polling coordinator. Doit renvoyer `{api_key_required, api_key_valid, permissions: {overlay, accessibility, microphone}}` |
| `/api/notify` | POST | Service `notify` + welcome notif. Payload strict (voir `notify.py`) |
| `/api/tts` | POST | Service `tts` |
| `/api/tts/stop` | POST | Service `tts_stop` |
| `/api/templates/list` | GET | OptionsFlow "Templates" + service `get_templates` |

**Header obligatoire si `api_key` configurée** : `X-API-Key: <key>`.

**Welcome notification** (envoyée à la création de l'entry) :
champ top-level `webhook_secret` à persister côté Android pour le
renvoyer en header `X-Peek-Secret` sur le webhook
`/api/webhook/peek_it_debug`.

---

## 4. Stack & commandes

| Outil | Version |
|---|---|
| Python | 3.12+ |
| Home Assistant | 2024.1.0+ |
| `aiohttp` | fourni par HA |
| Tests | `pytest-homeassistant-custom-component` |

```bash
# Installer les deps test
pip install -r requirements_test.txt

# Lancer les tests + coverage
pytest tests/ -v --cov=custom_components.peek_it_ha

# Lint
python -m ruff check custom_components/peek_it_ha/

# Vérifier la structure manifest / strings (hassfest)
python -m script.hassfest --integration-path custom_components/peek_it_ha
```

### Déploiement (Samba HA)

```bash
cp -r custom_components/peek_it_ha H:/custom_components/
# puis restart HA via API REST ou UI
```

---

## 5. Améliorations à faire

| # | Sujet | Statut |
|---|---|---|
| 1 | Validation `X-Peek-Secret` sur webhook | **fait** (1.1.0) |
| 2 | Type hints stricts `notify.async_send_message` | **fait** (1.1.0) |
| 3 | `PeekItCoordinator` partagé | **fait** (1.1.0) |
| 4 | `async_get_clientsession` partout | **fait** (1.1.0) |
| 5 | `DeviceInfo` + `EntityCategory.CONFIG` | **fait** (1.1.0) |
| 6 | Retry 2× sur `ClientError` | **fait** (1.1.0) |
| 7 | Suite pytest (~25 tests) | **fait** (1.1.0) |
| 8 | `CHANGELOG.md` + bump 1.1.0 | **fait** (1.1.0) |
| 9 | Repair issue Android TV | **fait** (1.1.0) |
| 10 | `CLAUDE.md` | **fait** (1.1.0) |

### À envisager (post-1.1.0)

- **Token Reload** : exposer dans l'OptionsFlow un bouton "régénérer le
  webhook secret" qui pousse un nouveau welcome notif au TV.
- **Translation FR/IT/HI/NL** : alignement complet (HA en a parfois
  besoin d'autres clés ajoutées plus tard).
- **ADB authentification** : ajouter un test de connectivité ADB dans
  le config_flow avant d'exposer les 6 boutons.
- **Backwards-compat** des entries 1.0.0 : valider que le secret
  auto-généré arrive bien sur le TV même sans re-save de l'entry (idée :
  endpoint TV `/api/secret/set` que HA peut appeler à la migration).
- **NotifyEntity `data`** : la classe HA `NotifyEntity` n'accepte
  officiellement que `message`+`title`. Le 3e param `data` est notre
  extension non standard ; tester avec le service générique
  `notify.send_message` vs `peek_it_ha.notify`.

---

## 6. Pointeurs externes

- Doc Home Assistant developers — Custom integrations :
  https://developers.home-assistant.io/docs/creating_integration_file_structure
- `DataUpdateCoordinator` :
  https://developers.home-assistant.io/docs/integration_fetching_data
- `NotifyEntity` (2024.x) :
  https://developers.home-assistant.io/docs/core/entity/notify
- `pytest-homeassistant-custom-component` :
  https://github.com/MatthewFlamm/pytest-homeassistant-custom-component
