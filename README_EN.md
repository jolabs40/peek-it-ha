# Peek-it [HA] — Home Assistant Integration

<p align="center">
  <img src="https://raw.githubusercontent.com/jolabs40/peek-it-ha/master/custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Turn your Android TV into a smart notification display.</strong><br/>
  Alerts, cameras, dashboards, TTS, menus — overlaid on your TV in real time.
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
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-how-it-works">How it works</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-installation">Installation</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-the-designer">Designer</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-usage">Usage</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-text-to-speech-tts">TTS</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-automations">Automations</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-advanced-reference">Advanced reference</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-waf--the-ultimate-kpi">WAF</a>
</p>

<p align="center">
  <b>Languages:</b>
  English |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md">Fran&ccedil;ais</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md">Deutsch</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_ES.md">Espa&ntilde;ol</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_NL.md">Nederlands</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md">Portugu&ecirc;s</a>
</p>

---

## Why Peek-it [HA]?

Your Android TV device is plugged into your TV 24/7. Why not put it to work?

The **Peek-it [TV]** app displays **rich overlay notifications** on top of whatever app is currently running: a movie, broadcast TV, a game... Watching a match? The score updates in a corner. Someone rings the doorbell? The front-door camera appears instantly. And **you design** these displays yourself, without writing a single line of code.

> 💡 **The key takeaway**
>
> 1. **You design** your notifications (and even entire pages) in the **Designer**, a visual drag-and-drop editor accessible from any browser. *It builds everything for you — you have nothing to code.*
> 2. **You trigger** them from **Home Assistant** using this integration… or from **Tasker, Node-RED, Jeedom** or any other HTTP client, since the app exposes a simple local API.

> 🧩 **Two components, two roles**
> The **Peek-it [TV] app** (Android, on the Play Store) draws the overlay, hosts the Designer and the template engine: it is the authority.
> The **Peek-it [HA] integration** (this repository) drives it from Home Assistant: sending notifications/TTS, monitoring status, button callbacks.

### What you can display

| | |
|------|---------|
| 📝 **Rich text** | Titles, messages, counters, weather |
| 🖼️ **Images** | Photos, snapshots, logos, QR codes |
| 🎥 **RTSP video streams** | Live surveillance cameras, ultra-low latency |
| 🌐 **Web pages** | HA dashboards, charts, weather widgets |
| 🔺 **Shapes & SVG** | Rectangles, ellipses, hexagons, arrows, vector icons |
| 🎮 **Buttons & menus** | Navigable by remote, trigger your HA automations |
| 📊 **HA entities & charts** | Real-time state and history of entities |
| 🔊 **Text-to-speech** | Voice announcements straight to the TV |

### Key features

- **Zero latency** — native Android overlay, no streaming or casting
- **Works with everything** — the overlay displays on top of any app
- **Visual Designer** — create everything via drag-and-drop, real-time preview
- **Reusable templates** — design once, reuse with dynamic parameters
- **Multi-device** — manage multiple TVs from a single HA instance
- **Open** — drivable from HA, Tasker, Node-RED, Jeedom… via a local HTTP API
- **6 languages** — EN, FR, DE, ES, NL, PT

---

## 🧩 How it works

Three steps, from visual to automation:

| Step | Where | What you do |
|------|-----|--------------------|
| **1. Design** | 🎨 Designer (browser) | Drag and drop your elements onto a canvas calibrated to your TV. The Designer generates all the rendering for you. |
| **2. Save** | 🎨 Designer | Save your creation as a reusable **template** (a simple ID is generated). |
| **3. Trigger** | 🏠 Home Assistant | Call the template from an automation, in a few lines, with dynamic values. |

```yaml
# Step 3: trigger a template designed in the Designer
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Security alert"
    camera_url: "rtsp://192.168.1.50:554/stream1"
```

