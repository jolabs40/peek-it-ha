# Peek-it [HA] — Home Assistant Integration

<p align="center">
  <img src="custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Verwandeln Sie Ihr Android TV in ein intelligentes Benachrichtigungsdisplay.</strong><br/>
  Warnungen, Kameras, Dashboards, TTS, Menüs — Overlay auf Ihrem Fernseher in Echtzeit.
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
  <a href="#-installation">Installation</a> •
  <a href="#-verwendung">Verwendung</a> •
  <a href="#-der-designer">Designer</a> •
  <a href="#-templates--parameter">Templates</a> •
  <a href="#-text-to-speech-tts">TTS</a> •
  <a href="#-ton">Ton</a> •
  <a href="#-interaktives-menü">Menü</a> •
  <a href="#-automatisierungen">Automatisierungen</a> •
  <a href="#-waf--der-ultimative-kpi">WAF</a>
</p>

<p align="center">
  <b>Sprachen:</b>
  <a href="README.md">English</a> |
  <a href="README_FR.md">Fran&ccedil;ais</a> |
  Deutsch |
  <a href="README_ES.md">Espa&ntilde;ol</a> |
  <a href="README_NL.md">Nederlands</a> |
  <a href="README_PT.md">Portugu&ecirc;s</a>
</p>

---

## Warum Peek-it [HA]?

Ihr Android TV-Gerät ist rund um die Uhr an Ihren Fernseher angeschlossen. Warum nutzen Sie es nicht?

**Peek-it [HA]** ist die Home Assistant Integration für die **Peek-it [TV]** Android-App. Zusammen zeigen sie **reichhaltige Overlay-Benachrichtigungen** über jeder laufenden Anwendung an. Schauen Sie einen Film? Ein Kamerabild erscheint 5 Sekunden lang in der Ecke. Sportabend? Der Spielstand aktualisiert sich in Echtzeit. Es klingelt an der Tür? Das Bild der Haustürkamera erscheint sofort.

### Was Sie anzeigen können

| Typ | Beispiel |
|-----|----------|
| **Formatierter Text** | Titel, Nachrichten, Zähler, Wetter |
| **Bilder** | Fotos, Schnappschüsse, Logos, QR-Codes |
| **RTSP-Videostreams** | Live-Überwachungskameras, ultra-niedrige Latenz |
| **Webseiten** | HA-Dashboards, Diagramme, Wetter-Widgets |
| **SVG** | Vektor-Icons, Anzeigen, Diagramme |
| **Formen** | Rechtecke, Ellipsen, Linien, Pfeile — vollständige Layouts erstellen |
| **Interaktive Schaltflächen** | Über die TV-Fernbedienung steuerbar, HA-Automatisierungen auslösen |
| **Interaktive Menüs** | D-Pad-navigierbare Menüs mit HA-Entity-Schaltern |
| **HA-Entity-Widgets** | Echtzeit-Entity-Status über WebSocket/REST |
| **HA-Diagramme** | CSS/SVG Flächen-, Linien- und Balkendiagramme |
| **Text-to-Speech** | Sprachdurchsagen auf Ihrem Fernseher |

### Hauptmerkmale

- **Keine Latenz** — natives Android-Overlay, kein Streaming oder Casting
- **Funktioniert mit allem** — das Overlay erscheint über jeder App
- **Visueller Designer** — Benachrichtigungen per Drag & Drop in jedem Browser erstellen
- **Wiederverwendbare Templates** — einmal gestalten, mit dynamischen Parametern wiederverwenden
- **7 Animationen** — Fade, Slide, Pop... unabhängige Ein- und Ausgangseffekte
- **Text-to-Speech** — Sprachdurchsagen direkt auf dem Fernseher
- **Ton-Benachrichtigungen** — Benachrichtigungstöne zusammen mit visuellen Anzeigen abspielen
- **Interaktive Menüs** — D-Pad-navigierbare Overlay-Menüs mit HA-Schaltern
- **Multi-Gerät** — mehrere Fernseher von einer einzigen HA-Instanz verwalten
- **6 Sprachen** — EN, FR, DE, ES, NL, PT

