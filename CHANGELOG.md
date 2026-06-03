# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.6.0] — 2026-06-03

### Added

- **Service `save_template`** : persiste un template réutilisable
  (`template_id` + `elements` JSON, `name` et `overwrite` optionnels) sur la/les
  TV via un nouvel endpoint app `POST /api/templates/save`. Réutilise les
  patterns existants — fan-out parallèle, `target`, skip des TV offline,
  `supports_response` (retourne `{nom_tv: {saved, reason, http_status}}`). Les
  éléments passent par `sanitize_element` (types Java forcés, comme le mode 2 de
  `notify`). Affichage ultérieur du template sauvé : service `notify` existant
  (`template_id` + `params`), inchangé.

### Changed

- `payload.py` : nouveau builder `build_save_template_payload`.
- `_dispatch` paramétré par une fabrique `error_result` (forme `delivered` pour
  notify/tts/dismiss, `saved` pour save_template) — zéro régression sur les
  services existants.
- `services.yaml` : schéma UI du service `save_template`.

### Contrat app — implémenté ✅

- `POST /api/templates/save` — body `{id, name?, elements[], overwrite?, source}`,
  réponse HTTP 200 `{"status":"ok","saved":true,"id":…}` ou
  `{…"saved":false,"reason":"invalid_id|empty_elements|exists|storage_error"}`
  (200 même en cas de refus, comme `/api/notify`). Implémenté côté app
  (`../peek-it`) en route **polymorphe** : un `elements` à la racine route vers
  le contrat HA, le Concepteur (`content.elements`) garde son contrat
  historique. Le slug HA devient la clé `<slug>.json` dans `Template_Custom/`,
  visible dans `/api/templates/list` et rendable par `/api/notify`.

## [1.5.0] — 2026-06-02

### Added

- **Service `dismiss` (C2)** : ferme la notification au sommet de la pile
  (raccourci lisible de `action: CLOSE`), avec `target` optionnel et statut de
  livraison remonté. Champ `notification_id` réservé (envoyé si fourni, ignoré
  par l'app tant que la fermeture ciblée n'est pas supportée côté app).
- **Device triggers (C3)** : l'event `peekit_button_press` est exposé en
  *device trigger* « Bouton de l'overlay pressé », utilisable dans les
  automations standard. Le webhook enrichit l'event avec `device_id` (résolu
  depuis l'IP de la TV émettrice) ; l'event reste rétrocompatible
  (`{action[, device_id]}`).

### Changed

- **`priority` documenté (C4)** : champ indicatif — l'app le journalise mais
  n'outrepasse pas (encore) le mode Ne Pas Déranger.
- `services.yaml` : service `dismiss`, description de `priority` clarifiée.
- `strings.json` + 6 traductions : libellé du device trigger.
- README (6 langues) : section « Boutons cliquables & fermeture ».

## [1.4.0] — 2026-06-02

### Added

