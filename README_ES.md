# Peek-it [HA] — Integracion Home Assistant

<p align="center">
  <img src="custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Convierte tu Android TV en una pantalla de notificaciones inteligente.</strong><br/>
  Alertas, camaras, paneles, TTS, menus — overlay en tu TV en tiempo real.
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
  <a href="#-instalacion">Instalacion</a> •
  <a href="#-uso">Uso</a> •
  <a href="#-el-designer">Designer</a> •
  <a href="#-templates-y-parametros">Templates</a> •
  <a href="#-texto-a-voz-tts">TTS</a> •
  <a href="#-sonido">Sonido</a> •
  <a href="#-menu-interactivo">Menu</a> •
  <a href="#-automatizaciones">Automatizaciones</a> •
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

## Por que Peek-it [HA]?

Tu dispositivo Android TV esta conectado a tu televisor 24/7. Por que no ponerlo a trabajar?

**Peek-it [HA]** es la integracion de Home Assistant para la aplicacion Android **Peek-it [TV]**. Juntos, muestran **notificaciones enriquecidas en overlay** sobre cualquier aplicacion en ejecucion. Viendo una pelicula? La imagen de una camara aparece 5 segundos en una esquina. Noche de futbol? El marcador se actualiza en tiempo real. Suena el timbre? La camara de la puerta aparece al instante.

### Que puedes mostrar

| Tipo | Ejemplo |
|------|---------|
| **Texto enriquecido** | Titulos, mensajes, contadores, meteorologia |
| **Imagenes** | Fotos, capturas, logos, codigos QR |
| **Flujos de video RTSP** | Camaras de seguridad en directo, latencia ultra baja |
| **Paginas web** | Paneles de HA, graficos, widgets meteorologicos |
| **SVG** | Iconos vectoriales, medidores, diagramas |
| **Formas** | Rectangulos, elipses, lineas, flechas — para componer layouts completos |
| **Botones interactivos** | Controlables con el mando del TV, activan automatizaciones HA |
| **Menus interactivos** | Menus navegables con D-pad con toggles de entidades HA |
| **Widgets de entidades HA** | Visualizacion en tiempo real del estado de entidades via WebSocket/REST |
| **Graficos HA** | Graficos CSS/SVG de area, linea y barras |
| **Texto a voz** | Anuncios de voz en tu TV |

### Caracteristicas principales

- **Latencia cero** — overlay nativo Android, sin streaming ni casting
- **Funciona con todo** — el overlay se superpone sobre cualquier aplicacion
- **Designer visual** — crea notificaciones con arrastrar y soltar desde cualquier navegador
- **Templates reutilizables** — disena una vez, reutiliza con parametros dinamicos
- **7 animaciones** — fade, slide, pop... efectos de entrada y salida independientes
- **Texto a voz** — anuncios de voz directamente en el TV
- **Alertas sonoras** — reproduce sonidos de notificacion junto con las visuales
- **Menus interactivos** — menus overlay navegables con D-pad y toggles HA
- **Multi-dispositivo** — gestiona multiples TVs desde una sola instancia de HA
- **6 idiomas** — EN, FR, DE, ES, NL, PT

---

## Requisitos previos

1. **Un dispositivo Android TV** con la aplicacion **Peek-it [TV]** instalada
2. **Home Assistant** instalado y en funcionamiento
3. Ambos dispositivos en la **misma red local**

### Instalar la aplicacion Peek-it [TV]

> La aplicacion no esta (todavia) en la Play Store. Se instala mediante sideload.