---

## Voraussetzungen

1. **Ein Android TV-Gerät** mit der **Peek-it [TV]** App
2. **Home Assistant** installiert und aktiv
3. Beide Geräte im **gleichen lokalen Netzwerk**

### Peek-it [TV] App installieren

> Die App ist (noch) nicht im Play Store verfügbar. Installieren Sie sie per Sideload.

1. Laden Sie die APK von der [Releases-Seite](https://github.com/jolabs40/peek-it-ha/releases) herunter
2. Übertragen Sie sie auf Ihr Gerät (USB-Stick, `adb install` oder eine Dateimanager-App)
3. Starten Sie die App — sie fordert die Overlay-Berechtigung an (Über anderen Apps anzeigen)
4. Erteilen Sie die Berechtigung — der Dienst startet automatisch
5. Notieren Sie die **IP-Adresse** auf dem Hauptbildschirm (z.B. `192.168.1.42`)
6. Standard-Port ist **8081** (in der App konfigurierbar)

> **Tipp**: Der Dienst startet automatisch beim Gerätestart. Einstecken und vergessen.

---

## Installation

### Methode 1: HACS (empfohlen)

1. Öffnen Sie HACS in Home Assistant
2. Gehen Sie zu **Integrationen** > 3-Punkte-Menü > **Benutzerdefinierte Repositories**
3. Fügen Sie die Repository-URL hinzu: `https://github.com/jolabs40/peek-it-ha`
4. Kategorie: **Integration**
5. Klicken Sie auf **Peek-it [HA]** > **Herunterladen**
6. **Home Assistant neu starten**

### Methode 2: Manuelle Installation

1. Kopieren Sie den Ordner `peek_it_ha/` in Ihr Verzeichnis `custom_components/`:
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
2. **Home Assistant neu starten**

### Integration hinzufügen

1. Gehen Sie zu **Einstellungen** > **Geräte & Dienste** > **Integration hinzufügen**
2. Suchen Sie nach **Peek-it [HA]**
3. Füllen Sie aus:
   - **IP-Adresse**: die IP Ihres Android TV-Geräts (in der App angezeigt)
   - **Port**: `8081` (Standard)
   - **Name**: ein sprechender Name für Ihren Fernseher (z.B. "Wohnzimmer TV")
   - **API Key**: falls die Authentifizierung in der TV-App aktiviert ist
4. Bestätigen — die Integration testet die Verbindung und konfiguriert sich selbst

### Was automatisch erstellt wird

| Entity | Typ | Beschreibung |
|--------|-----|--------------|
| `binary_sensor.living_room_tv_status` | Binary Sensor | Verbindungsstatus (online/offline), Abfrage alle 30s |
| `notify.living_room_tv` | Notify | Entity zum Senden von Benachrichtigungen |

Der `binary_sensor` stellt außerdem ein Attribut `designer_url` bereit mit einem direkten Link zum Web-Designer.

---

## Integrationsoptionen (Zahnrad-Symbol)

Klicken Sie auf das **Zahnrad-Symbol** auf der Peek-it [HA] Integrationskarte, um auf 3 Menüs zuzugreifen:

### Einstellungen

IP, Port, Name oder API Key bearbeiten. Die Integration wird nach dem Speichern automatisch neu geladen.

### Templates

Durchsuchen Sie alle auf Ihrem Fernseher verfügbaren Templates, sortiert nach Kategorie:

- **Official** — integrierte Templates, die mit der App ausgeliefert werden
- **Custom** — Ihre fertigen Templates, jeweils mit einer eindeutigen UUID
- **Drafts** — in Arbeit befindliche Entwürfe, noch ohne zugewiesene ID

Jedes Template zeigt seinen **Namen**, seine **ID** (kopierbar) und die verfügbaren **Parameter**.

### Designer

Direkter Link zum Öffnen des Web-Designers in einem neuen Tab. Praktisch zum Bearbeiten von Templates, ohne HA verlassen zu müssen.

---

## Verwendung

### Modus 1: Einfache Nachricht

Der schnellste Weg — senden Sie eine Textnachricht, die am unteren Bildschirmrand mit dunklem Hintergrund erscheint.

```yaml
service: peek_it_ha.notify
data:
  message: "Die Waschmaschine ist fertig!"
  title: "Haushalt"
  duration: 8000
```

### Modus 2: Template + Parameter

Der praktischste Weg — verwenden Sie ein bestehendes Template und injizieren Sie dynamische Werte.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Sicherheitswarnung"
    message: "Bewegung im Garten erkannt"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

Der Server lädt das Template, ersetzt die `{{Platzhalter}}` durch die `params`-Werte und zeigt das Ergebnis an.

**Wie finde ich die template_id?**
- Im Designer: Klicken Sie auf das grüne "ID"-Badge eines Templates in der Bibliothek
- In HA: Zahnrad-Symbol > Templates > die angezeigte ID kopieren
- Per Service: `peek_it_ha.get_templates` gibt die vollständige Liste zurück

### Modus 3: Rohe Elemente (vollständiges JSON)

Der flexibelste Weg — definieren Sie jedes Widget manuell.

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
      content: "Gartenkamera"
      style:
        left: 62
        top: 28
        width: 34
        height: 5
        size: 18
        color: "#FFFFFF"
        align: center
```

### Benachrichtigung schließen

```yaml
service: peek_it_ha.notify
data:
  action: CLOSE
```

### Dauerhafte (unendliche) Benachrichtigung

```yaml
service: peek_it_ha.notify
data:
  message: "Warte auf Bestätigung..."
  duration: 0
```

`duration: 0` = die Benachrichtigung bleibt auf dem Bildschirm, bis ein explizites `CLOSE` oder ein Tastendruck erfolgt.

---

## Text-to-Speech (TTS)

### Eigenständiges TTS

Senden Sie eine Sprachnachricht an alle konfigurierten Fernseher:

```yaml
service: peek_it_ha.tts
data:
  text: "Das Essen ist fertig!"
  lang: "de"
  speed: 1.0
  pitch: 1.0
  volume: 1.0
```

### TTS stoppen

```yaml
service: peek_it_ha.tts_stop
```

### TTS mit Benachrichtigung

Kombinieren Sie eine visuelle Benachrichtigung mit einer Sprachnachricht:

```yaml
service: peek_it_ha.notify
data:
  message: "Bewegung im Garten erkannt"
  title: "Sicherheit"
  duration: 10000
  tts: "Bewegung im Garten erkannt"
  ttsLang: "de"
  ttsSpeed: 1.25
  ttsVolume: 0.8
```

### TTS-Parameter

| Parameter | Typ | Standard | Beschreibung |
|-----------|-----|----------|--------------|
| `text` | string | — | Auszusprechender Text (eigenständiger Service) |
| `lang` | string | `en` | Sprachcode (en, fr, de, es, nl, pt) |
| `speed` | float | `1.0` | Sprechgeschwindigkeit (0.5 bis 2.0) |
| `pitch` | float | `1.0` | Tonhöhe (0.5 bis 2.0) |
| `volume` | float | `1.0` | Lautstärke (0.0 bis 1.0) |

Bei Verwendung innerhalb von `peek_it_ha.notify` werden die Felder mit Präfix versehen: `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

---

## Ton

Spielen Sie einen Ton mit Ihrer Benachrichtigung ab:

```yaml
service: peek_it_ha.notify
data:
  message: "Paket zugestellt"
  title: "Türklingel"
  sound: "01_notify.wav"
  soundVolume: 0.8
```

| Parameter | Typ | Standard | Beschreibung |
|-----------|-----|----------|--------------|
| `sound` | string | — | Name der Tondatei (z.B. "01_notify.wav") |
| `soundVolume` | float | `1.0` | Lautstärke (0.0 bis 1.0) |

Die Peek-it [TV] App wird mit integrierten Tönen ausgeliefert und unterstützt das Hochladen eigener Töne über den Designer.

---

## Interaktives Menü

Der Widget-Typ `menu` erstellt ein D-Pad-navigierbares Overlay-Menü auf dem Fernseher. Menüs unterstützen Untermenüs, HA-Entity-Schalter mit Echtzeit-Statusabfrage, Aktions-Callbacks und Schließen-Schaltflächen.

### Menübeispiel per Automatisierung

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Schnellsteuerung",
          "titleIcon": "mdi:menu",
          "bgColor": "#1E1E1E",
          "textColor": "#FFFFFF",
          "accentColor": "#00E676",
          "items": [
            {"type": "submenu", "label": "Lichter", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Wohnzimmer", "icon": "mdi:lightbulb", "entity_id": "light.living_room"},
              {"type": "toggle", "label": "Küche", "icon": "mdi:lightbulb", "entity_id": "light.kitchen"},
              {"type": "close", "label": "Zurück", "icon": "mdi:arrow-left"}
            ]},
            {"type": "action", "label": "Filmmodus", "icon": "mdi:movie", "action": "movie_mode"},
            {"type": "close", "label": "Schließen", "icon": "mdi:close"}
          ]
        }
      style:
        left: 35
        top: 10
        width: 30
        height: 80
