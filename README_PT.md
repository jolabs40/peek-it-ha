# Peek-it [HA] — Integração Home Assistant

<p align="center">
  <img src="https://raw.githubusercontent.com/jolabs40/peek-it-ha/master/custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Transforme a sua Android TV num painel de notificações inteligente.</strong><br/>
  Alertas, câmaras, painéis, TTS, menus — em overlay sobre a sua TV em tempo real.
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
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-como-funciona">Como funciona</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-instalação">Instalação</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-o-designer">Designer</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-utilização">Utilização</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-síntese-de-voz-tts">TTS</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-automações">Automações</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-referência-avançada">Referência avançada</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-waf--o-kpi-supremo">WAF</a>
</p>

<p align="center">
  <b>Idiomas:</b>
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md">English</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md">Fran&ccedil;ais</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md">Deutsch</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_ES.md">Espa&ntilde;ol</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_NL.md">Nederlands</a> |
  Portugu&ecirc;s
</p>

---

## Porquê Peek-it [HA]?

O seu dispositivo Android TV está ligado à sua TV 24 horas por dia. Porque não pô-lo a trabalhar?

A aplicação **Peek-it [TV]** apresenta **notificações ricas em overlay** por cima de qualquer aplicação em execução: um filme, a TDT, um jogo... Está a ver uma partida? O resultado atualiza-se a um canto. Tocam à porta? A câmara da entrada aparece instantaneamente. E é **você quem desenha** estas exibições, sem escrever uma linha de código.

> 💡 **O essencial a reter**
>
> 1. **Você concebe** as suas notificações (e até páginas inteiras) no **Designer**, um editor visual por arrastar e largar acessível a partir de qualquer navegador. *É ele que constrói tudo — não tem nada para programar.*
> 2. **Você dispara-as** a partir do **Home Assistant** graças a esta integração… ou a partir do **Tasker, Node-RED, Jeedom** ou qualquer outro cliente HTTP, pois a app expõe uma API local simples.

> 🧩 **Dois componentes, dois papéis**
> A **aplicação Peek-it [TV]** (Android, na Play Store) desenha o overlay, aloja o Designer e o motor de templates: é a autoridade.
> A **integração Peek-it [HA]** (este repositório) pilota-a a partir do Home Assistant: envio de notificações/TTS, monitorização do estado, retornos de botões.

### O que pode apresentar

| | |
|------|---------|
| 📝 **Texto rico** | Títulos, mensagens, contadores, meteorologia |
| 🖼️ **Imagens** | Fotos, capturas, logótipos, códigos QR |
| 🎥 **Fluxos de vídeo RTSP** | Câmaras de vigilância em direto, latência ultrabaixa |
| 🌐 **Páginas web** | Painéis HA, gráficos, widgets meteorológicos |
| 🔺 **Formas e SVG** | Retângulos, elipses, hexágonos, setas, ícones vetoriais |
| 🎮 **Botões e menus** | Navegáveis pelo comando, disparam as suas automações HA |
| 📊 **Entidades e gráficos HA** | Estado em tempo real e histórico das entidades |
| 🔊 **Síntese de voz** | Anúncios por voz diretamente na TV |

### Funcionalidades-chave

- **Zero latência** — overlay Android nativo, sem streaming nem casting
- **Compatível com tudo** — o overlay aparece por cima de qualquer aplicação
- **Designer visual** — crie tudo por arrastar e largar, pré-visualização em tempo real
- **Templates reutilizáveis** — conceba uma vez, reutilize com parâmetros dinâmicos
- **Multidispositivo** — gira várias TV a partir de uma única instância HA
- **Aberto** — pilotável a partir do HA, Tasker, Node-RED, Jeedom… via uma API HTTP local
- **6 idiomas** — EN, FR, DE, ES, NL, PT

---

## 🧩 Como funciona

Três passos, do visual para a automação:

| Passo | Onde | O que faz |
|------|-----|--------------------|
| **1. Conceber** | 🎨 Designer (navegador) | Arrastar e largar os seus elementos numa tela calibrada para a sua TV. O Designer gera toda a renderização por si. |
| **2. Guardar** | 🎨 Designer | Guardar a sua criação como **template** reutilizável (é gerado um simples ID). |
| **3. Disparar** | 🏠 Home Assistant | Chamar o template a partir de uma automação, em poucas linhas, com valores dinâmicos. |