1. Descarga el APK desde la [pagina de Releases](https://github.com/jolabs40/peek-it-ha/releases)
2. Transfierelo a tu dispositivo (USB, `adb install`, o una aplicacion de gestion de archivos)
3. Abre la aplicacion — solicitara el permiso de overlay (mostrar sobre otras aplicaciones)
4. Concede el permiso — el servicio se inicia automaticamente
5. Anota la **direccion IP** que se muestra en la pantalla principal (ej. `192.168.1.42`)
6. El puerto por defecto es **8081** (configurable en la aplicacion)

> **Consejo**: El servicio se inicia automaticamente al encender el dispositivo. Conectalo y olvidate.

---

## Instalacion

### Metodo 1: HACS (recomendado)

1. Abre HACS en Home Assistant
2. Ve a **Integraciones** > menu de 3 puntos > **Repositorios personalizados**
3. Anade la URL del repositorio: `https://github.com/jolabs40/peek-it-ha`
4. Categoria: **Integracion**
5. Haz clic en **Peek-it [HA]** > **Descargar**
6. **Reinicia Home Assistant**

### Metodo 2: Instalacion manual

1. Copia la carpeta `peek_it_ha/` en tu directorio `custom_components/`:
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
2. **Reinicia Home Assistant**

### Anadir la integracion

1. Ve a **Ajustes** > **Dispositivos y servicios** > **Anadir integracion**
2. Busca **Peek-it [HA]**
3. Rellena:
   - **Direccion IP**: la IP de tu dispositivo Android TV (mostrada en la aplicacion)
   - **Puerto**: `8081` (por defecto)
   - **Nombre**: un nombre descriptivo para tu TV (ej. "TV del salon")
   - **API Key**: si la autenticacion esta activada en la aplicacion del TV
4. Envia — la integracion prueba la conexion y se configura automaticamente

### Que se crea automaticamente

| Entidad | Tipo | Descripcion |
|---------|------|-------------|
| `binary_sensor.tv_del_salon_status` | Binary Sensor | Estado de conexion (online/offline), consulta cada 30s |
| `notify.tv_del_salon` | Notify | Entidad de envio de notificaciones |

El `binary_sensor` tambien expone un atributo `designer_url` con un enlace directo al Designer web.

---

## Opciones de la integracion (icono de engranaje)

Haz clic en el **icono de engranaje** en la tarjeta de la integracion Peek-it [HA] para acceder a 3 menus:

### Ajustes

Edita la IP, el puerto, el nombre o la API key. La integracion se recarga automaticamente al guardar.

### Templates

Explora todos los templates disponibles en tu TV, ordenados por categoria:

- **Oficiales** — templates integrados que vienen con la aplicacion
- **Personalizados** — tus templates finalizados, cada uno con un UUID unico
- **Borradores** — trabajo en progreso, sin ID asignado aun

Cada template muestra su **nombre**, **ID** (copiable) y **parametros** disponibles.

### Designer

Enlace directo para abrir el Designer web en una nueva pestana. Muy practico para editar templates sin salir de HA.

---

## Uso

### Modo 1: Mensaje simple

La forma mas rapida — envia un mensaje de texto que aparece en la parte inferior de la pantalla con fondo oscuro.

```yaml
service: peek_it_ha.notify
data:
  message: "La lavadora ha terminado!"
  title: "Hogar"
  duration: 8000
```

### Modo 2: Template + parametros

Lo mas practico — reutiliza un template existente inyectando valores dinamicos.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Alerta de seguridad"
    message: "Movimiento detectado en el jardin"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

El servidor carga el template, reemplaza los `{{placeholders}}` con los valores de `params` y muestra el resultado.

**Como encontrar el template_id?**
- En el Designer: haz clic en la insignia verde "ID" de un template en la biblioteca
- En HA: icono de engranaje > Templates > copia el ID mostrado
- Via servicio: `peek_it_ha.get_templates` devuelve la lista completa

### Modo 3: Elementos crudos (JSON completo)

Lo mas flexible — define cada widget manualmente.

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
      content: "Camara del jardin"
      style:
        left: 62
        top: 28
        width: 34
        height: 5
        size: 18
        color: "#FFFFFF"
        align: center
```

### Cerrar una notificacion

```yaml
service: peek_it_ha.notify
data:
  action: CLOSE
```

### Notificacion persistente (infinita)

```yaml
service: peek_it_ha.notify
data:
  message: "Esperando confirmacion..."
  duration: 0
```

Duracion `0` = la notificacion permanece en pantalla hasta un `CLOSE` explicito o una pulsacion de boton.

---

## Texto a voz (TTS)

### TTS independiente

Envia un mensaje de voz a todos los TVs configurados:

```yaml
service: peek_it_ha.tts
data:
  text: "La cena esta lista!"
  lang: "es"
  speed: 1.0
  pitch: 1.0
  volume: 1.0
```

### Detener TTS

```yaml
service: peek_it_ha.tts_stop
```

### TTS con notificacion

Combina una notificacion visual con un mensaje de voz:

```yaml
service: peek_it_ha.notify
data:
  message: "Movimiento detectado en el jardin"
  title: "Seguridad"
  duration: 10000
  tts: "Movimiento detectado en el jardin"
  ttsLang: "es"
  ttsSpeed: 1.25
  ttsVolume: 0.8
```

### Parametros TTS

| Parametro | Tipo | Por defecto | Descripcion |
|-----------|------|-------------|-------------|
| `text` | string | — | Texto a pronunciar (servicio independiente) |
| `lang` | string | `en` | Codigo de idioma (en, fr, de, es, nl, pt) |
| `speed` | float | `1.0` | Velocidad del habla (0.5 a 2.0) |
| `pitch` | float | `1.0` | Tono de voz (0.5 a 2.0) |
| `volume` | float | `1.0` | Volumen (0.0 a 1.0) |

Cuando se usa dentro de `peek_it_ha.notify`, los campos llevan prefijo: `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

---

## Sonido

Reproduce un sonido con tu notificacion:

```yaml
service: peek_it_ha.notify
data:
  message: "Paquete entregado"
  title: "Timbre"
  sound: "01_notify.wav"
  soundVolume: 0.8
```

| Parametro | Tipo | Por defecto | Descripcion |
|-----------|------|-------------|-------------|
| `sound` | string | — | Nombre del archivo de sonido (ej. "01_notify.wav") |
| `soundVolume` | float | `1.0` | Volumen (0.0 a 1.0) |

La aplicacion Peek-it [TV] incluye sonidos integrados y permite subir sonidos personalizados a traves del Designer.

---

## Menu interactivo

El tipo de widget `menu` crea un menu overlay navegable con D-pad en el TV. Los menus admiten sub-menus, toggles de entidades HA con consulta de estado en tiempo real, callbacks de acciones y botones de cierre.

### Ejemplo de menu via automatizacion

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Controles rapidos",
          "titleIcon": "mdi:menu",
          "bgColor": "#1E1E1E",
          "textColor": "#FFFFFF",
          "accentColor": "#00E676",
          "items": [
            {"type": "submenu", "label": "Luces", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Salon", "icon": "mdi:lightbulb", "entity_id": "light.living_room"},
              {"type": "toggle", "label": "Cocina", "icon": "mdi:lightbulb", "entity_id": "light.kitchen"},
              {"type": "close", "label": "Volver", "icon": "mdi:arrow-left"}
            ]},
            {"type": "action", "label": "Modo pelicula", "icon": "mdi:movie", "action": "movie_mode"},
            {"type": "close", "label": "Cerrar", "icon": "mdi:close"}
          ]
        }
      style:
        left: 35
        top: 10
        width: 30
        height: 80
