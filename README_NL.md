# Peek-it [HA] — Home Assistant-integratie

<p align="center">
  <img src="custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Maak van uw Android TV een slim notificatiescherm.</strong><br/>
  Meldingen, camera's, dashboards, TTS, menu's — als overlay op uw TV in realtime.
</p>

<p align="center">
  <a href="https://github.com/jolabs40/peek-it-ha/releases"><img src="https://img.shields.io/github/v/release/jolabs40/peek-it-ha?style=for-the-badge&color=blue&label=Release" alt="Release"/></a>
  <a href="https://github.com/jolabs40/peek-it-ha"><img src="https://img.shields.io/github/stars/jolabs40/peek-it-ha?style=for-the-badge&color=yellow" alt="Stars"/></a>
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/LICENSE"><img src="https://img.shields.io/github/license/jolabs40/peek-it-ha?style=for-the-badge&color=green" alt="License"/></a>
  <a href="https://github.com/hacs/integration"><img src="https://img.shields.io/badge/HACS-Custom-orange?style=for-the-badge" alt="HACS"/></a>
  <a href="https://play.google.com/store/apps/details?id=net.jolabs40.peekit"><img src="https://img.shields.io/badge/Google%20Play-Peek--it%20[TV]-414141?style=for-the-badge&logo=googleplay&logoColor=white" alt="Google Play"/></a>
  <img src="https://img.shields.io/badge/Android%20TV-Compatible-brightgreen?style=for-the-badge&logo=android" alt="Android TV"/>
  <img src="https://img.shields.io/badge/Home%20Assistant-Integration-41BDF5?style=for-the-badge&logo=homeassistant&logoColor=white" alt="Home Assistant"/>
</p>

<p align="center">
  <a href="#-hoe-het-werkt">Hoe het werkt</a> •
  <a href="#-installatie">Installatie</a> •
  <a href="#-de-designer">Designer</a> •
  <a href="#-gebruik">Gebruik</a> •
  <a href="#-spraaksynthese-tts">TTS</a> •
  <a href="#-automatiseringen">Automatiseringen</a> •
  <a href="#-geavanceerde-referentie">Geavanceerde referentie</a> •
  <a href="#-waf--de-ultieme-kpi">WAF</a>
</p>

<p align="center">
  <b>Talen:</b>
  <a href="README.md">English</a> |
  <a href="README_FR.md">Fran&ccedil;ais</a> |
  <a href="README_DE.md">Deutsch</a> |
  <a href="README_ES.md">Espa&ntilde;ol</a> |
  Nederlands |
  <a href="README_PT.md">Portugu&ecirc;s</a>
</p>

---

## Waarom Peek-it [HA]?

Uw Android TV-apparaat is 24 uur per dag aangesloten op uw TV. Waarom zou u het niet aan het werk zetten?

De app **Peek-it [TV]** toont **rijke notificaties als overlay** bovenop welke lopende toepassing dan ook: een film, de televisie, een spel... Kijkt u naar een wedstrijd? De stand wordt bijgewerkt in een hoekje. Wordt er aangebeld? De deurcamera verschijnt onmiddellijk. En **u tekent** deze weergaven zelf, zonder ook maar één regel code te schrijven.

