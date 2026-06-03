# Peek-it [HA] — Intégration Home Assistant

<p align="center">
  <img src="https://raw.githubusercontent.com/jolabs40/peek-it-ha/master/custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Transformez votre Android TV en afficheur de notifications intelligent.</strong><br/>
  Alertes, caméras, tableaux de bord, TTS, menus — en overlay sur votre TV en temps réel.
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
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-comment-ça-marche">Comment ça marche</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-installation">Installation</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-le-designer">Designer</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-utilisation">Utilisation</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-synthèse-vocale-tts">TTS</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-automatisations">Automatisations</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-référence-avancée">Référence avancée</a> •
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-waf--le-kpi-ultime">WAF</a>
</p>

<p align="center">
  <b>Langues :</b>
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_EN.md">English</a> |
  Fran&ccedil;ais |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_DE.md">Deutsch</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_ES.md">Espa&ntilde;ol</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_NL.md">Nederlands</a> |
  <a href="https://github.com/jolabs40/peek-it-ha/blob/master/README_PT.md">Portugu&ecirc;s</a>
</p>

---

## Pourquoi Peek-it [HA] ?

Votre appareil Android TV est branché sur votre TV 24 h/24. Pourquoi ne pas le faire travailler ?

L'application **Peek-it [TV]** affiche des **notifications riches en overlay** par-dessus n'importe quelle application en cours : un film, la TNT, un jeu... Vous regardez un match ? Le score se met à jour dans un coin. On sonne à la porte ? La caméra de l'entrée s'affiche instantanément. Et c'est **vous qui dessinez** ces affichages, sans écrire une ligne de code.

> 💡 **L'essentiel à retenir**
>
> 1. **Vous concevez** vos notifications (et même des pages entières) dans le **Designer**, un éditeur visuel par glisser-déposer accessible depuis n'importe quel navigateur. *C'est lui qui construit tout — vous n'avez rien à coder.*
> 2. **Vous les déclenchez** depuis **Home Assistant** grâce à cette intégration… ou depuis **Tasker, Node-RED, Jeedom** ou tout autre client HTTP, car l'app expose une API locale simple.

> 🧩 **Deux composants, deux rôles**
> L'**application Peek-it [TV]** (Android, sur le Play Store) dessine l'overlay, héberge le Designer et le moteur de templates : c'est l'autorité.
> L'**intégration Peek-it [HA]** (ce dépôt) la pilote depuis Home Assistant : envoi de notifications/TTS, surveillance de l'état, retours de boutons.

### Ce que vous pouvez afficher

| | |
|------|---------|
| 📝 **Texte riche** | Titres, messages, compteurs, météo |
| 🖼️ **Images** | Photos, captures, logos, QR codes |
| 🎥 **Flux vidéo RTSP** | Caméras de surveillance en direct, latence ultra-faible |
| 🌐 **Pages web** | Tableaux de bord HA, graphiques, widgets météo |
| 🔺 **Formes & SVG** | Rectangles, ellipses, hexagones, flèches, icônes vectorielles |
| 🎮 **Boutons & menus** | Navigables à la télécommande, déclenchent vos automatisations HA |
| 📊 **Entités & graphiques HA** | État en temps réel et historique des entités |
| 🔊 **Synthèse vocale** | Annonces vocales directement sur la TV |

### Fonctionnalités clés

- **Zéro latence** — overlay Android natif, pas de streaming ni de casting
- **Compatible avec tout** — l'overlay s'affiche par-dessus n'importe quelle application
- **Designer visuel** — créez tout en glisser-déposer, aperçu en temps réel
- **Templates réutilisables** — concevez une fois, réutilisez avec des paramètres dynamiques
- **Multi-appareils** — gérez plusieurs TV depuis une seule instance HA
- **Ouvert** — pilotable depuis HA, Tasker, Node-RED, Jeedom… via une API HTTP locale
- **6 langues** — EN, FR, DE, ES, NL, PT

---