```

### Tipos de elementos del menu

| Tipo | Descripcion |
|------|-------------|
| `action` | Lanza un evento HA (`peekit_button_press`) con el ID de `action` especificado |
| `submenu` | Abre un sub-menu anidado con sus propios elementos `children` |
| `toggle` | Conmuta una entidad HA (requiere `entity_id`), consulta el estado cada 5s |
| `text` | Texto informativo (no interactivo) |
| `close` | Cierra el menu |

### Navegacion

- **Arriba/Abajo**: navegar entre elementos
- **Derecha/Enter**: abrir un sub-menu
- **Izquierda/Atras**: volver al menu anterior
- **Atras en raiz**: cerrar el menu

---

## Widget de entidades HA

Muestra el estado de entidades HA en tiempo real directamente en el TV usando un widget `webview` conectado via WebSocket o consulta REST.

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

## Widget de graficos HA

La aplicacion Peek-it [TV] soporta graficos CSS/SVG para mostrar el historial de entidades. Tipos de graficos: **area**, **linea** y **barras**.

Los graficos se renderizan como CSS/SVG puro — no se necesitan bibliotecas externas. Configuralos a traves del editor de graficos del Designer.

---

## Configuracion del overlay

### Reloj overlay

La aplicacion Peek-it [TV] puede mostrar un reloj overlay persistente. Configuralo a traves de los Ajustes del Designer o del endpoint `/api/config/clock`:

- Activar/desactivar
- Formato (12h/24h)
- Posicion, color, tamano, opacidad

### Atenuacion de fondo

Una capa configurable de atenuacion de fondo. Configurable a traves de los Ajustes del Designer o `/api/config/dimming`:

- Activar/desactivar
- Color, opacidad

---

## Parametros disponibles

### Campos principales

| Parametro | Tipo | Por defecto | Descripcion |
|-----------|------|-------------|-------------|
| `action` | string | `DISPLAY` | `DISPLAY` para mostrar, `CLOSE` para cerrar |
| `duration` | int | `10000` | Duracion en milisegundos (0 = infinita) |
| `priority` | string | `normal` | `normal` o `urgent` |
| `animationIn` | string | `fade` | Animacion de entrada |
| `animationOut` | string | `fade` | Animacion de salida |
| `template_id` | string | — | UUID del template a utilizar |
| `params` | dict | — | Parametros dinamicos del template |
| `elements` | list | — | Lista de widgets (modo avanzado) |
| `message` | string | — | Texto simple (modo simple) |
| `title` | string | — | Texto del titulo (modo simple) |
| `sound` | string | — | Nombre del archivo de sonido |
| `soundVolume` | float | `1.0` | Volumen del sonido (0.0-1.0) |
| `tts` | string | — | Texto TTS (leido en voz alta con la notificacion) |
| `ttsLang` | string | `en` | Codigo de idioma TTS |
| `ttsSpeed` | float | `1.0` | Velocidad del habla TTS (0.5-2.0) |
| `ttsPitch` | float | `1.0` | Tono de voz TTS (0.5-2.0) |
| `ttsVolume` | float | `1.0` | Volumen TTS (0.0-1.0) |

### Animaciones disponibles

| Nombre | Efecto |
|--------|--------|
| `none` | Instantaneo, sin animacion |
| `fade` | Aparicion/desaparicion gradual |
| `slide_right` | Deslizar desde/hacia la derecha |
| `slide_left` | Deslizar desde/hacia la izquierda |
| `slide_top` | Deslizar desde/hacia arriba |
| `slide_bottom` | Deslizar desde/hacia abajo |
| `pop` | Efecto de zoom/escala |

### Tipos de widgets

| Tipo | Descripcion | Contenido (`content`) |
|------|-------------|-----------------------|
| `text` | Texto estatico | El texto a mostrar |
| `button` | Boton interactivo (mando del TV) | Etiqueta del boton |
| `box` | Rectangulo / contenedor | — |
| `circle` | Circulo | — |
| `ellipse` | Elipse / ovalo | — |
| `image` | Imagen (PNG, JPG, URL) | URL de la imagen |
| `video` | Flujo de video RTSP / HTTP | URL del flujo |
| `webview` | Pagina web embebida | URL de la pagina |
| `svg` | Imagen vectorial SVG | URL o ruta SVG |
| `line` | Linea horizontal | — |
| `arrow` | Flecha (apuntando a la derecha) | — |
| `menu` | Menu interactivo D-pad | JSON MenuConfig |

### Propiedades de estilo

| Propiedad | Tipo | Descripcion |
|-----------|------|-------------|
| `left` | float | Posicion X en % de pantalla (0-100) |
| `top` | float | Posicion Y en % de pantalla (0-100) |
| `width` | float | Ancho en % de pantalla |
| `height` | float | Alto en % de pantalla |
| `color` | string | Color del texto (hex, ej. `#FFFFFF`) |
| `bgColor` | string | Color de fondo (hex con alfa, ej. `#CC000000`) |
| `size` | int | Tamano de fuente |
| `font` | string | Familia de fuente (Roboto, sans-serif, etc.) |
| `weight` | string | Grosor de fuente (`normal`, `bold`) |
| `align` | string | Alineacion (`left`, `center`, `right`) |
| `opacity` | float | Opacidad (0.0 a 1.0) |
| `radius` | int | Radio de esquina (pixeles) |
| `borderWidth` | int | Grosor del borde (pixeles) |
| `borderColor` | string | Color del borde (hex) |
| `rotation` | float | Rotacion en grados |
| `focusColor` | string | Color del borde con foco |
| `focusBgColor` | string | Color de fondo con foco |

