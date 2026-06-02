# Peek-it [HA] — Home-Assistant-Integration

<p align="center">
  <img src="https://raw.githubusercontent.com/jolabs40/peek-it-ha/master/custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Verwandeln Sie Ihren Android-TV in eine intelligente Benachrichtigungsanzeige.</strong><br/>
  Warnungen, Kameras, Dashboards, TTS, Menüs — als Overlay auf Ihrem TV in Echtzeit.
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
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-funktionsweise">Funktionsweise</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-installation">Installation</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-der-designer">Designer</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-verwendung">Verwendung</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-sprachausgabe-tts">TTS</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-automatisierungen">Automatisierungen</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-erweiterte-referenz">Erweiterte Referenz</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-waf--der-ultimative-kpi">WAF</a>
</p>

<p align="center">
  <b>Sprachen:</b>
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md">English</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md">Fran&ccedil;ais</a> |
  Deutsch |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_ES.md">Espa&ntilde;ol</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_NL.md">Nederlands</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md">Portugu&ecirc;s</a>
</p>

---

## Warum Peek-it [HA]?

Ihr Android-TV-Gerät ist rund um die Uhr an Ihrem Fernseher angeschlossen. Warum lassen Sie es nicht arbeiten?

Die Anwendung **Peek-it [TV]** zeigt **umfangreiche Benachrichtigungen als Overlay** über jeder gerade laufenden Anwendung an: einem Film, dem Antennenfernsehen, einem Spiel … Sie schauen ein Spiel? Der Spielstand wird in einer Ecke aktualisiert. Es klingelt an der Tür? Die Türkamera erscheint sofort. Und **Sie selbst gestalten** diese Anzeigen, ohne eine einzige Zeile Code zu schreiben.

> 💡 **Das Wichtigste in Kürze**
>
> 1. **Sie gestalten** Ihre Benachrichtigungen (und sogar ganze Seiten) im **Designer**, einem visuellen Drag-and-Drop-Editor, der von jedem Browser aus erreichbar ist. *Er baut alles auf — Sie müssen nichts programmieren.*
> 2. **Sie lösen sie aus** über **Home Assistant** dank dieser Integration … oder über **Tasker, Node-RED, Jeedom** oder einen beliebigen anderen HTTP-Client, denn die App stellt eine einfache lokale API bereit.

> 🧩 **Zwei Komponenten, zwei Rollen**
> Die **Anwendung Peek-it [TV]** (Android, im Play Store) zeichnet das Overlay, beherbergt den Designer und die Template-Engine: Sie ist die Autorität.
> Die **Integration Peek-it [HA]** (dieses Repository) steuert sie von Home Assistant aus: Versand von Benachrichtigungen/TTS, Statusüberwachung, Tastenrückmeldungen.

### Was Sie anzeigen können

| | |
|------|---------|
| 📝 **Umfangreicher Text** | Titel, Nachrichten, Zähler, Wetter |
| 🖼️ **Bilder** | Fotos, Screenshots, Logos, QR-Codes |
| 🎥 **RTSP-Videostreams** | Überwachungskameras in Echtzeit, ultraniedrige Latenz |
| 🌐 **Webseiten** | HA-Dashboards, Diagramme, Wetter-Widgets |
| 🔺 **Formen & SVG** | Rechtecke, Ellipsen, Sechsecke, Pfeile, Vektorsymbole |
| 🎮 **Tasten & Menüs** | Per Fernbedienung navigierbar, lösen Ihre HA-Automatisierungen aus |
| 📊 **HA-Entitäten & Diagramme** | Echtzeitstatus und Verlauf der Entitäten |
| 🔊 **Sprachausgabe** | Sprachansagen direkt auf dem TV |

### Schlüsselfunktionen

- **Null Latenz** — natives Android-Overlay, kein Streaming und kein Casting
- **Mit allem kompatibel** — das Overlay wird über jeder beliebigen Anwendung angezeigt
- **Visueller Designer** — erstellen Sie alles per Drag-and-Drop, mit Echtzeitvorschau
- **Wiederverwendbare Templates** — einmal gestalten, mit dynamischen Parametern wiederverwenden
- **Mehrere Geräte** — verwalten Sie mehrere TVs von einer einzigen HA-Instanz aus
- **Offen** — steuerbar über HA, Tasker, Node-RED, Jeedom … via lokaler HTTP-API
- **6 Sprachen** — EN, FR, DE, ES, NL, PT