```

### Menüeintragstypen

| Typ | Beschreibung |
|-----|--------------|
| `action` | Löst ein HA-Event (`peekit_button_press`) mit der angegebenen `action`-ID aus |
| `submenu` | Öffnet ein verschachteltes Untermenü mit eigenen `children`-Einträgen |
| `toggle` | Schaltet eine HA-Entity um (erfordert `entity_id`), Statusabfrage alle 5s |
| `text` | Informativer Text (nicht interaktiv) |
| `close` | Schließt das Menü |

### Navigation

- **Hoch/Runter**: zwischen Einträgen navigieren
- **Rechts/Enter**: Untermenü öffnen
- **Links/Zurück**: zum übergeordneten Menü zurückkehren
- **Zurück auf Hauptebene**: Menü schließen

---

## HA-Entity-Widget

Zeigen Sie HA-Entity-Zustände in Echtzeit direkt auf dem Fernseher an, mit einem `webview`-Widget über WebSocket oder REST-Polling.

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

## HA-Diagramm-Widget

Die Peek-it [TV] App unterstützt CSS/SVG-Diagramme zur Anzeige von Entity-Verläufen. Diagrammtypen: **Fläche**, **Linie** und **Balken**.

Diagramme werden als reines CSS/SVG gerendert — keine externen Bibliotheken erforderlich. Konfigurieren Sie sie über den Diagramm-Editor im Designer.

---

## Overlay-Konfiguration

### Uhr-Overlay

Die Peek-it [TV] App kann ein dauerhaftes Uhr-Overlay anzeigen. Konfigurieren Sie es über die Designer-Einstellungen oder den Endpunkt `/api/config/clock`:

- Aktivieren/Deaktivieren
- Format (12h/24h)
- Position, Farbe, Größe, Deckkraft

### Abdunkelungs-Overlay

Eine konfigurierbare Hintergrund-Abdunkelungsebene. Konfigurieren über die Designer-Einstellungen oder `/api/config/dimming`:

- Aktivieren/Deaktivieren
- Farbe, Deckkraft

---

## Verfügbare Parameter

### Hauptfelder

| Parameter | Typ | Standard | Beschreibung |
|-----------|-----|----------|--------------|
| `action` | string | `DISPLAY` | `DISPLAY` zum Anzeigen, `CLOSE` zum Schließen |
| `duration` | int | `10000` | Dauer in Millisekunden (0 = unendlich) |
| `priority` | string | `normal` | `normal` oder `urgent` |
| `animationIn` | string | `fade` | Eingangsanimation |
| `animationOut` | string | `fade` | Ausgangsanimation |
| `template_id` | string | — | UUID des zu verwendenden Templates |
| `params` | dict | — | Dynamische Template-Parameter |
| `elements` | list | — | Widget-Liste (erweiterter Modus) |
| `message` | string | — | Einfacher Text (einfacher Modus) |
| `title` | string | — | Titeltext (einfacher Modus) |
| `sound` | string | — | Name der Tondatei |
| `soundVolume` | float | `1.0` | Tonlautstärke (0.0-1.0) |
| `tts` | string | — | TTS-Text (wird mit der Benachrichtigung vorgelesen) |
| `ttsLang` | string | `en` | TTS-Sprachcode |
| `ttsSpeed` | float | `1.0` | TTS-Sprechgeschwindigkeit (0.5-2.0) |
| `ttsPitch` | float | `1.0` | TTS-Tonhöhe (0.5-2.0) |
| `ttsVolume` | float | `1.0` | TTS-Lautstärke (0.0-1.0) |

### Verfügbare Animationen

| Name | Effekt |
|------|--------|
| `none` | Sofort, keine Animation |
| `fade` | Ein-/Ausblenden |
| `slide_right` | Von/nach rechts gleiten |
| `slide_left` | Von/nach links gleiten |
| `slide_top` | Von/nach oben gleiten |
| `slide_bottom` | Von/nach unten gleiten |
| `pop` | Zoom-/Skalierungseffekt |

### Widget-Typen

| Typ | Beschreibung | Inhalt (`content`) |
|-----|--------------|-------------------|
| `text` | Statischer Text | Der anzuzeigende Text |
| `button` | Interaktive Schaltfläche (TV-Fernbedienung) | Beschriftung der Schaltfläche |
| `box` | Rechteck / Container | — |
| `circle` | Kreis | — |
| `ellipse` | Ellipse / Oval | — |
| `image` | Bild (PNG, JPG, URL) | Bild-URL |
| `video` | RTSP / HTTP Videostream | Stream-URL |
| `webview` | Eingebettete Webseite | Seiten-URL |
| `svg` | SVG-Vektorbild | URL oder SVG-Pfad |
| `line` | Horizontale Linie | — |
| `arrow` | Pfeil (nach rechts zeigend) | — |
| `menu` | Interaktives D-Pad-Menü | JSON MenuConfig |

### Style-Eigenschaften

| Eigenschaft | Typ | Beschreibung |
|-------------|-----|--------------|
| `left` | float | X-Position in % des Bildschirms (0-100) |
| `top` | float | Y-Position in % des Bildschirms (0-100) |
| `width` | float | Breite in % des Bildschirms |
| `height` | float | Höhe in % des Bildschirms |
| `color` | string | Textfarbe (Hex, z.B. `#FFFFFF`) |
| `bgColor` | string | Hintergrundfarbe (Hex mit Alpha, z.B. `#CC000000`) |
| `size` | int | Schriftgröße |
| `font` | string | Schriftfamilie (Roboto, sans-serif, usw.) |
| `weight` | string | Schriftstärke (`normal`, `bold`) |
| `align` | string | Ausrichtung (`left`, `center`, `right`) |
| `opacity` | float | Deckkraft (0.0 bis 1.0) |
| `radius` | int | Eckenradius (Pixel) |
| `borderWidth` | int | Rahmenstärke (Pixel) |
| `borderColor` | string | Rahmenfarbe (Hex) |
| `rotation` | float | Rotation in Grad |
| `focusColor` | string | Rahmenfarbe bei Fokus |
| `focusBgColor` | string | Hintergrundfarbe bei Fokus |

