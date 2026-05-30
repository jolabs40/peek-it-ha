# Peek-it [HA] — Integración de Home Assistant

<p align="center">
  <img src="custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Convierte tu Android TV en una pantalla de notificaciones inteligente.</strong><br/>
  Alertas, cámaras, paneles, TTS, menús — en overlay sobre tu TV en tiempo real.
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
  <a href="#-cómo-funciona">Cómo funciona</a> •
  <a href="#-instalación">Instalación</a> •
  <a href="#-el-designer">Designer</a> •
  <a href="#-uso">Uso</a> •
  <a href="#-síntesis-de-voz-tts">TTS</a> •
  <a href="#-automatizaciones">Automatizaciones</a> •
  <a href="#-referencia-avanzada">Referencia avanzada</a> •
  <a href="#-waf--el-kpi-definitivo">WAF</a>
</p>

<p align="center">
  <b>Idiomas:</b>
  <a href="README.md">English</a> |
  <a href="README_FR.md">Fran&ccedil;ais</a> |
  <a href="README_DE.md">Deutsch</a> |
  Espa&ntilde;ol |
  <a href="README_NL.md">Nederlands</a> |
  <a href="README_PT.md">Portugu&ecirc;s</a>
</p>

---

## ¿Por qué Peek-it [HA]?

Tu dispositivo Android TV está conectado a tu televisor las 24 horas del día. ¿Por qué no ponerlo a trabajar?

La aplicación **Peek-it [TV]** muestra **notificaciones enriquecidas en overlay** por encima de cualquier aplicación en curso: una película, la TDT, un juego... ¿Estás viendo un partido? El marcador se actualiza en una esquina. ¿Llaman a la puerta? La cámara de la entrada aparece al instante. Y eres **tú quien diseña** estas visualizaciones, sin escribir una sola línea de código.

> 💡 **Lo esencial que debes recordar**
>
> 1. **Tú diseñas** tus notificaciones (e incluso páginas enteras) en el **Designer**, un editor visual de arrastrar y soltar accesible desde cualquier navegador. *Es él quien lo construye todo — no tienes que programar nada.*
> 2. **Tú las lanzas** desde **Home Assistant** gracias a esta integración… o desde **Tasker, Node-RED, Jeedom** o cualquier otro cliente HTTP, ya que la app expone una API local sencilla.

> 🧩 **Dos componentes, dos roles**
> La **aplicación Peek-it [TV]** (Android, en la Play Store) dibuja el overlay, aloja el Designer y el motor de plantillas: es la autoridad.
> La **integración Peek-it [HA]** (este repositorio) la pilota desde Home Assistant: envío de notificaciones/TTS, supervisión del estado, retornos de botones.

### Lo que puedes mostrar

| | |
|------|---------|
| 📝 **Texto enriquecido** | Títulos, mensajes, contadores, meteorología |
| 🖼️ **Imágenes** | Fotos, capturas, logotipos, códigos QR |
| 🎥 **Flujos de vídeo RTSP** | Cámaras de vigilancia en directo, latencia ultrabaja |
| 🌐 **Páginas web** | Paneles de HA, gráficos, widgets de meteorología |
| 🔺 **Formas y SVG** | Rectángulos, elipses, hexágonos, flechas, iconos vectoriales |
| 🎮 **Botones y menús** | Navegables con el mando, lanzan tus automatizaciones de HA |
| 📊 **Entidades y gráficos de HA** | Estado en tiempo real e historial de las entidades |
| 🔊 **Síntesis de voz** | Anuncios de voz directamente en la TV |

### Funcionalidades clave

- **Cero latencia** — overlay nativo de Android, sin streaming ni casting
- **Compatible con todo** — el overlay se muestra por encima de cualquier aplicación
- **Designer visual** — créalo todo con arrastrar y soltar, vista previa en tiempo real
- **Plantillas reutilizables** — diseña una vez, reutiliza con parámetros dinámicos
- **Multidispositivo** — gestiona varias TV desde una sola instancia de HA
- **Abierto** — pilotable desde HA, Tasker, Node-RED, Jeedom… a través de una API HTTP local
- **6 idiomas** — EN, FR, DE, ES, NL, PT