- **Mode simple enrichi (B3)** : champs optionnels `position`
  (`top`/`center`/`bottom`), `level` (`info`/`warning`/`alert` → couleur
  d'accent + icône), `icon` (`mdi:…`) et `color`, qui génèrent les `elements`
  automatiquement. Le rendu par défaut est **inchangé** si ces champs sont
  absents (chemin legacy préservé à l'identique).
- **Image dans le mode simple (C1)** : `image_url` (+ `image_fit`
  contain/cover/fill) → élément `image` (URL http(s), `data:base64` ou chemin
  local, via Glide). Cas d'usage : photo d'un visiteur de sonnette. Le mode
  image-seule (sans `message`) est supporté.
- **Service `get_sounds` (B4)** : liste les sons disponibles (`official` +
  `custom`) de chaque TV via `GET /api/sounds/list`.
- **Langue TTS par défaut = langue Home Assistant (B2)** : `ttsLang`/`lang`
  non précisé → 1er segment de `hass.config.language` (ex. `fr`), pour
  `peek_it_ha.tts` et le mode TTS de `peek_it_ha.notify`.

### Changed

- `services.yaml` : nouveaux champs `position`/`level`/`icon`/`color`/
  `image_url`/`image_fit`, service `get_sounds`, liste des sons intégrés
  documentée, langue TTS par défaut clarifiée.
- README (6 langues) : section « Mode simple enrichi (presets & image) ».

## [1.3.0] — 2026-06-02

### Added

- **Statut de livraison remonté** : les services `peek_it_ha.notify` et
  `peek_it_ha.tts` exploitent désormais le corps de réponse de l'app
  (`{"delivered":false,"reason":"dnd_active|overlay_permission_denied|…",
  "fallback":…}`) et le **remontent** via `supports_response` —
  `{nom_tv: {delivered, reason, fallback, http_status}}`, exploitable avec
  `response_variable`. Une notification refusée (Ne Pas Déranger, overlay
  révoqué…) n'est plus comptée comme un succès silencieux ; elle est aussi
  journalisée en warning. Les TV hors ligne apparaissent avec
  `reason="offline"`. Rétrocompatible (réponse ignorable).

### Changed

- **Refactorisation interne (aucun changement de comportement)** :
  - nouveau module `payload.py` centralisant `build_notify_payload` /
    `build_tts_payload` / `sanitize_element`, partagés par le service de
    domaine et l'entité `notify` (fin de la duplication du builder) ;
  - nouveau helper `async_get_json` dans `http.py` (pendant GET de
    `async_post_json`) ; `_test_connection`, `_fetch_templates`,
    `_send_welcome_notification` et `get_templates` passent par les helpers
    HTTP communs au lieu de réécrire le POST/GET.

## [1.2.0] — 2026-06-02

### Added

- **Paramètre `target`** sur les services `peek_it_ha.notify`, `peek_it_ha.tts`
  et `peek_it_ha.tts_stop` : cible une ou plusieurs TV précises (sélecteur
  *device* dans l'UI ; accepte aussi un nom de device ou une IP en YAML).
  Sans `target`, toutes les TV sont visées comme avant (rétrocompatible).
  C'est désormais le moyen d'envoyer une notification **riche** (TTS, son,
  animations) à une seule TV, ce que l'entité `notify.<tv>` ne permet pas
  (schéma `send_message` figé à `message`+`title`).

### Fixed

- **Fan-out parallèle** des services `notify`/`tts`/`tts_stop` via
  `asyncio.gather` : le coût total n'est plus la somme des TV mais celui de
  la plus lente. Auparavant, chaque TV éteinte ajoutait ~19 s de retries en
  séquentiel et pouvait faire échouer l'appel de service entier
  (« operation aborted »).
- **TV hors ligne ignorées** : les services s'appuient sur
  `coordinator.is_online` pour écarter (fail-fast) les TV éteintes et
  journaliser clairement celles qui sont sautées, sans impacter l'envoi
  vers les TV en ligne.
- **`notify.<tv>` plus figé en `unavailable`** : l'entité notify hérite
  désormais de `CoordinatorEntity` et réévalue sa disponibilité à chaque
  poll `/api/status`, alignée sur le binary_sensor de statut.

## [1.1.5] — 2026-05-31

### Changed

- Retrait du fichier de notes de développement interne du dépôt public
  (déplacé hors suivi Git). Aucun changement fonctionnel de l'intégration.

## [1.1.4] — 2026-05-30

### Changed

- **README transformé en vitrine** : `info.md` n'étant plus rendu par
  HACS depuis la 2.0, le `README.md` (affiché par HACS) devient une page
  de présentation courte qui renvoie vers la documentation complète sur
  GitHub. La doc complète anglaise est déplacée dans `README_EN.md`.
- Le guide complet existe désormais par langue : `README_EN.md`,
  `README_FR.md`, `README_DE.md`, `README_ES.md`, `README_NL.md`,
  `README_PT.md`. Le lien « English » des sélecteurs pointe vers
  `README_EN.md`.
- `hacs.json` : `render_readme` rétabli ; `info.md` supprimé.

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
- `CHANGELOG.md`, pytest suite under `tests/` with
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