---

## 🧩 Funktionsweise

Drei Schritte, vom Visuellen zur Automatisierung:

| Schritt | Wo | Was Sie tun |
|------|-----|--------------------|
| **1. Gestalten** | 🎨 Designer (Browser) | Ziehen Sie Ihre Elemente per Drag-and-Drop auf eine auf Ihren TV kalibrierte Arbeitsfläche. Der Designer erzeugt das gesamte Rendering für Sie. |
| **2. Speichern** | 🎨 Designer | Speichern Sie Ihre Kreation als wiederverwendbares **Template** (es wird einfach eine ID erzeugt). |
| **3. Auslösen** | 🏠 Home Assistant | Rufen Sie das Template aus einer Automatisierung auf, in wenigen Zeilen, mit dynamischen Werten. |

```yaml
# Schritt 3: ein im Designer gestaltetes Template auslösen
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Sicherheitsalarm"
    camera_url: "rtsp://192.168.1.50:554/stream1"
```

> ✅ **Sie müssen fast nie JSON von Hand schreiben.** Der Designer kümmert sich um das Layout; auf der Home-Assistant-Seite geben Sie nur die ID des Templates und einige Werte an. Die [Erweiterte Referenz](https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-erweiterte-referenz) (rohes JSON, Widget-Typen, API …) ist nur für besondere Fälle gedacht.

---

## 📥 Installation

### 1. Die Anwendung Peek-it [TV] installieren

