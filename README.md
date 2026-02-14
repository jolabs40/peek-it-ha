# Peek-it [HA] — Home Assistant Integration

<p align="center">
  <img src="custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Turn your Android TV into a smart notification display.</strong><br/>
  Alerts, cameras, dashboards, TTS, menus — overlay on your TV in real time.
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
  <a href="#-usage">Usage</a> •
  <a href="#-the-designer">Designer</a> •
  <a href="#-templates--parameters">Templates</a> •
  <a href="#-text-to-speech-tts">TTS</a> •
  <a href="#-sound">Sound</a> •
  <a href="#-interactive-menu">Menu</a> •
  <a href="#-automations">Automations</a> •
  <a href="#-waf--the-ultimate-kpi">WAF</a>
</p>

<p align="center">
  <b>Languages:</b>
  English |
  <a href="README_FR.md">Fran&ccedil;ais</a> |
  <a href="README_DE.md">Deutsch</a> |
  <a href="README_ES.md">Espa&ntilde;ol</a> |
  <a href="README_NL.md">Nederlands</a> |
  <a href="README_PT.md">Portugu&ecirc;s</a>
</p>

---

## Why Peek-it [HA]?

Your Android TV device is plugged into your TV 24/7. Why not put it to work?

**Peek-it [HA]** is the Home Assistant integration for the **Peek-it [TV]** Android app. Together, they display **rich overlay notifications** on top of any running application. Watching a movie? A camera feed pops up for 5 seconds in the corner. Sports night? The score updates in real time. Doorbell rings? The front door camera appears instantly.

### What you can display

| Type | Example |
|------|---------|
| **Rich text** | Titles, messages, counters, weather |
| **Images** | Photos, snapshots, logos, QR codes |
| **RTSP video streams** | Live security cameras, ultra-low latency |
| **Web pages** | HA dashboards, charts, weather widgets |
| **SVG** | Vector icons, gauges, diagrams |
| **Shapes** | Rectangles, ellipses, lines, arrows — build complete layouts |
| **Interactive buttons** | TV remote-controlled, trigger HA automations |
| **Interactive menus** | D-pad navigable menus with HA entity toggles |
| **HA entity widgets** | Real-time entity state display via WebSocket/REST |
| **HA charts** | CSS/SVG area, line, and bar charts |
| **Text-to-speech** | Voice announcements on your TV |

### Key features

- **Zero latency** — native Android overlay, no streaming or casting
- **Works with everything** — the overlay goes on top of any app
- **Visual Designer** — create notifications with drag & drop from any browser
- **Reusable templates** — design once, reuse with dynamic parameters
- **7 animations** — fade, slide, pop... independent entrance and exit effects
- **Text-to-speech** — voice announcements directly on the TV
- **Sound alerts** — play notification sounds alongside visuals
- **Interactive menus** — D-pad navigable overlay menus with HA toggles
- **Multi-device** — manage multiple TVs from a single HA instance
- **6 languages** — EN, FR, DE, ES, NL, PT

---

## Prerequisites

1. **An Android TV device** running the **Peek-it [TV]** app
2. **Home Assistant** installed and running
3. Both devices on the **same local network**

### Install the Peek-it [TV] app

> The app is not (yet) on the Play Store. Install it via sideload.