> ✅ **You almost never need to write JSON by hand.** The Designer handles the layout; on the Home Assistant side you only provide the template ID and a few values. The [Advanced reference](https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-advanced-reference) (raw JSON, widget types, API…) is there only for edge cases.

---

## 📥 Installation

### 1. Install the Peek-it [TV] app

**Recommended — Google Play Store**: search for **"Peek-it"** in the Play Store on your Android TV, or open the listing:
[play.google.com/store/apps/details?id=net.jolabs40.peekit](https://play.google.com/store/apps/details?id=net.jolabs40.peekit)

> Device without Play Store (some Android TV boxes, Fire TV…): sideload the APK from the [Releases page](https://github.com/jolabs40/peek-it-ha/releases) (USB stick, `adb install`, or a file manager).

Then, whichever method you used:

1. Launch the app — grant the **overlay permission** (display over other apps); the service starts automatically.
2. Note the **IP address** shown on the main screen (e.g. `192.168.1.42`). Default port: **8081**.

### 2. Install the Home Assistant integration

**Via HACS (recommended)**: HACS → *Integrations* → 3-dot menu → *Custom repositories* → add `https://github.com/jolabs40/peek-it-ha` (category *Integration*) → *Download* → **restart HA**.

<details>
<summary>Manual installation</summary>

Copy the `peek_it_ha/` folder into `config/custom_components/`, then restart Home Assistant:

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

### 3. Add the integration

*Settings → Devices & Services → Add Integration → Peek-it [HA]*. Enter the **IP**, the **port** (`8081`), a **name** and, if the TV app requires it, an **API key**. If the device is published via Zeroconf (`_peekit._tcp`), HA can also **discover it automatically**.

<details>
<summary>What is created automatically (HA entities)</summary>

All entities are grouped into a **single device card**. For each TV:

| Entity | Type | Description |
|--------|------|-------------|
| `binary_sensor.<name>_status` | Connectivity | Online / offline (polled every 30 s); exposes the `designer_url` attribute |
| `binary_sensor.<name>_overlay_permission` | Diagnostic | Overlay permission granted |
| `binary_sensor.<name>_accessibility_permission` | Diagnostic | Accessibility service active |
| `binary_sensor.<name>_microphone_permission` | Diagnostic | Microphone permission granted |
| `notify.<name>` | Notify | Send notifications |
| `button.<name>_*_assist / overlay / accessibility` | Config (×6) | Enable/disable permissions via ADB — see [ADB buttons](https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-configuration-buttons-adb) |

A single `GET /api/status` request is issued per TV every 30 s; all entities share this snapshot (shared coordinator).
</details>

---

## 🎨 The Designer

**The heart of Peek-it.** This is where you create your notifications and pages — visually, without coding. It is a **web editor embedded in the app**, accessible from any browser on the local network:

**URL**: `http://<TV_IP>:<PORT>/` (e.g. `http://192.168.1.42:8081/`) — also reachable via the `designer_url` attribute of the status sensor, or *gear icon → Designer* in the integration options.

- **Drag and drop** your widgets onto a canvas calibrated to the actual resolution of your TV (16:9, 21:9…)
- **Real-time JSON preview** — you watch the render being built
- **Template library** — save, load, rename, export/import
- **Dynamic parameters** — mark the variable elements (`paramKey`) to fill them from HA
- **Configuration** of the default sound, the language, and the **HA access token** (see below)
- **SEND buttons** (send to the TV) and **KILL** (close) to test immediately

> 🔑 **Home Assistant access token (optional).** Some features require the app to call HA's API **directly**: toggling an entity from a menu, showing an entity's state in real time, drawing a history chart, or displaying a camera snapshot. For this, create a **long-lived access token** in HA (*your profile → at the very bottom → Long-Lived Access Tokens → Create*) and paste it into the Designer settings. It is stored encrypted on the TV. Not needed if you only send notifications from HA.
>
> Not to be confused with the **webhook secret** (`X-Peek-Secret`), which works in the other direction (TV button callbacks → HA) and which the integration manages **automatically**.

> From HA, *gear icon → Templates* lists all your templates with their **ID** (copyable) and their **parameters**, sorted into *Official* / *Custom* / *Drafts*.

---

## 🚀 Usage

Three ways to send, from the simplest to the most advanced. **The template mode is the most convenient**: it builds on your Designer creations.

### Simple message

Text displayed at the bottom of the screen on a dark background — ideal for a quick alert.

```yaml
service: peek_it_ha.notify
data:
  message: "The washing machine is done!"
  title: "Home"
  duration: 8000
```

### Template + parameters *(recommended)*

Reuse a template designed in the Designer by injecting dynamic values.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Security alert"
    message: "Motion detected in the garden"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

The server loads the template, replaces the `{{placeholders}}` with the values from `params`, and displays the result.

### Close / keep a notification

```yaml
# Close immediately
service: peek_it_ha.notify
data:
  action: CLOSE
```

`duration: 0` keeps the notification on screen until an explicit `CLOSE` or a button press.

<details>
<summary><b>Advanced mode — raw elements (full JSON)</b></summary>

For cases where you want to define each widget by hand, without going through a template. *In practice, the Designer does all of this visually.*

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
      content: "Garden camera"
      style: { left: 62, top: 28, width: 34, height: 5, size: 18, color: "#FFFFFF", align: center }
```

The full vocabulary (widget types, style properties) is documented in the [Advanced reference](https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-advanced-reference).
</details>

---

## 🔔 Text-to-speech (TTS)

Make the TV speak, on its own or alongside a notification.

```yaml
# Standalone TTS
service: peek_it_ha.tts
data:
  text: "Dinner is ready!"
  lang: "en"
  speed: 1.0     # 0.5 to 2.0
  volume: 1.0    # 0.0 to 1.0
```

```yaml
# TTS with a visual notification
service: peek_it_ha.notify
data:
  message: "Motion detected in the garden"
  title: "Security"
  tts: "Motion detected in the garden"
  ttsLang: "en"
  ttsSpeed: 1.25
```

Stop playback: `service: peek_it_ha.tts_stop`. In `notify`, the fields are prefixed `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

## 🔊 Sound

```yaml
service: peek_it_ha.notify
data:
  message: "Package delivered"
  sound: "01_notify.wav"
  soundVolume: 0.8   # 0.0 to 1.0
```

The app ships with built-in sounds and accepts your custom sounds (via the Designer).

---

## 📺 Configuration buttons (ADB)

The integration exposes **6 buttons** (*Config* category) that drive the TV via **ADB over TCP**, to set in one click those permissions that are painful to enable with the remote:

| Button | Action on the TV |
|--------|------------------|
| **Enable / Disable Assist** | Sets / restores Peek-it as the default assistant |
| **Enable / Disable Overlay** | Grants / revokes the `SYSTEM_ALERT_WINDOW` permission |
| **Enable / Disable Accessibility** | Enables / disables the `MenuKeyService` accessibility service |

<details>
<summary>ADB prerequisites (one-time setup)</summary>

The buttons use the `adb-shell` library (installed automatically by HA) and connect to the TV's IP on **port 5555**.

1. **Enable network ADB debugging**: *Settings → Device Preferences → About →* tap *Build* 7 times, then *Developer options →* **USB debugging** (and **Wireless debugging** if offered).
2. **Authorize the RSA key on the first press**: an "Allow debugging?" dialog appears on the TV → check *Always allow*. The key is generated once and stored in `.storage/peek_it_adb_key`.
3. The official **Android TV** integration is recommended (HA flags this in *Repairs*) for stable ADB management.

If `adb-shell` is missing or the TV refuses the connection, the action fails with an error in the HA log.
</details>

---

## 🤖 Automations

### Motion alert with camera

```yaml
automation:
  - alias: "Garden motion alert"
    trigger:
      - platform: state
        entity_id: binary_sensor.garden_motion
        to: "on"
    action:
      - service: peek_it_ha.notify
        data:
          template_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
          params:
            title: "Motion detected!"
            camera_url: "rtsp://192.168.1.50:554/stream1"
          duration: 15000
          animationIn: slide_right
```

### Morning weather bulletin

```yaml
automation:
  - alias: "Morning weather"
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
          title: "Today's weather"
```

### Button callback to HA

Pressing a notification button (remote) triggers an HA event:

```yaml
automation:
  - alias: "TV button - Turn off lights"
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
<summary>Persistent alert with a close button (raw JSON)</summary>

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  animationIn: pop
  priority: urgent
  tts: "Warning! Water leak detected!"
  ttsLang: "en"
  elements:
    - type: rect
      style: { left: 20, top: 20, width: 60, height: 60, bgColor: "#EE990000", radius: 20 }
    - type: text
      content: "WATER LEAK DETECTED"
      style: { left: 25, top: 30, width: 50, height: 10, size: 40, color: "#FFFFFF", weight: bold, align: center }
    - type: button
      content: "Got it"
      action: CLOSE
      focusable: true
      directFocus: true
      style: { left: 35, top: 55, width: 30, height: 10, size: 24, color: "#FFFFFF", bgColor: "#CC333333", align: center, radius: 10, focusColor: "#FF6666", focusBgColor: "#CC660000" }
```
</details>

<details>
<summary>RTSP camera stream</summary>

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

Ultra-low latency (~50 ms) thanks to an optimized ExoPlayer configuration.
</details>

---

## 🧰 Advanced reference

> 🛟 **You normally don't need this section.** The Designer builds your notifications visually and provides ready-to-use templates. What follows is only useful for the raw JSON mode, the API, or third-party integrations.

<details>
<summary><b>Parameters of the <code>notify</code> service</b></summary>

| Parameter | Type | Default | Description |
|-----------|------|--------|-------------|
| `action` | string | `DISPLAY` | `DISPLAY` to show, `CLOSE` to close |
| `duration` | int | `10000` | Duration in ms (0 = infinite) |
| `priority` | string | `normal` | `normal` or `urgent` |
| `animationIn` / `animationOut` | string | `fade` | See animations below |
| `template_id` | string | — | UUID of the template to use |
| `params` | dict | — | Dynamic values for the template |
| `elements` | list | — | List of widgets (raw JSON mode) |
| `message` / `title` | string | — | Simple message mode |
| `sound` / `soundVolume` | string / float | — / `1.0` | Sound and volume (0.0-1.0) |
| `tts` / `ttsLang` / `ttsSpeed` / `ttsPitch` / `ttsVolume` | — | — | TTS read with the notification |

**Animations**: `none`, `fade`, `slide_right`, `slide_left`, `slide_top`, `slide_bottom`, `pop` (entry and exit are independent).
</details>

<details>
<summary><b>Widget types</b></summary>

The type is interpreted by the app. **Any unrecognized type (`text`, `message`, `title`, `button`…) is rendered as a text widget**; a `button` is distinguished by `focusable` + `action`. If `content` starts with `mdi:` (e.g. `mdi:home-assistant`), a **Material Design Icons** icon is displayed.

| Type | Description | `content` |
|------|-------------|-----------|
| `text` | Static text (default type) | The text, or `mdi:<icon>` |
| `button` | Interactive text (focusable, action) | Label |
| `rect` | Rectangle / container | — |
| `ellipse` | Ellipse / oval | — |
| `hexagon` | Hexagon | — |
| `circle` | Round container (image / MDI icon) | URL or `mdi:<icon>` |
| `image` | PNG/JPG image | URL |
| `video` | RTSP / HTTP stream | URL |
| `webview` | Embedded web page | URL |
| `svg` | Vector image | URL or path |
| `line` / `arrow` | Line / arrow | — |
| `confetti` | Full-screen confetti animation | — |
| `menu` | Interactive D-pad menu | MenuConfig JSON |

> Older examples using `type: box` still display (text fallback + `bgColor`), but the canonical rectangle type is `rect`.
</details>

<details>
<summary><b>Style and interaction properties</b></summary>

**Style**: `left`, `top`, `width`, `height` (in % of the screen, 0-100) · `color` · `bgColor` (hex with alpha) · `size` · `font` · `weight` (`normal`/`bold`) · `align` (`left`/`center`/`right`) · `opacity` · `radius` · `borderWidth` · `borderColor` · `rotation` · `focusColor` · `focusBgColor`.

**Interaction (buttons)**: `focusable` (receives remote focus) · `directFocus` (focus on display) · `action` (`CLOSE` or a custom ID for the webhook) · `paramKey` (binds the content to a template parameter) · `actionParamKey` (binds the action to a parameter).
</details>

<details>
<summary><b>Interactive menu (JSON config)</b></summary>

The `menu` widget creates an overlay menu navigable with the D-pad (submenus, HA entity toggles, actions).

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Quick controls",
          "items": [
            {"type": "submenu", "label": "Lights", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Living room", "entity_id": "light.living_room"},
              {"type": "close", "label": "Back"}
            ]},
            {"type": "action", "label": "Movie mode", "action": "movie_mode"},
            {"type": "close", "label": "Close"}
          ]
        }
      style: { left: 35, top: 10, width: 30, height: 80 }
