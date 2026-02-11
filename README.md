# peek-it TV — Home Assistant Integration

<p align="center">
  <img src="peek_it_tv/icon@2x.png" alt="peek-it TV" width="128"/>
</p>

<p align="center">
  <strong>Turn your Android TV into a smart notification display.</strong><br/>
  Alerts, cameras, dashboards, messages — overlay on your TV in real time.
</p>

<p align="center">
  <a href="https://gitlab.com/jolabs40/peek-it/releases"><img src="https://img.shields.io/github/v/release/jolabs40/peek-it?style=for-the-badge&color=blue&label=Release" alt="Release"/></a>
  <a href="https://gitlab.com/jolabs40/peek-it"><img src="https://img.shields.io/github/stars/jolabs40/peek-it?style=for-the-badge&color=yellow" alt="Stars"/></a>
  <a href="https://gitlab.com/jolabs40/peek-it/blob/master/LICENSE"><img src="https://img.shields.io/github/license/jolabs40/peek-it?style=for-the-badge&color=green" alt="License"/></a>
  <a href="https://github.com/hacs/integration"><img src="https://img.shields.io/badge/HACS-Custom-orange?style=for-the-badge" alt="HACS"/></a>
  <img src="https://img.shields.io/badge/Android%20TV-Compatible-brightgreen?style=for-the-badge&logo=android" alt="Android TV"/>
  <img src="https://img.shields.io/badge/Home%20Assistant-Integration-41BDF5?style=for-the-badge&logo=homeassistant&logoColor=white" alt="Home Assistant"/>
</p>

<p align="center">
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-the-designer--your-best-friend">Designer</a> •
  <a href="#-templates--parameters">Templates</a> •
  <a href="#-automations">Automations</a> •
  <a href="#-waf--the-ultimate-kpi">WAF</a> •
  <a href="README_FR.md">Version Francaise</a>
</p>

---

## Why peek-it TV?

Your Android TV device (NVIDIA Shield, Chromecast with Google TV, Xiaomi Mi Box, etc.) is plugged into your TV 24/7. Why not put it to work?

**peek-it TV** displays **rich overlay notifications** on top of any running application. Watching Netflix? A camera feed pops up for 5 seconds in the top-right corner. Sports night? The score updates in real time. Doorbell rings? The front door camera appears instantly.

### What you can display

| Type | Example |
|------|---------|
| **Rich text** | Titles, messages, counters, weather |
| **Images** | Photos, snapshots, logos, QR codes |
| **RTSP video streams** | Live security cameras, ultra-low latency |
| **Web pages** | HA dashboards, Grafana charts, weather widgets |
| **SVG** | Vector icons, gauges, diagrams |
| **Shapes** | Rectangles, ellipses, lines, arrows — build complete layouts |
| **Interactive buttons** | TV remote-controlled, trigger HA automations |

### Key features

- **Zero latency** — native Android overlay, no streaming or casting
- **Works with everything** — Netflix, Plex, Kodi, YouTube, games... the overlay goes on top
- **Visual Designer** — create notifications with drag & drop from any browser
- **Reusable templates** — design once, reuse with dynamic parameters
- **7 animations** — fade, slide, pop... independent entrance and exit effects
- **Interactive buttons** — TV remote triggers Home Assistant automations
- **Multi-device** — manage multiple TVs from a single HA instance

<p align="center">
  <picture>
    <img src="docs/screenshots/01_hero_overlay.png" alt="peek-it TV overlay showing a camera feed on top of a streaming app" width="700"/>
  </picture>
  <br/><em>A camera feed displayed as overlay while streaming — zero interruption.</em>
</p>

---

## Prerequisites

1. **An Android TV device** (NVIDIA Shield, Chromecast with Google TV, Xiaomi Mi Box, etc.)
2. **The peek-it TV app** installed on the device
3. **Home Assistant** installed and running
4. Both devices on the **same local network**

### Install the Android TV app

> The app is not (yet) on the Play Store. Install it via sideload.

