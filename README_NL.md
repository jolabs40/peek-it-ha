# Peek-it [HA] — Home Assistant-integratie

<p align="center">
  <img src="custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Maak van je Android TV een slim notificatiescherm.</strong><br/>
  Meldingen, camera's, dashboards, TTS, menu's — overlay op je TV in realtime.
</p>

<p align="center">
  <a href="https://github.com/jolabs40/peek-it-ha/releases"><img src="https://img.shields.io/github/v/release/jolabs40/peek-it-ha?style=for-the-badge&color=blue&label=Release" alt="Release"/></a>
  <a href="https://github.com/jolabs40/peek-it-ha"><img src="https://img.shields.io/github/stars/jolabs40/peek-it-ha?style=for-the-badge&color=yellow" alt="Stars"/></a>
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/LICENSE"><img src="https://img.shields.io/github/license/jolabs40/peek-it-ha?style=for-the-badge&color=green" alt="License"/></a>
  <a href="https://github.com/hacs/integration"><img src="https://img.shields.io/badge/HACS-Custom-orange?style=for-the-badge" alt="HACS"/></a>
  <img src="https://img.shields.io/badge/Android%20TV-Compatible-brightgreen?style=for-the-badge&logo=android" alt="Android TV"/>
  <img src="https://img.shields.io/badge/Home%20Assistant-Integration-41BDF5?style=for-the-badge&logo=homeassistant&logoColor=white" alt="Home Assistant"/>
</p>

<p align="center">
  <a href="#-installatie">Installatie</a> •
  <a href="#-gebruik">Gebruik</a> •
  <a href="#-de-designer">Designer</a> •
  <a href="#-templates--parameters">Templates</a> •
  <a href="#-tekst-naar-spraak-tts">TTS</a> •
  <a href="#-geluid">Geluid</a> •
  <a href="#-interactief-menu">Menu</a> •
  <a href="#-automatiseringen">Automatiseringen</a> •
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

Je Android TV-apparaat is 24/7 aangesloten op je TV. Waarom er niet meer mee doen?

**Peek-it [HA]** is de Home Assistant-integratie voor de **Peek-it [TV]** Android-app. Samen tonen ze **rijke overlay-notificaties** bovenop elke draaiende applicatie. Film aan het kijken? Een camerabeeld verschijnt 5 seconden in de hoek. Sportavond? De score wordt in realtime bijgewerkt. Deurbel gaat? De voordeurcamera verschijnt direct.

### Wat kun je weergeven

| Type | Voorbeeld |
|------|-----------|
| **Rijke tekst** | Titels, berichten, tellers, weer |
| **Afbeeldingen** | Foto's, snapshots, logo's, QR-codes |
| **RTSP-videostreams** | Live beveiligingscamera's, ultrakorte latentie |
| **Webpagina's** | HA-dashboards, grafieken, weerwidgets |
| **SVG** | Vectoriconen, meters, diagrammen |
| **Vormen** | Rechthoeken, ellipsen, lijnen, pijlen — bouw complete lay-outs |
| **Interactieve knoppen** | Bedienbaar met de TV-afstandsbediening, activeer HA-automatiseringen |
| **Interactieve menu's** | D-pad-navigeerbare menu's met HA-entiteitschakelaars |
| **HA-entiteitwidgets** | Realtime entiteitsstatus via WebSocket/REST |
| **HA-grafieken** | CSS/SVG vlak-, lijn- en staafdiagrammen |
| **Tekst-naar-spraak** | Spraakberichten op je TV |

### Belangrijkste functies

- **Geen latentie** — native Android-overlay, geen streaming of casting
- **Werkt met alles** — de overlay verschijnt bovenop elke app
- **Visuele Designer** — maak notificaties met drag & drop vanuit elke browser
- **Herbruikbare templates** — ontwerp eenmalig, hergebruik met dynamische parameters
- **7 animaties** — fade, slide, pop... onafhankelijke in- en uitgangseffecten
- **Tekst-naar-spraak** — spraakberichten rechtstreeks op de TV
- **Geluidswaarschuwingen** — speel notificatiegeluiden af bij visuele meldingen
- **Interactieve menu's** — D-pad-navigeerbare overlay-menu's met HA-schakelaars
- **Multi-apparaat** — beheer meerdere TV's vanuit een enkele HA-instantie
- **6 talen** — EN, FR, DE, ES, NL, PT

---