```

| Item type | Role |
|------|-------------|
| `action` | Triggers `peekit_button_press` with the `action` ID |
| `submenu` | Opens a submenu (`children`) |
| `toggle` | Toggles an HA entity (`entity_id`), state refreshed every 5 s |
| `text` | Informational text |
| `close` | Closes the menu |

**Navigation**: Up/Down to navigate · Right/Enter to open a submenu · Left/Back to go back · Back at the root closes.
</details>

<details>
<summary><b>HA entity widgets, charts & overlays (app capabilities)</b></summary>

These features are configured on the **app** side (Designer); the HA integration does not drive them directly. They require an **HA long-lived access token** entered in the Designer (cf. [The Designer](https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-the-designer)), since the app calls HA's API directly.

- **HA entity widget**: a `webview` connected over WebSocket/REST displays entity state in real time.
- **HA charts**: area / line / bar, rendered in pure CSS/SVG.
- **Overlay clock** (`/api/config/clock`): 12h/24h format, position, color, opacity.
- **Dimming** (`/api/config/dimming`): color and opacity of a background layer.
</details>

<details>
<summary><b>API & webhook (for Tasker, Node-RED, Jeedom, developers)</b></summary>

The app exposes a local HTTP API (port `8081`). If an API key is configured, **all** requests carry the `X-API-Key: <key>` header. This is the API that any HTTP client (Tasker, Node-RED, Jeedom…) can call.

| Endpoint | Method | Usage |
|---|---|---|
| `/api/status` | GET | Status, permissions, resolution |
| `/api/notify` | POST | Display / close a notification |
| `/api/tts` · `/api/tts/stop` | POST | Text-to-speech |
| `/api/templates/list` | GET | List of templates |

**Response of `/api/status`**:
```json
{
  "status": "online", "version": "v10.9", "device_name": "Living Room TV",
  "api_key_required": false, "api_key_valid": true,
  "screen": { "width": 1920, "height": 1080, "density": 1.0 },
  "permissions": { "overlay": true, "accessibility": false, "microphone": true }
}
```

**Webhook (callbacks from the TV → HA)**: `/api/webhook/peek_it_debug`. Since 1.1.0, every request must present the **`X-Peek-Secret`** header (otherwise HTTP 401). The secret is delivered to the TV via the **welcome notification** (`webhook_secret` field) when the entry is created/saved.

| `level` | `message` | HA effect |
|---------|-----------|----------|
| `ACTION` | `BUTTON_CLICK:<id>` | Emits the `peekit_button_press` event `{ "action": "<id>" }` |
| `ERROR` / `WARN` / `INFO` | text | Logged as `[PEEK-IT REPORT]` |

> **Migration from 1.0.0**: *Configure → Settings → Validate* to push a new welcome notification containing the `webhook_secret`.
</details>

---

## 🌍 Multi-device & languages

Add each TV as a separate integration. The `notify`, `tts`, `tts_stop` and `get_templates` services apply to **all devices**. To target a single TV:

```yaml
service: notify.send_message
target:
  entity_id: notify.living_room_tv