**Empfohlen — Google Play Store**: Suchen Sie nach **„Peek-it"** im Play Store Ihres Android-TV oder öffnen Sie die Seite:
[play.google.com/store/apps/details?id=net.jolabs40.peekit](https://play.google.com/store/apps/details?id=net.jolabs40.peekit)

> Gerät ohne Play Store (manche Android-TV-Boxen, Fire TV …): Installieren Sie das APK per Sideload von der [Releases-Seite](https://github.com/jolabs40/peek-it-ha/releases) (USB-Stick, `adb install` oder ein Dateimanager).

Anschließend, unabhängig von der Methode:

1. Starten Sie die Anwendung — gewähren Sie die **Overlay-Berechtigung** (Anzeige über anderen Anwendungen); der Dienst startet automatisch.
2. Notieren Sie sich die auf dem Hauptbildschirm angezeigte **IP-Adresse** (z. B. `192.168.1.42`). Standardport: **8081**.

### 2. Die Home-Assistant-Integration installieren

**Über HACS (empfohlen)**: HACS → *Integrations* → Drei-Punkte-Menü → *Custom repositories* → fügen Sie `https://github.com/jolabs40/peek-it-ha` hinzu (Kategorie *Integration*) → *Download* → **starten Sie HA neu**.

<details>
<summary>Manuelle Installation</summary>

Kopieren Sie den Ordner `peek_it_ha/` nach `config/custom_components/` und starten Sie anschließend Home Assistant neu:

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

### 3. Die Integration hinzufügen

*Einstellungen → Geräte und Dienste → Integration hinzufügen → Peek-it [HA]*. Geben Sie die **IP**, den **Port** (`8081`), einen **Namen** und, falls die TV-App es verlangt, einen **API-Schlüssel** an. Wenn das Gerät per Zeroconf (`_peekit._tcp`) veröffentlicht wird, kann HA es auch **automatisch erkennen**.

<details>
<summary>Was automatisch erstellt wird (HA-Entitäten)</summary>

Alle Entitäten werden in einer **einzigen Gerätekarte** zusammengefasst. Für jeden TV:

| Entität | Typ | Beschreibung |
|--------|------|-------------|
| `binary_sensor.<name>_status` | Konnektivität | Online / offline (alle 30 s abgefragt); stellt das Attribut `designer_url` bereit |
| `binary_sensor.<name>_overlay_permission` | Diagnose | Overlay-Berechtigung gewährt |
| `binary_sensor.<name>_accessibility_permission` | Diagnose | Bedienungshilfendienst aktiv |
| `binary_sensor.<name>_microphone_permission` | Diagnose | Mikrofonberechtigung gewährt |
| `notify.<name>` | Notify | Versand von Benachrichtigungen |
| `button.<name>_*_assist / overlay / accessibility` | Config (×6) | Berechtigungen über ADB aktivieren/deaktivieren — siehe [ADB-Tasten](https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-konfigurationstasten-adb) |

Pro TV wird alle 30 s nur eine einzige Anfrage `GET /api/status` gesendet; alle Entitäten teilen sich diesen Schnappschuss (gemeinsamer Koordinator).
</details>

---

## 🎨 Der Designer

**Das Herzstück von Peek-it.** Hier erstellen Sie Ihre Benachrichtigungen und Seiten — visuell, ohne zu programmieren. Es handelt sich um einen **in die App eingebetteten Web-Editor**, der von jedem Browser im lokalen Netzwerk aus erreichbar ist:

**URL**: `http://<IP_TV>:<PORT>/` (z. B. `http://192.168.1.42:8081/`) — ebenfalls erreichbar über das Attribut `designer_url` des Status-Sensors oder über *Zahnradsymbol → Designer* in den Optionen der Integration.

- **Drag-and-Drop** Ihrer Widgets auf eine Arbeitsfläche, die auf die tatsächliche Auflösung Ihres TV kalibriert ist (16:9, 21:9 …)
- **JSON-Vorschau in Echtzeit** — Sie sehen, wie das Rendering entsteht
- **Template-Bibliothek** — speichern, laden, umbenennen, exportieren/importieren
- **Dynamische Parameter** — markieren Sie variable Elemente (`paramKey`), um sie von HA aus zu befüllen
- **Konfiguration** des Standardklangs, der Sprache und des **HA-Zugriffstokens** (siehe unten)
- **SEND-Tasten** (an den TV senden) und **KILL-Tasten** (schließen) zum sofortigen Testen

> 🔑 **Home-Assistant-Zugriffstoken (optional).** Manche Funktionen verlangen, dass die App die HA-API **direkt** aufruft: eine Entität aus einem Menü umschalten, den Status einer Entität in Echtzeit anzeigen, ein Verlaufsdiagramm zeichnen oder einen Kamera-Schnappschuss anzeigen. Erstellen Sie dazu ein **langlebiges Zugriffstoken (Long-Lived Access Token)** in HA (*Ihr Profil → ganz unten → Langlebige Zugriffstoken → Erstellen*) und fügen Sie es in die Einstellungen des Designers ein. Es wird verschlüsselt auf dem TV gespeichert. Nicht nötig, wenn Sie sich darauf beschränken, Benachrichtigungen von HA aus zu senden.
>
> Nicht zu verwechseln mit dem **Webhook-Secret** (`X-Peek-Secret`), das in die andere Richtung dient (Tastenrückmeldungen TV → HA) und das die Integration **automatisch** verwaltet.

> Von HA aus listet *Zahnradsymbol → Templates* all Ihre Templates mit ihrer **ID** (kopierbar) und ihren **Parametern** auf, sortiert in *Official* / *Custom* / *Drafts*.

---

## 🚀 Verwendung

Drei Wege zum Senden, vom einfachsten bis zum fortgeschrittensten. **Der Template-Modus ist der praktischste**: Er stützt sich auf Ihre im Designer erstellten Kreationen.

### Einfache Nachricht

Ein Text, der am unteren Bildschirmrand auf dunklem Hintergrund angezeigt wird — ideal für eine schnelle Warnung.

```yaml
service: peek_it_ha.notify
data:
  message: "Die Waschmaschine ist fertig!"
  title: "Zuhause"
  duration: 8000
```

### Template + Parameter *(empfohlen)*

Verwenden Sie ein im Designer gestaltetes Template wieder, indem Sie dynamische Werte einspeisen.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Sicherheitsalarm"
    message: "Bewegung im Garten erkannt"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

Der Server lädt das Template, ersetzt die `{{placeholders}}` durch die Werte aus `params` und zeigt das Ergebnis an.

### Eine Benachrichtigung schließen / behalten

```yaml
# Sofort schließen
service: peek_it_ha.notify
data:
  action: CLOSE
```

`duration: 0` behält die Benachrichtigung auf dem Bildschirm, bis ein explizites `CLOSE` erfolgt oder eine Taste gedrückt wird.

<details>
<summary><b>Erweiterter Modus — rohe Elemente (vollständiges JSON)</b></summary>

Für die Fälle, in denen Sie jedes Widget von Hand definieren möchten, ohne ein Template zu verwenden. *In der Praxis erledigt der Designer all das visuell.*

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
      content: "Gartenkamera"
      style: { left: 62, top: 28, width: 34, height: 5, size: 18, color: "#FFFFFF", align: center }
```

Das vollständige Vokabular (Widget-Typen, Stileigenschaften) ist in der [Erweiterten Referenz](https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-erweiterte-referenz) dokumentiert.
</details>

---

## 🔔 Sprachausgabe (TTS)

Lassen Sie den TV sprechen, allein oder begleitend zu einer Benachrichtigung.

```yaml
# Eigenständiges TTS
service: peek_it_ha.tts
data:
  text: "Das Abendessen ist fertig!"
  lang: "de"
  speed: 1.0     # 0.5 bis 2.0
  volume: 1.0    # 0.0 bis 1.0
```

```yaml
# TTS mit visueller Benachrichtigung
service: peek_it_ha.notify
data:
  message: "Bewegung im Garten erkannt"
  title: "Sicherheit"
  tts: "Bewegung im Garten erkannt"
  ttsLang: "de"
  ttsSpeed: 1.25
```

Wiedergabe stoppen: `service: peek_it_ha.tts_stop`. In `notify` sind die Felder mit `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume` präfigiert.

## 🔊 Klang

```yaml
service: peek_it_ha.notify
data:
  message: "Paket geliefert"
  sound: "01_notify.wav"
  soundVolume: 0.8   # 0.0 bis 1.0
```

Die App wird mit integrierten Klängen geliefert (`01_notify.wav`…`05_notify.wav`, `06-notify.ogg`, `07-notify.ogg`, `08-notify.mp3`…`10-notify.mp3`) und akzeptiert Ihre eigenen Klänge (über den Designer). Der Dienst **`peek_it_ha.get_sounds`** listet die verfügbaren Klänge einer TV auf (`{official, custom}`).

---

## 🎨 Erweiterter einfacher Modus (Presets & Bild)

Ohne das `elements`-JSON anzufassen akzeptiert der einfache Modus optionale **Presets** — `position` (`top`/`center`/`bottom`), `level` (`info`/`warning`/`alert`, wählt Akzentfarbe + Icon), `icon` (`mdi:…`) und `color` (Hex-Akzent) — sowie ein **Bild** (`image_url` + `image_fit`). Die Standarddarstellung bleibt unverändert, wenn diese Felder fehlen.

```yaml
# Warnung mit Icon und Akzent
service: peek_it_ha.notify
data:
  message: "Wasserleck erkannt"
  level: alert
  position: center
```

```yaml
# Besucher-Schnappschuss (Türklingel) auf dem TV
service: peek_it_ha.notify
data:
  message: "Jemand an der Tür"
  image_url: "http://192.168.1.50/snapshot.jpg"
  image_fit: cover        # contain | cover | fill
```

> `image_url` akzeptiert eine http(s)-URL, ein `data:base64` oder einen lokalen Pfad. Ohne `message` wird nur das Bild angezeigt. Die TTS-Sprache (`ttsLang`/`lang`) folgt der Home-Assistant-Sprache, wenn nicht angegeben.

---

## 📺 Konfigurationstasten (ADB)

Die Integration stellt **6 Tasten** bereit (Kategorie *Config*), die den TV über **ADB über TCP** steuern, um per Klick Berechtigungen zu setzen, die sich mit der Fernbedienung mühsam aktivieren lassen:

| Taste | Aktion auf dem TV |
|--------|------------------|
| **Enable / Disable Assist** | Setzt Peek-it als Standardassistent / stellt diesen wieder her |
| **Enable / Disable Overlay** | Gewährt / widerruft die Berechtigung `SYSTEM_ALERT_WINDOW` |
| **Enable / Disable Accessibility** | Aktiviert / deaktiviert den Bedienungshilfendienst `MenuKeyService` |

<details>
<summary>ADB-Voraussetzungen (einmalig zu erledigen)</summary>

Die Tasten nutzen die Bibliothek `adb-shell` (automatisch von HA installiert) und verbinden sich mit der IP des TV über den **Port 5555**.

1. **Aktivieren Sie das ADB-Netzwerk-Debugging**: *Einstellungen → Geräteeinstellungen → Info →* tippen Sie 7-mal auf *Build-Nummer*, dann *Entwickleroptionen →* **USB-Debugging** (und **Drahtloses Debugging**, falls angeboten).
2. **Autorisieren Sie den RSA-Schlüssel beim ersten Drücken**: Auf dem TV erscheint ein Fenster „Debugging zulassen?" → aktivieren Sie *Immer zulassen*. Der Schlüssel wird einmal erzeugt und in `.storage/peek_it_adb_key` gespeichert.
3. Die offizielle **Android-TV**-Integration wird empfohlen (HA weist in *Reparaturen* darauf hin) für eine stabile ADB-Verwaltung.

Wenn `adb-shell` fehlt oder der TV die Verbindung ablehnt, schlägt die Aktion mit einem Fehler im HA-Protokoll fehl.
</details>

---

## 🤖 Automatisierungen

### Bewegungsalarm mit Kamera

```yaml
automation:
  - alias: "Bewegungsalarm Garten"
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
```

### Morgendlicher Wetterbericht

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
```

### Tastenrückmeldung an HA

Ein Druck auf eine Benachrichtigungstaste (Fernbedienung) löst ein HA-Ereignis aus:

```yaml
automation:
  - alias: "TV-Taste - Lichter ausschalten"
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
<summary>Dauerhafte Warnung mit Schließen-Taste (rohes JSON)</summary>

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  animationIn: pop
  priority: urgent
  tts: "Achtung! Wasserleck erkannt!"
  ttsLang: "de"
  elements:
    - type: rect
      style: { left: 20, top: 20, width: 60, height: 60, bgColor: "#EE990000", radius: 20 }
    - type: text
      content: "WASSERLECK ERKANNT"
      style: { left: 25, top: 30, width: 50, height: 10, size: 40, color: "#FFFFFF", weight: bold, align: center }
    - type: button
      content: "Verstanden"
      action: CLOSE
      focusable: true
      directFocus: true
      style: { left: 35, top: 55, width: 30, height: 10, size: 24, color: "#FFFFFF", bgColor: "#CC333333", align: center, radius: 10, focusColor: "#FF6666", focusBgColor: "#CC660000" }
```
</details>

<details>
<summary>RTSP-Kamerastream</summary>

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

Ultraniedrige Latenz (~50 ms) dank einer optimierten ExoPlayer-Konfiguration.
</details>

---

## 🧰 Erweiterte Referenz

> 🛟 **Normalerweise benötigen Sie diesen Abschnitt nicht.** Der Designer baut Ihre Benachrichtigungen visuell auf und liefert Ihnen gebrauchsfertige Templates. Das Folgende ist nur für den rohen JSON-Modus, die API oder Drittanbieter-Integrationen nützlich.

<details>
<summary><b>Parameter des Dienstes <code>notify</code></b></summary>

| Parameter | Typ | Standard | Beschreibung |
|-----------|------|--------|-------------|
| `action` | string | `DISPLAY` | `DISPLAY` zum Anzeigen, `CLOSE` zum Schließen |
| `duration` | int | `10000` | Dauer in ms (0 = unendlich) |
| `priority` | string | `normal` | `normal` oder `urgent` |
| `animationIn` / `animationOut` | string | `fade` | Siehe Animationen unten |
| `template_id` | string | — | UUID des zu verwendenden Templates |
| `params` | dict | — | Dynamische Werte des Templates |
| `elements` | list | — | Liste von Widgets (roher JSON-Modus) |
| `message` / `title` | string | — | Modus einfache Nachricht |
| `sound` / `soundVolume` | string / float | — / `1.0` | Klang und Lautstärke (0.0-1.0) |
| `tts` / `ttsLang` / `ttsSpeed` / `ttsPitch` / `ttsVolume` | — | — | TTS, das mit der Benachrichtigung abgespielt wird |

**Animationen**: `none`, `fade`, `slide_right`, `slide_left`, `slide_top`, `slide_bottom`, `pop` (Ein- und Ausgang unabhängig voneinander).
</details>

<details>
<summary><b>Widget-Typen</b></summary>

Der Typ wird von der App interpretiert. **Jeder nicht erkannte Typ (`text`, `message`, `title`, `button` …) wird als Text-Widget gerendert**; ein `button` zeichnet sich durch `focusable` + `action` aus. Wenn `content` mit `mdi:` beginnt (z. B. `mdi:home-assistant`), wird ein **Material-Design-Icons-Symbol** angezeigt.

| Typ | Beschreibung | `content` |
|------|-------------|-----------|
| `text` | Statischer Text (Standardtyp) | Der Text oder `mdi:<symbol>` |
| `button` | Interaktiver Text (focusable, action) | Beschriftung |
| `rect` | Rechteck / Container | — |
| `ellipse` | Ellipse / Oval | — |
| `hexagon` | Sechseck | — |
| `circle` | Runder Container (Bild / MDI-Symbol) | URL oder `mdi:<symbol>` |
| `image` | PNG/JPG-Bild | URL |
| `video` | RTSP- / HTTP-Stream | URL |
| `webview` | Eingebettete Webseite | URL |
| `svg` | Vektorbild | URL oder Pfad |
| `line` / `arrow` | Linie / Pfeil | — |
| `confetti` | Konfetti-Animation über den gesamten Bildschirm | — |
| `menu` | Interaktives D-Pad-Menü | JSON MenuConfig |

> Ältere Beispiele mit `type: box` werden weiterhin angezeigt (Fallback: Text + `bgColor`), aber der kanonische Typ des Rechtecks ist `rect`.
</details>

<details>
<summary><b>Stil- und Interaktionseigenschaften</b></summary>

**Stil**: `left`, `top`, `width`, `height` (in % des Bildschirms, 0-100) · `color` · `bgColor` (hex mit Alpha) · `size` · `font` · `weight` (`normal`/`bold`) · `align` (`left`/`center`/`right`) · `opacity` · `radius` · `borderWidth` · `borderColor` · `rotation` · `focusColor` · `focusBgColor`.

**Interaktion (Tasten)**: `focusable` (erhält den Fernbedienungsfokus) · `directFocus` (Fokus bei der Anzeige) · `action` (`CLOSE` oder benutzerdefinierte ID für den Webhook) · `paramKey` (verknüpft den Inhalt mit einem Template-Parameter) · `actionParamKey` (verknüpft die Aktion mit einem Parameter).
</details>

<details>
<summary><b>Interaktives Menü (JSON-Konfiguration)</b></summary>

Das Widget `menu` erstellt ein per D-Pad navigierbares Overlay-Menü (Untermenüs, HA-Entitätsumschaltungen, Aktionen).

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Schnellsteuerung",
          "items": [
            {"type": "submenu", "label": "Lichter", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Wohnzimmer", "entity_id": "light.living_room"},
              {"type": "close", "label": "Zurück"}
            ]},
            {"type": "action", "label": "Kinomodus", "action": "movie_mode"},
            {"type": "close", "label": "Schließen"}
          ]
        }
      style: { left: 35, top: 10, width: 30, height: 80 }