## 🧩 Comment ça marche

Trois étapes, du visuel vers l'automatisation :

| Étape | Où | Ce que vous faites |
|------|-----|--------------------|
| **1. Concevoir** | 🎨 Designer (navigateur) | Glisser-déposer vos éléments sur un canevas calibré à votre TV. Le Designer génère tout le rendu pour vous. |
| **2. Sauvegarder** | 🎨 Designer | Enregistrer votre création comme **template** réutilisable (un simple ID est généré). |
| **3. Déclencher** | 🏠 Home Assistant | Appeler le template depuis une automatisation, en quelques lignes, avec des valeurs dynamiques. |

```yaml
# Étape 3 : déclencher un template conçu dans le Designer
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Alerte sécurité"
    camera_url: "rtsp://192.168.1.50:554/stream1"
```

> ✅ **Vous n'avez quasiment jamais besoin d'écrire du JSON à la main.** Le Designer s'occupe de la mise en page ; côté Home Assistant vous ne fournissez que l'ID du template et quelques valeurs. La [Référence avancée](https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-référence-avancée) (JSON brut, types de widgets, API…) n'est là que pour les cas pointus.

---

## 📥 Installation

### 1. Installer l'application Peek-it [TV]

**Recommandé — Google Play Store** : recherchez **« Peek-it »** dans le Play Store de votre Android TV, ou ouvrez la fiche :
[play.google.com/store/apps/details?id=net.jolabs40.peekit](https://play.google.com/store/apps/details?id=net.jolabs40.peekit)

> Appareil sans Play Store (certaines box Android TV, Fire TV…) : installez l'APK par sideload depuis la [page des Releases](https://github.com/jolabs40/peek-it-ha/releases) (clé USB, `adb install`, ou un gestionnaire de fichiers).

Puis, quelle que soit la méthode :

1. Lancez l'application — accordez la **permission d'overlay** (affichage par-dessus les autres applications) ; le service démarre automatiquement.
2. Notez l'**adresse IP** affichée sur l'écran principal (ex. `192.168.1.42`). Port par défaut : **8081**.

### 2. Installer l'intégration Home Assistant

**Via HACS (recommandé)** : HACS → *Integrations* → menu 3 points → *Custom repositories* → ajoutez `https://github.com/jolabs40/peek-it-ha` (catégorie *Integration*) → *Download* → **redémarrez HA**.

<details>
<summary>Installation manuelle</summary>

Copiez le dossier `peek_it_ha/` dans `config/custom_components/`, puis redémarrez Home Assistant :

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

### 3. Ajouter l'intégration

*Paramètres → Appareils et services → Ajouter une intégration → Peek-it [HA]*. Renseignez l'**IP**, le **port** (`8081`), un **nom** et, si l'app TV l'exige, une **clé API**. Si l'appareil est publié en Zeroconf (`_peekit._tcp`), HA peut aussi le **découvrir automatiquement**.

<details>
<summary>Ce qui est créé automatiquement (entités HA)</summary>

Toutes les entités sont regroupées dans une **seule carte d'appareil**. Pour chaque TV :

| Entité | Type | Description |
|--------|------|-------------|
| `binary_sensor.<nom>_status` | Connectivité | En ligne / hors ligne (interrogé toutes les 30 s) ; expose l'attribut `designer_url` |
| `binary_sensor.<nom>_overlay_permission` | Diagnostic | Permission d'overlay accordée |
| `binary_sensor.<nom>_accessibility_permission` | Diagnostic | Service d'accessibilité actif |
| `binary_sensor.<nom>_microphone_permission` | Diagnostic | Permission micro accordée |
| `notify.<nom>` | Notify | Envoi de notifications |
| `button.<nom>_*_assist / overlay / accessibility` | Config (×6) | Activer/désactiver les permissions via ADB — voir [Boutons ADB](https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-boutons-de-configuration-adb) |

Une seule requête `GET /api/status` est émise par TV toutes les 30 s ; toutes les entités partagent cet instantané (coordinateur mutualisé).
</details>

---

## 🎨 Le Designer

**Le cœur de Peek-it.** C'est ici que vous créez vos notifications et vos pages — visuellement, sans coder. C'est un **éditeur web embarqué dans l'app**, accessible depuis n'importe quel navigateur du réseau local :

**URL** : `http://<IP_TV>:<PORT>/` (ex. `http://192.168.1.42:8081/`) — aussi accessible via l'attribut `designer_url` du capteur de statut, ou *icône engrenage → Designer* dans les options de l'intégration.

- **Glisser-déposer** vos widgets sur un canevas calibré à la résolution réelle de votre TV (16:9, 21:9…)
- **Aperçu JSON en temps réel** — vous voyez le rendu se construire
- **Bibliothèque de templates** — sauvegarder, charger, renommer, exporter/importer
- **Paramètres dynamiques** — marquez les éléments variables (`paramKey`) pour les remplir depuis HA
- **Configuration** du son par défaut, de la langue, et du **jeton d'accès HA** (voir ci-dessous)
- **Boutons SEND** (envoyer vers la TV) et **KILL** (fermer) pour tester immédiatement

> 🔑 **Jeton d'accès Home Assistant (optionnel).** Certaines fonctions demandent à l'app d'appeler **directement** l'API de HA : basculer une entité depuis un menu, afficher l'état d'une entité en temps réel, dessiner un graphique d'historique, ou afficher un instantané de caméra. Pour cela, créez un **jeton d'accès longue durée** dans HA (*votre profil → tout en bas → Jetons d'accès longue durée → Créer*) et collez-le dans les paramètres du Designer. Il est stocké chiffré sur la TV. Inutile si vous vous contentez d'envoyer des notifications depuis HA.
>
> À ne pas confondre avec le **secret du webhook** (`X-Peek-Secret`), qui sert dans l'autre sens (retours de boutons TV → HA) et que l'intégration gère **automatiquement**.

> Depuis HA, *icône engrenage → Templates* liste tous vos templates avec leur **ID** (copiable) et leurs **paramètres**, triés en *Official* / *Custom* / *Drafts*.

> Depuis HA, le service **`peek_it_ha.save_template`** enregistre un template (`template_id` + `elements` JSON, `name` optionnel) sur la TV, où il rejoint la liste ci-dessus et peut ensuite être affiché via `notify` (`template_id` + `params`). `overwrite: false` refuse de remplacer un id existant.

---

## 🚀 Utilisation

Trois façons d'envoyer, de la plus simple à la plus avancée. **Le mode template est le plus pratique** : il s'appuie sur vos créations du Designer.

### Message simple

Un texte qui s'affiche en bas de l'écran sur fond sombre — idéal pour une alerte rapide.

```yaml
service: peek_it_ha.notify
data:
  message: "La machine à laver a terminé !"
  title: "Maison"
  duration: 8000
```

### Template + paramètres *(recommandé)*

Réutilisez un template conçu dans le Designer en injectant des valeurs dynamiques.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Alerte sécurité"
    message: "Mouvement détecté dans le jardin"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

Le serveur charge le template, remplace les `{{placeholders}}` par les valeurs de `params`, et affiche le résultat.

### Fermer / garder une notification

```yaml
# Fermer immédiatement
service: peek_it_ha.notify
data:
  action: CLOSE
```

`duration: 0` garde la notification à l'écran jusqu'à un `CLOSE` explicite ou un appui sur un bouton.

<details>
<summary><b>Mode avancé — éléments bruts (JSON complet)</b></summary>

Pour les cas où vous voulez définir chaque widget à la main, sans passer par un template. *En pratique, le Designer fait tout cela visuellement.*

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
      content: "Caméra du jardin"
      style: { left: 62, top: 28, width: 34, height: 5, size: 18, color: "#FFFFFF", align: center }
```

Le vocabulaire complet (types de widgets, propriétés de style) est documenté dans la [Référence avancée](https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-référence-avancée).
</details>

---

## 🔔 Synthèse vocale (TTS)

Faites parler la TV, seule ou en accompagnement d'une notification.

```yaml
# TTS autonome
service: peek_it_ha.tts
data:
  text: "Le dîner est prêt !"
  lang: "fr"
  speed: 1.0     # 0.5 à 2.0
  volume: 1.0    # 0.0 à 1.0
```

```yaml
# TTS avec notification visuelle
service: peek_it_ha.notify
data:
  message: "Mouvement détecté dans le jardin"
  title: "Sécurité"
  tts: "Mouvement détecté dans le jardin"
  ttsLang: "fr"
  ttsSpeed: 1.25
```

Arrêter la lecture : `service: peek_it_ha.tts_stop`. Dans `notify`, les champs sont préfixés `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

## 🔊 Son

```yaml
service: peek_it_ha.notify
data:
  message: "Colis livré"
  sound: "01_notify.wav"
  soundVolume: 0.8   # 0.0 à 1.0
```

L'app est livrée avec des sons intégrés (`01_notify.wav`…`05_notify.wav`, `06-notify.ogg`, `07-notify.ogg`, `08-notify.mp3`…`10-notify.mp3`) et accepte vos sons personnalisés (via le Designer). Le service **`peek_it_ha.get_sounds`** liste les sons disponibles d'une TV (`{official, custom}`).

---

## 🎨 Mode simple enrichi (presets & image)

Sans toucher au JSON `elements`, le mode simple accepte des **presets** optionnels — `position` (`top`/`center`/`bottom`), `level` (`info`/`warning`/`alert`, qui choisit une couleur d'accent + une icône), `icon` (`mdi:…`) et `color` (accent hex) — ainsi qu'une **image** (`image_url` + `image_fit`). Le rendu par défaut reste inchangé si ces champs sont absents.

```yaml
# Alerte avec icône et accent
service: peek_it_ha.notify
data:
  message: "Fuite d'eau détectée"
  level: alert            # accent rouge + mdi:alert-octagon
  position: center
```

```yaml
# Photo du visiteur (sonnette Doorbird) sur la TV
service: peek_it_ha.notify
data:
  message: "Quelqu'un à la porte"
  image_url: "http://192.168.1.50/snapshot.jpg"
  image_fit: cover        # contain | cover | fill
```

> `image_url` accepte une URL http(s), un `data:base64` ou un chemin local. Sans `message`, seule l'image est affichée. La langue du TTS (`ttsLang`/`lang`) suit la langue Home Assistant si elle n'est pas précisée.

---

## 🖱️ Boutons cliquables & fermeture

Un élément overlay `focusable` doté d'une `action` renvoie l'appui à HA. Déclenchez une automation via le **device trigger** « Bouton de l'overlay pressé » (*Appareil* → votre TV), ou écoutez l'event `peekit_button_press` (données `{action, device_id}`).

Fermer la notification au sommet : service **`peek_it_ha.dismiss`** (raccourci lisible de `action: CLOSE`), avec `target` optionnel.

> `priority: urgent` est transmis mais reste **indicatif** : l'app le journalise sans (encore) outrepasser le mode Ne Pas Déranger.

---

## 📺 Boutons de configuration (ADB)

L'intégration expose **6 boutons** (catégorie *Config*) qui pilotent la TV via **ADB sur TCP**, pour régler en un clic des permissions pénibles à activer à la télécommande :

| Bouton | Action sur la TV |
|--------|------------------|
| **Enable / Disable Assist** | Définit / restaure Peek-it comme assistant par défaut |
| **Enable / Disable Overlay** | Accorde / révoque la permission `SYSTEM_ALERT_WINDOW` |
| **Enable / Disable Accessibility** | Active / désactive le service d'accessibilité `MenuKeyService` |

<details>
<summary>Prérequis ADB (à faire une seule fois)</summary>

Les boutons utilisent la bibliothèque `adb-shell` (installée automatiquement par HA) et se connectent à l'IP de la TV sur le **port 5555**.

1. **Activez le débogage ADB réseau** : *Paramètres → Préférences de l'appareil → À propos →* tapez 7 fois sur *Version*, puis *Options pour les développeurs →* **Débogage USB** (et **Débogage sans fil** si proposé).
2. **Autorisez la clé RSA au premier appui** : une fenêtre « Autoriser le débogage ? » apparaît sur la TV → cochez *Toujours autoriser*. La clé est générée une fois et stockée dans `.storage/peek_it_adb_key`.
3. L'intégration officielle **Android TV** est recommandée (HA le signale dans *Réparations*) pour une gestion ADB stable.

Si `adb-shell` manque ou si la TV refuse la connexion, l'action échoue avec une erreur dans le journal HA.
</details>

---

## 🤖 Automatisations

### Alerte mouvement avec caméra

```yaml
automation:
  - alias: "Alerte mouvement jardin"
    trigger:
      - platform: state
        entity_id: binary_sensor.garden_motion
        to: "on"
    action:
      - service: peek_it_ha.notify
        data:
          template_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
          params:
            title: "Mouvement détecté !"
            camera_url: "rtsp://192.168.1.50:554/stream1"
          duration: 15000
          animationIn: slide_right
```

### Bulletin météo du matin

```yaml
automation:
  - alias: "Météo du matin"
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
          title: "Météo du jour"
```

### Retour d'un bouton vers HA

Un appui sur un bouton de notification (télécommande) déclenche un événement HA :

```yaml
automation:
  - alias: "Bouton TV - Éteindre lumières"
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
<summary>Alerte persistante avec bouton de fermeture (JSON brut)</summary>

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  animationIn: pop
  priority: urgent
  tts: "Attention ! Fuite d'eau détectée !"
  ttsLang: "fr"
  elements:
    - type: rect
      style: { left: 20, top: 20, width: 60, height: 60, bgColor: "#EE990000", radius: 20 }
    - type: text
      content: "FUITE D'EAU DÉTECTÉE"
      style: { left: 25, top: 30, width: 50, height: 10, size: 40, color: "#FFFFFF", weight: bold, align: center }
    - type: button
      content: "Compris"
      action: CLOSE
      focusable: true
      directFocus: true
      style: { left: 35, top: 55, width: 30, height: 10, size: 24, color: "#FFFFFF", bgColor: "#CC333333", align: center, radius: 10, focusColor: "#FF6666", focusBgColor: "#CC660000" }
```
</details>

<details>
<summary>Flux caméra RTSP</summary>

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

Latence ultra-faible (~50 ms) grâce à une configuration ExoPlayer optimisée.
</details>

---

## 🧰 Référence avancée

> 🛟 **Vous n'avez normalement pas besoin de cette section.** Le Designer construit vos notifications visuellement et vous fournit des templates prêts à l'emploi. Ce qui suit n'est utile que pour le mode JSON brut, l'API ou les intégrations tierces.

<details>
<summary><b>Paramètres du service <code>notify</code></b></summary>

| Paramètre | Type | Défaut | Description |
|-----------|------|--------|-------------|
| `action` | string | `DISPLAY` | `DISPLAY` pour afficher, `CLOSE` pour fermer |
| `duration` | int | `10000` | Durée en ms (0 = infini) |
| `priority` | string | `normal` | `normal` ou `urgent` |
| `animationIn` / `animationOut` | string | `fade` | Voir animations ci-dessous |
| `template_id` | string | — | UUID du template à utiliser |
| `params` | dict | — | Valeurs dynamiques du template |
| `elements` | list | — | Liste de widgets (mode JSON brut) |
| `message` / `title` | string | — | Mode message simple |
| `sound` / `soundVolume` | string / float | — / `1.0` | Son et volume (0.0-1.0) |
| `tts` / `ttsLang` / `ttsSpeed` / `ttsPitch` / `ttsVolume` | — | — | TTS lu avec la notification |

**Animations** : `none`, `fade`, `slide_right`, `slide_left`, `slide_top`, `slide_bottom`, `pop` (entrée et sortie indépendantes).
</details>

<details>
<summary><b>Types de widgets</b></summary>

Le type est interprété par l'app. **Tout type non reconnu (`text`, `message`, `title`, `button`…) est rendu comme un widget texte** ; un `button` se distingue par `focusable` + `action`. Si `content` commence par `mdi:` (ex. `mdi:home-assistant`), une **icône Material Design Icons** est affichée.

| Type | Description | `content` |
|------|-------------|-----------|
| `text` | Texte statique (type par défaut) | Le texte, ou `mdi:<icône>` |
| `button` | Texte interactif (focusable, action) | Libellé |
| `rect` | Rectangle / conteneur | — |
| `ellipse` | Ellipse / ovale | — |
| `hexagon` | Hexagone | — |
| `circle` | Conteneur rond (image / icône MDI) | URL ou `mdi:<icône>` |
| `image` | Image PNG/JPG | URL |
| `video` | Flux RTSP / HTTP | URL |
| `webview` | Page web embarquée | URL |
| `svg` | Image vectorielle | URL ou chemin |
| `line` / `arrow` | Ligne / flèche | — |
| `confetti` | Animation de confettis plein écran | — |
| `menu` | Menu interactif D-pad | JSON MenuConfig |

> Les anciens exemples en `type: box` s'affichent encore (fallback texte + `bgColor`), mais le type canonique du rectangle est `rect`.
</details>

<details>
<summary><b>Propriétés de style et d'interaction</b></summary>

**Style** : `left`, `top`, `width`, `height` (en % de l'écran, 0-100) · `color` · `bgColor` (hex avec alpha) · `size` · `font` · `weight` (`normal`/`bold`) · `align` (`left`/`center`/`right`) · `opacity` · `radius` · `borderWidth` · `borderColor` · `rotation` · `focusColor` · `focusBgColor`.

**Interaction (boutons)** : `focusable` (reçoit le focus télécommande) · `directFocus` (focus à l'affichage) · `action` (`CLOSE` ou ID personnalisé pour le webhook) · `paramKey` (lie le contenu à un paramètre de template) · `actionParamKey` (lie l'action à un paramètre).
</details>

<details>
<summary><b>Menu interactif (config JSON)</b></summary>

Le widget `menu` crée un menu overlay navigable au D-pad (sous-menus, bascules d'entités HA, actions).

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Contrôles rapides",
          "items": [
            {"type": "submenu", "label": "Lumières", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Salon", "entity_id": "light.living_room"},
              {"type": "close", "label": "Retour"}
            ]},
            {"type": "action", "label": "Mode cinéma", "action": "movie_mode"},
            {"type": "close", "label": "Fermer"}
          ]
        }
      style: { left: 35, top: 10, width: 30, height: 80 }
```

| Type d'élément | Rôle |
|------|-------------|
| `action` | Déclenche `peekit_button_press` avec l'ID `action` |
| `submenu` | Ouvre un sous-menu (`children`) |
| `toggle` | Bascule une entité HA (`entity_id`), état rafraîchi toutes les 5 s |
| `text` | Texte informatif |
| `close` | Ferme le menu |

**Navigation** : Haut/Bas naviguer · Droite/Entrée ouvrir un sous-menu · Gauche/Retour revenir · Retour à la racine ferme.
</details>

<details>
<summary><b>Widgets entité HA, graphiques & overlays (capacités de l'app)</b></summary>

Ces fonctions sont configurées côté **app** (Designer) ; l'intégration HA ne les pilote pas directement. Elles nécessitent un **jeton d'accès longue durée HA** saisi dans le Designer (cf. [Le Designer](https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-le-designer)), car l'app appelle l'API de HA directement.

- **Widget d'entité HA** : un `webview` connecté en WebSocket/REST affiche l'état d'entités en temps réel.
- **Graphiques HA** : aire / ligne / barres, rendus en pur CSS/SVG.
- **Horloge en overlay** (`/api/config/clock`) : format 12 h/24 h, position, couleur, opacité.
- **Assombrissement** (`/api/config/dimming`) : couleur et opacité d'une couche de fond.
</details>

<details>
<summary><b>API & webhook (pour Tasker, Node-RED, Jeedom, développeurs)</b></summary>

L'app expose une API HTTP locale (port `8081`). Si une clé API est configurée, **toutes** les requêtes portent le header `X-API-Key: <clé>`. C'est cette API que tout client HTTP (Tasker, Node-RED, Jeedom…) peut appeler.

| Endpoint | Méthode | Usage |
|---|---|---|
| `/api/status` | GET | État, permissions, résolution |
| `/api/notify` | POST | Afficher / fermer une notification |
| `/api/tts` · `/api/tts/stop` | POST | Synthèse vocale |
| `/api/templates/list` | GET | Liste des templates |
| `/api/templates/save` | POST | Sauvegarde d'un template (service `save_template`) |

**Réponse de `/api/status`** :
```json
{
  "status": "online", "version": "v10.9", "device_name": "Living Room TV",
  "api_key_required": false, "api_key_valid": true,
  "screen": { "width": 1920, "height": 1080, "density": 1.0 },
  "permissions": { "overlay": true, "accessibility": false, "microphone": true }
}
```

**Webhook (retours de la TV → HA)** : `/api/webhook/peek_it_debug`. Depuis la 1.1.0, chaque requête doit présenter le header **`X-Peek-Secret`** (sinon HTTP 401). Le secret est transmis à la TV via la **notification de bienvenue** (champ `webhook_secret`) à la création/sauvegarde de l'entrée.

| `level` | `message` | Effet HA |
|---------|-----------|----------|
| `ACTION` | `BUTTON_CLICK:<id>` | Émet l'événement `peekit_button_press` `{ "action": "<id>" }` |
| `ERROR` / `WARN` / `INFO` | texte | Journalisé `[PEEK-IT REPORT]` |

> **Migration depuis 1.0.0** : *Configurer → Paramètres → Valider* pour pousser une nouvelle notification de bienvenue contenant le `webhook_secret`.
</details>

---

## 🌍 Multi-appareils & langues

Ajoutez chaque TV comme une intégration séparée. Par défaut, les services `notify`, `tts`, `tts_stop` et `get_templates` s'appliquent à **toutes les TV configurées** ; le fan-out est **parallèle** et les TV hors ligne sont **ignorées** (plus de blocage quand une TV est éteinte).

**Cibler une seule TV avec les options riches** — utilisez le paramètre `target` du service de domaine `peek_it_ha.notify` (ou `peek_it_ha.tts` / `peek_it_ha.tts_stop`). C'est le **seul** moyen d'envoyer du TTS, du son ou des animations à une TV précise : l'entité `notify.<tv>` fige le schéma de `send_message` à `message`+`title` (toute clé en plus → HTTP 400).

```yaml
# Notification riche sur UNE seule TV
service: peek_it_ha.notify
data:
  target: <device_id_de_la_TV>   # via l'UI ; un nom de device ou une IP fonctionne aussi
  message: "Uniquement sur cette TV"
  tts: "Mouvement détecté"
  sound: "01_notify.wav"
```

```yaml
# Message simple sur une TV (sans options riches) — l'entité notify suffit
service: notify.send_message
target:
  entity_id: notify.tv_du_salon
data:
  message: "Uniquement sur cette TV"
```

> `target` absent → toutes les TV (comportement historique, rétrocompatible).

**Statut de livraison** : `peek_it_ha.notify` et `peek_it_ha.tts` renvoient l'état par TV (utilisable via `response_variable`). Une notif refusée par la TV (Ne Pas Déranger, overlay révoqué…) n'est plus un faux succès.

```yaml
action: peek_it_ha.notify
data:
  message: "Test"
response_variable: peekit
# peekit = { "TV du salon": { delivered: false, reason: "dnd_active",
#            fallback: "none", http_status: 200 } }
```

L'intégration et l'app sont disponibles en **6 langues** : `en` (défaut), `fr`, `de`, `es`, `nl`, `pt`. Configurable dans le Designer ou l'app.

---

## 😅 WAF — Le KPI ultime

Le légendaire **WAF** — *Wife Acceptance Factor*. Cette métrique non officielle mais absolument cruciale qui mesure la tolérance de votre moitié envers vos expériences domotiques.

- 🧺 **Linge intelligent** : « Lessive terminée ! » apparaît discrètement pendant le film. Fini les lessives oubliées 3 jours. *(WAF : +23)*
- ☀️ **Météo du matin** : chaque jour à 7 h 30, la météo sur la TV de la cuisine. *(WAF : +15)*
- 🔔 **Caméra de la sonnette** : on sonne, le flux apparaît. Délibération depuis le canapé. Personne ne s'est levé. *(WAF : +38)*
- ⚽ **Score sportif** : un discret « 2 - 1, 78' » 3 secondes dans le coin. Personne n'a changé de chaîne. *(WAF : +52)*

### Le cas qui RUINE votre WAF

🌙 **Débogage en production** : vous testez vos notifications à 23 h pendant le grand final de la saison. « Test 1 », « Lorem ipsum », « AAAA ÇA MARCHE ! », un gros rectangle noir, puis plus rien...

> *(WAF : -347. Récupération estimée : 3 semaines de bon comportement. Et un bouquet de fleurs.)*

**Conseil de pro** : testez AVANT 21 h. Ou utilisez le bouton **KILL** du Designer. Il existe pour une raison.

---

## 🔧 Dépannage

| Problème | Solution |
|----------|----------|
| Intégration introuvable | Dossier dans `custom_components/peek_it_ha/` ? Redémarrez HA. |
| « Impossible de se connecter » | Vérifiez IP/port. Testez `http://IP:8081/api/status` dans un navigateur. |
| Capteur toujours « hors ligne » | L'app tourne-t-elle ? Le service démarre-t-il au boot ? |
| La notification ne s'affiche pas | Vérifiez la permission d'overlay dans les paramètres Android TV. |
| Le Designer ne se connecte pas | Même réseau ? Essayez `http://IP:PORT/`. |
| Le bouton TV ne déclenche pas HA | Retour TV → HA = webhook : re-sauvegardez les *Paramètres* de l'intégration (transmet le `webhook_secret`) et vérifiez que `ha_ip` est joignable depuis la TV. |
| Les toggles de menu / widgets d'entité ne marchent pas | Appel direct app → HA : créez un **jeton d'accès longue durée** HA et collez-le dans le Designer (voir [Le Designer](https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-le-designer)). |
| Les boutons ADB échouent | Débogage ADB (port 5555) activé et clé RSA autorisée ? Voir [Boutons ADB](https://github.com/jolabs40/peek-it-ha/blob/master/README_FR.md#-boutons-de-configuration-adb). |
| Le TTS ne parle pas | Un moteur TTS est-il installé sur l'Android TV (Google TTS) ? |
| Le menu ne répond pas au D-pad | L'élément menu doit avoir le focus ; utilisez `duration: 0`. |

---

## Contribuer

Les contributions sont les bienvenues ! Ouvrez une issue ou une pull request sur le [dépôt GitHub](https://github.com/jolabs40/peek-it-ha).

## Licence

Projet distribué sous licence MIT. Voir le fichier [LICENSE](https://github.com/jolabs40/peek-it-ha/blob/master/LICENSE).

---

<p align="center">
  Fait avec du café, beaucoup trop de fichiers YAML, et un amour déraisonnable pour les overlays.<br/>
  <strong>Peek-it [HA]</strong> — parce que votre TV peut faire bien plus que vous ne le pensez.
</p>
