# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.3] — 2026-05-30

### Added

- **Vitrine HACS** : fichier `info.md` à la racine, rendu par HACS à la
  place du README. Présentation courte du produit avec un appel clair à
  **ouvrir la documentation complète sur GitHub** (le panneau HACS ne
  gère ni les ancres ni la navigation interne). Le `README.md` complet
  reste la doc de référence sur GitHub.

### Changed

- `hacs.json` : suppression de `render_readme` (remplacé par `info.md`).

## [1.1.2] — 2026-05-30

### Fixed

- **README dans HACS** : l'image d'en-tête et les liens (sommaire,
  sélecteur de langue, renvois inter-sections) utilisaient des chemins
  relatifs et des ancres `#…`, non gérés par le panneau d'information
  HACS (image cassée, liens renvoyant vers `/hacs`). Tous convertis en
  URL absolues GitHub (`raw.githubusercontent.com` pour l'image,
  `github.com/.../blob/master/…` pour les liens) — fonctionnent
  désormais sur GitHub *et* dans HACS. Appliqué aux 6 langues.

## [1.1.1] — 2026-05-30

### Fixed

- **Dépendance `adb-shell` manquante** : `manifest.json` déclarait
  `requirements: []`, donc Home Assistant n'installait jamais la
  bibliothèque utilisée par les 6 boutons ADB — ceux-ci échouaient
  silencieusement. Ajout de `adb-shell==0.4.4`.

### Added

- `issue_tracker` dans le `manifest.json`.
- Fichier `LICENSE` (MIT) — le badge et le lien du README étaient morts.
- Assets `icon.png`, `icon@2x.png`, `logo.png`, `logo@2x.png`.

### Changed

- **Refonte de la documentation** (README EN/FR/DE/ES/NL/PT) :
  mise en page « Designer-first », sections techniques repliées,
  diacritiques corrigés, distinction app/intégration. Alignement de la
  doc sur le contrat réel : entités exposées (4 capteurs + notify +
  6 boutons ADB), types de widgets (`rect`/`hexagon`/`confetti`),
  réponse `/api/status`, webhook `X-Peek-Secret`, jeton d'accès HA,
  installation via Google Play Store.

## [1.1.0] — 2026-05-27

### ⚠ Breaking changes

- **Webhook signature** — `/api/webhook/peek_it_debug` now requires a
  per-entry secret in the `X-Peek-Secret` HTTP header. Requests without
  the header (or with the wrong value) are rejected with HTTP 401.
  - **Migration** — re-open *Settings → Devices & Services → Peek-it
    [HA] → Configure → Settings* and click *Submit*. This pushes a new
    welcome notification to the TV, which contains the new
    `webhook_secret` so the Android client can persist it and use it
    on every callback.
  - Existing entries that have no secret yet get one auto-generated at
    setup with a `WARNING` log inviting the same re-save.
  - Companion change required on the Peek-it Android app
    (`HaApiHandler`): store `webhook_secret` from the welcome payload
    and send it on every `peek_it_debug` POST.

### Added

- `PeekItCoordinator` ([`coordinator.py`](custom_components/peek_it_ha/coordinator.py)):
  a single `DataUpdateCoordinator` per TV polls `GET /api/status` every
  30 s. All entities (connectivity sensor, 3 permission sensors, notify,
  6 buttons) share that snapshot — one HTTP request per device per
  interval, regardless of how many entities are exposed.
- Shared HTTP helper ([`http.py`](custom_components/peek_it_ha/http.py))
  reusing Home Assistant's managed `aiohttp` client session via
  `async_get_clientsession()`, with a 2-retry backoff (1 s, 3 s) on
  transient `ClientError`. Used by `notify`, `tts`, `tts_stop`.
- `DeviceInfo` on every entity (identifiers `(DOMAIN, ip)`,
  `manufacturer="jolabs40"`, `model="peek-it"`, `configuration_url=`
  Designer URL) so the ~10 entities now group under a single peek-it
  device card in Home Assistant.
- `EntityCategory.CONFIG` on the 6 ADB setup buttons (Assist /
  Overlay / Accessibility ×2).
- New translation key `binary_sensor.status` for the connectivity
  sensor — synced across EN/FR/DE/ES/PT/NL.
- Repair issue `androidtv_missing` (warning severity, non-fixable)
  shown in *Settings → Repairs* when the Android TV companion
  integration is not configured.
- `CHANGELOG.md`, `CLAUDE.md`, pytest suite under `tests/` with
  `pytest-homeassistant-custom-component`.

### Changed

- Strict typing: `notify.async_send_message(message, title=None,
  data=None)` is now `title: str | None = None, data: dict | None =
  None` (PEP 484 conforming).
- `binary_sensor.py` switched to `CoordinatorEntity` — no more
  independent `aiohttp.ClientSession()` per entity per poll.
- `notify.py`, `config_flow.py` (test_connection / welcome /
  fetch_templates) and the four `__init__.py` services all use the
  shared HA session.
- The persistent notification "Android TV recommended" is replaced by
  a proper Repair Issue.
- Webhook is now registered once per integration (instead of once per
  entry) — multiple TV entries no longer trip
  `HomeAssistantError("Handler is already defined!")`.

### Fixed

- `notify.py`: bad type hint `title: str = None, data: dict = None`
  rejected by strict mypy.
- `__init__.py:async_unload_entry`: no longer drops the webhook on
  every entry unload — it stays alive until the last entry leaves.

## [1.0.0] — Initial release

- `config_flow` with Zeroconf discovery (`_peekit._tcp.local.`) and
  manual IP/port/API key.
- 4 `binary_sensor` entities (status + 3 Android permissions).
- 1 `NotifyEntity` with 3 modes (simple message, raw elements,
  `template_id` + params).
- 6 ADB `ButtonEntity` (Assist, Overlay, Accessibility — enable /
  disable).
- 4 services: `get_templates`, `notify`, `tts`, `tts_stop`.
- Webhook `peek_it_debug` receiving `BUTTON_CLICK:*` events and log
  forwarding.