1. Download the APK from the [Releases page](https://gitlab.com/jolabs40/peek-it/releases)
2. Transfer it to your device (USB drive, `adb install`, or a file manager app)
3. Launch the app — it will request the overlay permission (display over other apps)
4. Grant the permission — the service starts automatically
5. Note the **IP address** shown on the main screen (e.g., `192.168.1.42`)
6. Default port is **8081** (configurable in the app)

> **Tip**: The service auto-starts on device boot. Plug it in, forget about it.

<p align="center">
  <picture>
    <img src="docs/screenshots/02_android_app.png" alt="peek-it TV Android app main screen showing IP address, port, and service status" width="400"/>
  </picture>
  <br/><em>Android TV app — IP address, port, and service status at a glance.</em>
</p>

---

## Installation

### Method 1: HACS (recommended)

1. Open HACS in Home Assistant
2. Go to **Integrations** > 3-dot menu > **Custom repositories**
3. Add the repository URL: `https://gitlab.com/jolabs40/peek-it`
4. Category: **Integration**
5. Click **peek-it TV** > **Download**
6. **Restart Home Assistant**

### Method 2: Manual installation

1. Copy the `peek_it_tv/` folder into your `custom_components/` directory:
   ```
   config/
   └── custom_components/
       └── peek_it_tv/
           ├── __init__.py
           ├── config_flow.py
           ├── const.py
           ├── manifest.json
           ├── notify.py
           ├── binary_sensor.py
           ├── services.yaml
           ├── strings.json
           ├── translations/
           │   └── en.json
           ├── icon.png
           ├── icon@2x.png
           ├── logo.png
           └── logo@2x.png
   ```
2. **Restart Home Assistant**

### Adding the integration

1. Go to **Settings** > **Devices & Services** > **Add Integration**
2. Search for **peek-it TV**
3. Fill in:
   - **IP Address**: your Android TV device IP (shown in the app)
   - **Port**: `8081` (default)
   - **Name**: a friendly name for your TV (e.g., "Living Room TV")
4. Submit — the integration tests the connection and configures itself

<p align="center">
  <picture>
    <img src="docs/screenshots/03_config_flow.png" alt="Home Assistant config flow form with IP, port, and name fields" width="400"/>
  </picture>
  <br/><em>Simple setup — just IP, port, and a name.</em>
</p>

### What gets created automatically

| Entity | Type | Description |
|--------|------|-------------|
| `binary_sensor.living_room_tv_status` | Binary Sensor | Connection status (online/offline), polls every 30s |
| `notify.living_room_tv` | Notify | Notification sending entity |

The `binary_sensor` also exposes a `designer_url` attribute with a direct link to the web Designer.

---

## Integration options (gear icon)

Click the **gear icon** on the peek-it TV integration card to access 3 menus:

<p align="center">
  <picture>
    <img src="docs/screenshots/04_gear_menu.png" alt="Integration options menu showing Settings, Templates, and Designer options" width="400"/>
  </picture>
  <br/><em>Three options: Settings, Templates, and Designer.</em>
</p>

### Settings

Edit the IP, port, or device name. The integration reloads automatically after saving.

### Templates

Browse all templates available on your TV Box, sorted by category:

- **Official** — built-in templates shipped with the app
- **Custom** — your finalized templates, each with a unique UUID
- **Drafts** — work in progress, no ID assigned yet

Each template shows its **name**, **ID** (copyable), and available **parameters**.

<p align="center">
  <picture>
    <img src="docs/screenshots/05_templates_list.png" alt="Template list showing official and custom templates with IDs and parameters" width="400"/>
  </picture>
  <br/><em>Templates at a glance — name, ID, and parameters.</em>
</p>

### Designer

Direct link to open the web Designer in a new tab. Handy for editing templates without leaving HA.

---

## Usage

### Mode 1: Simple message

The quickest way — send a text message that appears at the bottom of the screen with a dark background.

```yaml
service: peek_it_tv.notify
data:
  message: "The washing machine is done!"
  title: "Home"
  duration: 8000
```

Result: a dark banner at the bottom with the title in blue and the message in white.

<p align="center">
  <picture>
    <img src="docs/screenshots/06_simple_message.png" alt="Simple text notification overlay on TV screen" width="600"/>
  </picture>
  <br/><em>Simple message — clean, readable, non-intrusive.</em>
</p>

### Mode 2: Template + parameters

The most practical — reuse an existing template by injecting dynamic values.

```yaml
service: peek_it_tv.notify
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
- Via service: `peek_it_tv.get_templates` returns the full list

### Mode 3: Raw elements (full JSON)

The most flexible — define each widget manually.

```yaml
service: peek_it_tv.notify
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
service: peek_it_tv.notify
data:
  action: CLOSE
```

### Persistent (infinite) notification

```yaml
service: peek_it_tv.notify
data:
  message: "Waiting for confirmation..."
  duration: 0
```

Duration `0` = the notification stays on screen until an explicit `CLOSE` or a button action press.

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
| `angle` | int | Rotation in degrees (0-360) |
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

## The Designer — your best friend

The Designer is a **visual web editor** embedded in the Android TV app. Access it from any browser on your local network.

**URL**: `http://<TV_IP>:<PORT>/` (e.g., `http://192.168.1.42:8081/`)

You can also access it via:
- The `designer_url` attribute of the binary_sensor in HA
- The gear icon > Designer in the integration options

<p align="center">
  <picture>
    <img src="docs/screenshots/07_designer_overview.png" alt="Designer web app overview with canvas, toolbar, and sidebar" width="700"/>
  </picture>
  <br/><em>The Designer — drag, drop, style, send. That's it.</em>
</p>

### Interface layout

```
+-------------------------------------------------------------+
|  Header: animations, duration, background, send/kill         |
+------+--------------------------------+---------------------+
| Tool |  Workspace                     | Sidebar             |
| bar  |  +------------------------+   | - Layers            |
|      |  |                        |   | - Content           |
| (11  |  |   Simulated TV screen  |   | - Text styling      |
| types|  |   (calibrated ratio)   |   | - Appearance        |
|  )   |  |                        |   | - Action & Focus    |
|      |  +------------------------+   |                     |
+------+--------------------------------+---------------------+
|  Footer: real-time JSON payload preview                      |
+-------------------------------------------------------------+
```

### Toolbar (left)

11 widget types available in one click:

| Icon | Type | Use case |
|------|------|----------|
| Aa | `text` | Labels, titles, descriptions |
| Button | `button` | Interactive TV remote buttons |
| Image | `image` | Photos, logos (URL) |
| Circle | `circle` | Circular shape |
| Rectangle | `box` | Containers, backgrounds, dividers |
| Camera | `video` | Live RTSP streams |
| Globe | `webview` | Web pages, HA dashboards |
| Pencil | `svg` | Vector graphics |
| Oval | `ellipse` | Elliptical shape |
| Line | `line` | Separator line |
| Arrow | `arrow` | Direction indicator |

### Widget manipulation

| Action | Gesture |
|--------|---------|
| **Move** | Click and drag |
| **Resize** | North/South/East/West handles |
| **Multi-select** | Ctrl + click |
| **Disable snap** | Alt + drag |
| **Delete** | Delete key |
| **Duplicate** | Button in sidebar |
| **Z-order** | 4 buttons (front/back, up/down) |

### Sidebar (right)

<p align="center">
  <picture>
    <img src="docs/screenshots/08_designer_sidebar.png" alt="Designer sidebar showing layer list and property panels" width="300"/>
  </picture>
  <br/><em>All properties at your fingertips.</em>
</p>

#### Layers
All widgets listed with type and name. Click to select. Order = stacking order (z-index).

#### Content
- **content** — text or URL depending on widget type
- **paramKey** — dynamic parameter name (yellow badge on canvas)

#### Text
- **Font**: Regular, Medium, Black, Light, Condensed
- **Size**: in pixels
- **Color**: color picker
- **Alignment**: left / center / right

#### Appearance
- Background color, border color, opacity
- Corner radius
- Border width
- Rotation angle (0-360)
- "Transparent" checkbox (removes background)

#### Action & Focus
- **directFocus** — widget gets focus on launch (one per notification)
- **focusable** — navigable with TV remote
- **CLOSE** — closes the notification on press
- **action** — custom ID (triggers HA event)
- Customizable focus colors

### Template management

#### Save
1. Click the save icon
2. Name your template
3. Choose:
   - **Draft** — work in progress, no ID assigned
   - **Custom (Final)** — finalized template, UUID auto-generated

#### Load
1. Click the load icon
2. Browse 3 categories:
   - **OFFICIAL** (lock icon) — built-in, read-only
   - **DRAFT** (yellow) — editable work in progress
   - **CUSTOM** (star) — your finalized templates

<p align="center">
  <picture>
    <img src="docs/screenshots/09_designer_library.png" alt="Designer template library showing official, draft, and custom categories" width="500"/>
  </picture>
  <br/><em>Template library — organized, with IDs ready to copy.</em>
</p>

#### Template operations
- **Green "ID" badge** — click to copy UUID to clipboard
- **Download icon** — export template as JSON to your PC
- **Pencil icon** — rename (draft/custom only)
- **Trash icon** — delete with confirmation

#### Import a template
**IMPORT PC** button: upload a `.json` file from your computer. The template is placed in drafts.

### Send and test

- **SEND button** (blue) — sends the current layout to the TV immediately
- **KILL button** (red) — closes the current notification
- **JSON preview** (footer) — see the exact payload that will be sent

### Auto-calibration

On load, the Designer queries `/api/status` to get the real resolution of your TV. The canvas ratio adapts automatically (16:9, 21:9, etc.). A green badge confirms the connection and detected resolution.

### HA configuration in the Designer

Click the **gear icon** in the Designer header to:
- Enter your **Home Assistant token** (needed for webhook callbacks)
- The token is saved on-device, never exposed in plain text

<p align="center">
  <picture>
    <img src="docs/screenshots/10_designer_settings.png" alt="Designer settings modal for Home Assistant token configuration" width="400"/>
  </picture>
  <br/><em>Paste your HA token — that's all it takes for webhooks to work.</em>
</p>

---

## Templates & parameters

### Concept

A template is a reusable notification layout. Instead of sending 15 lines of JSON every time, you:

1. **Create** the layout in the Designer (drag & drop)
2. **Define parameters** (`paramKey`) on dynamic elements
3. **Save** as Custom (UUID generated)
4. **Use** the `template_id` + `params` in your automations

### Practical example

#### In the Designer

Create an "Camera Alert" template with:
- A dark background (`box`)
- A text title with `paramKey: title`
- A video stream with `paramKey: camera_url`
- A "Close" button with action `CLOSE`

Save as Custom. Note the UUID: `a1b2c3d4-...`

#### In Home Assistant

```yaml
service: peek_it_tv.notify
data:
  template_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
  params:
    title: "Motion detected - Garden"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 20000
  priority: urgent
  animationIn: slide_right
```

The result: your template displays with the title and camera injected dynamically. Reuse the same template for all your cameras — only the `params` change.

### Retrieve the template list

```yaml
service: peek_it_tv.get_templates
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
      - service: peek_it_tv.notify
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
      - service: peek_it_tv.notify
        data:
          message: "{{ states('weather.home') }} — {{ state_attr('weather.home', 'temperature') }}°C"
          title: "Today's Weather"
          duration: 10000
          animationIn: fade
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

To make it work, in the Designer, create a button with:
- `focusable`: enabled
- `action`: `lights_off` (any ID you want)

The user navigates with the remote's arrow keys and presses OK to confirm. The `peekit_button_press` event fires in HA with the corresponding `action`.

<p align="center">
  <picture>
    <img src="docs/screenshots/11_interactive_buttons.png" alt="Template with interactive buttons in the Designer and the corresponding HA automation" width="600"/>
  </picture>
  <br/><em>Buttons on the TV that trigger real HA actions. Yes, really.</em>
</p>

### Persistent alert with dismiss button

```yaml
automation:
  - alias: "Water leak alert"
    trigger:
      - platform: state
        entity_id: binary_sensor.water_leak
        to: "on"
    action:
      - service: peek_it_tv.notify
        data:
          duration: 0
          animationIn: pop
          priority: urgent
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

The notification stays on screen (`duration: 0`) until someone presses "Got it" on the remote.

### HA dashboard as overlay

```yaml
service: peek_it_tv.notify
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

### RTSP camera feed

```yaml
service: peek_it_tv.notify
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

The feed displays with ultra-low latency (~50ms) thanks to an optimized ExoPlayer setup. Perfect for doorbells and security cameras.

---

## Service `peek_it_tv.get_templates`

Retrieves the complete template list from all configured devices. Useful in scripts and automations for building dynamic interfaces.

```yaml
service: peek_it_tv.get_templates
response_variable: result
```

The `result` variable contains a dictionary where key = device name, value = templates.

---

## Webhooks & events

The integration listens for a webhook to receive logs and button actions from the TV Box.

| HA Event | Trigger | Data |
|----------|---------|------|
| `peekit_button_press` | Button press on the TV | `{ "action": "button_id" }` |

Box logs are also forwarded to the HA logger with the prefix `[BOX TV REPORT]`.

---

## Multi-device

The integration supports **multiple devices**. Add each TV as a separate integration. The `peek_it_tv.notify` and `get_templates` services automatically send to **all configured devices**.

To target a single device, use the specific `notify` entity:

```yaml
service: notify.send_message
target:
  entity_id: notify.living_room_tv
data:
  message: "Only on this TV"
```

---

## WAF — The Ultimate KPI

Ah, the legendary **WAF** — *Wife Acceptance Factor*. That unofficial yet absolutely critical metric that measures your partner's tolerance for your home automation experiments. With peek-it TV, your WAF score is about to skyrocket. Here's why.

### Before peek-it

> **You**: "Honeyyy, someone's at the door!"
> *(frantically checking your phone, Grafana open across 3 dashboards)*
>
> **Your partner**: "...You could just look out the window like a normal person?"

### After peek-it

The front door camera pops up **directly on the TV**, as an overlay, while Netflix keeps playing in the background. Nobody had to move from the couch.

> **Your partner**: "Oh, it's the delivery guy! That's actually useful."
>
> *(WAF: +47 points)*

### Use cases that boost your WAF

**The smart washing machine**: a "Laundry done!" notification pops up discreetly during the movie. No more loads forgotten for 3 days, slowly developing their own ecosystem.

> *(WAF: +23 points, -12 points for last week's forgotten load)*

**Morning weather**: every day at 7:30 AM, the weather pops up on the kitchen TV. Your partner finally knows if they need an umbrella without asking "Hey Google, what's the weather?".

> *(WAF: +15 points)*

**School bus alert**: "Bus arrives in 5 minutes!" overlays on screen. The kids are (almost) on time. Almost.

> *(WAF: +31 points, kids: -200 points)*

**The sports score**: your partner is watching their show, you're waiting for the score. A discreet "Man City 2 - 1, 78'" appears for 3 seconds in the top-right corner. Everyone's happy. Nobody changed the channel. Household peace: preserved.

> *(WAF: +52 points, diplomatic neutrality achieved)*

**The doorbell cam**: someone rings, the camera feed pops up on screen. Your partner makes a judgment call from the couch: "That's Karen from next door. We're not home." The TV returns to its regularly scheduled programming. No one got up. No one opened the door. Everyone wins.

> *(WAF: +38 points, introvert bonus: +15 points)*

### The use case that TANKS your WAF

**Debugging in production**: you're testing your notifications at 11 PM. "Test 1", "Test 2", "Lorem ipsum", "AAAA IT WORKS!" flash across the TV in rapid succession while your partner is trying to watch the season finale.

> **Your partner**: "If I see ONE more black rectangle on MY show, your precious box is sleeping in the garage tonight."
>
> *(WAF: -347 points. Estimated recovery: 3 weeks of exemplary behavior.)*

**Pro tip**: test your automations BEFORE 9 PM. Or better yet, use the **KILL** button in the Designer. It exists for a reason.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Integration not found in HA | Make sure the folder is in `custom_components/peek_it_tv/`. Restart HA. |
| "Cannot connect" on setup | Check the IP and port. The app must be running on the TV. Test `http://IP:8081/api/status` in a browser. |
| Binary sensor always "offline" | Is the Android TV app running? Does the service start on boot? |
| Notification doesn't show | Check the overlay permission in Android TV settings. |
| Designer won't connect | Make sure you're on the same network. Try `http://IP:PORT/` in your browser. |
| Empty templates in gear menu | The TV Box must be powered on and reachable. Check the binary_sensor status. |
| TV button doesn't trigger HA | Configure the HA token in the Designer (gear icon). Verify `ha_ip` is reachable from the TV. |

---

## Screenshots to take

To illustrate this documentation, here are the recommended captures. Save them in `docs/screenshots/` with the filenames below:

| # | Filename | What to capture |
|---|----------|-----------------|
| 1 | `01_hero_overlay.png` | A camera or notification overlay on top of Netflix/YouTube |
| 2 | `02_android_app.png` | Android TV app main screen (IP, port, service status) |
| 3 | `03_config_flow.png` | HA integration setup form (IP, port, name) |
| 4 | `04_gear_menu.png` | Gear icon menu with 3 options (Settings, Templates, Designer) |
| 5 | `05_templates_list.png` | Template list in gear menu with IDs and params |
| 6 | `06_simple_message.png` | Simple text notification on the TV |
| 7 | `07_designer_overview.png` | Designer full view with a template being edited |
| 8 | `08_designer_sidebar.png` | Designer sidebar with properties panel |
| 9 | `09_designer_library.png` | Designer template library modal (3 categories) |
| 10 | `10_designer_settings.png` | Designer settings modal (HA token) |
| 11 | `11_interactive_buttons.png` | Template with interactive buttons + HA automation example |
| 12 | `12_rtsp_camera.png` | RTSP camera feed as overlay |
| 13 | `13_ha_automation.png` | HA automation editor with peek_it_tv service |

---

## Contributing

Contributions are welcome! Open an issue or a pull request on the [GitHub repository](https://gitlab.com/jolabs40/peek-it).

## License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with coffee, too many YAML files, and an unreasonable love for overlays.<br/>
  <strong>peek-it TV</strong> — because your TV can do more than stream cat videos.<br/>
  <em>(Although it's very good at that too.)</em>
</p>