### Interaktionseigenschaften (Schaltflächen)

| Eigenschaft | Typ | Beschreibung |
|-------------|-----|--------------|
| `focusable` | bool | Widget empfängt TV-Fernbedienungsfokus |
| `directFocus` | bool | Widget erhält Fokus bei Anzeige |
| `action` | string | `CLOSE` zum Schließen, oder benutzerdefinierte ID für Webhook |
| `paramKey` | string | Verknüpft Inhalt mit einem Template-Parameter |
| `actionParamKey` | string | Verknüpft Aktion mit einem Template-Parameter |

---

## Der Designer

Der Designer ist ein **visueller Web-Editor**, der in die Peek-it [TV] App eingebettet ist. Greifen Sie von jedem Browser in Ihrem lokalen Netzwerk darauf zu.

**URL**: `http://<TV_IP>:<PORT>/` (z.B. `http://192.168.1.42:8081/`)

Sie können auch darauf zugreifen über:
- Das Attribut `designer_url` des binary_sensor in HA
- Das Zahnrad-Symbol > Designer in den Integrationsoptionen

### Funktionen

- **11 Widget-Typen** — per Drag & Drop auf eine kalibrierte TV-Leinwand ziehen
- **Echtzeit-JSON-Vorschau** — sehen Sie den exakten Payload, der erstellt wird
- **Template-Bibliothek** — speichern, laden, umbenennen, löschen, exportieren/importieren
- **Parametersystem** — definieren Sie `paramKey` an Widgets für dynamische Inhalte
- **Automatische Kalibrierung** — passt sich an die tatsächliche Auflösung Ihres TVs an (16:9, 21:9, usw.)
- **Ton-Konfiguration** — Standard-Benachrichtigungston-Einstellungen
- **HA-Token-Konfiguration** — erforderlich für Webhook-Callbacks
- **Internationalisierung** — verfügbar in 6 Sprachen (EN, FR, DE, ES, NL, PT)