---

## 🧩 Cómo funciona

Tres pasos, de lo visual a la automatización:

| Paso | Dónde | Lo que haces |
|------|-----|--------------------|
| **1. Diseñar** | 🎨 Designer (navegador) | Arrastrar y soltar tus elementos sobre un lienzo calibrado a tu TV. El Designer genera todo el renderizado por ti. |
| **2. Guardar** | 🎨 Designer | Guardar tu creación como **plantilla** reutilizable (se genera un simple ID). |
| **3. Lanzar** | 🏠 Home Assistant | Llamar a la plantilla desde una automatización, en unas pocas líneas, con valores dinámicos. |

```yaml
# Paso 3: lanzar una plantilla diseñada en el Designer
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Alerta de seguridad"
    camera_url: "rtsp://192.168.1.50:554/stream1"
```

> ✅ **Casi nunca necesitas escribir JSON a mano.** El Designer se encarga de la maquetación; del lado de Home Assistant solo proporcionas el ID de la plantilla y unos pocos valores. La [Referencia avanzada](#-referencia-avanzada) (JSON en bruto, tipos de widgets, API…) está ahí solo para los casos avanzados.

---

## 📥 Instalación

### 1. Instalar la aplicación Peek-it [TV]

**Recomendado — Google Play Store**: busca **«Peek-it»** en la Play Store de tu Android TV, o abre la ficha:
[play.google.com/store/apps/details?id=net.jolabs40.peekit](https://play.google.com/store/apps/details?id=net.jolabs40.peekit)

> Dispositivo sin Play Store (algunas cajas Android TV, Fire TV…): instala el APK mediante sideload desde la [página de Releases](https://github.com/jolabs40/peek-it-ha/releases) (memoria USB, `adb install`, o un gestor de archivos).

Después, sea cual sea el método:

1. Inicia la aplicación — concede el **permiso de overlay** (mostrar por encima de las demás aplicaciones); el servicio se inicia automáticamente.
2. Anota la **dirección IP** mostrada en la pantalla principal (ej. `192.168.1.42`). Puerto por defecto: **8081**.

### 2. Instalar la integración de Home Assistant

**Mediante HACS (recomendado)**: HACS → *Integrations* → menú de 3 puntos → *Custom repositories* → añade `https://github.com/jolabs40/peek-it-ha` (categoría *Integration*) → *Download* → **reinicia HA**.

<details>
<summary>Instalación manual</summary>

Copia la carpeta `peek_it_ha/` en `config/custom_components/`, luego reinicia Home Assistant:

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

### 3. Añadir la integración

*Ajustes → Dispositivos y servicios → Añadir integración → Peek-it [HA]*. Indica la **IP**, el **puerto** (`8081`), un **nombre** y, si la app TV lo exige, una **clave API**. Si el dispositivo se publica mediante Zeroconf (`_peekit._tcp`), HA también puede **descubrirlo automáticamente**.

<details>
<summary>Lo que se crea automáticamente (entidades de HA)</summary>

Todas las entidades se agrupan en una **única tarjeta de dispositivo**. Para cada TV:

| Entidad | Tipo | Descripción |
|--------|------|-------------|
| `binary_sensor.<nombre>_status` | Conectividad | En línea / fuera de línea (consultado cada 30 s); expone el atributo `designer_url` |
| `binary_sensor.<nombre>_overlay_permission` | Diagnóstico | Permiso de overlay concedido |
| `binary_sensor.<nombre>_accessibility_permission` | Diagnóstico | Servicio de accesibilidad activo |
| `binary_sensor.<nombre>_microphone_permission` | Diagnóstico | Permiso de micrófono concedido |
| `notify.<nombre>` | Notify | Envío de notificaciones |
| `button.<nombre>_*_assist / overlay / accessibility` | Config (×6) | Activar/desactivar los permisos mediante ADB — ver [Botones ADB](#-botones-de-configuración-adb) |

Se emite una sola petición `GET /api/status` por TV cada 30 s; todas las entidades comparten esta instantánea (coordinador compartido).
</details>

---

## 🎨 El Designer

**El corazón de Peek-it.** Es aquí donde creas tus notificaciones y tus páginas — visualmente, sin programar. Es un **editor web integrado en la app**, accesible desde cualquier navegador de la red local:

**URL**: `http://<IP_TV>:<PUERTO>/` (ej. `http://192.168.1.42:8081/`) — también accesible mediante el atributo `designer_url` del sensor de estado, o *icono de engranaje → Designer* en las opciones de la integración.

- **Arrastrar y soltar** tus widgets sobre un lienzo calibrado a la resolución real de tu TV (16:9, 21:9…)
- **Vista previa JSON en tiempo real** — ves cómo se construye el renderizado
- **Biblioteca de plantillas** — guardar, cargar, renombrar, exportar/importar
- **Parámetros dinámicos** — marca los elementos variables (`paramKey`) para rellenarlos desde HA
- **Configuración** del sonido por defecto, del idioma, y del **token de acceso de HA** (ver más abajo)
- **Botones SEND** (enviar a la TV) y **KILL** (cerrar) para probar de inmediato

> 🔑 **Token de acceso de Home Assistant (opcional).** Algunas funciones piden a la app que llame **directamente** a la API de HA: conmutar una entidad desde un menú, mostrar el estado de una entidad en tiempo real, dibujar un gráfico de historial, o mostrar una instantánea de cámara. Para ello, crea un **token de acceso de larga duración (Long-Lived Access Token)** en HA (*tu perfil → hasta abajo del todo → Tokens de acceso de larga duración → Crear*) y pégalo en los ajustes del Designer. Se almacena cifrado en la TV. No es necesario si solo vas a enviar notificaciones desde HA.
>
> No confundir con el **secreto del webhook** (`X-Peek-Secret`), que sirve en el otro sentido (retornos de botones TV → HA) y que la integración gestiona **automáticamente**.

> Desde HA, *icono de engranaje → Templates* lista todas tus plantillas con su **ID** (copiable) y sus **parámetros**, ordenadas en *Official* / *Custom* / *Drafts*.

---

## 🚀 Uso

Tres formas de enviar, de la más simple a la más avanzada. **El modo plantilla es el más práctico**: se apoya en tus creaciones del Designer.

### Mensaje simple

Un texto que se muestra en la parte inferior de la pantalla sobre fondo oscuro — ideal para una alerta rápida.

```yaml
service: peek_it_ha.notify
data:
  message: "¡La lavadora ha terminado!"
  title: "Casa"
  duration: 8000
```

### Plantilla + parámetros *(recomendado)*

Reutiliza una plantilla diseñada en el Designer inyectando valores dinámicos.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Alerta de seguridad"
    message: "Movimiento detectado en el jardín"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

El servidor carga la plantilla, reemplaza los `{{placeholders}}` por los valores de `params`, y muestra el resultado.

### Cerrar / mantener una notificación

```yaml
# Cerrar inmediatamente
service: peek_it_ha.notify
data:
  action: CLOSE
```

`duration: 0` mantiene la notificación en pantalla hasta un `CLOSE` explícito o una pulsación de un botón.

<details>
<summary><b>Modo avanzado — elementos en bruto (JSON completo)</b></summary>

Para los casos en los que quieras definir cada widget a mano, sin pasar por una plantilla. *En la práctica, el Designer hace todo esto visualmente.*

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
      content: "Cámara del jardín"
      style: { left: 62, top: 28, width: 34, height: 5, size: 18, color: "#FFFFFF", align: center }
```

El vocabulario completo (tipos de widgets, propiedades de estilo) está documentado en la [Referencia avanzada](#-referencia-avanzada).
</details>

---

## 🔔 Síntesis de voz (TTS)

Haz hablar a la TV, sola o como acompañamiento de una notificación.

```yaml
# TTS autónomo
service: peek_it_ha.tts
data:
  text: "¡La cena está lista!"
  lang: "es"
  speed: 1.0     # 0.5 a 2.0
  volume: 1.0    # 0.0 a 1.0
```

```yaml
# TTS con notificación visual
service: peek_it_ha.notify
data:
  message: "Movimiento detectado en el jardín"
  title: "Seguridad"
  tts: "Movimiento detectado en el jardín"
  ttsLang: "es"
  ttsSpeed: 1.25
```

Detener la reproducción: `service: peek_it_ha.tts_stop`. En `notify`, los campos llevan el prefijo `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

## 🔊 Sonido

```yaml
service: peek_it_ha.notify
data:
  message: "Paquete entregado"
  sound: "01_notify.wav"
  soundVolume: 0.8   # 0.0 a 1.0
```

La app viene con sonidos integrados y acepta tus sonidos personalizados (mediante el Designer).

---

## 📺 Botones de configuración (ADB)

La integración expone **6 botones** (categoría *Config*) que pilotan la TV mediante **ADB sobre TCP**, para ajustar con un clic permisos engorrosos de activar con el mando:

| Botón | Acción en la TV |
|--------|------------------|
| **Enable / Disable Assist** | Define / restaura Peek-it como asistente por defecto |
| **Enable / Disable Overlay** | Concede / revoca el permiso `SYSTEM_ALERT_WINDOW` |
| **Enable / Disable Accessibility** | Activa / desactiva el servicio de accesibilidad `MenuKeyService` |

<details>
<summary>Requisitos ADB (hacer una sola vez)</summary>

Los botones utilizan la biblioteca `adb-shell` (instalada automáticamente por HA) y se conectan a la IP de la TV en el **puerto 5555**.

1. **Activa la depuración ADB por red**: *Ajustes → Preferencias del dispositivo → Acerca de →* toca 7 veces en *Versión*, luego *Opciones para desarrolladores →* **Depuración USB** (y **Depuración inalámbrica** si se ofrece).
2. **Autoriza la clave RSA en la primera pulsación**: aparece una ventana «¿Permitir la depuración?» en la TV → marca *Permitir siempre*. La clave se genera una vez y se almacena en `.storage/peek_it_adb_key`.
3. Se recomienda la integración oficial **Android TV** (HA lo indica en *Reparaciones*) para una gestión ADB estable.

Si falta `adb-shell` o si la TV rechaza la conexión, la acción falla con un error en el registro de HA.
</details>

---

## 🤖 Automatizaciones

### Alerta de movimiento con cámara

```yaml
automation:
  - alias: "Alerta de movimiento en el jardín"
    trigger:
      - platform: state
        entity_id: binary_sensor.garden_motion
        to: "on"
    action:
      - service: peek_it_ha.notify
        data:
          template_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
          params:
            title: "¡Movimiento detectado!"
            camera_url: "rtsp://192.168.1.50:554/stream1"
          duration: 15000
          animationIn: slide_right
```

### Boletín meteorológico de la mañana

```yaml
automation:
  - alias: "Meteorología de la mañana"
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
          title: "El tiempo de hoy"
```

### Retorno de un botón hacia HA

Una pulsación de un botón de notificación (mando) lanza un evento de HA:

```yaml
automation:
  - alias: "Botón TV - Apagar luces"
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
<summary>Alerta persistente con botón de cierre (JSON en bruto)</summary>

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  animationIn: pop
  priority: urgent
  tts: "¡Atención! ¡Fuga de agua detectada!"
  ttsLang: "es"
  elements:
    - type: rect
      style: { left: 20, top: 20, width: 60, height: 60, bgColor: "#EE990000", radius: 20 }
    - type: text
      content: "FUGA DE AGUA DETECTADA"
      style: { left: 25, top: 30, width: 50, height: 10, size: 40, color: "#FFFFFF", weight: bold, align: center }
    - type: button
      content: "Entendido"
      action: CLOSE
      focusable: true
      directFocus: true
      style: { left: 35, top: 55, width: 30, height: 10, size: 24, color: "#FFFFFF", bgColor: "#CC333333", align: center, radius: 10, focusColor: "#FF6666", focusBgColor: "#CC660000" }
```
</details>

<details>
<summary>Flujo de cámara RTSP</summary>

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

Latencia ultrabaja (~50 ms) gracias a una configuración optimizada de ExoPlayer.
</details>

---

## 🧰 Referencia avanzada

> 🛟 **Normalmente no necesitas esta sección.** El Designer construye tus notificaciones visualmente y te proporciona plantillas listas para usar. Lo que sigue solo es útil para el modo JSON en bruto, la API o las integraciones de terceros.

<details>
<summary><b>Parámetros del servicio <code>notify</code></b></summary>

| Parámetro | Tipo | Por defecto | Descripción |
|-----------|------|--------|-------------|
| `action` | string | `DISPLAY` | `DISPLAY` para mostrar, `CLOSE` para cerrar |
| `duration` | int | `10000` | Duración en ms (0 = infinito) |
| `priority` | string | `normal` | `normal` o `urgent` |
| `animationIn` / `animationOut` | string | `fade` | Ver animaciones más abajo |
| `template_id` | string | — | UUID de la plantilla a usar |
| `params` | dict | — | Valores dinámicos de la plantilla |
| `elements` | list | — | Lista de widgets (modo JSON en bruto) |
| `message` / `title` | string | — | Modo mensaje simple |
| `sound` / `soundVolume` | string / float | — / `1.0` | Sonido y volumen (0.0-1.0) |
| `tts` / `ttsLang` / `ttsSpeed` / `ttsPitch` / `ttsVolume` | — | — | TTS reproducido con la notificación |

**Animaciones**: `none`, `fade`, `slide_right`, `slide_left`, `slide_top`, `slide_bottom`, `pop` (entrada y salida independientes).
</details>

<details>
<summary><b>Tipos de widgets</b></summary>

El tipo es interpretado por la app. **Todo tipo no reconocido (`text`, `message`, `title`, `button`…) se renderiza como un widget de texto**; un `button` se distingue por `focusable` + `action`. Si `content` empieza por `mdi:` (ej. `mdi:home-assistant`), se muestra un **icono Material Design Icons**.

| Tipo | Descripción | `content` |
|------|-------------|-----------|
| `text` | Texto estático (tipo por defecto) | El texto, o `mdi:<icono>` |
| `button` | Texto interactivo (focusable, action) | Etiqueta |
| `rect` | Rectángulo / contenedor | — |
| `ellipse` | Elipse / óvalo | — |
| `hexagon` | Hexágono | — |
| `circle` | Contenedor redondo (imagen / icono MDI) | URL o `mdi:<icono>` |
| `image` | Imagen PNG/JPG | URL |
| `video` | Flujo RTSP / HTTP | URL |
| `webview` | Página web integrada | URL |
| `svg` | Imagen vectorial | URL o ruta |
| `line` / `arrow` | Línea / flecha | — |
| `confetti` | Animación de confeti a pantalla completa | — |
| `menu` | Menú interactivo D-pad | JSON MenuConfig |

> Los ejemplos antiguos en `type: box` se siguen mostrando (fallback de texto + `bgColor`), pero el tipo canónico del rectángulo es `rect`.
</details>

<details>
<summary><b>Propiedades de estilo y de interacción</b></summary>

**Estilo**: `left`, `top`, `width`, `height` (en % de la pantalla, 0-100) · `color` · `bgColor` (hex con alfa) · `size` · `font` · `weight` (`normal`/`bold`) · `align` (`left`/`center`/`right`) · `opacity` · `radius` · `borderWidth` · `borderColor` · `rotation` · `focusColor` · `focusBgColor`.

**Interacción (botones)**: `focusable` (recibe el foco del mando) · `directFocus` (foco al mostrarse) · `action` (`CLOSE` o ID personalizado para el webhook) · `paramKey` (vincula el contenido a un parámetro de plantilla) · `actionParamKey` (vincula la acción a un parámetro).
</details>

<details>
<summary><b>Menú interactivo (config JSON)</b></summary>

El widget `menu` crea un menú overlay navegable con el D-pad (submenús, conmutadores de entidades de HA, acciones).

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Controles rápidos",
          "items": [
            {"type": "submenu", "label": "Luces", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Salón", "entity_id": "light.living_room"},
              {"type": "close", "label": "Volver"}
            ]},
            {"type": "action", "label": "Modo cine", "action": "movie_mode"},
            {"type": "close", "label": "Cerrar"}
          ]
        }
      style: { left: 35, top: 10, width: 30, height: 80 }
```

| Tipo de elemento | Rol |
|------|-------------|
| `action` | Lanza `peekit_button_press` con el ID `action` |
| `submenu` | Abre un submenú (`children`) |
| `toggle` | Conmuta una entidad de HA (`entity_id`), estado refrescado cada 5 s |
| `text` | Texto informativo |
| `close` | Cierra el menú |

**Navegación**: Arriba/Abajo navegar · Derecha/Enter abrir un submenú · Izquierda/Atrás volver · Atrás en la raíz cierra.
</details>

<details>
<summary><b>Widgets de entidad de HA, gráficos y overlays (capacidades de la app)</b></summary>

Estas funciones se configuran del lado de la **app** (Designer); la integración HA no las pilota directamente. Requieren un **token de acceso de larga duración (Long-Lived Access Token) de HA** introducido en el Designer (cf. [El Designer](#-el-designer)), ya que la app llama a la API de HA directamente.

- **Widget de entidad de HA**: un `webview` conectado por WebSocket/REST muestra el estado de entidades en tiempo real.
- **Gráficos de HA**: área / línea / barras, renderizados en CSS/SVG puro.
- **Reloj en overlay** (`/api/config/clock`): formato 12 h/24 h, posición, color, opacidad.
- **Oscurecimiento** (`/api/config/dimming`): color y opacidad de una capa de fondo.
</details>

<details>
<summary><b>API y webhook (para Tasker, Node-RED, Jeedom, desarrolladores)</b></summary>

La app expone una API HTTP local (puerto `8081`). Si hay configurada una clave API, **todas** las peticiones llevan el header `X-API-Key: <clave>`. Es esta API la que cualquier cliente HTTP (Tasker, Node-RED, Jeedom…) puede llamar.

| Endpoint | Método | Uso |
|---|---|---|
| `/api/status` | GET | Estado, permisos, resolución |
| `/api/notify` | POST | Mostrar / cerrar una notificación |
| `/api/tts` · `/api/tts/stop` | POST | Síntesis de voz |
| `/api/templates/list` | GET | Lista de plantillas |

**Respuesta de `/api/status`**:
```json
{
  "status": "online", "version": "v10.9", "device_name": "Living Room TV",
  "api_key_required": false, "api_key_valid": true,
  "screen": { "width": 1920, "height": 1080, "density": 1.0 },
  "permissions": { "overlay": true, "accessibility": false, "microphone": true }
}
```

**Webhook (retornos de la TV → HA)**: `/api/webhook/peek_it_debug`. Desde la 1.1.0, cada petición debe presentar el header **`X-Peek-Secret`** (de lo contrario HTTP 401). El secreto se transmite a la TV mediante la **notificación de bienvenida** (campo `webhook_secret`) en la creación/guardado de la entrada.

| `level` | `message` | Efecto en HA |
|---------|-----------|----------|
| `ACTION` | `BUTTON_CLICK:<id>` | Emite el evento `peekit_button_press` `{ "action": "<id>" }` |
| `ERROR` / `WARN` / `INFO` | texto | Registrado `[PEEK-IT REPORT]` |

> **Migración desde 1.0.0**: *Configurar → Ajustes → Validar* para enviar una nueva notificación de bienvenida que contenga el `webhook_secret`.
</details>

---

## 🌍 Multidispositivo e idiomas

Añade cada TV como una integración separada. Los servicios `notify`, `tts`, `tts_stop` y `get_templates` se aplican a **todos los dispositivos**. Para apuntar a una sola TV:

```yaml
service: notify.send_message
target:
  entity_id: notify.tv_del_salon
data:
  message: "Solo en esta TV"
```

La integración y la app están disponibles en **6 idiomas**: `en` (por defecto), `fr`, `de`, `es`, `nl`, `pt`. Configurable en el Designer o la app.

---

## 😅 WAF — El KPI definitivo

El legendario **WAF** — *Wife Acceptance Factor* (Factor de Aceptación de la Esposa). Esa métrica no oficial pero absolutamente crucial que mide la tolerancia de tu media naranja hacia tus experimentos domóticos.

- 🧺 **Colada inteligente**: «¡Colada terminada!» aparece discretamente durante la película. Se acabaron las coladas olvidadas 3 días. *(WAF: +23)*
- ☀️ **Meteorología de la mañana**: cada día a las 7:30, el tiempo en la TV de la cocina. *(WAF: +15)*
- 🔔 **Cámara del timbre**: llaman, el flujo aparece. Deliberación desde el sofá. Nadie se levantó. *(WAF: +38)*
- ⚽ **Marcador deportivo**: un discreto «2 - 1, 78'» 3 segundos en la esquina. Nadie cambió de canal. *(WAF: +52)*

### El caso que ARRUINA tu WAF

🌙 **Depuración en producción**: pruebas tus notificaciones a las 23 h durante el gran final de la temporada. «Test 1», «Lorem ipsum», «¡AAAA FUNCIONA!», un gran rectángulo negro, y luego nada más...

> *(WAF: -347. Recuperación estimada: 3 semanas de buen comportamiento. Y un ramo de flores.)*

**Consejo profesional**: prueba ANTES de las 21 h. O usa el botón **KILL** del Designer. Existe por una razón.

---

## 🔧 Resolución de problemas

| Problema | Solución |
|----------|----------|
| Integración no encontrada | ¿Carpeta en `custom_components/peek_it_ha/`? Reinicia HA. |
| «Imposible conectar» | Verifica IP/puerto. Prueba `http://IP:8081/api/status` en un navegador. |
| Sensor siempre «fuera de línea» | ¿La app está en marcha? ¿El servicio se inicia al arrancar? |
| La notificación no se muestra | Verifica el permiso de overlay en los ajustes de Android TV. |
| El Designer no se conecta | ¿Misma red? Prueba `http://IP:PUERTO/`. |
| El botón de la TV no lanza HA | Retorno TV → HA = webhook: vuelve a guardar los *Ajustes* de la integración (transmite el `webhook_secret`) y verifica que `ha_ip` sea accesible desde la TV. |
| Los conmutadores de menú / widgets de entidad no funcionan | Llamada directa app → HA: crea un **token de acceso de larga duración (Long-Lived Access Token)** de HA y pégalo en el Designer (ver [El Designer](#-el-designer)). |
| Los botones ADB fallan | ¿Depuración ADB (puerto 5555) activada y clave RSA autorizada? Ver [Botones ADB](#-botones-de-configuración-adb). |
| El TTS no habla | ¿Hay un motor TTS instalado en el Android TV (Google TTS)? |
| El menú no responde al D-pad | El elemento menú debe tener el foco; usa `duration: 0`. |

---

## Contribuir

¡Las contribuciones son bienvenidas! Abre una issue o un pull request en el [repositorio de GitHub](https://github.com/jolabs40/peek-it-ha).

## Licencia

Proyecto distribuido bajo licencia MIT. Consulta el archivo [LICENSE](LICENSE).

---

<p align="center">
  Hecho con café, demasiados archivos YAML, y un amor irracional por los overlays.<br/>
  <strong>Peek-it [HA]</strong> — porque tu TV puede hacer mucho más de lo que crees.
</p>