> 💡 **Het belangrijkste om te onthouden**
>
> 1. **U ontwerpt** uw notificaties (en zelfs hele pagina's) in de **Designer**, een visuele drag-and-drop-editor die toegankelijk is vanuit elke browser. *Hij bouwt alles op — u hoeft niets te coderen.*
> 2. **U activeert** ze vanuit **Home Assistant** dankzij deze integratie… of vanuit **Tasker, Node-RED, Jeedom** of elke andere HTTP-client, want de app stelt een eenvoudige lokale API beschikbaar.

> 🧩 **Twee componenten, twee rollen**
> De **applicatie Peek-it [TV]** (Android, in de Play Store) tekent de overlay, host de Designer en de template-engine: dat is de autoriteit.
> De **integratie Peek-it [HA]** (deze repository) bestuurt hem vanuit Home Assistant: versturen van notificaties/TTS, statusbewaking, terugkoppeling van knoppen.

### Wat u kunt weergeven

| | |
|------|---------|
| 📝 **Rijke tekst** | Titels, berichten, tellers, weer |
| 🖼️ **Afbeeldingen** | Foto's, screenshots, logo's, QR-codes |
| 🎥 **RTSP-videostreams** | Bewakingscamera's live, ultralage latentie |
| 🌐 **Webpagina's** | HA-dashboards, grafieken, weerwidgets |
| 🔺 **Vormen & SVG** | Rechthoeken, ellipsen, zeshoeken, pijlen, vectoriconen |
| 🎮 **Knoppen & menu's** | Navigeerbaar met de afstandsbediening, activeren uw HA-automatiseringen |
| 📊 **HA-entiteiten & grafieken** | Realtime status en historiek van entiteiten |
| 🔊 **Spraaksynthese** | Gesproken aankondigingen rechtstreeks op de TV |

### Kernfuncties

- **Nul latentie** — native Android-overlay, geen streaming of casting
- **Compatibel met alles** — de overlay verschijnt bovenop welke toepassing dan ook
- **Visuele Designer** — maak alles met drag-and-drop, realtime voorbeeld
- **Herbruikbare templates** — ontwerp één keer, hergebruik met dynamische parameters
- **Multi-apparaat** — beheer meerdere TV's vanuit één enkele HA-instantie
- **Open** — bestuurbaar vanuit HA, Tasker, Node-RED, Jeedom… via een lokale HTTP-API
- **6 talen** — EN, FR, DE, ES, NL, PT

---

## 🧩 Hoe het werkt

Drie stappen, van het visuele naar de automatisering:

| Stap | Waar | Wat u doet |
|------|-----|--------------------|
| **1. Ontwerpen** | 🎨 Designer (browser) | Sleep uw elementen op een canvas dat gekalibreerd is op uw TV. De Designer genereert de volledige weergave voor u. |
| **2. Opslaan** | 🎨 Designer | Sla uw creatie op als herbruikbare **template** (er wordt eenvoudig een ID gegenereerd). |
| **3. Activeren** | 🏠 Home Assistant | Roep de template aan vanuit een automatisering, in enkele regels, met dynamische waarden. |

```yaml
# Stap 3: een in de Designer ontworpen template activeren
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Beveiligingsmelding"
    camera_url: "rtsp://192.168.1.50:554/stream1"
```

> ✅ **U hoeft vrijwel nooit handmatig JSON te schrijven.** De Designer regelt de lay-out; aan de kant van Home Assistant levert u alleen de ID van de template en enkele waarden aan. De [Geavanceerde referentie](#-geavanceerde-referentie) (ruwe JSON, widgettypes, API…) is er alleen voor speciale gevallen.

---

## 📥 Installatie

### 1. De app Peek-it [TV] installeren

**Aanbevolen — Google Play Store**: zoek naar **« Peek-it »** in de Play Store van uw Android TV, of open de pagina:
[play.google.com/store/apps/details?id=net.jolabs40.peekit](https://play.google.com/store/apps/details?id=net.jolabs40.peekit)

> Apparaat zonder Play Store (sommige Android TV-boxen, Fire TV…): installeer de APK via sideloading vanaf de [Releases-pagina](https://github.com/jolabs40/peek-it-ha/releases) (USB-stick, `adb install`, of een bestandsbeheerder).

Vervolgens, ongeacht de methode:

1. Start de applicatie — verleen de **overlay-permissie** (weergave bovenop andere applicaties); de service start automatisch.
2. Noteer het **IP-adres** dat op het hoofdscherm wordt weergegeven (bijv. `192.168.1.42`). Standaardpoort: **8081**.

### 2. De Home Assistant-integratie installeren

**Via HACS (aanbevolen)**: HACS → *Integrations* → menu met 3 puntjes → *Custom repositories* → voeg `https://github.com/jolabs40/peek-it-ha` toe (categorie *Integration*) → *Download* → **herstart HA**.

<details>
<summary>Handmatige installatie</summary>

Kopieer de map `peek_it_ha/` naar `config/custom_components/` en herstart vervolgens Home Assistant:

```
config/
└── custom_components/
    └── peek_it_ha/
        ├── __init__.py
        ├── binary_sensor.py
        ├── button.py
        ├── config_flow.py
        ├── const.py
        ├── coordinator.py
        ├── http.py
        ├── manifest.json
        ├── notify.py
        ├── services.yaml
        ├── strings.json
        ├── translations/  (en, fr, de, es, nl, pt)
        └── icon.png / icon@2x.png / logo.png / logo@2x.png
```
</details>

### 3. De integratie toevoegen

*Instellingen → Apparaten en services → Integratie toevoegen → Peek-it [HA]*. Vul het **IP**, de **poort** (`8081`), een **naam** in en, als de TV-app het vereist, een **API-sleutel**. Als het apparaat via Zeroconf wordt gepubliceerd (`_peekit._tcp`), kan HA het ook **automatisch ontdekken**.

<details>
<summary>Wat er automatisch wordt aangemaakt (HA-entiteiten)</summary>

Alle entiteiten worden gegroepeerd in **één enkele apparaatkaart**. Voor elke TV:

| Entiteit | Type | Beschrijving |
|--------|------|-------------|
| `binary_sensor.<naam>_status` | Connectiviteit | Online / offline (om de 30 s opgevraagd); stelt het attribuut `designer_url` beschikbaar |
| `binary_sensor.<naam>_overlay_permission` | Diagnostiek | Overlay-permissie verleend |
| `binary_sensor.<naam>_accessibility_permission` | Diagnostiek | Toegankelijkheidsservice actief |
| `binary_sensor.<naam>_microphone_permission` | Diagnostiek | Microfoonpermissie verleend |
| `notify.<naam>` | Notify | Versturen van notificaties |
| `button.<naam>_*_assist / overlay / accessibility` | Config (×6) | Permissies in-/uitschakelen via ADB — zie [ADB-knoppen](#-configuratieknoppen-adb) |

Per TV wordt om de 30 s slechts één `GET /api/status`-verzoek verstuurd; alle entiteiten delen deze momentopname (gedeelde coördinator).
</details>

---

## 🎨 De Designer

**Het hart van Peek-it.** Hier maakt u uw notificaties en uw pagina's — visueel, zonder te coderen. Het is een **in de app ingebedde web-editor**, toegankelijk vanuit elke browser op het lokale netwerk:

**URL**: `http://<IP_TV>:<PORT>/` (bijv. `http://192.168.1.42:8081/`) — ook toegankelijk via het attribuut `designer_url` van de statussensor, of *tandwielicoon → Designer* in de opties van de integratie.

- **Drag-and-drop** van uw widgets op een canvas dat gekalibreerd is op de werkelijke resolutie van uw TV (16:9, 21:9…)
- **Realtime JSON-voorbeeld** — u ziet de weergave opbouwen
- **Templatebibliotheek** — opslaan, laden, hernoemen, exporteren/importeren
- **Dynamische parameters** — markeer de variabele elementen (`paramKey`) om ze vanuit HA te vullen
- **Configuratie** van het standaardgeluid, de taal en het **HA-toegangstoken** (zie hieronder)
- **SEND**-knoppen (naar de TV versturen) en **KILL** (sluiten) om onmiddellijk te testen

> 🔑 **Home Assistant-toegangstoken (optioneel).** Bepaalde functies vragen de app om **rechtstreeks** de API van HA aan te roepen: een entiteit schakelen vanuit een menu, de status van een entiteit in realtime weergeven, een historiekgrafiek tekenen, of een camerasnapshot weergeven. Maak hiervoor een **langlevend toegangstoken (Long-Lived Access Token)** aan in HA (*uw profiel → helemaal onderaan → Langlevende toegangstokens → Aanmaken*) en plak het in de instellingen van de Designer. Het wordt versleuteld opgeslagen op de TV. Niet nodig als u alleen notificaties vanuit HA verstuurt.
>
> Niet te verwarren met het **webhook-secret** (`X-Peek-Secret`), dat in de andere richting dient (terugkoppeling van TV-knoppen → HA) en dat de integratie **automatisch** beheert.

> Vanuit HA toont *tandwielicoon → Templates* al uw templates met hun **ID** (kopieerbaar) en hun **parameters**, gesorteerd in *Official* / *Custom* / *Drafts*.

---

## 🚀 Gebruik

Drie manieren om te versturen, van het eenvoudigste naar het meest geavanceerde. **De templatemodus is het handigst**: hij steunt op uw creaties uit de Designer.

### Eenvoudig bericht

Een tekst die onderaan het scherm op een donkere achtergrond verschijnt — ideaal voor een snelle melding.

```yaml
service: peek_it_ha.notify
data:
  message: "De wasmachine is klaar!"
  title: "Thuis"
  duration: 8000
```

### Template + parameters *(aanbevolen)*

Hergebruik een in de Designer ontworpen template door dynamische waarden te injecteren.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Beveiligingsmelding"
    message: "Beweging gedetecteerd in de tuin"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

De server laadt de template, vervangt de `{{placeholders}}` door de waarden van `params` en geeft het resultaat weer.

### Een notificatie sluiten / behouden

```yaml
# Onmiddellijk sluiten
service: peek_it_ha.notify
data:
  action: CLOSE
```

`duration: 0` houdt de notificatie op het scherm tot aan een expliciete `CLOSE` of een druk op een knop.

<details>
<summary><b>Geavanceerde modus — ruwe elementen (volledige JSON)</b></summary>

Voor de gevallen waarin u elke widget handmatig wilt definiëren, zonder via een template te gaan. *In de praktijk doet de Designer dit alles visueel.*

```yaml
service: peek_it_ha.notify
data:
  action: DISPLAY
  duration: 10000
  animationIn: pop
  animationOut: slide_bottom
  elements:
    - type: rect
      style: { left: 60, top: 5, width: 38, height: 30, bgColor: "#DD000000", radius: 12 }
    - type: image
      content: "http://192.168.1.10:8123/local/garden_camera.jpg"
      style: { left: 62, top: 7, width: 34, height: 22 }
    - type: text
      content: "Tuincamera"
      style: { left: 62, top: 28, width: 34, height: 5, size: 18, color: "#FFFFFF", align: center }
```

De volledige woordenschat (widgettypes, stijleigenschappen) wordt gedocumenteerd in de [Geavanceerde referentie](#-geavanceerde-referentie).
</details>

---

## 🔔 Spraaksynthese (TTS)

Laat de TV spreken, alleen of als begeleiding bij een notificatie.

```yaml
# Zelfstandige TTS
service: peek_it_ha.tts
data:
  text: "Het diner is klaar!"
  lang: "nl"
  speed: 1.0     # 0.5 tot 2.0
  volume: 1.0    # 0.0 tot 1.0
```

```yaml
# TTS met visuele notificatie
service: peek_it_ha.notify
data:
  message: "Beweging gedetecteerd in de tuin"
  title: "Beveiliging"
  tts: "Beweging gedetecteerd in de tuin"
  ttsLang: "nl"
  ttsSpeed: 1.25
```

Het afspelen stoppen: `service: peek_it_ha.tts_stop`. In `notify` worden de velden voorafgegaan door `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

## 🔊 Geluid

```yaml
service: peek_it_ha.notify
data:
  message: "Pakket bezorgd"
  sound: "01_notify.wav"
  soundVolume: 0.8   # 0.0 tot 1.0
```

De app wordt geleverd met ingebouwde geluiden en accepteert uw eigen geluiden (via de Designer).

---

## 📺 Configuratieknoppen (ADB)

De integratie stelt **6 knoppen** beschikbaar (categorie *Config*) die de TV besturen via **ADB over TCP**, om met één klik permissies te regelen die lastig zijn om met de afstandsbediening in te schakelen:

| Knop | Actie op de TV |
|--------|------------------|
| **Enable / Disable Assist** | Stelt Peek-it in als standaardassistent / herstelt deze |
| **Enable / Disable Overlay** | Verleent / trekt de permissie `SYSTEM_ALERT_WINDOW` in |
| **Enable / Disable Accessibility** | Schakelt de toegankelijkheidsservice `MenuKeyService` in / uit |

<details>
<summary>ADB-vereisten (eenmalig te doen)</summary>

De knoppen gebruiken de bibliotheek `adb-shell` (automatisch geïnstalleerd door HA) en maken verbinding met het IP van de TV op **poort 5555**.

1. **Schakel netwerk-ADB-debugging in**: *Instellingen → Apparaatvoorkeuren → Over →* tik 7 keer op *Versie*, vervolgens *Ontwikkelaarsopties →* **USB-foutopsporing** (en **Draadloze foutopsporing** indien aangeboden).
2. **Autoriseer de RSA-sleutel bij de eerste druk**: een venster « Foutopsporing toestaan? » verschijnt op de TV → vink *Altijd toestaan* aan. De sleutel wordt één keer gegenereerd en opgeslagen in `.storage/peek_it_adb_key`.
3. De officiële **Android TV**-integratie wordt aanbevolen (HA meldt dit in *Reparaties*) voor een stabiel ADB-beheer.

Als `adb-shell` ontbreekt of als de TV de verbinding weigert, mislukt de actie met een fout in het HA-logboek.
</details>

---

## 🤖 Automatiseringen

### Bewegingsmelding met camera

```yaml
automation:
  - alias: "Bewegingsmelding tuin"
    trigger:
      - platform: state
        entity_id: binary_sensor.garden_motion
        to: "on"
    action:
      - service: peek_it_ha.notify
        data:
          template_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
          params:
            title: "Beweging gedetecteerd!"
            camera_url: "rtsp://192.168.1.50:554/stream1"
          duration: 15000
          animationIn: slide_right
```

### Ochtendweerbericht

```yaml
automation:
  - alias: "Ochtendweer"
    trigger:
      - platform: time
        at: "07:30:00"
    condition:
      - condition: state
        entity_id: binary_sensor.living_room_tv_status
        state: "on"
    action:
      - service: peek_it_ha.notify
        data:
          message: "{{ states('weather.home') }} — {{ state_attr('weather.home', 'temperature') }}°C"
          title: "Weer van vandaag"
```

### Terugkoppeling van een knop naar HA

Een druk op een notificatieknop (afstandsbediening) activeert een HA-gebeurtenis:

```yaml
automation:
  - alias: "TV-knop - Lichten uitdoen"
    trigger:
      - platform: event
        event_type: peekit_button_press
        event_data:
          action: "lights_off"
    action:
      - service: light.turn_off
        target:
          area_id: living_room
```

<details>
<summary>Persistente melding met sluitknop (ruwe JSON)</summary>

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  animationIn: pop
  priority: urgent
  tts: "Let op! Waterlek gedetecteerd!"
  ttsLang: "nl"
  elements:
    - type: rect
      style: { left: 20, top: 20, width: 60, height: 60, bgColor: "#EE990000", radius: 20 }
    - type: text
      content: "WATERLEK GEDETECTEERD"
      style: { left: 25, top: 30, width: 50, height: 10, size: 40, color: "#FFFFFF", weight: bold, align: center }
    - type: button
      content: "Begrepen"
      action: CLOSE
      focusable: true
      directFocus: true
      style: { left: 35, top: 55, width: 30, height: 10, size: 24, color: "#FFFFFF", bgColor: "#CC333333", align: center, radius: 10, focusColor: "#FF6666", focusBgColor: "#CC660000" }
```
</details>

<details>
<summary>RTSP-camerastream</summary>

```yaml
service: peek_it_ha.notify
data:
  duration: 20000
  animationIn: slide_right
  elements:
    - type: video
      content: "rtsp://192.168.1.50:554/stream1"
      style: { left: 65, top: 5, width: 30, height: 25, radius: 8 }
```

Ultralage latentie (~50 ms) dankzij een geoptimaliseerde ExoPlayer-configuratie.
</details>

---

## 🧰 Geavanceerde referentie

> 🛟 **Normaal gezien hebt u deze sectie niet nodig.** De Designer bouwt uw notificaties visueel op en levert u kant-en-klare templates. Wat volgt is alleen nuttig voor de ruwe JSON-modus, de API of integraties van derden.

<details>
<summary><b>Parameters van de service <code>notify</code></b></summary>

| Parameter | Type | Standaard | Beschrijving |
|-----------|------|--------|-------------|
| `action` | string | `DISPLAY` | `DISPLAY` om weer te geven, `CLOSE` om te sluiten |
| `duration` | int | `10000` | Duur in ms (0 = oneindig) |
| `priority` | string | `normal` | `normal` of `urgent` |
| `animationIn` / `animationOut` | string | `fade` | Zie animaties hieronder |
| `template_id` | string | — | UUID van de te gebruiken template |
| `params` | dict | — | Dynamische waarden van de template |
| `elements` | list | — | Lijst van widgets (ruwe JSON-modus) |
| `message` / `title` | string | — | Eenvoudige berichtmodus |
| `sound` / `soundVolume` | string / float | — / `1.0` | Geluid en volume (0.0-1.0) |
| `tts` / `ttsLang` / `ttsSpeed` / `ttsPitch` / `ttsVolume` | — | — | TTS afgespeeld met de notificatie |

**Animaties**: `none`, `fade`, `slide_right`, `slide_left`, `slide_top`, `slide_bottom`, `pop` (in- en uitgang onafhankelijk).
</details>

<details>
<summary><b>Widgettypes</b></summary>

Het type wordt geïnterpreteerd door de app. **Elk niet-herkend type (`text`, `message`, `title`, `button`…) wordt weergegeven als een tekstwidget**; een `button` onderscheidt zich door `focusable` + `action`. Als `content` begint met `mdi:` (bijv. `mdi:home-assistant`), wordt een **Material Design Icons-icoon** weergegeven.

| Type | Beschrijving | `content` |
|------|-------------|-----------|
| `text` | Statische tekst (standaardtype) | De tekst, of `mdi:<icoon>` |
| `button` | Interactieve tekst (focusable, action) | Label |
| `rect` | Rechthoek / container | — |
| `ellipse` | Ellips / ovaal | — |
| `hexagon` | Zeshoek | — |
| `circle` | Ronde container (afbeelding / MDI-icoon) | URL of `mdi:<icoon>` |
| `image` | PNG/JPG-afbeelding | URL |
| `video` | RTSP- / HTTP-stream | URL |
| `webview` | Ingebedde webpagina | URL |
| `svg` | Vectorafbeelding | URL of pad |
| `line` / `arrow` | Lijn / pijl | — |
| `confetti` | Confetti-animatie op volledig scherm | — |
| `menu` | Interactief D-pad-menu | JSON MenuConfig |

> De oude voorbeelden met `type: box` worden nog steeds weergegeven (tekst-fallback + `bgColor`), maar het canonieke type voor de rechthoek is `rect`.
</details>

<details>
<summary><b>Stijl- en interactie-eigenschappen</b></summary>

**Stijl**: `left`, `top`, `width`, `height` (in % van het scherm, 0-100) · `color` · `bgColor` (hex met alpha) · `size` · `font` · `weight` (`normal`/`bold`) · `align` (`left`/`center`/`right`) · `opacity` · `radius` · `borderWidth` · `borderColor` · `rotation` · `focusColor` · `focusBgColor`.

**Interactie (knoppen)**: `focusable` (krijgt de focus van de afstandsbediening) · `directFocus` (focus bij weergave) · `action` (`CLOSE` of aangepaste ID voor de webhook) · `paramKey` (koppelt de inhoud aan een templateparameter) · `actionParamKey` (koppelt de actie aan een parameter).
</details>

<details>
<summary><b>Interactief menu (JSON-config)</b></summary>

De widget `menu` creëert een overlay-menu dat navigeerbaar is met de D-pad (submenu's, schakelaars voor HA-entiteiten, acties).

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Snelle bediening",
          "items": [
            {"type": "submenu", "label": "Lichten", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Woonkamer", "entity_id": "light.living_room"},
              {"type": "close", "label": "Terug"}
            ]},
            {"type": "action", "label": "Bioscoopmodus", "action": "movie_mode"},
            {"type": "close", "label": "Sluiten"}
          ]
        }
      style: { left: 35, top: 10, width: 30, height: 80 }
```

| Type element | Rol |
|------|-------------|
| `action` | Activeert `peekit_button_press` met de ID `action` |
| `submenu` | Opent een submenu (`children`) |
| `toggle` | Schakelt een HA-entiteit (`entity_id`), status om de 5 s vernieuwd |
| `text` | Informatieve tekst |
| `close` | Sluit het menu |

**Navigatie**: Omhoog/Omlaag navigeren · Rechts/Enter een submenu openen · Links/Terug teruggaan · Terug naar de root sluit.
</details>

<details>
<summary><b>HA-entiteitwidgets, grafieken & overlays (app-mogelijkheden)</b></summary>

Deze functies worden geconfigureerd aan de kant van de **app** (Designer); de HA-integratie bestuurt ze niet rechtstreeks. Ze vereisen een **langlevend toegangstoken (Long-Lived Access Token) van HA** dat in de Designer is ingevoerd (zie [De Designer](#-de-designer)), want de app roept de API van HA rechtstreeks aan.

- **HA-entiteitwidget**: een `webview` verbonden via WebSocket/REST geeft de status van entiteiten in realtime weer.
- **HA-grafieken**: vlak / lijn / staven, weergegeven in pure CSS/SVG.
- **Klok als overlay** (`/api/config/clock`): formaat 12 u/24 u, positie, kleur, opaciteit.
- **Verduistering** (`/api/config/dimming`): kleur en opaciteit van een achtergrondlaag.
</details>

<details>
<summary><b>API & webhook (voor Tasker, Node-RED, Jeedom, ontwikkelaars)</b></summary>

De app stelt een lokale HTTP-API beschikbaar (poort `8081`). Als een API-sleutel is geconfigureerd, dragen **alle** verzoeken de header `X-API-Key: <sleutel>`. Het is deze API die elke HTTP-client (Tasker, Node-RED, Jeedom…) kan aanroepen.

| Endpoint | Methode | Gebruik |
|---|---|---|
| `/api/status` | GET | Status, permissies, resolutie |
| `/api/notify` | POST | Een notificatie weergeven / sluiten |
| `/api/tts` · `/api/tts/stop` | POST | Spraaksynthese |
| `/api/templates/list` | GET | Lijst van templates |

**Antwoord van `/api/status`**:
```json
{
  "status": "online", "version": "v10.9", "device_name": "Living Room TV",
  "api_key_required": false, "api_key_valid": true,
  "screen": { "width": 1920, "height": 1080, "density": 1.0 },
  "permissions": { "overlay": true, "accessibility": false, "microphone": true }
}
```

**Webhook (terugkoppeling van de TV → HA)**: `/api/webhook/peek_it_debug`. Sinds 1.1.0 moet elk verzoek de header **`X-Peek-Secret`** presenteren (anders HTTP 401). Het secret wordt naar de TV doorgegeven via de **welkomstnotificatie** (veld `webhook_secret`) bij het aanmaken/opslaan van het item.

| `level` | `message` | HA-effect |
|---------|-----------|----------|
| `ACTION` | `BUTTON_CLICK:<id>` | Verzendt de gebeurtenis `peekit_button_press` `{ "action": "<id>" }` |
| `ERROR` / `WARN` / `INFO` | tekst | Gelogd als `[PEEK-IT REPORT]` |

> **Migratie vanaf 1.0.0**: *Configureren → Instellingen → Valideren* om een nieuwe welkomstnotificatie met het `webhook_secret` te versturen.
</details>

---

## 🌍 Multi-apparaat & talen

Voeg elke TV toe als een aparte integratie. De services `notify`, `tts`, `tts_stop` en `get_templates` zijn van toepassing op **alle apparaten**. Om één enkele TV aan te sturen:

```yaml
service: notify.send_message
target:
  entity_id: notify.tv_du_salon
data:
  message: "Alleen op deze TV"
```

De integratie en de app zijn beschikbaar in **6 talen**: `en` (standaard), `fr`, `de`, `es`, `nl`, `pt`. Configureerbaar in de Designer of de app.

---

## 😅 WAF — De ultieme KPI

De legendarische **WAF** — *Wife Acceptance Factor*. Die niet-officiële maar absoluut cruciale metriek die de tolerantie van uw wederhelft tegenover uw domotica-experimenten meet.

- 🧺 **Slim wasgoed**: « Was klaar! » verschijnt discreet tijdens de film. Geen drie dagen lang vergeten wasbeurten meer. *(WAF: +23)*
- ☀️ **Ochtendweer**: elke dag om 7.30 uur, het weer op de TV van de keuken. *(WAF: +15)*
- 🔔 **Deurbelcamera**: er wordt aangebeld, de stream verschijnt. Beraadslaging vanaf de bank. Niemand is opgestaan. *(WAF: +38)*
- ⚽ **Sportuitslag**: een discreet « 2 - 1, 78' » 3 seconden in de hoek. Niemand heeft van zender gewisseld. *(WAF: +52)*

### Het geval dat uw WAF RUÏNEERT

🌙 **Foutopsporing in productie**: u test uw notificaties om 23 uur tijdens de grote seizoensfinale. « Test 1 », « Lorem ipsum », « AAAA HET WERKT! », een grote zwarte rechthoek, en dan niets meer...

> *(WAF: -347. Geschat herstel: 3 weken goed gedrag. En een boeket bloemen.)*

**Pro-tip**: test VÓÓR 21 uur. Of gebruik de **KILL**-knop van de Designer. Die bestaat niet voor niets.

---

## 🔧 Probleemoplossing

| Probleem | Oplossing |
|----------|----------|
| Integratie niet te vinden | Map in `custom_components/peek_it_ha/`? Herstart HA. |
| « Kan geen verbinding maken » | Controleer IP/poort. Test `http://IP:8081/api/status` in een browser. |
| Sensor altijd « offline » | Draait de app? Start de service bij het opstarten? |
| De notificatie verschijnt niet | Controleer de overlay-permissie in de Android TV-instellingen. |
| De Designer maakt geen verbinding | Zelfde netwerk? Probeer `http://IP:PORT/`. |
| De TV-knop activeert HA niet | Terugkoppeling TV → HA = webhook: sla de *Instellingen* van de integratie opnieuw op (geeft het `webhook_secret` door) en controleer of `ha_ip` bereikbaar is vanaf de TV. |
| De menuschakelaars / entiteitwidgets werken niet | Rechtstreekse aanroep app → HA: maak een **langlevend toegangstoken (Long-Lived Access Token)** van HA aan en plak het in de Designer (zie [De Designer](#-de-designer)). |
| De ADB-knoppen mislukken | ADB-debugging (poort 5555) ingeschakeld en RSA-sleutel geautoriseerd? Zie [ADB-knoppen](#-configuratieknoppen-adb). |
| De TTS spreekt niet | Is er een TTS-engine geïnstalleerd op de Android TV (Google TTS)? |
| Het menu reageert niet op de D-pad | Het menu-element moet de focus hebben; gebruik `duration: 0`. |

---

## Bijdragen

Bijdragen zijn welkom! Open een issue of een pull request op de [GitHub-repository](https://github.com/jolabs40/peek-it-ha).

## Licentie

Project gedistribueerd onder de MIT-licentie. Zie het bestand [LICENSE](LICENSE).

---

<p align="center">
  Gemaakt met koffie, veel te veel YAML-bestanden, en een onredelijke liefde voor overlays.<br/>
  <strong>Peek-it [HA]</strong> — omdat uw TV veel meer kan dan u denkt.
</p>