### Senden und Testen

- **SENDEN-Taste** (blau) — sendet das aktuelle Layout sofort an den Fernseher
- **KILL-Taste** (rot) — schließt die aktuelle Benachrichtigung
- **JSON-Vorschau** (Fußzeile) — sehen Sie den exakten Payload, der gesendet wird

---

## Templates & Parameter

### Konzept

Ein Template ist ein wiederverwendbares Benachrichtigungslayout. Anstatt jedes Mal 15 Zeilen JSON zu senden:

1. **Erstellen** Sie das Layout im Designer (Drag & Drop)
2. **Definieren Sie Parameter** (`paramKey`) auf dynamischen Elementen
3. **Speichern** als Custom (UUID wird generiert)
4. **Verwenden** Sie die `template_id` + `params` in Ihren Automatisierungen

### Template-Liste abrufen

```yaml
service: peek_it_ha.get_templates
response_variable: result
```

Gibt ein Dictionary pro konfiguriertem Gerät zurück:
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

## Automatisierungen

### Bewegungserkennungsalarm

```yaml
automation:
  - alias: "Garten-Bewegungsalarm"
    trigger:
      - platform: state
        entity_id: binary_sensor.garden_motion
        to: "on"
    action:
      - service: peek_it_ha.notify
        data:
          template_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
          params:
            title: "Bewegung erkannt!"
            camera_url: "rtsp://192.168.1.50:554/stream1"
          duration: 15000
          animationIn: slide_right
          animationOut: fade
```