### Propiedades de interaccion (botones)

| Propiedad | Tipo | Descripcion |
|-----------|------|-------------|
| `focusable` | bool | El widget recibe foco del mando del TV |
| `directFocus` | bool | El widget obtiene foco al mostrarse |
| `action` | string | `CLOSE` para cerrar, o ID personalizado para webhook |
| `paramKey` | string | Vincula el contenido a un parametro de template |
| `actionParamKey` | string | Vincula la accion a un parametro de template |

---

## El Designer

El Designer es un **editor visual web** integrado en la aplicacion Peek-it [TV]. Accede desde cualquier navegador en tu red local.

**URL**: `http://<IP_TV>:<PUERTO>/` (ej. `http://192.168.1.42:8081/`)

Tambien puedes acceder a traves de:
- El atributo `designer_url` del binary_sensor en HA
- El icono de engranaje > Designer en las opciones de la integracion

### Funcionalidades

- **11 tipos de widgets** — arrastrar y soltar sobre un lienzo calibrado para TV
- **Vista previa JSON en tiempo real** — observa el payload exacto que se esta construyendo
- **Biblioteca de templates** — guardar, cargar, renombrar, eliminar, exportar/importar
- **Sistema de parametros** — define `paramKey` en los widgets para contenido dinamico
- **Auto-calibracion** — se adapta a la resolucion real de tu TV (16:9, 21:9, etc.)
- **Configuracion de sonido** — ajustes de sonido de notificacion por defecto
- **Configuracion del token HA** — necesario para los callbacks de webhook
- **Internacionalizacion** — disponible en 6 idiomas (EN, FR, DE, ES, NL, PT)