## Vereisten

1. **Een Android TV-apparaat** met de **Peek-it [TV]**-app
2. **Home Assistant** geinstalleerd en actief
3. Beide apparaten op **hetzelfde lokale netwerk**

### Installeer de Peek-it [TV]-app

> De app staat (nog) niet in de Play Store. Installeer via sideload.

1. Download de APK van de [Releases-pagina](https://github.com/jolabs40/peek-it-ha/releases)
2. Zet het bestand over naar je apparaat (USB-stick, `adb install`, of een bestandsbeheer-app)
3. Start de app — deze vraagt de overlay-toestemming aan (weergave over andere apps)
4. Verleen de toestemming — de service start automatisch
5. Noteer het **IP-adres** dat op het hoofdscherm wordt getoond (bijv. `192.168.1.42`)
6. Standaardpoort is **8081** (configureerbaar in de app)

> **Tip**: De service start automatisch bij het opstarten van het apparaat. Aansluiten en vergeten.

---

## Installatie

### Methode 1: HACS (aanbevolen)

1. Open HACS in Home Assistant
2. Ga naar **Integraties** > 3-puntenmenu > **Aangepaste repositories**
3. Voeg de repository-URL toe: `https://github.com/jolabs40/peek-it-ha`
4. Categorie: **Integratie**
5. Klik op **Peek-it [HA]** > **Downloaden**
6. **Herstart Home Assistant**

### Methode 2: Handmatige installatie

1. Kopieer de map `peek_it_ha/` naar je `custom_components/`-directory:
   ```
   config/
   └── custom_components/
       └── peek_it_ha/
           ├── __init__.py
           ├── config_flow.py
           ├── const.py
           ├── manifest.json
           ├── notify.py
           ├── binary_sensor.py
           ├── services.yaml
           ├── strings.json
           ├── translations/
           │   ├── en.json
           │   ├── fr.json
           │   ├── de.json
           │   ├── es.json
           │   ├── nl.json
           │   └── pt.json
           ├── icon.png
           ├── icon@2x.png
           ├── logo.png
           └── logo@2x.png
   ```
2. **Herstart Home Assistant**

### De integratie toevoegen

1. Ga naar **Instellingen** > **Apparaten & Services** > **Integratie toevoegen**
2. Zoek naar **Peek-it [HA]**
3. Vul in:
   - **IP-adres**: het IP-adres van je Android TV-apparaat (getoond in de app)
   - **Poort**: `8081` (standaard)
   - **Naam**: een beschrijvende naam voor je TV (bijv. "Woonkamer TV")
   - **API Key**: als authenticatie is ingeschakeld op de TV-app
4. Bevestig — de integratie test de verbinding en configureert zichzelf

### Wat automatisch wordt aangemaakt

| Entiteit | Type | Beschrijving |
|----------|------|--------------|
| `binary_sensor.living_room_tv_status` | Binary Sensor | Verbindingsstatus (online/offline), pollt elke 30s |
| `notify.living_room_tv` | Notify | Entiteit voor het versturen van notificaties |

De `binary_sensor` bevat ook een `designer_url`-attribuut met een directe link naar de web-Designer.

---

## Integratie-opties (tandwielicoon)

Klik op het **tandwielicoon** op de Peek-it [HA]-integratiekaart om 3 menu's te openen:

### Instellingen

Bewerk het IP-adres, de poort, naam of API key. De integratie herlaadt automatisch na het opslaan.

### Templates

Bekijk alle beschikbare templates op je TV, gesorteerd per categorie:

- **Official** — ingebouwde templates die met de app worden meegeleverd
- **Custom** — je afgeronde templates, elk met een unieke UUID
- **Drafts** — werk in uitvoering, nog geen ID toegewezen

Elke template toont de **naam**, het **ID** (kopieerbaar) en de beschikbare **parameters**.

### Designer

Directe link om de web-Designer in een nieuw tabblad te openen. Handig om templates te bewerken zonder HA te verlaten.

---

## Gebruik

### Modus 1: Eenvoudig bericht

De snelste manier — stuur een tekstbericht dat onderaan het scherm verschijnt met een donkere achtergrond.

```yaml
service: peek_it_ha.notify
data:
  message: "De wasmachine is klaar!"
  title: "Thuis"
  duration: 8000
```

### Modus 2: Template + parameters

De meest praktische manier — hergebruik een bestaand template door dynamische waarden in te vullen.

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

De server laadt het template, vervangt `{{placeholders}}` door `params`-waarden en toont het resultaat.

**Hoe vind je de template_id?**
- In de Designer: klik op het groene "ID"-badge bij een template in de bibliotheek
- In HA: tandwielicoon > Templates > kopieer het getoonde ID
- Via service: `peek_it_ha.get_templates` retourneert de volledige lijst

### Modus 3: Ruwe elementen (volledig JSON)

De meest flexibele manier — definieer elke widget handmatig.

```yaml
service: peek_it_ha.notify
data:
  action: DISPLAY
  duration: 10000
  animationIn: pop
  animationOut: slide_bottom
  elements:
    - type: box
      style:
        left: 60
        top: 5
        width: 38
        height: 30
        bgColor: "#DD000000"
        radius: 12
    - type: image
      content: "http://192.168.1.10:8123/local/garden_camera.jpg"
      style:
        left: 62
        top: 7
        width: 34
        height: 22
    - type: text
      content: "Tuincamera"
      style:
        left: 62
        top: 28
        width: 34
        height: 5
        size: 18
        color: "#FFFFFF"
        align: center
```

### Een notificatie sluiten

```yaml
service: peek_it_ha.notify
data:
  action: CLOSE
```

### Permanente (oneindige) notificatie

```yaml
service: peek_it_ha.notify
data:
  message: "Wachten op bevestiging..."
  duration: 0
```

Duur `0` = de notificatie blijft op het scherm tot een expliciete `CLOSE` of een knopdruk.

---

## Tekst-naar-spraak (TTS)

### Zelfstandige TTS

Stuur een spraakbericht naar alle geconfigureerde TV's:

```yaml
service: peek_it_ha.tts
data:
  text: "Het eten is klaar!"
  lang: "nl"
  speed: 1.0
  pitch: 1.0
  volume: 1.0
```

### TTS stoppen

```yaml
service: peek_it_ha.tts_stop
```

### TTS met notificatie

Combineer een visuele notificatie met een spraakbericht:

```yaml
service: peek_it_ha.notify
data:
  message: "Beweging gedetecteerd in de tuin"
  title: "Beveiliging"
  duration: 10000
  tts: "Beweging gedetecteerd in de tuin"
  ttsLang: "nl"
  ttsSpeed: 1.25
  ttsVolume: 0.8
```

### TTS-parameters

| Parameter | Type | Standaard | Beschrijving |
|-----------|------|-----------|--------------|
| `text` | string | — | Tekst om voor te lezen (zelfstandige service) |
| `lang` | string | `en` | Taalcode (en, fr, de, es, nl, pt) |
| `speed` | float | `1.0` | Spraaksnelheid (0,5 tot 2,0) |
| `pitch` | float | `1.0` | Stemtoonhoogte (0,5 tot 2,0) |
| `volume` | float | `1.0` | Volume (0,0 tot 1,0) |

Bij gebruik binnen `peek_it_ha.notify` worden de velden voorafgegaan door: `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

---

## Geluid

Speel een geluid af bij je notificatie:

```yaml
service: peek_it_ha.notify
data:
  message: "Pakket bezorgd"
  title: "Deurbel"
  sound: "01_notify.wav"
  soundVolume: 0.8
```

| Parameter | Type | Standaard | Beschrijving |
|-----------|------|-----------|--------------|
| `sound` | string | — | Naam van het geluidsbestand (bijv. "01_notify.wav") |
| `soundVolume` | float | `1.0` | Volume (0,0 tot 1,0) |

De Peek-it [TV]-app wordt geleverd met ingebouwde geluiden en ondersteunt aangepaste geluiden via de Designer.

---

## Interactief menu

Het widgettype `menu` maakt een D-pad-navigeerbaar overlay-menu op de TV. Menu's ondersteunen submenu's, HA-entiteitsschakelaars met realtime statuspolling, actiecallbacks en sluitknoppen.

### Menuvoorbeeld via automatisering

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Snelle bediening",
          "titleIcon": "mdi:menu",
          "bgColor": "#1E1E1E",
          "textColor": "#FFFFFF",
          "accentColor": "#00E676",
          "items": [
            {"type": "submenu", "label": "Verlichting", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Woonkamer", "icon": "mdi:lightbulb", "entity_id": "light.living_room"},
              {"type": "toggle", "label": "Keuken", "icon": "mdi:lightbulb", "entity_id": "light.kitchen"},
              {"type": "close", "label": "Terug", "icon": "mdi:arrow-left"}
            ]},
            {"type": "action", "label": "Filmmodus", "icon": "mdi:movie", "action": "movie_mode"},
            {"type": "close", "label": "Sluiten", "icon": "mdi:close"}
          ]
        }
      style:
        left: 35
        top: 10
        width: 30
        height: 80
```

### Menu-itemtypes

| Type | Beschrijving |
|------|--------------|
| `action` | Triggert een HA-event (`peekit_button_press`) met het opgegeven `action`-ID |
| `submenu` | Opent een genest submenu met eigen `children`-items |
| `toggle` | Schakelt een HA-entiteit (vereist `entity_id`), pollt status elke 5s |
| `text` | Informatieve tekst (niet-interactief) |
| `close` | Sluit het menu |

### Navigatie

- **Omhoog/Omlaag**: navigeer tussen items
- **Rechts/Enter**: open een submenu
- **Links/Terug**: ga terug naar het bovenliggende menu
- **Terug op hoofdniveau**: sluit het menu

---

## HA-entiteitwidget

Geef realtime HA-entiteitsstatussen weer op de TV met een `webview`-widget die is verbonden via WebSocket of REST-polling.

```yaml
service: peek_it_ha.notify
data:
  duration: 30000
  elements:
    - type: webview
      content: "http://192.168.1.10:8123/lovelace/overview"
      style:
        left: 5
        top: 5
        width: 90
        height: 90
```

---

## HA-grafiekwidget

De Peek-it [TV]-app ondersteunt CSS/SVG-grafieken voor het weergeven van entiteitsgeschiedenis. Grafiektypes: **vlak**, **lijn** en **staaf**.

Grafieken worden weergegeven als pure CSS/SVG — geen externe bibliotheken nodig. Configureer ze via de grafiekeditor in de Designer.

---

## Overlay-configuratie

### Klok-overlay

De Peek-it [TV]-app kan een permanente klok-overlay weergeven. Configureer via de Designer-instellingen of het `/api/config/clock`-endpoint:

- In-/uitschakelen
- Formaat (12u/24u)
- Positie, kleur, grootte, transparantie

### Dimming-overlay

Een configureerbare achtergrondverdunsteringslaag. Configureer via de Designer-instellingen of `/api/config/dimming`:

- In-/uitschakelen
- Kleur, transparantie

---

## Beschikbare parameters

### Hoofdvelden

| Parameter | Type | Standaard | Beschrijving |
|-----------|------|-----------|--------------|
| `action` | string | `DISPLAY` | `DISPLAY` om te tonen, `CLOSE` om te sluiten |
| `duration` | int | `10000` | Duur in milliseconden (0 = oneindig) |
| `priority` | string | `normal` | `normal` of `urgent` |
| `animationIn` | string | `fade` | Ingangsanimatie |
| `animationOut` | string | `fade` | Uitgangsanimatie |
| `template_id` | string | — | UUID van het te gebruiken template |
| `params` | dict | — | Dynamische templateparameters |
| `elements` | list | — | Widgetlijst (geavanceerde modus) |
| `message` | string | — | Eenvoudige tekst (eenvoudige modus) |
| `title` | string | — | Titeltekst (eenvoudige modus) |
| `sound` | string | — | Naam van het geluidsbestand |
| `soundVolume` | float | `1.0` | Geluidsvolume (0,0-1,0) |
| `tts` | string | — | TTS-tekst (wordt voorgelezen bij notificatie) |
| `ttsLang` | string | `en` | TTS-taalcode |
| `ttsSpeed` | float | `1.0` | TTS-spraaksnelheid (0,5-2,0) |
| `ttsPitch` | float | `1.0` | TTS-stemtoonhoogte (0,5-2,0) |
| `ttsVolume` | float | `1.0` | TTS-volume (0,0-1,0) |

### Beschikbare animaties

| Naam | Effect |
|------|--------|
| `none` | Direct, geen animatie |
| `fade` | Vervagen in/uit |
| `slide_right` | Schuiven van/naar rechts |
| `slide_left` | Schuiven van/naar links |
| `slide_top` | Schuiven van/naar boven |
| `slide_bottom` | Schuiven van/naar beneden |
| `pop` | Zoom-/schaaleffect |

### Widgettypes

| Type | Beschrijving | Inhoud (`content`) |
|------|--------------|---------------------|
| `text` | Statische tekst | De weer te geven tekst |
| `button` | Interactieve knop (TV-afstandsbediening) | Knoplabel |
| `box` | Rechthoek / container | — |
| `circle` | Cirkel | — |
| `ellipse` | Ellips / ovaal | — |
| `image` | Afbeelding (PNG, JPG, URL) | Afbeeldings-URL |
| `video` | RTSP / HTTP-videostream | Stream-URL |
| `webview` | Ingebedde webpagina | Pagina-URL |
| `svg` | SVG-vectorafbeelding | URL of SVG-pad |
| `line` | Horizontale lijn | — |
| `arrow` | Pijl (naar rechts wijzend) | — |
| `menu` | Interactief D-pad-menu | JSON MenuConfig |

### Stijleigenschappen

| Eigenschap | Type | Beschrijving |
|------------|------|--------------|
| `left` | float | X-positie in % van het scherm (0-100) |
| `top` | float | Y-positie in % van het scherm (0-100) |
| `width` | float | Breedte in % van het scherm |
| `height` | float | Hoogte in % van het scherm |
| `color` | string | Tekstkleur (hex, bijv. `#FFFFFF`) |
| `bgColor` | string | Achtergrondkleur (hex met alpha, bijv. `#CC000000`) |
| `size` | int | Lettergrootte |
| `font` | string | Lettertype (Roboto, sans-serif, etc.) |
| `weight` | string | Lettergewicht (`normal`, `bold`) |
| `align` | string | Uitlijning (`left`, `center`, `right`) |
| `opacity` | float | Transparantie (0,0 tot 1,0) |
| `radius` | int | Hoekradius (pixels) |
| `borderWidth` | int | Randdikte (pixels) |
| `borderColor` | string | Randkleur (hex) |
| `rotation` | float | Rotatie in graden |
| `focusColor` | string | Randkleur bij focus |
| `focusBgColor` | string | Achtergrondkleur bij focus |

### Interactie-eigenschappen (knoppen)

| Eigenschap | Type | Beschrijving |
|------------|------|--------------|
| `focusable` | bool | Widget ontvangt TV-afstandsbedieningsfocus |
| `directFocus` | bool | Widget krijgt focus bij weergave |
| `action` | string | `CLOSE` om te sluiten, of aangepast ID voor webhook |
| `paramKey` | string | Koppelt inhoud aan een templateparameter |
| `actionParamKey` | string | Koppelt actie aan een templateparameter |

---

## De Designer

De Designer is een **visuele webeditor** ingebouwd in de Peek-it [TV]-app. Open hem vanuit elke browser op je lokale netwerk.

**URL**: `http://<TV_IP>:<POORT>/` (bijv. `http://192.168.1.42:8081/`)

Je kunt hem ook openen via:
- Het `designer_url`-attribuut van de binary_sensor in HA
- Het tandwielicoon > Designer in de integratie-opties

### Functies

- **11 widgettypes** — drag & drop op een gekalibreerd TV-canvas
- **Realtime JSON-voorbeeld** — bekijk precies de payload die wordt opgebouwd
- **Template-bibliotheek** — opslaan, laden, hernoemen, verwijderen, exporteren/importeren
- **Parametersysteem** — definieer `paramKey` op widgets voor dynamische inhoud
- **Autokalibratie** — past zich aan de werkelijke resolutie van je TV aan (16:9, 21:9, etc.)
- **Geluidsconfiguratie** — standaard notificatiegeluidsinstellingen
- **HA-tokenconfiguratie** — vereist voor webhookcallbacks
- **Internationalisering** — beschikbaar in 6 talen (EN, FR, DE, ES, NL, PT)

### Verzenden en testen

- **SEND-knop** (blauw) — stuurt de huidige lay-out direct naar de TV
- **KILL-knop** (rood) — sluit de huidige notificatie
- **JSON-voorbeeld** (voettekst) — bekijk precies de payload die wordt verstuurd

---

## Templates & parameters

### Concept

Een template is een herbruikbare notificatie-lay-out. In plaats van elke keer 15 regels JSON te versturen:

1. **Maak** de lay-out in de Designer (drag & drop)
2. **Definieer parameters** (`paramKey`) op dynamische elementen
3. **Sla op** als Custom (UUID wordt gegenereerd)
4. **Gebruik** de `template_id` + `params` in je automatiseringen

### De templatelijst ophalen

```yaml
service: peek_it_ha.get_templates
response_variable: result
```

Retourneert een woordenboek per geconfigureerd apparaat:
```json
{
  "Living Room TV": {
    "official": [
      { "filename": "demo.json", "id": "70c3f0c7-...", "params": ["title", "message"] }
    ],
    "custom": [
      { "filename": "camera_alert.json", "id": "a1b2c3d4-...", "params": ["title", "camera_url"] }
    ],
    "draft": ["test_draft.json"]
  }
}
```

---

## Automatiseringen

### Bewegingsdetectiemelding

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
          animationOut: fade
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
          title: "Het weer vandaag"
          duration: 10000
          animationIn: fade
```

### TTS-aankondiging automatisering

```yaml
automation:
  - alias: "Deurbel TTS-melding"
    trigger:
      - platform: state
        entity_id: binary_sensor.doorbell
        to: "on"
    action:
      - service: peek_it_ha.tts
        data:
          text: "Er staat iemand aan de voordeur"
          lang: "nl"
          speed: 1.25
          volume: 1.0
```

### Notificatie met geluid

```yaml
automation:
  - alias: "Wasmachine klaar melding"
    trigger:
      - platform: state
        entity_id: sensor.washing_machine
        to: "idle"
    action:
      - service: peek_it_ha.notify
        data:
          message: "De wasmachine is klaar!"
          title: "Was"
          duration: 8000
          sound: "08-notify.mp3"
          soundVolume: 0.7
```

### Interactieve knoppen — feedback naar HA

Wanneer een gebruiker op een knop drukt in een notificatie (via de TV-afstandsbediening), wordt een HA-event afgevuurd:

```yaml
automation:
  - alias: "TV-knop - Lichten uit"
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

### Permanente melding met sluitknop

```yaml
automation:
  - alias: "Waterlek melding"
    trigger:
      - platform: state
        entity_id: binary_sensor.water_leak
        to: "on"
    action:
      - service: peek_it_ha.notify
        data:
          duration: 0
          animationIn: pop
          priority: urgent
          tts: "Waarschuwing! Waterlek gedetecteerd!"
          ttsLang: "nl"
          elements:
            - type: box
              style:
                left: 20
                top: 20
                width: 60
                height: 60
                bgColor: "#EE990000"
                radius: 20
            - type: text
              content: "WATERLEK GEDETECTEERD"
              style:
                left: 25
                top: 30
                width: 50
                height: 10
                size: 40
                color: "#FFFFFF"
                weight: bold
                align: center
            - type: button
              content: "Begrepen"
              action: CLOSE
              focusable: true
              directFocus: true
              style:
                left: 35
                top: 55
                width: 30
                height: 10
                size: 24
                color: "#FFFFFF"
                bgColor: "#CC333333"
                align: center
                radius: 10
                focusColor: "#FF6666"
                focusBgColor: "#CC660000"
```

### RTSP-camerafeed

```yaml
service: peek_it_ha.notify
data:
  duration: 20000
  animationIn: slide_right
  elements:
    - type: video
      content: "rtsp://192.168.1.50:554/stream1"
      style:
        left: 65
        top: 5
        width: 30
        height: 25
        radius: 8
```

De feed wordt weergegeven met ultrakorte latentie (~50ms) dankzij een geoptimaliseerde ExoPlayer-configuratie.

---

## Services-referentie

| Service | Beschrijving |
|---------|--------------|
| `peek_it_ha.notify` | Verstuur notificatie naar alle geconfigureerde apparaten |
| `peek_it_ha.get_templates` | Haal templatelijst op van alle apparaten |
| `peek_it_ha.tts` | Verstuur TTS naar alle geconfigureerde apparaten |
| `peek_it_ha.tts_stop` | Stop TTS op alle geconfigureerde apparaten |

---

## Webhooks & events

De integratie luistert naar een webhook om logs en knopacties van de TV te ontvangen.

| HA-event | Trigger | Data |
|----------|---------|------|
| `peekit_button_press` | Knopdruk op de TV | `{ "action": "button_id" }` |

TV-logs worden doorgestuurd naar de HA-logger met het voorvoegsel `[PEEK-IT REPORT]`.

---

## Multi-apparaat

De integratie ondersteunt **meerdere apparaten**. Voeg elke TV toe als een aparte integratie. De services `peek_it_ha.notify`, `tts`, `tts_stop` en `get_templates` sturen automatisch naar **alle geconfigureerde apparaten**.

Om een enkel apparaat aan te spreken, gebruik je de specifieke `notify`-entiteit:

```yaml
service: notify.send_message
target:
  entity_id: notify.living_room_tv
data:
  message: "Alleen op deze TV"
```

---

## Internationalisering

De integratie en de Peek-it [TV]-app ondersteunen **6 talen**:

| Code | Taal |
|------|------|
| `en` | Engels (standaard) |
| `fr` | Frans |
| `de` | Duits |
| `es` | Spaans |
| `nl` | Nederlands |
| `pt` | Portugees |

De taal kan worden ingesteld in de Designer-instellingen of op het instellingenscherm van de Peek-it [TV]-app.

---

## WAF — De ultieme KPI

De legendarische **WAF** — *Wife Acceptance Factor*. Die onofficiële maar kritieke maatstaf die meet hoe tolerant je partner is ten opzichte van je domotica-experimenten.

### Toepassingen die je WAF verhogen

**Slimme was**: een "Was is klaar!"-notificatie verschijnt discreet tijdens de film. Nooit meer een vergeten was die drie dagen in de machine ligt te fermenteren.

> *(WAF: +23 punten)*

**Ochtendweer**: elke dag om 07:30 verschijnt het weerbericht op de keuken-TV. Beter dan de wekker, en je hoeft er niet eens naar te vragen.

> *(WAF: +15 punten)*

**Deurbelcamera**: er wordt gebeld, het camerabeeld verschijnt op het scherm. Beoordeling vanaf de bank. Niemand hoefde op te staan. De ultieme Nederlandse oplossing.

> *(WAF: +38 punten)*

**Sportuitslagen**: een discreet "2 - 1, 78'" verschijnt 3 seconden in de rechterbovenhoek. Iedereen blij. Niemand heeft van zender gewisseld.

> *(WAF: +52 punten)*

### De toepassing die je WAF VERNIETIGT

**Debuggen in productie**: je bent om 23:00 uur je notificaties aan het testen terwijl je partner naar de seizoensfinale kijkt.

> *(WAF: -347 punten. Geschatte hersteltijd: 3 weken. Plus bloemen.)*

**Pro tip**: test je automatiseringen VOOR 21:00 uur. Of gebruik de **KILL**-knop in de Designer.

---

## Probleemoplossing

| Probleem | Oplossing |
|----------|----------|
| Integratie niet gevonden in HA | Controleer of de map in `custom_components/peek_it_ha/` staat. Herstart HA. |
| "Kan niet verbinden" bij setup | Controleer het IP-adres en de poort. De app moet draaien op de TV. Test `http://IP:8081/api/status` in een browser. |
| Binary sensor altijd "offline" | Draait de Peek-it [TV]-app? Start de service bij het opstarten? |
| Notificatie verschijnt niet | Controleer de overlay-toestemming in de Android TV-instellingen. |
| Designer maakt geen verbinding | Controleer of je op hetzelfde netwerk zit. Probeer `http://IP:POORT/` in je browser. |
| Lege templates in tandwielmenu | De TV moet aan staan en bereikbaar zijn. Controleer de binary_sensor-status. |
| TV-knop triggert geen HA | Configureer het HA-token in de Designer (tandwielicoon). Controleer of `ha_ip` bereikbaar is vanaf de TV. |
| TTS spreekt niet | Controleer of er een TTS-engine is geinstalleerd op de Android TV (Google TTS is meestal voorgeinstalleerd). |
| Geen geluid bij notificatie | Controleer of het geluidsbestand bestaat (check via Designer-instellingen). Sommige streaming-apps kunnen audiomixing blokkeren. |
| Menu reageert niet op D-pad | Zorg dat het menu-element focus heeft. Stel `duration: 0` in zodat het menu open blijft. |

---

## Bijdragen

Bijdragen zijn welkom! Open een issue of een pull request op de [GitHub-repository](https://github.com/jolabs40/peek-it-ha).

## Licentie

Dit project wordt gedistribueerd onder de MIT-licentie. Zie het [LICENSE](LICENSE)-bestand voor details.

---

<p align="center">
  Gemaakt met koffie, te veel YAML-bestanden en een onredelijke liefde voor overlays.<br/>
  <strong>Peek-it [HA]</strong> — want je TV kan meer dan je denkt.
</p>