### Morgens Wetterbericht

```yaml
automation:
  - alias: "Morgenwetter"
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
          title: "Wetter heute"
          duration: 10000
          animationIn: fade
```

### TTS-Durchsage-Automatisierung

```yaml
automation:
  - alias: "Türklingel TTS-Alarm"
    trigger:
      - platform: state
        entity_id: binary_sensor.doorbell
        to: "on"
    action:
      - service: peek_it_ha.tts
        data:
          text: "Es ist jemand an der Haustür"
          lang: "de"
          speed: 1.25
          volume: 1.0
```

### Benachrichtigung mit Ton

```yaml
automation:
  - alias: "Wäsche fertig Alarm"
    trigger:
      - platform: state
        entity_id: sensor.washing_machine
        to: "idle"
    action:
      - service: peek_it_ha.notify
        data:
          message: "Die Waschmaschine ist fertig!"
          title: "Wäsche"
          duration: 8000
          sound: "08-notify.mp3"
          soundVolume: 0.7
```

### Interaktive Schaltflächen — Rückmeldung an HA

Wenn ein Benutzer eine Schaltfläche in einer Benachrichtigung drückt (über die TV-Fernbedienung), wird ein HA-Event ausgelöst:

```yaml
automation:
  - alias: "TV-Taste - Lichter aus"
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

### Daueralarm mit Bestätigungstaste

```yaml
automation:
  - alias: "Wasserleck-Alarm"
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
          tts: "Achtung! Wasserleck erkannt!"
          ttsLang: "de"
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
              content: "WASSERLECK ERKANNT"
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
              content: "Verstanden"
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