```

| Elementtyp | Rolle |
|------|-------------|
| `action` | Löst `peekit_button_press` mit der ID `action` aus |
| `submenu` | Öffnet ein Untermenü (`children`) |
| `toggle` | Schaltet eine HA-Entität um (`entity_id`), Status alle 5 s aktualisiert |
| `text` | Informativer Text |
| `close` | Schließt das Menü |

**Navigation**: Auf/Ab navigieren · Rechts/Eingabe ein Untermenü öffnen · Links/Zurück zurückgehen · Zurück bei der Wurzel schließt.
</details>

<details>
<summary><b>HA-Entitäts-Widgets, Diagramme & Overlays (App-Fähigkeiten)</b></summary>

Diese Funktionen werden auf der **App**-Seite konfiguriert (Designer); die HA-Integration steuert sie nicht direkt. Sie erfordern ein **langlebiges Zugriffstoken (Long-Lived Access Token)** von HA, das im Designer eingegeben wird (vgl. [Der Designer](https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-der-designer)), da die App die HA-API direkt aufruft.

- **HA-Entitäts-Widget**: Eine über WebSocket/REST verbundene `webview` zeigt den Status von Entitäten in Echtzeit an.
- **HA-Diagramme**: Flächen- / Linien- / Balkendiagramme, in reinem CSS/SVG gerendert.
- **Overlay-Uhr** (`/api/config/clock`): 12-h-/24-h-Format, Position, Farbe, Deckkraft.
- **Abdunkeln** (`/api/config/dimming`): Farbe und Deckkraft einer Hintergrundschicht.
</details>

<details>
<summary><b>API & Webhook (für Tasker, Node-RED, Jeedom, Entwickler)</b></summary>

Die App stellt eine lokale HTTP-API bereit (Port `8081`). Wenn ein API-Schlüssel konfiguriert ist, tragen **alle** Anfragen den Header `X-API-Key: <schlüssel>`. Diese API kann von jedem HTTP-Client (Tasker, Node-RED, Jeedom …) aufgerufen werden.

| Endpoint | Methode | Verwendung |
|---|---|---|
| `/api/status` | GET | Status, Berechtigungen, Auflösung |
| `/api/notify` | POST | Eine Benachrichtigung anzeigen / schließen |
| `/api/tts` · `/api/tts/stop` | POST | Sprachausgabe |
| `/api/templates/list` | GET | Liste der Templates |

**Antwort von `/api/status`**:
```json
{
  "status": "online", "version": "v10.9", "device_name": "Living Room TV",
  "api_key_required": false, "api_key_valid": true,
  "screen": { "width": 1920, "height": 1080, "density": 1.0 },
  "permissions": { "overlay": true, "accessibility": false, "microphone": true }
}
```

**Webhook (Rückmeldungen vom TV → HA)**: `/api/webhook/peek_it_debug`. Seit Version 1.1.0 muss jede Anfrage den Header **`X-Peek-Secret`** vorweisen (sonst HTTP 401). Das Secret wird dem TV über die **Willkommensbenachrichtigung** (Feld `webhook_secret`) bei der Erstellung/Speicherung des Eintrags übermittelt.

| `level` | `message` | HA-Effekt |
|---------|-----------|----------|
| `ACTION` | `BUTTON_CLICK:<id>` | Sendet das Ereignis `peekit_button_press` `{ "action": "<id>" }` |
| `ERROR` / `WARN` / `INFO` | Text | Protokolliert als `[PEEK-IT REPORT]` |

> **Migration von 1.0.0**: *Konfigurieren → Einstellungen → Bestätigen*, um eine neue Willkommensbenachrichtigung mit dem `webhook_secret` zu senden.
</details>

---

## 🌍 Mehrere Geräte & Sprachen

Fügen Sie jeden TV als separate Integration hinzu. Standardmäßig gelten die Dienste `notify`, `tts`, `tts_stop` und `get_templates` für **alle konfigurierten TVs**; der Versand erfolgt **parallel** und Offline-TVs werden **übersprungen** (kein Blockieren mehr, wenn ein TV ausgeschaltet ist).

**Einen einzelnen TV mit Rich-Optionen ansprechen** – verwenden Sie den Parameter `target` des Domänendienstes `peek_it_ha.notify` (oder `peek_it_ha.tts` / `peek_it_ha.tts_stop`). Dies ist die **einzige** Möglichkeit, TTS, Ton oder Animationen an einen bestimmten TV zu senden: Die Entität `notify.<tv>` friert das `send_message`-Schema auf `message`+`title` ein (jeder zusätzliche Schlüssel → HTTP 400).

```yaml
# Rich-Benachrichtigung auf NUR EINEM TV
service: peek_it_ha.notify
data:
  target: <tv_device_id>   # über die UI; ein Gerätename oder eine IP funktioniert ebenfalls
  message: "Nur auf diesem TV"
  tts: "Bewegung erkannt"
  sound: "01_notify.wav"