data:
  message: "Only on this TV"
```

The integration and the app are available in **6 languages**: `en` (default), `fr`, `de`, `es`, `nl`, `pt`. Configurable in the Designer or the app.

---

## 😅 WAF — The ultimate KPI

The legendary **WAF** — *Wife Acceptance Factor*. That unofficial but absolutely crucial metric measuring your significant other's tolerance for your home-automation experiments.

- 🧺 **Smart laundry**: "Laundry done!" appears discreetly during the movie. No more loads forgotten for 3 days. *(WAF: +23)*
- ☀️ **Morning weather**: every day at 7:30 a.m., the weather on the kitchen TV. *(WAF: +15)*
- 🔔 **Doorbell camera**: someone rings, the stream appears. Deliberation from the couch. Nobody got up. *(WAF: +38)*
- ⚽ **Sports score**: a discreet "2 - 1, 78'" for 3 seconds in the corner. Nobody changed the channel. *(WAF: +52)*

### The case that RUINS your WAF

🌙 **Debugging in production**: you test your notifications at 11 p.m. during the season finale. "Test 1", "Lorem ipsum", "AAAA IT WORKS!", a big black rectangle, then nothing...

> *(WAF: -347. Estimated recovery: 3 weeks of good behavior. And a bouquet of flowers.)*

**Pro tip**: test BEFORE 9 p.m. Or use the **KILL** button in the Designer. It exists for a reason.

---

## 🔧 Troubleshooting

| Problem | Solution |
|----------|----------|
| Integration not found | Folder in `custom_components/peek_it_ha/`? Restart HA. |
| "Cannot connect" | Check IP/port. Test `http://IP:8081/api/status` in a browser. |
| Sensor always "offline" | Is the app running? Does the service start at boot? |
| The notification doesn't display | Check the overlay permission in the Android TV settings. |
| The Designer won't connect | Same network? Try `http://IP:PORT/`. |
| The TV button doesn't trigger HA | TV → HA callback = webhook: re-save the integration *Settings* (delivers the `webhook_secret`) and check that `ha_ip` is reachable from the TV. |
| Menu toggles / entity widgets don't work | Direct app → HA call: create an HA **long-lived access token** and paste it into the Designer (see [The Designer](https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-the-designer)). |
| The ADB buttons fail | ADB debugging (port 5555) enabled and RSA key authorized? See [ADB buttons](https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md#-configuration-buttons-adb). |
| TTS won't speak | Is a TTS engine installed on the Android TV (Google TTS)? |
| The menu doesn't respond to the D-pad | The menu element must have focus; use `duration: 0`. |

---

## Contributing

Contributions are welcome! Open an issue or a pull request on the [GitHub repository](https://github.com/jolabs40/peek-it-ha).

## License

Project distributed under the MIT license. See the [LICENSE](https://github.com/jolabs40/peek-it-ha/blob/master/LICENSE) file.

---

<p align="center">
  Made with coffee, way too many YAML files, and an unreasonable love of overlays.<br/>
  <strong>Peek-it [HA]</strong> — because your TV can do a lot more than you think.
</p>