### RTSP-Kamerabild

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

Das Bild wird dank eines optimierten ExoPlayer-Setups mit extrem niedriger Latenz (~50ms) angezeigt.

---

## Service-Referenz

| Service | Beschreibung |
|---------|--------------|
| `peek_it_ha.notify` | Benachrichtigung an alle konfigurierten Geräte senden |
| `peek_it_ha.get_templates` | Template-Liste von allen Geräten abrufen |
| `peek_it_ha.tts` | TTS an alle konfigurierten Geräte senden |
| `peek_it_ha.tts_stop` | TTS auf allen konfigurierten Geräten stoppen |

---

## Webhooks & Events

Die Integration lauscht auf einen Webhook, um Logs und Tastenaktionen vom Fernseher zu empfangen.

| HA-Event | Auslöser | Daten |
|----------|----------|-------|
| `peekit_button_press` | Tastendruck auf dem Fernseher | `{ "action": "button_id" }` |

TV-Logs werden an den HA-Logger mit dem Präfix `[PEEK-IT REPORT]` weitergeleitet.

---

## Multi-Gerät

Die Integration unterstützt **mehrere Geräte**. Fügen Sie jeden Fernseher als separate Integration hinzu. Die Services `peek_it_ha.notify`, `tts`, `tts_stop` und `get_templates` senden automatisch an **alle konfigurierten Geräte**.

Um ein einzelnes Gerät anzusprechen, verwenden Sie die spezifische `notify`-Entity:

```yaml
service: notify.send_message
target:
  entity_id: notify.living_room_tv
data:
  message: "Nur auf diesem Fernseher"
```

---

## Internationalisierung

Die Integration und die Peek-it [TV] App unterstützen **6 Sprachen**:

| Code | Sprache |
|------|---------|
| `en` | Englisch (Standard) |
| `fr` | Französisch |
| `de` | Deutsch |
| `es` | Spanisch |
| `nl` | Niederländisch |
| `pt` | Portugiesisch |

Die Sprache kann in den Designer-Einstellungen oder im Einstellungsbildschirm der Peek-it [TV] App konfiguriert werden.

---

## WAF — Der ultimative KPI

Der legendäre **WAF** — *Wife Acceptance Factor* (Ehefrau-Akzeptanz-Faktor). Diese inoffizielle, aber absolut geschäftskritische Kennzahl, die die Toleranz Ihrer besseren Hälfte gegenüber Ihren Hausautomations-Experimenten misst.

### Anwendungsfälle, die Ihren WAF steigern

**Intelligente Wäsche**: Eine "Wäsche fertig!"-Benachrichtigung erscheint dezent während des Films. Nie wieder vergessene Wäsche, die drei Tage in der Trommel vor sich hin müffelt.

> *(WAF: +23 Punkte)*

