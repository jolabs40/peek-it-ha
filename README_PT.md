# Peek-it [HA] — Integra&ccedil;&atilde;o Home Assistant

<p align="center">
  <img src="custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Transforme a sua Android TV num ecrã de notificações inteligente.</strong><br/>
  Alertas, câmaras, dashboards, TTS, menus — overlay na sua TV em tempo real.
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
  <a href="#-instalação">Instalação</a> •
  <a href="#-utilização">Utilização</a> •
  <a href="#-o-designer">Designer</a> •
  <a href="#-templates--parâmetros">Templates</a> •
  <a href="#-texto-para-voz-tts">TTS</a> •
  <a href="#-som">Som</a> •
  <a href="#-menu-interativo">Menu</a> •
  <a href="#-automações">Automações</a> •
  <a href="#-waf--o-kpi-supremo">WAF</a>
</p>

<p align="center">
  <b>Idiomas:</b>
  <a href="README.md">English</a> |
  <a href="README_FR.md">Fran&ccedil;ais</a> |
  <a href="README_DE.md">Deutsch</a> |
  <a href="README_ES.md">Espa&ntilde;ol</a> |
  <a href="README_NL.md">Nederlands</a> |
  Portugu&ecirc;s
</p>

---

## Porquê Peek-it [HA]?

O seu dispositivo Android TV está ligado à televisão 24 horas por dia. Porque não aproveitá-lo?

**Peek-it [HA]** é a integração Home Assistant para a aplicação Android **Peek-it [TV]**. Juntos, apresentam **notificações ricas em overlay** por cima de qualquer aplicação em execução. A ver um filme? A imagem de uma câmara aparece durante 5 segundos num canto. Noite de futebol? O resultado atualiza-se em tempo real. Tocam à campainha? A câmara da porta surge instantaneamente.

### O que pode apresentar

| Tipo | Exemplo |
|------|---------|
| **Texto rico** | Títulos, mensagens, contadores, meteorologia |
| **Imagens** | Fotografias, capturas, logótipos, códigos QR |
| **Streams de vídeo RTSP** | Câmaras de segurança ao vivo, latência ultra-baixa |
| **Páginas web** | Dashboards HA, gráficos, widgets meteorológicos |
| **SVG** | Ícones vetoriais, indicadores, diagramas |
| **Formas** | Retângulos, elipses, linhas, setas — construa layouts completos |
| **Botões interativos** | Controláveis pelo telecomando da TV, acionam automações HA |
| **Menus interativos** | Menus navegáveis por D-pad com toggles de entidades HA |
| **Widgets de entidades HA** | Apresentação do estado de entidades em tempo real via WebSocket/REST |
| **Gráficos HA** | Gráficos CSS/SVG de área, linha e barras |
| **Texto para voz** | Anúncios de voz na sua TV |

### Funcionalidades principais

- **Zero latência** — overlay nativo Android, sem streaming nem casting
- **Funciona com tudo** — o overlay sobrepõe-se a qualquer aplicação
- **Designer visual** — crie notificações com arrastar e largar a partir de qualquer navegador
- **Templates reutilizáveis** — desenhe uma vez, reutilize com parâmetros dinâmicos
- **7 animações** — fade, slide, pop... efeitos de entrada e saída independentes
- **Texto para voz** — anúncios de voz diretamente na TV
- **Alertas sonoros** — reproduza sons de notificação acompanhando os visuais
- **Menus interativos** — menus overlay navegáveis por D-pad com toggles HA
- **Multi-dispositivo** — gerencie várias TVs a partir de uma única instância HA
- **6 idiomas** — EN, FR, DE, ES, NL, PT

---

## Pré-requisitos

1. **Um dispositivo Android TV** com a aplicação **Peek-it [TV]** instalada
2. **Home Assistant** instalado e em execução
3. Ambos os dispositivos na **mesma rede local**

### Instalar a aplicação Peek-it [TV]

> A aplicação (ainda) não está na Play Store. Instale-a via sideload.