```yaml
# Passo 3: acionar um template criado no Designer
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Alerta de segurança"
    camera_url: "rtsp://192.168.1.50:554/stream1"
```

> ✅ **Quase nunca precisa de escrever JSON à mão.** O Designer trata da disposição; do lado do Home Assistant fornece apenas o ID do template e alguns valores. A [Referência avançada](https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-referência-avançada) (JSON bruto, tipos de widgets, API…) só está aqui para os casos mais avançados.

---

## 📥 Instalação

### 1. Instalar a aplicação Peek-it [TV]

**Recomendado — Google Play Store**: procure **«Peek-it»** na Play Store da sua Android TV, ou abra a ficha:
[play.google.com/store/apps/details?id=net.jolabs40.peekit](https://play.google.com/store/apps/details?id=net.jolabs40.peekit)

> Dispositivo sem Play Store (algumas box Android TV, Fire TV…): instale o APK por sideload a partir da [página de Releases](https://github.com/jolabs40/peek-it-ha/releases) (pen USB, `adb install`, ou um gestor de ficheiros).

Depois, qualquer que seja o método:

1. Inicie a aplicação — conceda a **permissão de overlay** (exibição por cima das outras aplicações); o serviço inicia automaticamente.
2. Anote o **endereço IP** apresentado no ecrã principal (ex. `192.168.1.42`). Porta predefinida: **8081**.

### 2. Instalar a integração Home Assistant

**Via HACS (recomendado)**: HACS → *Integrations* → menu de 3 pontos → *Custom repositories* → adicione `https://github.com/jolabs40/peek-it-ha` (categoria *Integration*) → *Download* → **reinicie o HA**.

<details>
<summary>Instalação manual</summary>

Copie a pasta `peek_it_ha/` para `config/custom_components/`, depois reinicie o Home Assistant:

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

### 3. Adicionar a integração

*Definições → Dispositivos e serviços → Adicionar uma integração → Peek-it [HA]*. Indique o **IP**, a **porta** (`8081`), um **nome** e, se a app TV o exigir, uma **chave API**. Se o dispositivo for publicado em Zeroconf (`_peekit._tcp`), o HA também pode **descobri-lo automaticamente**.

<details>
<summary>O que é criado automaticamente (entidades HA)</summary>

Todas as entidades são agrupadas num **único cartão de dispositivo**. Para cada TV:

| Entidade | Tipo | Descrição |
|--------|------|-------------|
| `binary_sensor.<nome>_status` | Conectividade | Online / offline (consultado a cada 30 s); expõe o atributo `designer_url` |
| `binary_sensor.<nome>_overlay_permission` | Diagnóstico | Permissão de overlay concedida |
| `binary_sensor.<nome>_accessibility_permission` | Diagnóstico | Serviço de acessibilidade ativo |
| `binary_sensor.<nome>_microphone_permission` | Diagnóstico | Permissão de micro concedida |
| `notify.<nome>` | Notify | Envio de notificações |
| `button.<nome>_*_assist / overlay / accessibility` | Config (×6) | Ativar/desativar as permissões via ADB — ver [Botões ADB](https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-botões-de-configuração-adb) |

Apenas um pedido `GET /api/status` é emitido por TV a cada 30 s; todas as entidades partilham este instantâneo (coordenador mutualizado).
</details>

---

## 🎨 O Designer

**O coração do Peek-it.** É aqui que cria as suas notificações e as suas páginas — visualmente, sem programar. É um **editor web embebido na app**, acessível a partir de qualquer navegador da rede local:

**URL**: `http://<IP_TV>:<PORT>/` (ex. `http://192.168.1.42:8081/`) — também acessível através do atributo `designer_url` do sensor de estado, ou *ícone de engrenagem → Designer* nas opções da integração.

- **Arrastar e largar** os seus widgets numa tela calibrada para a resolução real da sua TV (16:9, 21:9…)
- **Pré-visualização JSON em tempo real** — vê a renderização a construir-se
- **Biblioteca de templates** — guardar, carregar, renomear, exportar/importar
- **Parâmetros dinâmicos** — marque os elementos variáveis (`paramKey`) para os preencher a partir do HA
- **Configuração** do som predefinido, do idioma e do **token de acesso HA** (ver abaixo)
- **Botões SEND** (enviar para a TV) e **KILL** (fechar) para testar imediatamente

> 🔑 **Token de acesso Home Assistant (opcional).** Algumas funções pedem à app para chamar **diretamente** a API do HA: alternar uma entidade a partir de um menu, apresentar o estado de uma entidade em tempo real, desenhar um gráfico de histórico, ou apresentar um instantâneo de câmara. Para isso, crie um **token de acesso de longa duração (Long-Lived Access Token)** no HA (*o seu perfil → no fim de tudo → Tokens de acesso de longa duração → Criar*) e cole-o nas definições do Designer. É armazenado cifrado na TV. Desnecessário se apenas pretende enviar notificações a partir do HA.
>
> Não confundir com o **segredo do webhook** (`X-Peek-Secret`), que serve no outro sentido (retornos de botões TV → HA) e que a integração gere **automaticamente**.

> A partir do HA, *ícone de engrenagem → Templates* lista todos os seus templates com o respetivo **ID** (copiável) e os seus **parâmetros**, ordenados em *Official* / *Custom* / *Drafts*.

> A partir do HA, o serviço **`peek_it_ha.save_template`** guarda um template (`template_id` + `elements` JSON, `name` opcional) na TV, onde se junta à lista acima e pode depois ser apresentado via `notify` (`template_id` + `params`). `overwrite: false` recusa substituir um id existente.

---

## 🚀 Utilização

Três formas de enviar, da mais simples à mais avançada. **O modo template é o mais prático**: apoia-se nas suas criações do Designer.

### Mensagem simples

Um texto que aparece na parte inferior do ecrã sobre fundo escuro — ideal para um alerta rápido.

```yaml
service: peek_it_ha.notify
data:
  message: "A máquina de lavar terminou!"
  title: "Casa"
  duration: 8000
```

### Template + parâmetros *(recomendado)*

Reutilize um template concebido no Designer injetando valores dinâmicos.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Alerta de segurança"
    message: "Movimento detetado no jardim"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

O servidor carrega o template, substitui os `{{placeholders}}` pelos valores de `params`, e apresenta o resultado.

### Fechar / manter uma notificação

```yaml
# Fechar imediatamente
service: peek_it_ha.notify
data:
  action: CLOSE
```

`duration: 0` mantém a notificação no ecrã até um `CLOSE` explícito ou uma pressão num botão.

<details>
<summary><b>Modo avançado — elementos brutos (JSON completo)</b></summary>

Para os casos em que pretende definir cada widget à mão, sem passar por um template. *Na prática, o Designer faz tudo isto visualmente.*

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
      content: "Câmara do jardim"
      style: { left: 62, top: 28, width: 34, height: 5, size: 18, color: "#FFFFFF", align: center }
```

O vocabulário completo (tipos de widgets, propriedades de estilo) está documentado na [Referência avançada](https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-referência-avançada).
</details>

---

## 🔔 Síntese de voz (TTS)

Faça a TV falar, sozinha ou a acompanhar uma notificação.

```yaml
# TTS autónomo
service: peek_it_ha.tts
data:
  text: "O jantar está pronto!"
  lang: "pt"
  speed: 1.0     # 0.5 a 2.0
  volume: 1.0    # 0.0 a 1.0
```

```yaml
# TTS com notificação visual
service: peek_it_ha.notify
data:
  message: "Movimento detetado no jardim"
  title: "Segurança"
  tts: "Movimento detetado no jardim"
  ttsLang: "pt"
  ttsSpeed: 1.25
```

Parar a leitura: `service: peek_it_ha.tts_stop`. Em `notify`, os campos têm o prefixo `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

## 🔊 Som

```yaml
service: peek_it_ha.notify
data:
  message: "Encomenda entregue"
  sound: "01_notify.wav"
  soundVolume: 0.8   # 0.0 a 1.0
```

A app vem com sons integrados (`01_notify.wav`…`05_notify.wav`, `06-notify.ogg`, `07-notify.ogg`, `08-notify.mp3`…`10-notify.mp3`) e aceita os seus sons personalizados (via o Designer). O serviço **`peek_it_ha.get_sounds`** lista os sons disponíveis de uma TV (`{official, custom}`).

---

## 🎨 Modo simples enriquecido (presets e imagem)

Sem tocar no JSON `elements`, o modo simples aceita **presets** opcionais — `position` (`top`/`center`/`bottom`), `level` (`info`/`warning`/`alert`, que escolhe uma cor de acento + ícone), `icon` (`mdi:…`) e `color` (acento hex) — além de uma **imagem** (`image_url` + `image_fit`). A renderização predefinida não muda se estes campos estiverem ausentes.

```yaml
# Alerta com ícone e acento
service: peek_it_ha.notify
data:
  message: "Fuga de água detetada"
  level: alert
  position: center
```

```yaml
# Foto do visitante (campainha) na TV
service: peek_it_ha.notify
data:
  message: "Alguém à porta"
  image_url: "http://192.168.1.50/snapshot.jpg"
  image_fit: cover        # contain | cover | fill
```

> `image_url` aceita um URL http(s), um `data:base64` ou um caminho local. Sem `message`, apenas a imagem é exibida. O idioma do TTS (`ttsLang`/`lang`) segue o idioma do Home Assistant se omitido.

---

## 🖱️ Botões clicáveis e fecho

Um elemento overlay `focusable` com uma `action` reenvia o clique para o HA. Crie uma automação através do **device trigger** «Botão do overlay premido» (*Dispositivo* → a sua TV), ou ouça o evento `peekit_button_press` (dados `{action, device_id}`).

Fechar a notificação no topo: serviço **`peek_it_ha.dismiss`** (atalho legível de `action: CLOSE`), com `target` opcional.

> `priority: urgent` é enviado mas é **indicativo**: a app regista-o sem (ainda) ignorar o modo Não Incomodar.

---

## 📺 Botões de configuração (ADB)

A integração expõe **6 botões** (categoria *Config*) que pilotam a TV via **ADB sobre TCP**, para configurar com um clique permissões difíceis de ativar pelo comando:

| Botão | Ação na TV |
|--------|------------------|
| **Enable / Disable Assist** | Define / restaura o Peek-it como assistente predefinido |
| **Enable / Disable Overlay** | Concede / revoga a permissão `SYSTEM_ALERT_WINDOW` |
| **Enable / Disable Accessibility** | Ativa / desativa o serviço de acessibilidade `MenuKeyService` |

<details>
<summary>Pré-requisitos ADB (a fazer uma única vez)</summary>

Os botões utilizam a biblioteca `adb-shell` (instalada automaticamente pelo HA) e ligam-se ao IP da TV na **porta 5555**.

1. **Ative a depuração ADB em rede**: *Definições → Preferências do dispositivo → Acerca de →* toque 7 vezes em *Versão*, depois *Opções de programador →* **Depuração USB** (e **Depuração sem fios** se proposto).
2. **Autorize a chave RSA na primeira pressão**: aparece uma janela «Autorizar a depuração?» na TV → marque *Permitir sempre*. A chave é gerada uma vez e armazenada em `.storage/peek_it_adb_key`.
3. A integração oficial **Android TV** é recomendada (o HA assinala-o em *Reparações*) para uma gestão ADB estável.

Se a `adb-shell` faltar ou se a TV recusar a ligação, a ação falha com um erro no registo do HA.
</details>

---

## 🤖 Automações

### Alerta de movimento com câmara

```yaml
automation:
  - alias: "Alerta de movimento jardim"
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
```

### Boletim meteorológico da manhã

```yaml
automation:
  - alias: "Meteorologia da manhã"
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
          title: "Meteorologia do dia"
```

### Retorno de um botão para o HA

Uma pressão num botão de notificação (comando) dispara um evento HA:

```yaml
automation:
  - alias: "Botão TV - Apagar luzes"
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
<summary>Alerta persistente com botão de fecho (JSON bruto)</summary>

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  animationIn: pop
  priority: urgent
  tts: "Atenção! Fuga de água detetada!"
  ttsLang: "pt"
  elements:
    - type: rect
      style: { left: 20, top: 20, width: 60, height: 60, bgColor: "#EE990000", radius: 20 }
    - type: text
      content: "FUGA DE ÁGUA DETETADA"
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
<summary>Fluxo de câmara RTSP</summary>

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

Latência ultrabaixa (~50 ms) graças a uma configuração ExoPlayer otimizada.
</details>

---

## 🧰 Referência avançada

> 🛟 **Normalmente não precisa desta secção.** O Designer constrói as suas notificações visualmente e fornece-lhe templates prontos a usar. O que se segue só é útil para o modo JSON bruto, a API ou as integrações de terceiros.

<details>
<summary><b>Parâmetros do serviço <code>notify</code></b></summary>

| Parâmetro | Tipo | Predefinição | Descrição |
|-----------|------|--------|-------------|
| `action` | string | `DISPLAY` | `DISPLAY` para apresentar, `CLOSE` para fechar |
| `duration` | int | `10000` | Duração em ms (0 = infinito) |
| `priority` | string | `normal` | `normal` ou `urgent` |
| `animationIn` / `animationOut` | string | `fade` | Ver animações abaixo |
| `template_id` | string | — | UUID do template a utilizar |
| `params` | dict | — | Valores dinâmicos do template |
| `elements` | list | — | Lista de widgets (modo JSON bruto) |
| `message` / `title` | string | — | Modo mensagem simples |
| `sound` / `soundVolume` | string / float | — / `1.0` | Som e volume (0.0-1.0) |
| `tts` / `ttsLang` / `ttsSpeed` / `ttsPitch` / `ttsVolume` | — | — | TTS lido com a notificação |

**Animações**: `none`, `fade`, `slide_right`, `slide_left`, `slide_top`, `slide_bottom`, `pop` (entrada e saída independentes).
</details>

<details>
<summary><b>Tipos de widgets</b></summary>

O tipo é interpretado pela app. **Qualquer tipo não reconhecido (`text`, `message`, `title`, `button`…) é renderizado como um widget de texto**; um `button` distingue-se por `focusable` + `action`. Se `content` começar por `mdi:` (ex. `mdi:home-assistant`), é apresentado um **ícone Material Design Icons**.

| Tipo | Descrição | `content` |
|------|-------------|-----------|
| `text` | Texto estático (tipo predefinido) | O texto, ou `mdi:<ícone>` |
| `button` | Texto interativo (focusable, action) | Rótulo |
| `rect` | Retângulo / contentor | — |
| `ellipse` | Elipse / oval | — |
| `hexagon` | Hexágono | — |
| `circle` | Contentor redondo (imagem / ícone MDI) | URL ou `mdi:<ícone>` |
| `image` | Imagem PNG/JPG | URL |
| `video` | Fluxo RTSP / HTTP | URL |
| `webview` | Página web embebida | URL |
| `svg` | Imagem vetorial | URL ou caminho |
| `line` / `arrow` | Linha / seta | — |
| `confetti` | Animação de confetes em ecrã inteiro | — |
| `menu` | Menu interativo D-pad | JSON MenuConfig |

> Os antigos exemplos em `type: box` ainda são apresentados (fallback texto + `bgColor`), mas o tipo canónico do retângulo é `rect`.
</details>

<details>
<summary><b>Propriedades de estilo e de interação</b></summary>

**Estilo**: `left`, `top`, `width`, `height` (em % do ecrã, 0-100) · `color` · `bgColor` (hex com alpha) · `size` · `font` · `weight` (`normal`/`bold`) · `align` (`left`/`center`/`right`) · `opacity` · `radius` · `borderWidth` · `borderColor` · `rotation` · `focusColor` · `focusBgColor`.

**Interação (botões)**: `focusable` (recebe o foco do comando) · `directFocus` (foco na exibição) · `action` (`CLOSE` ou ID personalizado para o webhook) · `paramKey` (liga o conteúdo a um parâmetro de template) · `actionParamKey` (liga a ação a um parâmetro).
</details>

<details>
<summary><b>Menu interativo (config JSON)</b></summary>

O widget `menu` cria um menu overlay navegável pelo D-pad (submenus, alternâncias de entidades HA, ações).

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Controlos rápidos",
          "items": [
            {"type": "submenu", "label": "Luzes", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Sala", "entity_id": "light.living_room"},
              {"type": "close", "label": "Voltar"}
            ]},
            {"type": "action", "label": "Modo cinema", "action": "movie_mode"},
            {"type": "close", "label": "Fechar"}
          ]
        }
      style: { left: 35, top: 10, width: 30, height: 80 }
```

| Tipo de elemento | Papel |
|------|-------------|
| `action` | Dispara `peekit_button_press` com o ID `action` |
| `submenu` | Abre um submenu (`children`) |
| `toggle` | Alterna uma entidade HA (`entity_id`), estado atualizado a cada 5 s |
| `text` | Texto informativo |
| `close` | Fecha o menu |

**Navegação**: Cima/Baixo navegar · Direita/Enter abrir um submenu · Esquerda/Voltar regressar · Voltar na raiz fecha.
</details>

<details>
<summary><b>Widgets de entidade HA, gráficos e overlays (capacidades da app)</b></summary>

Estas funções são configuradas do lado da **app** (Designer); a integração HA não as pilota diretamente. Requerem um **token de acesso de longa duração (Long-Lived Access Token) HA** introduzido no Designer (cf. [O Designer](https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-o-designer)), pois a app chama a API do HA diretamente.

- **Widget de entidade HA**: um `webview` ligado por WebSocket/REST apresenta o estado de entidades em tempo real.
- **Gráficos HA**: área / linha / barras, renderizados em puro CSS/SVG.
- **Relógio em overlay** (`/api/config/clock`): formato 12 h/24 h, posição, cor, opacidade.
- **Escurecimento** (`/api/config/dimming`): cor e opacidade de uma camada de fundo.
</details>

<details>
<summary><b>API e webhook (para Tasker, Node-RED, Jeedom, programadores)</b></summary>

A app expõe uma API HTTP local (porta `8081`). Se estiver configurada uma chave API, **todos** os pedidos levam o cabeçalho `X-API-Key: <chave>`. É esta API que qualquer cliente HTTP (Tasker, Node-RED, Jeedom…) pode chamar.

| Endpoint | Método | Uso |
|---|---|---|
| `/api/status` | GET | Estado, permissões, resolução |
| `/api/notify` | POST | Apresentar / fechar uma notificação |
| `/api/tts` · `/api/tts/stop` | POST | Síntese de voz |
| `/api/templates/list` | GET | Lista dos templates |
| `/api/templates/save` | POST | Guardar um template (serviço `save_template`) |

**Resposta de `/api/status`**:
```json
{
  "status": "online", "version": "v10.9", "device_name": "Living Room TV",
  "api_key_required": false, "api_key_valid": true,
  "screen": { "width": 1920, "height": 1080, "density": 1.0 },
  "permissions": { "overlay": true, "accessibility": false, "microphone": true }
}
```

**Webhook (retornos da TV → HA)**: `/api/webhook/peek_it_debug`. Desde a 1.1.0, cada pedido deve apresentar o cabeçalho **`X-Peek-Secret`** (caso contrário HTTP 401). O segredo é transmitido à TV através da **notificação de boas-vindas** (campo `webhook_secret`) na criação/gravação da entrada.

| `level` | `message` | Efeito HA |
|---------|-----------|----------|
| `ACTION` | `BUTTON_CLICK:<id>` | Emite o evento `peekit_button_press` `{ "action": "<id>" }` |
| `ERROR` / `WARN` / `INFO` | texto | Registado `[PEEK-IT REPORT]` |

> **Migração a partir da 1.0.0**: *Configurar → Definições → Validar* para enviar uma nova notificação de boas-vindas contendo o `webhook_secret`.
</details>

---

## 🌍 Multidispositivo e idiomas

Adicione cada TV como uma integração separada. Por predefinição, os serviços `notify`, `tts`, `tts_stop` e `get_templates` aplicam-se a **todas as TV configuradas**; o envio é **paralelo** e as TV offline são **ignoradas** (deixa de bloquear quando uma TV está desligada).

**Visar uma única TV com opções ricas** — use o parâmetro `target` do serviço de domínio `peek_it_ha.notify` (ou `peek_it_ha.tts` / `peek_it_ha.tts_stop`). É a **única** forma de enviar TTS, som ou animações para uma TV específica: a entidade `notify.<tv>` fixa o esquema de `send_message` em `message`+`title` (qualquer chave extra → HTTP 400).

```yaml
# Notificação rica em APENAS UMA TV
service: peek_it_ha.notify
data:
  target: <id_dispositivo_tv>   # via UI; um nome de dispositivo ou um IP também funciona
  message: "Apenas nesta TV"
  tts: "Movimento detetado"
  sound: "01_notify.wav"
```

```yaml
# Mensagem simples numa TV (sem opções ricas) — basta a entidade notify
service: notify.send_message
target:
  entity_id: notify.tv_da_sala
data:
  message: "Apenas nesta TV"
```

> Sem `target` → todas as TV (comportamento histórico, retrocompatível).

A integração e a app estão disponíveis em **6 idiomas**: `en` (predefinição), `fr`, `de`, `es`, `nl`, `pt`. Configurável no Designer ou na app.

---

## 😅 WAF — O KPI supremo

O lendário **WAF** — *Wife Acceptance Factor*. Aquela métrica não oficial mas absolutamente crucial que mede a tolerância da sua cara-metade para com as suas experiências domóticas.

- 🧺 **Roupa inteligente**: «Lavagem terminada!» aparece discretamente durante o filme. Acabaram-se as lavagens esquecidas 3 dias. *(WAF: +23)*
- ☀️ **Meteorologia da manhã**: todos os dias às 7h30, a meteorologia na TV da cozinha. *(WAF: +15)*
- 🔔 **Câmara da campainha**: tocam, o fluxo aparece. Deliberação a partir do sofá. Ninguém se levantou. *(WAF: +38)*
- ⚽ **Resultado desportivo**: um discreto «2 - 1, 78'» 3 segundos a um canto. Ninguém mudou de canal. *(WAF: +52)*

### O caso que ARRUÍNA o seu WAF

🌙 **Depuração em produção**: testa as suas notificações às 23 h durante o grande final da temporada. «Teste 1», «Lorem ipsum», «AAAA FUNCIONA!», um grande retângulo preto, e depois mais nada...

> *(WAF: -347. Recuperação estimada: 3 semanas de bom comportamento. E um ramo de flores.)*

**Dica de profissional**: teste ANTES das 21 h. Ou use o botão **KILL** do Designer. Existe por uma razão.

---

## 🔧 Resolução de problemas

| Problema | Solução |
|----------|----------|
| Integração não encontrada | Pasta em `custom_components/peek_it_ha/`? Reinicie o HA. |
| «Impossível ligar» | Verifique IP/porta. Teste `http://IP:8081/api/status` num navegador. |
| Sensor sempre «offline» | A app está em execução? O serviço inicia no arranque? |
| A notificação não aparece | Verifique a permissão de overlay nas definições da Android TV. |
| O Designer não liga | Mesma rede? Tente `http://IP:PORT/`. |
| O botão da TV não dispara o HA | Retorno TV → HA = webhook: volte a guardar as *Definições* da integração (transmite o `webhook_secret`) e verifique que `ha_ip` é alcançável a partir da TV. |
| As alternâncias de menu / widgets de entidade não funcionam | Chamada direta app → HA: crie um **token de acesso de longa duração (Long-Lived Access Token)** HA e cole-o no Designer (ver [O Designer](https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-o-designer)). |
| Os botões ADB falham | Depuração ADB (porta 5555) ativada e chave RSA autorizada? Ver [Botões ADB](https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md#-botões-de-configuração-adb). |
| O TTS não fala | Está instalado um motor TTS na Android TV (Google TTS)? |
| O menu não responde ao D-pad | O elemento menu deve ter o foco; use `duration: 0`. |

---

## Contribuir

As contribuições são bem-vindas! Abra uma issue ou um pull request no [repositório GitHub](https://github.com/jolabs40/peek-it-ha).

## Licença

Projeto distribuído sob a licença MIT. Veja o ficheiro [LICENSE](https://github.com/jolabs40/peek-it-ha/blob/master/LICENSE).

---

<p align="center">
  Feito com café, ficheiros YAML a mais, e um amor desmedido pelos overlays.<br/>
  <strong>Peek-it [HA]</strong> — porque a sua TV pode fazer muito mais do que pensa.
</p>