**Morgenwetter**: Jeden Morgen um 7:30 Uhr erscheint der Wetterbericht auf dem Küchen-TV. Ohne umständliches Handy-Fummelei beim Frühstück.

> *(WAF: +15 Punkte)*

**Türklingelkamera**: Es klingelt, das Kamerabild erscheint auf dem Bildschirm. Treffsichere Beurteilung vom Sofa aus. Niemand musste aufstehen. Das nennt man deutsche Effizienz.

> *(WAF: +38 Punkte)*

**Sportergebnis**: Ein dezentes "2 - 1, 78'" erscheint für 3 Sekunden in der oberen rechten Ecke. Alle sind zufrieden. Niemand hat umgeschaltet. Der Hausfrieden bleibt gewahrt.

> *(WAF: +52 Punkte)*

### Der Anwendungsfall, der Ihren WAF VERNICHTET

**Debugging in Produktion**: Sie testen Ihre Benachrichtigungen um 23 Uhr, während Ihre bessere Hälfte das Staffelfinale schaut. "Das war nur ein kurzer Test!" — berühmte letzte Worte.

> *(WAF: -347 Punkte. Geschätzte Erholungszeit: 3 Wochen. Blumenhandlung hat ab 8 Uhr geöffnet.)*

**Profi-Tipp**: Testen Sie Ihre Automatisierungen VOR 21 Uhr. Oder nutzen Sie die **KILL**-Taste im Designer. Ihr Beziehungsstatus wird es Ihnen danken.

---

## Fehlerbehebung

| Problem | Lösung |
|---------|--------|
| Integration in HA nicht gefunden | Stellen Sie sicher, dass der Ordner in `custom_components/peek_it_ha/` liegt. HA neu starten. |
| "Verbindung nicht möglich" bei der Einrichtung | IP und Port überprüfen. Die App muss auf dem Fernseher laufen. Testen Sie `http://IP:8081/api/status` im Browser. |
| Binary Sensor immer "offline" | Läuft die Peek-it [TV] App? Startet der Dienst beim Booten? |
| Benachrichtigung wird nicht angezeigt | Overlay-Berechtigung in den Android TV-Einstellungen überprüfen. |
| Designer verbindet sich nicht | Stellen Sie sicher, dass Sie im gleichen Netzwerk sind. Versuchen Sie `http://IP:PORT/` im Browser. |
| Leere Templates im Zahnrad-Menü | Der Fernseher muss eingeschaltet und erreichbar sein. Binary-Sensor-Status prüfen. |
| TV-Taste löst kein HA-Event aus | HA-Token im Designer konfigurieren (Zahnrad-Symbol). Überprüfen, ob `ha_ip` vom Fernseher erreichbar ist. |
| TTS spricht nicht | Prüfen Sie, ob eine TTS-Engine auf dem Android TV installiert ist (Google TTS ist normalerweise vorinstalliert). |
| Kein Ton bei Benachrichtigung | Überprüfen Sie, ob die Tondatei existiert (über Designer-Einstellungen prüfen). Einige Streaming-Apps können die Audio-Mischung blockieren. |
| Menü reagiert nicht auf D-Pad | Stellen Sie sicher, dass das Menüelement den Fokus hat. Setzen Sie `duration: 0`, damit das Menü geöffnet bleibt. |

---

## Mitwirken

Beiträge sind willkommen! Erstellen Sie ein Issue oder einen Pull Request im [GitHub-Repository](https://github.com/jolabs40/peek-it-ha).

## Lizenz

Dieses Projekt wird unter der MIT-Lizenz verteilt. Siehe die [LICENSE](LICENSE)-Datei für Details.

---

<p align="center">
  Gemacht mit Kaffee, viel zu vielen YAML-Dateien und einer unvernünftigen Liebe zu Overlays.<br/>
  <strong>Peek-it [HA]</strong> — weil Ihr Fernseher mehr kann, als Sie denken.
</p>