1. Descarregue o APK a partir da [página de Releases](https://github.com/jolabs40/peek-it-ha/releases)
2. Transfira-o para o seu dispositivo (pen USB, `adb install` ou uma aplicação de gestão de ficheiros)
3. Abra a aplicação — será solicitada a permissão de overlay (apresentar sobre outras apps)
4. Conceda a permissão — o serviço arranca automaticamente
5. Anote o **endereço IP** apresentado no ecrã principal (ex.: `192.168.1.42`)
6. A porta predefinida é **8081** (configurável na aplicação)

> **Dica**: O serviço arranca automaticamente com o dispositivo. Ligue-o e esqueça.

---

## Instalação

### Método 1: HACS (recomendado)

1. Abra o HACS no Home Assistant
2. Vá a **Integrações** > menu de 3 pontos > **Repositórios personalizados**
3. Adicione o URL do repositório: `https://github.com/jolabs40/peek-it-ha`
4. Categoria: **Integration**
5. Clique em **Peek-it [HA]** > **Descarregar**
6. **Reinicie o Home Assistant**

### Método 2: Instalação manual

1. Copie a pasta `peek_it_ha/` para o diretório `custom_components/`:
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
2. **Reinicie o Home Assistant**

### Adicionar a integração

1. Vá a **Definições** > **Dispositivos e Serviços** > **Adicionar Integração**
2. Procure **Peek-it [HA]**
3. Preencha:
   - **Endereço IP**: o IP do dispositivo Android TV (apresentado na aplicação)
   - **Porta**: `8081` (predefinida)
   - **Nome**: um nome amigável para a sua TV (ex.: "TV da Sala")
   - **API Key**: se a autenticação estiver ativada na aplicação da TV
4. Submeta — a integração testa a ligação e configura-se automaticamente

### O que é criado automaticamente

| Entidade | Tipo | Descrição |
|----------|------|-----------|
| `binary_sensor.living_room_tv_status` | Binary Sensor | Estado da ligação (online/offline), polling a cada 30s |
| `notify.living_room_tv` | Notify | Entidade de envio de notificações |

O `binary_sensor` também expõe um atributo `designer_url` com uma hiperligação direta para o Designer web.

---

## Opções da integração (ícone da engrenagem)

Clique no **ícone da engrenagem** no cartão da integração Peek-it [HA] para aceder a 3 menus:

### Definições

Edite o IP, a porta, o nome ou a API key. A integração recarrega automaticamente após guardar.

### Templates

Navegue por todos os templates disponíveis na sua TV, organizados por categoria:

- **Official** — templates incorporados fornecidos com a aplicação
- **Custom** — os seus templates finalizados, cada um com um UUID único
- **Drafts** — trabalho em curso, sem ID atribuído

Cada template apresenta o **nome**, o **ID** (copiável) e os **parâmetros** disponíveis.

### Designer

Hiperligação direta para abrir o Designer web num novo separador. Prático para editar templates sem sair do HA.

---

## Utilização

### Modo 1: Mensagem simples

A forma mais rápida — envie uma mensagem de texto que aparece na parte inferior do ecrã com fundo escuro.

```yaml
service: peek_it_ha.notify
data:
  message: "A máquina de lavar terminou!"
  title: "Casa"
  duration: 8000
```

### Modo 2: Template + parâmetros

O mais prático — reutilize um template existente injetando valores dinâmicos.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Alerta de Segurança"
    message: "Movimento detetado no jardim"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

O servidor carrega o template, substitui os `{{placeholders}}` pelos valores de `params` e apresenta o resultado.

**Como encontrar o template_id?**
- No Designer: clique no emblema verde "ID" num template da biblioteca
- No HA: ícone da engrenagem > Templates > copie o ID apresentado
- Via serviço: `peek_it_ha.get_templates` devolve a lista completa

### Modo 3: Elementos em bruto (JSON completo)

O mais flexível — defina cada widget manualmente.

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

### Fechar uma notificação

```yaml
service: peek_it_ha.notify
data:
  action: CLOSE
```

### Notificação persistente (infinita)

```yaml
service: peek_it_ha.notify
data:
  message: "A aguardar confirmação..."
  duration: 0
```

Duração `0` = a notificação permanece no ecrã até um `CLOSE` explícito ou o pressionar de um botão.

---

## Texto para voz (TTS)

### TTS autónomo

Envie uma mensagem de voz para todas as TVs configuradas:

```yaml
service: peek_it_ha.tts
data:
  text: "O jantar está pronto!"
  lang: "pt"
  speed: 1.0
  pitch: 1.0
  volume: 1.0
```

### Parar TTS

```yaml
service: peek_it_ha.tts_stop
```

### TTS com notificação

Combine uma notificação visual com uma mensagem de voz:

```yaml
service: peek_it_ha.notify
data:
  message: "Movimento detetado no jardim"
  title: "Segurança"
  duration: 10000
  tts: "Movimento detetado no jardim"
  ttsLang: "pt"
  ttsSpeed: 1.25
  ttsVolume: 0.8
```

### Parâmetros TTS

| Parâmetro | Tipo | Predefinição | Descrição |
|-----------|------|--------------|-----------|
| `text` | string | — | Texto a falar (serviço autónomo) |
| `lang` | string | `en` | Código do idioma (en, fr, de, es, nl, pt) |
| `speed` | float | `1.0` | Velocidade da fala (0.5 a 2.0) |
| `pitch` | float | `1.0` | Tom da voz (0.5 a 2.0) |
| `volume` | float | `1.0` | Volume (0.0 a 1.0) |

Quando usado dentro de `peek_it_ha.notify`, os campos são prefixados: `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

---

## Som

Reproduza um som com a sua notificação:

```yaml
service: peek_it_ha.notify
data:
  message: "Encomenda entregue"
  title: "Campainha"
  sound: "01_notify.wav"
  soundVolume: 0.8
```

| Parâmetro | Tipo | Predefinição | Descrição |
|-----------|------|--------------|-----------|
| `sound` | string | — | Nome do ficheiro de som (ex.: "01_notify.wav") |
| `soundVolume` | float | `1.0` | Volume (0.0 a 1.0) |

A aplicação Peek-it [TV] inclui sons incorporados e suporta o carregamento de sons personalizados através do Designer.

---

## Menu interativo

O tipo de widget `menu` cria um menu overlay navegável por D-pad na TV. Os menus suportam submenus, toggles de entidades HA com polling de estado em tempo real, callbacks de ação e botões de fecho.

### Exemplo de menu via automação

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

### Tipos de itens de menu

| Tipo | Descrição |
|------|-----------|
| `action` | Aciona um evento HA (`peekit_button_press`) com o `action` ID especificado |
| `submenu` | Abre um submenu aninhado com os seus próprios itens `children` |
| `toggle` | Alterna uma entidade HA (requer `entity_id`), polling de estado a cada 5s |
| `text` | Texto informativo (não interativo) |
| `close` | Fecha o menu |

### Navegação

- **Cima/Baixo**: navegar entre itens
- **Direita/Enter**: abrir um submenu
- **Esquerda/Voltar**: regressar ao menu anterior
- **Voltar na raiz**: fechar o menu

---

## Widget de entidades HA

Apresente estados de entidades HA em tempo real diretamente na TV utilizando um widget `webview` ligado via WebSocket ou polling REST.

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

## Widget de gráficos HA

A aplicação Peek-it [TV] suporta gráficos CSS/SVG para apresentar o histórico de entidades. Tipos de gráfico: **área**, **linha** e **barras**.

Os gráficos são renderizados em CSS/SVG puro — sem bibliotecas externas. Configure-os através do editor de gráficos do Designer.

---

## Configuração do overlay

### Overlay de relógio

A aplicação Peek-it [TV] pode apresentar um overlay de relógio persistente. Configure-o através das Definições do Designer ou do endpoint `/api/config/clock`:

- Ativar/desativar
- Formato (12h/24h)
- Posição, cor, tamanho, opacidade

### Overlay de escurecimento

Uma camada de escurecimento de fundo configurável. Configure através das Definições do Designer ou de `/api/config/dimming`:

- Ativar/desativar
- Cor, opacidade

---

## Parâmetros disponíveis

### Campos principais

| Parâmetro | Tipo | Predefinição | Descrição |
|-----------|------|--------------|-----------|
| `action` | string | `DISPLAY` | `DISPLAY` para mostrar, `CLOSE` para fechar |
| `duration` | int | `10000` | Duração em milissegundos (0 = infinita) |
| `priority` | string | `normal` | `normal` ou `urgent` |
| `animationIn` | string | `fade` | Animação de entrada |
| `animationOut` | string | `fade` | Animação de saída |
| `template_id` | string | — | UUID do template a utilizar |
| `params` | dict | — | Parâmetros dinâmicos do template |
| `elements` | list | — | Lista de widgets (modo avançado) |
| `message` | string | — | Texto simples (modo simples) |
| `title` | string | — | Texto do título (modo simples) |
| `sound` | string | — | Nome do ficheiro de som |
| `soundVolume` | float | `1.0` | Volume do som (0.0-1.0) |
| `tts` | string | — | Texto TTS (lido em voz alta com a notificação) |
| `ttsLang` | string | `en` | Código de idioma TTS |
| `ttsSpeed` | float | `1.0` | Velocidade de fala TTS (0.5-2.0) |
| `ttsPitch` | float | `1.0` | Tom de voz TTS (0.5-2.0) |
| `ttsVolume` | float | `1.0` | Volume TTS (0.0-1.0) |

### Animações disponíveis

| Nome | Efeito |
|------|--------|
| `none` | Instantâneo, sem animação |
| `fade` | Aparecimento/desaparecimento gradual |
| `slide_right` | Deslizar de/para a direita |
| `slide_left` | Deslizar de/para a esquerda |
| `slide_top` | Deslizar de/para cima |
| `slide_bottom` | Deslizar de/para baixo |
| `pop` | Efeito de zoom/escala |

### Tipos de widget

| Tipo | Descrição | Conteúdo (`content`) |
|------|-----------|----------------------|
| `text` | Texto estático | O texto a apresentar |
| `button` | Botão interativo (telecomando da TV) | Rótulo do botão |
| `box` | Retângulo / contentor | — |
| `circle` | Círculo | — |
| `ellipse` | Elipse / oval | — |
| `image` | Imagem (PNG, JPG, URL) | URL da imagem |
| `video` | Stream de vídeo RTSP / HTTP | URL do stream |
| `webview` | Página web incorporada | URL da página |
| `svg` | Imagem vetorial SVG | URL ou caminho SVG |
| `line` | Linha horizontal | — |
| `arrow` | Seta (a apontar para a direita) | — |
| `menu` | Menu interativo D-pad | JSON MenuConfig |

### Propriedades de estilo

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `left` | float | Posição X em % do ecrã (0-100) |
| `top` | float | Posição Y em % do ecrã (0-100) |
| `width` | float | Largura em % do ecrã |
| `height` | float | Altura em % do ecrã |
| `color` | string | Cor do texto (hex, ex.: `#FFFFFF`) |
| `bgColor` | string | Cor de fundo (hex com alfa, ex.: `#CC000000`) |
| `size` | int | Tamanho da fonte |
| `font` | string | Família da fonte (Roboto, sans-serif, etc.) |
| `weight` | string | Espessura da fonte (`normal`, `bold`) |
| `align` | string | Alinhamento (`left`, `center`, `right`) |
| `opacity` | float | Opacidade (0.0 a 1.0) |
| `radius` | int | Raio dos cantos (pixéis) |
| `borderWidth` | int | Espessura da borda (pixéis) |
| `borderColor` | string | Cor da borda (hex) |
| `rotation` | float | Rotação em graus |
| `focusColor` | string | Cor da borda quando focado |
| `focusBgColor` | string | Cor de fundo quando focado |

### Propriedades de interação (botões)

| Propriedade | Tipo | Descrição |
|-------------|------|-----------|
| `focusable` | bool | O widget recebe foco do telecomando da TV |
| `directFocus` | bool | O widget obtém foco ao ser apresentado |
| `action` | string | `CLOSE` para fechar, ou ID personalizado para webhook |
| `paramKey` | string | Liga o conteúdo a um parâmetro do template |
| `actionParamKey` | string | Liga a ação a um parâmetro do template |

---

## O Designer

O Designer é um **editor visual web** incorporado na aplicação Peek-it [TV]. Aceda a partir de qualquer navegador na sua rede local.

**URL**: `http://<IP_DA_TV>:<PORTA>/` (ex.: `http://192.168.1.42:8081/`)

Também pode aceder através de:
- O atributo `designer_url` do binary_sensor no HA
- O ícone da engrenagem > Designer nas opções da integração

### Funcionalidades

- **11 tipos de widget** — arrastar e largar sobre uma tela calibrada com a TV
- **Pré-visualização JSON em tempo real** — veja o payload exato a ser construído
- **Biblioteca de templates** — guardar, carregar, renomear, eliminar, exportar/importar
- **Sistema de parâmetros** — defina `paramKey` nos widgets para conteúdo dinâmico
- **Auto-calibração** — adapta-se à resolução real da sua TV (16:9, 21:9, etc.)
- **Configuração de som** — definições predefinidas de som de notificação
- **Configuração de token HA** — necessário para callbacks de webhook
- **Internacionalização** — disponível em 6 idiomas (EN, FR, DE, ES, NL, PT)

### Enviar e testar

- **Botão SEND** (azul) — envia o layout atual para a TV imediatamente
- **Botão KILL** (vermelho) — fecha a notificação atual
- **Pré-visualização JSON** (rodapé) — veja o payload exato que será enviado

---

## Templates & parâmetros

### Conceito

Um template é um layout de notificação reutilizável. Em vez de enviar 15 linhas de JSON de cada vez, pode:

1. **Criar** o layout no Designer (arrastar e largar)
2. **Definir parâmetros** (`paramKey`) nos elementos dinâmicos
3. **Guardar** como Custom (UUID gerado)
4. **Usar** o `template_id` + `params` nas suas automações

### Obter a lista de templates

```yaml
service: peek_it_ha.get_templates
response_variable: result
```

Devolve um dicionário por dispositivo configurado:
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

## Automações

### Alerta de deteção de movimento

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
            title: "Movimento detetado!"
            camera_url: "rtsp://192.168.1.50:554/stream1"
          duration: 15000
          animationIn: slide_right
          animationOut: fade
```

### Boletim meteorológico matinal

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
          title: "Meteorologia de hoje"
          duration: 10000
          animationIn: fade
```

### Automação de anúncio TTS

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
          text: "Está alguém à porta"
          lang: "pt"
          speed: 1.25
          volume: 1.0
```

### Notificação com som

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
          message: "A máquina de lavar terminou!"
          title: "Lavandaria"
          duration: 8000
          sound: "08-notify.mp3"
          soundVolume: 0.7
```

### Botões interativos — feedback para o HA

Quando um utilizador pressiona um botão numa notificação (via telecomando da TV), é disparado um evento HA:

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

### Alerta persistente com botão de fecho

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
          tts: "Atenção! Fuga de água detetada!"
          ttsLang: "pt"
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
              content: "FUGA DE ÁGUA DETETADA"
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

### Feed de câmara RTSP

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

O feed é apresentado com latência ultra-baixa (~50ms) graças a uma configuração otimizada do ExoPlayer.

---

## Referência de serviços

| Serviço | Descrição |
|---------|-----------|
| `peek_it_ha.notify` | Enviar notificação para todos os dispositivos configurados |
| `peek_it_ha.get_templates` | Obter lista de templates de todos os dispositivos |
| `peek_it_ha.tts` | Enviar TTS para todos os dispositivos configurados |
| `peek_it_ha.tts_stop` | Parar TTS em todos os dispositivos configurados |

---

## Webhooks e eventos

A integração escuta um webhook para receber logs e ações de botões da TV.

| Evento HA | Acionador | Dados |
|-----------|-----------|-------|
| `peekit_button_press` | Pressão de botão na TV | `{ "action": "button_id" }` |

Os logs da TV são encaminhados para o logger do HA com o prefixo `[PEEK-IT REPORT]`.

---

## Multi-dispositivo

A integração suporta **múltiplos dispositivos**. Adicione cada TV como uma integração separada. Os serviços `peek_it_ha.notify`, `tts`, `tts_stop` e `get_templates` enviam automaticamente para **todos os dispositivos configurados**.

Para visar um único dispositivo, utilize a entidade `notify` específica:

```yaml
service: notify.send_message
target:
  entity_id: notify.living_room_tv
data:
  message: "Apenas nesta TV"
```

---

## Internacionalização

A integração e a aplicação Peek-it [TV] suportam **6 idiomas**:

| Código | Idioma |
|--------|--------|
| `en` | Inglês (predefinição) |
| `fr` | Francês |
| `de` | Alemão |
| `es` | Espanhol |
| `nl` | Neerlandês |
| `pt` | Português |

O idioma pode ser configurado nas definições do Designer ou no ecrã de definições da aplicação Peek-it [TV].

---

## WAF — O KPI Supremo

O lendário **WAF** — *Wife Acceptance Factor* (Fator de Aceitação da Esposa). Aquela métrica não-oficial mas absolutamente crítica que mede a tolerância da sua cara-metade às suas experiências de domótica.

### Casos de uso que sobem o seu WAF

**Lavandaria inteligente**: uma notificação "A roupa está pronta!" aparece discretamente durante o filme. Nunca mais cargas esquecidas 3 dias dentro da máquina.

> *(WAF: +23 pontos)*

**Meteorologia matinal**: todos os dias às 7h30, a previsão do tempo aparece na TV da cozinha.

> *(WAF: +15 pontos)*

**Câmara da campainha**: alguém toca, a imagem da câmara surge no ecrã. Decisão tomada a partir do sofá. Ninguém se levantou.

> *(WAF: +38 pontos)*

**Resultado desportivo**: um discreto "2 - 1, 78'" aparece durante 3 segundos no canto superior direito. Toda a gente contente. Ninguém mudou de canal.

> *(WAF: +52 pontos)*

### O caso de uso que DESTRÓI o seu WAF

**Depuração em produção**: está a testar as suas notificações às 23h enquanto a sua cara-metade assiste ao último episódio da temporada. No ecrã aparece um enorme retângulo vermelho com "TESTE 47 - IGNORAR" em Comic Sans.

> *(WAF: -347 pontos. Tempo estimado de recuperação: 3 semanas. Dormir no sofá incluído.)*

**Dica profissional**: teste as suas automações ANTES das 21h. Ou use o botão **KILL** no Designer. A sua relação agradece.

---

## Resolução de problemas

| Problema | Solução |
|----------|---------|
| Integração não encontrada no HA | Certifique-se de que a pasta está em `custom_components/peek_it_ha/`. Reinicie o HA. |
| "Não é possível ligar" ao configurar | Verifique o IP e a porta. A aplicação deve estar a correr na TV. Teste `http://IP:8081/api/status` num navegador. |
| Binary sensor sempre "offline" | A aplicação Peek-it [TV] está a correr? O serviço arranca no arranque? |
| A notificação não aparece | Verifique a permissão de overlay nas definições do Android TV. |
| O Designer não liga | Certifique-se de que está na mesma rede. Tente `http://IP:PORTA/` no seu navegador. |
| Templates vazios no menu da engrenagem | A TV deve estar ligada e acessível. Verifique o estado do binary_sensor. |
| O botão da TV não aciona o HA | Configure o token HA no Designer (ícone da engrenagem). Verifique se `ha_ip` é acessível a partir da TV. |
| O TTS não fala | Verifique se um motor TTS está instalado no Android TV (o Google TTS normalmente vem pré-instalado). |
| Sem som com a notificação | Verifique se o ficheiro de som existe (consulte nas definições do Designer). Algumas aplicações de streaming podem bloquear a mistura de áudio. |
| O menu não responde ao D-pad | Certifique-se de que o elemento de menu tem foco. Defina `duration: 0` para que o menu permaneça aberto. |

---

## Contribuir

Contribuições são bem-vindas! Abra uma issue ou um pull request no [repositório GitHub](https://github.com/jolabs40/peek-it-ha).

## Licença

Este projeto é distribuído sob a Licença MIT. Consulte o ficheiro [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">
  Feito com café, demasiados ficheiros YAML e um amor desmedido por overlays.<br/>
  <strong>Peek-it [HA]</strong> — porque a sua TV consegue fazer mais do que imagina.
</p>