### Enviar y probar

- **Boton ENVIAR** (azul) — envia el layout actual al TV inmediatamente
- **Boton KILL** (rojo) — cierra la notificacion actual
- **Vista previa JSON** (pie de pagina) — observa el payload exacto que se enviara

---

## Templates y parametros

### Concepto

Un template es un layout de notificacion reutilizable. En vez de enviar 15 lineas de JSON cada vez, puedes:

1. **Crear** el layout en el Designer (arrastrar y soltar)
2. **Definir parametros** (`paramKey`) en los elementos dinamicos
3. **Guardar** como Personalizado (se genera un UUID)
4. **Usar** el `template_id` + `params` en tus automatizaciones

### Recuperar la lista de templates

```yaml
service: peek_it_ha.get_templates
response_variable: result
```

Devuelve un diccionario por dispositivo configurado:
```json
{
  "TV del salon": {
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

## Automatizaciones

### Alerta de deteccion de movimiento

```yaml
automation:
  - alias: "Alerta movimiento en el jardin"
    trigger:
      - platform: state
        entity_id: binary_sensor.garden_motion
        to: "on"
    action:
      - service: peek_it_ha.notify
        data:
          template_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
          params:
            title: "Movimiento detectado!"
            camera_url: "rtsp://192.168.1.50:554/stream1"
          duration: 15000
          animationIn: slide_right
          animationOut: fade
```

### Parte meteorologico matutino

```yaml
automation:
  - alias: "Meteorologia matutina"
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
          title: "El tiempo hoy"
          duration: 10000
          animationIn: fade
```

### Automatizacion de anuncio TTS

```yaml
automation:
  - alias: "Alerta TTS timbre"
    trigger:
      - platform: state
        entity_id: binary_sensor.doorbell
        to: "on"
    action:
      - service: peek_it_ha.tts
        data:
          text: "Alguien esta en la puerta"
          lang: "es"
          speed: 1.25
          volume: 1.0
```

### Notificacion con sonido

```yaml
automation:
  - alias: "Alerta lavadora terminada"
    trigger:
      - platform: state
        entity_id: sensor.washing_machine
        to: "idle"
    action:
      - service: peek_it_ha.notify
        data:
          message: "La lavadora ha terminado!"
          title: "Colada"
          duration: 8000
          sound: "08-notify.mp3"
          soundVolume: 0.7
```

### Botones interactivos — respuesta a HA

Cuando un usuario pulsa un boton en una notificacion (con el mando del TV), se lanza un evento HA:

```yaml
automation:
  - alias: "Boton TV - Apagar luces"
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

### Alerta persistente con boton de cierre

```yaml
automation:
  - alias: "Alerta fuga de agua"
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
          tts: "Atencion! Fuga de agua detectada!"
          ttsLang: "es"
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
              content: "FUGA DE AGUA DETECTADA"
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
              content: "Entendido"
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

### Flujo de camara RTSP

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

El flujo se muestra con latencia ultra baja (~50ms) gracias a una configuracion optimizada de ExoPlayer.

---

## Referencia de servicios

| Servicio | Descripcion |
|----------|-------------|
| `peek_it_ha.notify` | Enviar notificacion a todos los dispositivos configurados |
| `peek_it_ha.get_templates` | Recuperar la lista de templates de todos los dispositivos |
| `peek_it_ha.tts` | Enviar TTS a todos los dispositivos configurados |
| `peek_it_ha.tts_stop` | Detener TTS en todos los dispositivos configurados |

---

## Webhooks y eventos

La integracion escucha un webhook para recibir logs y acciones de botones desde el TV.

| Evento HA | Disparador | Datos |
|-----------|------------|-------|
| `peekit_button_press` | Pulsacion de boton en el TV | `{ "action": "button_id" }` |

Los logs del TV se reenvian al logger de HA con el prefijo `[PEEK-IT REPORT]`.

---

## Multi-dispositivo

La integracion soporta **multiples dispositivos**. Anade cada TV como una integracion separada. Los servicios `peek_it_ha.notify`, `tts`, `tts_stop` y `get_templates` envian automaticamente a **todos los dispositivos configurados**.

Para dirigirte a un solo dispositivo, usa la entidad `notify` especifica:

```yaml
service: notify.send_message
target:
  entity_id: notify.tv_del_salon