```

```yaml
# Einfache Nachricht auf einem TV (ohne Rich-Optionen) – die notify-Entität genügt
service: notify.send_message
target:
  entity_id: notify.wohnzimmer_tv
data:
  message: "Nur auf diesem TV"
```

> Kein `target` → alle TVs (historisches, abwärtskompatibles Verhalten).

Die Integration und die App sind in **6 Sprachen** verfügbar: `en` (Standard), `fr`, `de`, `es`, `nl`, `pt`. Konfigurierbar im Designer oder in der App.

---

## 😅 WAF — Der ultimative KPI

Der legendäre **WAF** — *Wife Acceptance Factor*. Diese inoffizielle, aber absolut entscheidende Kennzahl, die die Toleranz Ihrer besseren Hälfte gegenüber Ihren Heimautomatisierungs-Experimenten misst.

- 🧺 **Intelligente Wäsche**: „Wäsche fertig!" erscheint dezent während des Films. Schluss mit 3 Tage lang vergessener Wäsche. *(WAF: +23)*
- ☀️ **Morgenwetter**: jeden Tag um 7:30 Uhr das Wetter auf dem Küchen-TV. *(WAF: +15)*
- 🔔 **Türklingelkamera**: Es klingelt, der Stream erscheint. Beratung vom Sofa aus. Niemand ist aufgestanden. *(WAF: +38)*
- ⚽ **Sport-Spielstand**: ein dezentes „2 - 1, 78'" für 3 Sekunden in der Ecke. Niemand hat umgeschaltet. *(WAF: +52)*

### Der Fall, der Ihren WAF RUINIERT

🌙 **Debugging in der Produktion**: Sie testen Ihre Benachrichtigungen um 23 Uhr während des großen Saisonfinales. „Test 1", „Lorem ipsum", „AAAA ES FUNKTIONIERT!", ein großes schwarzes Rechteck, dann nichts mehr …

> *(WAF: -347. Geschätzte Erholungszeit: 3 Wochen gutes Benehmen. Und ein Blumenstrauß.)*

**Profi-Tipp**: Testen Sie VOR 21 Uhr. Oder verwenden Sie die **KILL**-Taste des Designers. Sie existiert aus gutem Grund.

---

## 🔧 Fehlerbehebung

| Problem | Lösung |
|----------|----------|
| Integration nicht auffindbar | Ordner in `custom_components/peek_it_ha/`? Starten Sie HA neu. |
| „Verbindung nicht möglich" | Prüfen Sie IP/Port. Testen Sie `http://IP:8081/api/status` in einem Browser. |
| Sensor immer „offline" | Läuft die App? Startet der Dienst beim Booten? |
| Die Benachrichtigung wird nicht angezeigt | Prüfen Sie die Overlay-Berechtigung in den Android-TV-Einstellungen. |
| Der Designer verbindet sich nicht | Gleiches Netzwerk? Versuchen Sie `http://IP:PORT/`. |
| Die TV-Taste löst HA nicht aus | Rückmeldung TV → HA = Webhook: speichern Sie die *Einstellungen* der Integration erneut (übermittelt das `webhook_secret`) und prüfen Sie, dass `ha_ip` vom TV aus erreichbar ist. |
| Menü-Umschalter / Entitäts-Widgets funktionieren nicht | Direkter Aufruf App → HA: erstellen Sie ein **langlebiges Zugriffstoken (Long-Lived Access Token)** von HA und fügen Sie es in den Designer ein (siehe [Der Designer](https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-der-designer)). |
| Die ADB-Tasten schlagen fehl | ADB-Debugging (Port 5555) aktiviert und RSA-Schlüssel autorisiert? Siehe [ADB-Tasten](https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md#-konfigurationstasten-adb). |
| Das TTS spricht nicht | Ist eine TTS-Engine auf dem Android-TV installiert (Google TTS)? |
| Das Menü reagiert nicht auf das D-Pad | Das Menü-Element muss den Fokus haben; verwenden Sie `duration: 0`. |

---

## Mitwirken

Beiträge sind willkommen! Öffnen Sie ein Issue oder einen Pull Request im [GitHub-Repository](https://github.com/jolabs40/peek-it-ha).

## Lizenz

Projekt unter der MIT-Lizenz verteilt. Siehe die Datei [LICENSE](https://github.com/jolabs40/peek-it-ha/blob/master/LICENSE).

---

<p align="center">
  Gemacht mit Kaffee, viel zu vielen YAML-Dateien und einer unvernünftigen Liebe zu Overlays.<br/>
  <strong>Peek-it [HA]</strong> — weil Ihr TV viel mehr kann, als Sie denken.
</p>