1. Download the APK from the [Releases page](https://github.com/jolabs40/peek-it-ha/releases)
2. Transfer it to your device (USB drive, `adb install`, or a file manager app)
3. Launch the app — it will request the overlay permission (display over other apps)
4. Grant the permission — the service starts automatically
5. Note the **IP address** shown on the main screen (e.g., `192.168.1.42`)
6. Default port is **8081** (configurable in the app)

> **Tip**: The service auto-starts on device boot. Plug it in, forget about it.

---

## Installation

### Method 1: HACS (recommended)

1. Open HACS in Home Assistant
2. Go to **Integrations** > 3-dot menu > **Custom repositories**
3. Add the repository URL: `https://github.com/jolabs40/peek-it-ha`
4. Category: **Integration**
5. Click **Peek-it [HA]** > **Download**
6. **Restart Home Assistant**

### Method 2: Manual installation

1. Copy the `peek_it_ha/` folder into your `custom_components/` directory:
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
2. **Restart Home Assistant**

### Adding the integration

1. Go to **Settings** > **Devices & Services** > **Add Integration**
2. Search for **Peek-it [HA]**
3. Fill in:
   - **IP Address**: your Android TV device IP (shown in the app)
   - **Port**: `8081` (default)
   - **Name**: a friendly name for your TV (e.g., "Living Room TV")
   - **API Key**: if authentication is enabled on the TV app
4. Submit — the integration tests the connection and configures itself

### What gets created automatically

| Entity | Type | Description |
|--------|------|-------------|
| `binary_sensor.living_room_tv_status` | Binary Sensor | Connection status (online/offline), polls every 30s |
| `notify.living_room_tv` | Notify | Notification sending entity |

The `binary_sensor` also exposes a `designer_url` attribute with a direct link to the web Designer.

---

## Integration options (gear icon)

Click the **gear icon** on the Peek-it [HA] integration card to access 3 menus:

### Settings

Edit the IP, port, name or API key. The integration reloads automatically after saving.

### Templates

Browse all templates available on your TV, sorted by category:

- **Official** — built-in templates shipped with the app
- **Custom** — your finalized templates, each with a unique UUID
- **Drafts** — work in progress, no ID assigned yet

Each template shows its **name**, **ID** (copyable), and available **parameters**.

### Designer

Direct link to open the web Designer in a new tab. Handy for editing templates without leaving HA.

---

## Usage

### Mode 1: Simple message

The quickest way — send a text message that appears at the bottom of the screen with a dark background.

```yaml
service: peek_it_ha.notify
data:
  message: "The washing machine is done!"
  title: "Home"
  duration: 8000
```

### Mode 2: Template + parameters

The most practical — reuse an existing template by injecting dynamic values.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Security Alert"
    message: "Motion detected in the garden"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

The server loads the template, replaces `{{placeholders}}` with `params` values, and displays the result.

**How to find the template_id?**
- In the Designer: click the green "ID" badge on a template in the library
- In HA: gear icon > Templates > copy the displayed ID
- Via service: `peek_it_ha.get_templates` returns the full list

### Mode 3: Raw elements (full JSON)

The most flexible — define each widget manually.

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
      content: "Garden Camera"
      style:
        left: 62
        top: 28
        width: 34
        height: 5
        size: 18
        color: "#FFFFFF"
        align: center
```

### Close a notification

```yaml
service: peek_it_ha.notify
data:
  action: CLOSE
```

### Persistent (infinite) notification

```yaml
service: peek_it_ha.notify
data:
  message: "Waiting for confirmation..."
  duration: 0
```

Duration `0` = the notification stays on screen until an explicit `CLOSE` or a button press.

---

## Text-to-speech (TTS)

### Standalone TTS

Send a voice message to all configured TVs:

```yaml
service: peek_it_ha.tts
data:
  text: "Dinner is ready!"
  lang: "en"
  speed: 1.0
  pitch: 1.0
  volume: 1.0
```

### Stop TTS

```yaml
service: peek_it_ha.tts_stop
```

### TTS with notification

Combine a visual notification with a voice message:

```yaml
service: peek_it_ha.notify
data:
  message: "Motion detected in the garden"
  title: "Security"
  duration: 10000
  tts: "Motion detected in the garden"
  ttsLang: "en"
  ttsSpeed: 1.25
  ttsVolume: 0.8
```

### TTS parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | string | — | Text to speak (standalone service) |
| `lang` | string | `en` | Language code (en, fr, de, es, nl, pt) |
| `speed` | float | `1.0` | Speech rate (0.5 to 2.0) |
| `pitch` | float | `1.0` | Voice pitch (0.5 to 2.0) |
| `volume` | float | `1.0` | Volume (0.0 to 1.0) |

When used inside `peek_it_ha.notify`, the fields are prefixed: `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

---

## Sound

Play a sound with your notification:

```yaml
service: peek_it_ha.notify
data:
  message: "Package delivered"
  title: "Doorbell"
  sound: "01_notify.wav"
  soundVolume: 0.8
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `sound` | string | — | Sound file name (e.g., "01_notify.wav") |
| `soundVolume` | float | `1.0` | Volume (0.0 to 1.0) |

The Peek-it [TV] app ships with built-in sounds and supports custom sound uploads via the Designer.

---

## Interactive menu

The `menu` widget type creates a D-pad navigable overlay menu on the TV. Menus support sub-menus, HA entity toggles with real-time state polling, action callbacks, and close buttons.

### Menu example via automation

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Quick Controls",
          "titleIcon": "mdi:menu",
          "bgColor": "#1E1E1E",
          "textColor": "#FFFFFF",
          "accentColor": "#00E676",
          "items": [
            {"type": "submenu", "label": "Lights", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Living Room", "icon": "mdi:lightbulb", "entity_id": "light.living_room"},
              {"type": "toggle", "label": "Kitchen", "icon": "mdi:lightbulb", "entity_id": "light.kitchen"},
              {"type": "close", "label": "Back", "icon": "mdi:arrow-left"}
            ]},
            {"type": "action", "label": "Movie Mode", "icon": "mdi:movie", "action": "movie_mode"},
            {"type": "close", "label": "Close", "icon": "mdi:close"}
          ]
        }
      style:
        left: 35
        top: 10
        width: 30
        height: 80
```

### Menu item types

| Type | Description |
|------|-------------|
| `action` | Triggers an HA event (`peekit_button_press`) with the specified `action` ID |
| `submenu` | Opens a nested sub-menu with its own `children` items |
| `toggle` | Toggles an HA entity (requires `entity_id`), polls state every 5s |
| `text` | Informational text (non-interactive) |
| `close` | Closes the menu |

### Navigation

- **Up/Down**: navigate between items
- **Right/Enter**: open a submenu
- **Left/Back**: go back to parent menu
- **Back on root**: close the menu

---

## HA entity widget

Display real-time HA entity states directly on the TV using a `webview` widget connected via WebSocket or REST polling.

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

## HA chart widget

The Peek-it [TV] app supports CSS/SVG charts for displaying entity history. Chart types: **area**, **line**, and **bar**.

Charts are rendered as pure CSS/SVG — no external libraries required. Configure them through the Designer's chart editor.

---

## Overlay configuration

### Clock overlay

The Peek-it [TV] app can display a persistent clock overlay. Configure it via the Designer Settings or the `/api/config/clock` endpoint:

- Enable/disable
- Format (12h/24h)
- Position, color, size, opacity

### Dimming overlay

A configurable background dimming layer. Configure via the Designer Settings or `/api/config/dimming`:

- Enable/disable
- Color, opacity

---

## Available parameters

### Main fields

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `action` | string | `DISPLAY` | `DISPLAY` to show, `CLOSE` to dismiss |
| `duration` | int | `10000` | Duration in milliseconds (0 = infinite) |
| `priority` | string | `normal` | `normal` or `urgent` |
| `animationIn` | string | `fade` | Entrance animation |
| `animationOut` | string | `fade` | Exit animation |
| `template_id` | string | — | UUID of the template to use |
| `params` | dict | — | Dynamic template parameters |
| `elements` | list | — | Widget list (advanced mode) |
| `message` | string | — | Simple text (simple mode) |
| `title` | string | — | Title text (simple mode) |
| `sound` | string | — | Sound file name |
| `soundVolume` | float | `1.0` | Sound volume (0.0-1.0) |
| `tts` | string | — | TTS text (read aloud with notification) |
| `ttsLang` | string | `en` | TTS language code |
| `ttsSpeed` | float | `1.0` | TTS speech rate (0.5-2.0) |
| `ttsPitch` | float | `1.0` | TTS voice pitch (0.5-2.0) |
| `ttsVolume` | float | `1.0` | TTS volume (0.0-1.0) |

### Available animations

| Name | Effect |
|------|--------|
| `none` | Instant, no animation |
| `fade` | Fade in/out |
| `slide_right` | Slide from/to the right |
| `slide_left` | Slide from/to the left |
| `slide_top` | Slide from/to the top |
| `slide_bottom` | Slide from/to the bottom |
| `pop` | Zoom/scale effect |

### Widget types

| Type | Description | Content (`content`) |
|------|-------------|---------------------|
| `text` | Static text | The text to display |
| `button` | Interactive button (TV remote) | Button label |
| `box` | Rectangle / container | — |
| `circle` | Circle | — |
| `ellipse` | Ellipse / oval | — |
| `image` | Image (PNG, JPG, URL) | Image URL |
| `video` | RTSP / HTTP video stream | Stream URL |
| `webview` | Embedded web page | Page URL |
| `svg` | SVG vector image | URL or SVG path |
| `line` | Horizontal line | — |
| `arrow` | Arrow (pointing right) | — |
| `menu` | Interactive D-pad menu | JSON MenuConfig |

### Style properties

| Property | Type | Description |
|----------|------|-------------|
| `left` | float | X position in % of screen (0-100) |
| `top` | float | Y position in % of screen (0-100) |
| `width` | float | Width in % of screen |
| `height` | float | Height in % of screen |
| `color` | string | Text color (hex, e.g., `#FFFFFF`) |
| `bgColor` | string | Background color (hex with alpha, e.g., `#CC000000`) |
| `size` | int | Font size |
| `font` | string | Font family (Roboto, sans-serif, etc.) |
| `weight` | string | Font weight (`normal`, `bold`) |
| `align` | string | Alignment (`left`, `center`, `right`) |
| `opacity` | float | Opacity (0.0 to 1.0) |
| `radius` | int | Corner radius (pixels) |
| `borderWidth` | int | Border thickness (pixels) |
| `borderColor` | string | Border color (hex) |
| `rotation` | float | Rotation in degrees |
| `focusColor` | string | Border color when focused |
| `focusBgColor` | string | Background color when focused |

### Interaction properties (buttons)

| Property | Type | Description |
|----------|------|-------------|
| `focusable` | bool | Widget receives TV remote focus |
| `directFocus` | bool | Widget gets focus on display |
| `action` | string | `CLOSE` to dismiss, or custom ID for webhook |
| `paramKey` | string | Links content to a template parameter |
| `actionParamKey` | string | Links action to a template parameter |

---

## The Designer

The Designer is a **visual web editor** embedded in the Peek-it [TV] app. Access it from any browser on your local network.

**URL**: `http://<TV_IP>:<PORT>/` (e.g., `http://192.168.1.42:8081/`)

You can also access it via:
- The `designer_url` attribute of the binary_sensor in HA
- The gear icon > Designer in the integration options

### Features

- **11 widget types** — drag & drop onto a calibrated TV canvas
- **Real-time JSON preview** — see the exact payload being built
- **Template library** — save, load, rename, delete, export/import
- **Parameter system** — define `paramKey` on widgets for dynamic content
- **Auto-calibration** — adapts to your TV's real resolution (16:9, 21:9, etc.)
- **Sound configuration** — default notification sound settings
- **HA token configuration** — required for webhook callbacks
- **Internationalization** — available in 6 languages (EN, FR, DE, ES, NL, PT)

### Send and test

- **SEND button** (blue) — sends the current layout to the TV immediately
- **KILL button** (red) — closes the current notification
- **JSON preview** (footer) — see the exact payload that will be sent

---

## Templates & parameters

### Concept

A template is a reusable notification layout. Instead of sending 15 lines of JSON every time, you:

1. **Create** the layout in the Designer (drag & drop)
2. **Define parameters** (`paramKey`) on dynamic elements
3. **Save** as Custom (UUID generated)
4. **Use** the `template_id` + `params` in your automations

### Retrieve the template list

```yaml
service: peek_it_ha.get_templates
response_variable: result
```

Returns a dictionary per configured device:
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

## Automations

### Motion detection alert

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
          animationOut: fade
```

### Morning weather briefing

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
          title: "Today's Weather"
          duration: 10000
          animationIn: fade
```

### TTS announcement automation

```yaml
automation:
  - alias: "Doorbell TTS alert"
    trigger:
      - platform: state
        entity_id: binary_sensor.doorbell
        to: "on"
    action:
      - service: peek_it_ha.tts
        data:
          text: "Someone is at the front door"
          lang: "en"
          speed: 1.25
          volume: 1.0
```

### Notification with sound

```yaml
automation:
  - alias: "Laundry done alert"
    trigger:
      - platform: state
        entity_id: sensor.washing_machine
        to: "idle"
    action:
      - service: peek_it_ha.notify
        data:
          message: "The washing machine is done!"
          title: "Laundry"
          duration: 8000
          sound: "08-notify.mp3"
          soundVolume: 0.7
```

### Interactive buttons — feedback to HA

When a user presses a button in a notification (via the TV remote), an HA event is fired:

```yaml
automation:
  - alias: "TV Button - Lights off"
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

### Persistent alert with dismiss button

```yaml
automation:
  - alias: "Water leak alert"
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
          tts: "Warning! Water leak detected!"
          ttsLang: "en"
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
              content: "WATER LEAK DETECTED"
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
              content: "Got it"
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

### RTSP camera feed

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

The feed displays with ultra-low latency (~50ms) thanks to an optimized ExoPlayer setup.

---

## Services reference

| Service | Description |
|---------|-------------|
| `peek_it_ha.notify` | Send notification to all configured devices |
| `peek_it_ha.get_templates` | Retrieve template list from all devices |
| `peek_it_ha.tts` | Send TTS to all configured devices |
| `peek_it_ha.tts_stop` | Stop TTS on all configured devices |

---

## Webhooks & events

The integration listens for a webhook to receive logs and button actions from the TV.

| HA Event | Trigger | Data |
|----------|---------|------|
| `peekit_button_press` | Button press on the TV | `{ "action": "button_id" }` |

TV logs are forwarded to the HA logger with the prefix `[PEEK-IT REPORT]`.

---

## Multi-device

The integration supports **multiple devices**. Add each TV as a separate integration. The `peek_it_ha.notify`, `tts`, `tts_stop`, and `get_templates` services automatically send to **all configured devices**.

To target a single device, use the specific `notify` entity:

```yaml
service: notify.send_message
target:
  entity_id: notify.living_room_tv
data:
  message: "Only on this TV"
```

---

## Internationalization

The integration and the Peek-it [TV] app support **6 languages**:

| Code | Language |
|------|----------|
| `en` | English (default) |
| `fr` | French |
| `de` | German |
| `es` | Spanish |
| `nl` | Dutch |
| `pt` | Portuguese |

Language can be configured in the Designer settings or on the Peek-it [TV] app settings screen.

---

## WAF — The Ultimate KPI

The legendary **WAF** — *Wife Acceptance Factor*. That unofficial yet critical metric that measures your partner's tolerance for your home automation experiments.

### Use cases that boost your WAF

**Smart laundry**: a "Laundry done!" notification pops up discreetly during the movie. No more loads forgotten for 3 days.

> *(WAF: +23 points)*

**Morning weather**: every day at 7:30 AM, the weather pops up on the kitchen TV.

> *(WAF: +15 points)*

**Doorbell camera**: someone rings, the camera feed pops up on screen. Judgment call from the couch. Nobody had to get up.

> *(WAF: +38 points)*

**Sports score**: a discreet "2 - 1, 78'" appears for 3 seconds in the top-right corner. Everyone's happy. Nobody changed the channel.

> *(WAF: +52 points)*

### The use case that TANKS your WAF

**Debugging in production**: you're testing your notifications at 11 PM while your partner watches the season finale.

> *(WAF: -347 points. Estimated recovery: 3 weeks.)*

**Pro tip**: test your automations BEFORE 9 PM. Or use the **KILL** button in the Designer.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Integration not found in HA | Make sure the folder is in `custom_components/peek_it_ha/`. Restart HA. |
| "Cannot connect" on setup | Check the IP and port. The app must be running on the TV. Test `http://IP:8081/api/status` in a browser. |
| Binary sensor always "offline" | Is the Peek-it [TV] app running? Does the service start on boot? |
| Notification doesn't show | Check the overlay permission in Android TV settings. |
| Designer won't connect | Make sure you're on the same network. Try `http://IP:PORT/` in your browser. |
| Empty templates in gear menu | The TV must be powered on and reachable. Check the binary_sensor status. |
| TV button doesn't trigger HA | Configure the HA token in the Designer (gear icon). Verify `ha_ip` is reachable from the TV. |
| TTS doesn't speak | Check that a TTS engine is installed on the Android TV (Google TTS is usually pre-installed). |
| No sound with notification | Verify the sound file exists (check via Designer settings). Some streaming apps may block audio mixing. |
| Menu doesn't respond to D-pad | Ensure the menu element has focus. Set `duration: 0` so the menu stays open. |

---

## Contributing

Contributions are welcome! Open an issue or a pull request on the [GitHub repository](https://github.com/jolabs40/peek-it-ha).

## License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with coffee, too many YAML files, and an unreasonable love for overlays.<br/>
  <strong>Peek-it [HA]</strong> — because your TV can do more than you think.
</p>