data:
  message: "Solo en este TV"
```

---

## Internacionalizacion

La integracion y la aplicacion Peek-it [TV] soportan **6 idiomas**:

| Codigo | Idioma |
|--------|--------|
| `en` | Ingles (por defecto) |
| `fr` | Frances |
| `de` | Aleman |
| `es` | Espanol |
| `nl` | Neerlandes |
| `pt` | Portugues |

El idioma se puede configurar en los ajustes del Designer o en la pantalla de ajustes de la aplicacion Peek-it [TV].

---

## WAF — El KPI definitivo

El legendario **WAF** — *Wife Acceptance Factor* (Factor de Aceptacion de la Esposa). Esa metrica no oficial pero absolutamente critica que mide la tolerancia de tu pareja hacia tus experimentos de domotica.

### Casos de uso que suben tu WAF

**Colada inteligente**: una notificacion "La lavadora ha terminado!" aparece discretamente durante la pelicula. Se acabaron las coladas olvidadas 3 dias en el tambor.

> *(WAF: +23 puntos)*

**Meteorologia matutina**: cada dia a las 7:30, el tiempo aparece en el TV de la cocina.

> *(WAF: +15 puntos)*

**Camara del timbre**: alguien llama, la imagen de la camara aparece en pantalla. Decision desde el sofa. Nadie tuvo que levantarse.

> *(WAF: +38 puntos)*

**Marcador deportivo**: un discreto "2 - 1, 78'" aparece 3 segundos en la esquina superior derecha. Todos contentos. Nadie cambio de canal.

> *(WAF: +52 puntos)*

### El caso de uso que DESTRUYE tu WAF

**Depurar en produccion**: estas probando tus notificaciones a las 23:00 mientras tu pareja ve el final de temporada de su serie favorita.

> *(WAF: -347 puntos. Tiempo estimado de recuperacion: 3 semanas. Y prepara cena romantica.)*

**Consejo pro**: prueba tus automatizaciones ANTES de las 21:00. O usa el boton **KILL** del Designer.

---

## Resolucion de problemas

| Problema | Solucion |
|----------|----------|
| La integracion no aparece en HA | Asegurate de que la carpeta esta en `custom_components/peek_it_ha/`. Reinicia HA. |
| "No se puede conectar" al configurar | Verifica la IP y el puerto. La aplicacion debe estar en ejecucion en el TV. Prueba `http://IP:8081/api/status` en un navegador. |
| El binary sensor siempre esta "offline" | La aplicacion Peek-it [TV] esta en ejecucion? El servicio se inicia al arrancar? |
| La notificacion no se muestra | Comprueba el permiso de overlay en los ajustes del Android TV. |
| El Designer no conecta | Asegurate de estar en la misma red. Prueba `http://IP:PUERTO/` en tu navegador. |
| Templates vacios en el menu de engranaje | El TV debe estar encendido y accesible. Comprueba el estado del binary_sensor. |
| El boton del TV no activa HA | Configura el token HA en el Designer (icono de engranaje). Verifica que `ha_ip` sea accesible desde el TV. |
| El TTS no habla | Comprueba que hay un motor TTS instalado en el Android TV (Google TTS suele estar preinstalado). |
| No hay sonido con la notificacion | Verifica que el archivo de sonido existe (comprueba en los ajustes del Designer). Algunas aplicaciones de streaming pueden bloquear la mezcla de audio. |
| El menu no responde al D-pad | Asegurate de que el elemento menu tiene foco. Usa `duration: 0` para que el menu permanezca abierto. |

---

## Contribuir

Las contribuciones son bienvenidas! Abre un issue o un pull request en el [repositorio de GitHub](https://github.com/jolabs40/peek-it-ha).

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para mas detalles.

---

<p align="center">
  Hecho con cafe, demasiados archivos YAML y un amor desmedido por los overlays.<br/>
  <strong>Peek-it [HA]</strong> — porque tu TV puede hacer mucho mas de lo que crees.
</p>
