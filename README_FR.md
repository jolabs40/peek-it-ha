# Peek-it [HA] — Integration Home Assistant

<p align="center">
  <img src="custom_components/peek_it_ha/icon@2x.png" alt="Peek-it [HA]" width="128"/>
</p>

<p align="center">
  <strong>Transformez votre Android TV en afficheur de notifications intelligent.</strong><br/>
  Alertes, cameras, tableaux de bord, TTS, menus — en overlay sur votre TV en temps reel.
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
  <a href="#-utilisation">Utilisation</a> •
  <a href="#-le-designer">Designer</a> •
  <a href="#-templates--parametres">Templates</a> •
  <a href="#-synthese-vocale-tts">TTS</a> •
  <a href="#-son">Son</a> •
  <a href="#-menu-interactif">Menu</a> •
  <a href="#-automatisations">Automatisations</a> •
  <a href="#-waf--le-kpi-ultime">WAF</a>
</p>

<p align="center">
  <b>Langues :</b>
  <a href="README.md">English</a> |
  Fran&ccedil;ais |
  <a href="README_DE.md">Deutsch</a> |
  <a href="README_ES.md">Espa&ntilde;ol</a> |
  <a href="README_NL.md">Nederlands</a> |
  <a href="README_PT.md">Portugu&ecirc;s</a>
</p>

---

## Pourquoi Peek-it [HA] ?

Votre appareil Android TV est branche sur votre TV 24h/24. Pourquoi ne pas le faire travailler ?

**Peek-it [HA]** est l'integration Home Assistant pour l'application Android **Peek-it [TV]**. Ensemble, ils affichent des **notifications riches en overlay** par-dessus n'importe quelle application en cours. Vous regardez un film ? Un flux camera apparait 5 secondes dans un coin. Soiree foot ? Le score se met a jour en temps reel. On sonne a la porte ? La camera de l'entree s'affiche instantanement.

### Ce que vous pouvez afficher

| Type | Exemple |
|------|---------|
| **Texte riche** | Titres, messages, compteurs, meteo |
| **Images** | Photos, captures, logos, QR codes |
| **Flux video RTSP** | Cameras de surveillance en direct, latence ultra-faible |
| **Pages web** | Tableaux de bord HA, graphiques, widgets meteo |
| **SVG** | Icones vectorielles, jauges, diagrammes |
| **Formes** | Rectangles, ellipses, lignes, fleches — construisez des mises en page completes |
| **Boutons interactifs** | Controlables avec la telecommande TV, declenchent des automatisations HA |
| **Menus interactifs** | Menus navigables au D-pad avec bascules d'entites HA |
| **Widgets d'entites HA** | Affichage en temps reel de l'etat des entites via WebSocket/REST |
| **Graphiques HA** | Graphiques CSS/SVG en aire, ligne et barres |
| **Synthese vocale** | Annonces vocales sur votre TV |

### Fonctionnalites cles

- **Zero latence** — overlay Android natif, pas de streaming ni de casting
- **Compatible avec tout** — l'overlay s'affiche par-dessus n'importe quelle application
- **Designer visuel** — creez des notifications en glisser-deposer depuis n'importe quel navigateur
- **Templates reutilisables** — concevez une fois, reutilisez avec des parametres dynamiques
- **7 animations** — fade, slide, pop... effets d'entree et de sortie independants
- **Synthese vocale** — annonces vocales directement sur la TV
- **Alertes sonores** — jouez des sons de notification avec les visuels
- **Menus interactifs** — menus overlay navigables au D-pad avec bascules HA
- **Multi-appareils** — gerez plusieurs TV depuis une seule instance HA
- **6 langues** — EN, FR, DE, ES, NL, PT

---

## Prerequis

1. **Un appareil Android TV** executant l'application **Peek-it [TV]**
2. **Home Assistant** installe et en fonctionnement
3. Les deux appareils sur le **meme reseau local**

### Installer l'application Peek-it [TV]

> L'application n'est pas (encore) sur le Play Store. Installez-la par sideload.

1. Telechargez l'APK depuis la [page des Releases](https://github.com/jolabs40/peek-it-ha/releases)
2. Transferez-le sur votre appareil (cle USB, `adb install`, ou une application de gestion de fichiers)
3. Lancez l'application — elle demandera la permission d'overlay (affichage par-dessus les autres applications)
4. Accordez la permission — le service demarre automatiquement
5. Notez l'**adresse IP** affichee sur l'ecran principal (ex. `192.168.1.42`)
6. Le port par defaut est **8081** (configurable dans l'application)

> **Astuce** : le service demarre automatiquement au demarrage de l'appareil. Branchez-le et oubliez-le.

---

## Installation

### Methode 1 : HACS (recommande)

1. Ouvrez HACS dans Home Assistant
2. Allez dans **Integrations** > menu 3 points > **Custom repositories**
3. Ajoutez l'URL du depot : `https://github.com/jolabs40/peek-it-ha`
4. Categorie : **Integration**
5. Cliquez sur **Peek-it [HA]** > **Download**
6. **Redemarrez Home Assistant**

### Methode 2 : Installation manuelle

1. Copiez le dossier `peek_it_ha/` dans votre repertoire `custom_components/` :
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
2. **Redemarrez Home Assistant**

### Ajouter l'integration

1. Allez dans **Parametres** > **Appareils et services** > **Ajouter une integration**
2. Recherchez **Peek-it [HA]**
3. Remplissez :
   - **Adresse IP** : l'IP de votre appareil Android TV (affichee dans l'application)
   - **Port** : `8081` (par defaut)
   - **Nom** : un nom convivial pour votre TV (ex. "TV du salon")
   - **Cle API** : si l'authentification est activee sur l'application TV
4. Validez — l'integration teste la connexion et se configure automatiquement

### Ce qui est cree automatiquement

| Entite | Type | Description |
|--------|------|-------------|
| `binary_sensor.tv_du_salon_status` | Binary Sensor | Etat de la connexion (en ligne/hors ligne), interroge toutes les 30s |
| `notify.tv_du_salon` | Notify | Entite d'envoi de notifications |

Le `binary_sensor` expose egalement un attribut `designer_url` avec un lien direct vers le Designer web.

---

## Options de l'integration (icone engrenage)

Cliquez sur l'**icone engrenage** sur la carte de l'integration Peek-it [HA] pour acceder a 3 menus :

### Parametres

Modifiez l'IP, le port, le nom ou la cle API. L'integration se recharge automatiquement apres la sauvegarde.

### Templates

Parcourez tous les templates disponibles sur votre TV, tries par categorie :

- **Official** — templates integres livres avec l'application
- **Custom** — vos templates finalises, chacun avec un UUID unique
- **Drafts** — brouillons en cours, pas encore d'ID attribue

Chaque template affiche son **nom**, son **ID** (copiable) et ses **parametres** disponibles.

### Designer

Lien direct pour ouvrir le Designer web dans un nouvel onglet. Pratique pour modifier des templates sans quitter HA.

---

## Utilisation

### Mode 1 : Message simple

Le plus rapide — envoyez un message texte qui s'affiche en bas de l'ecran avec un fond sombre.

```yaml
service: peek_it_ha.notify
data:
  message: "La machine a laver a termine !"
  title: "Maison"
  duration: 8000
```

### Mode 2 : Template + parametres

Le plus pratique — reutilisez un template existant en injectant des valeurs dynamiques.

```yaml
service: peek_it_ha.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    title: "Alerte securite"
    message: "Mouvement detecte dans le jardin"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

Le serveur charge le template, remplace les `{{placeholders}}` par les valeurs de `params`, et affiche le resultat.

**Comment trouver le template_id ?**
- Dans le Designer : cliquez sur le badge vert "ID" d'un template dans la bibliotheque
- Dans HA : icone engrenage > Templates > copiez l'ID affiche
- Via le service : `peek_it_ha.get_templates` retourne la liste complete

### Mode 3 : Elements bruts (JSON complet)

Le plus flexible — definissez chaque widget manuellement.

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
      content: "Camera du jardin"
      style:
        left: 62
        top: 28
        width: 34
        height: 5
        size: 18
        color: "#FFFFFF"
        align: center
```

### Fermer une notification

```yaml
service: peek_it_ha.notify
data:
  action: CLOSE
```

### Notification persistante (infinie)

```yaml
service: peek_it_ha.notify
data:
  message: "En attente de confirmation..."
  duration: 0
```

La duree `0` = la notification reste a l'ecran jusqu'a un `CLOSE` explicite ou un appui sur un bouton.

---

## Synthese vocale (TTS)

### TTS autonome

Envoyez un message vocal a toutes les TV configurees :

```yaml
service: peek_it_ha.tts
data:
  text: "Le diner est pret !"
  lang: "fr"
  speed: 1.0
  pitch: 1.0
  volume: 1.0
```

### Arreter le TTS

```yaml
service: peek_it_ha.tts_stop
```

### TTS avec notification

Combinez une notification visuelle avec un message vocal :

```yaml
service: peek_it_ha.notify
data:
  message: "Mouvement detecte dans le jardin"
  title: "Securite"
  duration: 10000
  tts: "Mouvement detecte dans le jardin"
  ttsLang: "fr"
  ttsSpeed: 1.25
  ttsVolume: 0.8
```

### Parametres TTS

| Parametre | Type | Defaut | Description |
|-----------|------|--------|-------------|
| `text` | string | — | Texte a prononcer (service autonome) |
| `lang` | string | `en` | Code langue (en, fr, de, es, nl, pt) |
| `speed` | float | `1.0` | Vitesse de parole (0.5 a 2.0) |
| `pitch` | float | `1.0` | Hauteur de la voix (0.5 a 2.0) |
| `volume` | float | `1.0` | Volume (0.0 a 1.0) |

Lorsqu'ils sont utilises dans `peek_it_ha.notify`, les champs sont prefixes : `tts`, `ttsLang`, `ttsSpeed`, `ttsPitch`, `ttsVolume`.

---

## Son

Jouez un son avec votre notification :

```yaml
service: peek_it_ha.notify
data:
  message: "Colis livre"
  title: "Sonnette"
  sound: "01_notify.wav"
  soundVolume: 0.8
```

| Parametre | Type | Defaut | Description |
|-----------|------|--------|-------------|
| `sound` | string | — | Nom du fichier son (ex. "01_notify.wav") |
| `soundVolume` | float | `1.0` | Volume (0.0 a 1.0) |

L'application Peek-it [TV] est livree avec des sons integres et prend en charge l'upload de sons personnalises via le Designer.

---

## Menu interactif

Le type de widget `menu` cree un menu overlay navigable au D-pad sur la TV. Les menus supportent les sous-menus, les bascules d'entites HA avec interrogation d'etat en temps reel, les callbacks d'action et les boutons de fermeture.

### Exemple de menu via automatisation

```yaml
service: peek_it_ha.notify
data:
  duration: 0
  elements:
    - type: menu
      content: >
        {
          "title": "Controles rapides",
          "titleIcon": "mdi:menu",
          "bgColor": "#1E1E1E",
          "textColor": "#FFFFFF",
          "accentColor": "#00E676",
          "items": [
            {"type": "submenu", "label": "Lumieres", "icon": "mdi:lightbulb-group", "children": [
              {"type": "toggle", "label": "Salon", "icon": "mdi:lightbulb", "entity_id": "light.living_room"},
              {"type": "toggle", "label": "Cuisine", "icon": "mdi:lightbulb", "entity_id": "light.kitchen"},
              {"type": "close", "label": "Retour", "icon": "mdi:arrow-left"}
            ]},
            {"type": "action", "label": "Mode cinema", "icon": "mdi:movie", "action": "movie_mode"},
            {"type": "close", "label": "Fermer", "icon": "mdi:close"}
          ]
        }
      style:
        left: 35
        top: 10
        width: 30
        height: 80
```

### Types d'elements de menu

| Type | Description |
|------|-------------|
| `action` | Declenche un evenement HA (`peekit_button_press`) avec l'ID `action` specifie |
| `submenu` | Ouvre un sous-menu imbrique avec ses propres elements `children` |
| `toggle` | Bascule une entite HA (necessite `entity_id`), interroge l'etat toutes les 5s |
| `text` | Texte informatif (non interactif) |
| `close` | Ferme le menu |

### Navigation

- **Haut/Bas** : naviguer entre les elements
- **Droite/Entree** : ouvrir un sous-menu
- **Gauche/Retour** : revenir au menu parent
- **Retour a la racine** : fermer le menu

---

## Widget d'entite HA

Affichez l'etat des entites HA en temps reel directement sur la TV a l'aide d'un widget `webview` connecte via WebSocket ou interrogation REST.

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

## Widget graphique HA

L'application Peek-it [TV] prend en charge les graphiques CSS/SVG pour afficher l'historique des entites. Types de graphiques : **aire**, **ligne** et **barres**.

Les graphiques sont rendus en pur CSS/SVG — aucune bibliotheque externe requise. Configurez-les via l'editeur de graphiques du Designer.

---

## Configuration de l'overlay

### Horloge en overlay

L'application Peek-it [TV] peut afficher une horloge persistante en overlay. Configurez-la via les Parametres du Designer ou le endpoint `/api/config/clock` :

- Activer/desactiver
- Format (12h/24h)
- Position, couleur, taille, opacite

### Overlay d'assombrissement

Une couche d'assombrissement configurable en arriere-plan. Configurez via les Parametres du Designer ou `/api/config/dimming` :

- Activer/desactiver
- Couleur, opacite

---

## Parametres disponibles

### Champs principaux

| Parametre | Type | Defaut | Description |
|-----------|------|--------|-------------|
| `action` | string | `DISPLAY` | `DISPLAY` pour afficher, `CLOSE` pour fermer |
| `duration` | int | `10000` | Duree en millisecondes (0 = infini) |
| `priority` | string | `normal` | `normal` ou `urgent` |
| `animationIn` | string | `fade` | Animation d'entree |
| `animationOut` | string | `fade` | Animation de sortie |
| `template_id` | string | — | UUID du template a utiliser |
| `params` | dict | — | Parametres dynamiques du template |
| `elements` | list | — | Liste de widgets (mode avance) |
| `message` | string | — | Texte simple (mode simple) |
| `title` | string | — | Titre (mode simple) |
| `sound` | string | — | Nom du fichier son |
| `soundVolume` | float | `1.0` | Volume du son (0.0-1.0) |
| `tts` | string | — | Texte TTS (lu a voix haute avec la notification) |
| `ttsLang` | string | `en` | Code langue TTS |
| `ttsSpeed` | float | `1.0` | Vitesse de parole TTS (0.5-2.0) |
| `ttsPitch` | float | `1.0` | Hauteur de voix TTS (0.5-2.0) |
| `ttsVolume` | float | `1.0` | Volume TTS (0.0-1.0) |

### Animations disponibles

| Nom | Effet |
|-----|-------|
| `none` | Instantane, pas d'animation |
| `fade` | Fondu entrant/sortant |
| `slide_right` | Glissement depuis/vers la droite |
| `slide_left` | Glissement depuis/vers la gauche |
| `slide_top` | Glissement depuis/vers le haut |
| `slide_bottom` | Glissement depuis/vers le bas |
| `pop` | Effet de zoom/echelle |

### Types de widgets

| Type | Description | Contenu (`content`) |
|------|-------------|---------------------|
| `text` | Texte statique | Le texte a afficher |
| `button` | Bouton interactif (telecommande TV) | Libelle du bouton |
| `box` | Rectangle / conteneur | — |
| `circle` | Cercle | — |
| `ellipse` | Ellipse / ovale | — |
| `image` | Image (PNG, JPG, URL) | URL de l'image |
| `video` | Flux video RTSP / HTTP | URL du flux |
| `webview` | Page web embarquee | URL de la page |
| `svg` | Image vectorielle SVG | URL ou chemin SVG |
| `line` | Ligne horizontale | — |
| `arrow` | Fleche (pointant a droite) | — |
| `menu` | Menu interactif D-pad | JSON MenuConfig |

### Proprietes de style

| Propriete | Type | Description |
|-----------|------|-------------|
| `left` | float | Position X en % de l'ecran (0-100) |
| `top` | float | Position Y en % de l'ecran (0-100) |
| `width` | float | Largeur en % de l'ecran |
| `height` | float | Hauteur en % de l'ecran |
| `color` | string | Couleur du texte (hex, ex. `#FFFFFF`) |
| `bgColor` | string | Couleur de fond (hex avec alpha, ex. `#CC000000`) |
| `size` | int | Taille de police |
| `font` | string | Famille de police (Roboto, sans-serif, etc.) |
| `weight` | string | Graisse de police (`normal`, `bold`) |
| `align` | string | Alignement (`left`, `center`, `right`) |
| `opacity` | float | Opacite (0.0 a 1.0) |
| `radius` | int | Rayon des coins (pixels) |
| `borderWidth` | int | Epaisseur de la bordure (pixels) |
| `borderColor` | string | Couleur de la bordure (hex) |
| `rotation` | float | Rotation en degres |
| `focusColor` | string | Couleur de la bordure au focus |
| `focusBgColor` | string | Couleur de fond au focus |

### Proprietes d'interaction (boutons)

| Propriete | Type | Description |
|-----------|------|-------------|
| `focusable` | bool | Le widget recoit le focus de la telecommande TV |
| `directFocus` | bool | Le widget obtient le focus a l'affichage |
| `action` | string | `CLOSE` pour fermer, ou un ID personnalise pour le webhook |
| `paramKey` | string | Lie le contenu a un parametre de template |
| `actionParamKey` | string | Lie l'action a un parametre de template |

---

## Le Designer

Le Designer est un **editeur web visuel** embarque dans l'application Peek-it [TV]. Accedez-y depuis n'importe quel navigateur sur votre reseau local.

**URL** : `http://<IP_TV>:<PORT>/` (ex. `http://192.168.1.42:8081/`)

Vous pouvez egalement y acceder via :
- L'attribut `designer_url` du binary_sensor dans HA
- L'icone engrenage > Designer dans les options de l'integration

### Fonctionnalites

- **11 types de widgets** — glisser-deposer sur un canevas TV calibre
- **Apercu JSON en temps reel** — visualisez le payload exact en cours de construction
- **Bibliotheque de templates** — sauvegarder, charger, renommer, supprimer, exporter/importer
- **Systeme de parametres** — definissez des `paramKey` sur les widgets pour du contenu dynamique
- **Auto-calibration** — s'adapte a la resolution reelle de votre TV (16:9, 21:9, etc.)
- **Configuration sonore** — parametres de son de notification par defaut
- **Configuration du token HA** — necessaire pour les callbacks webhook
- **Internationalisation** — disponible en 6 langues (EN, FR, DE, ES, NL, PT)

### Envoyer et tester

- **Bouton SEND** (bleu) — envoie la mise en page actuelle vers la TV immediatement
- **Bouton KILL** (rouge) — ferme la notification en cours
- **Apercu JSON** (pied de page) — visualisez le payload exact qui sera envoye

---

## Templates & parametres

### Concept

Un template est une mise en page de notification reutilisable. Au lieu d'envoyer 15 lignes de JSON a chaque fois, vous :

1. **Creez** la mise en page dans le Designer (glisser-deposer)
2. **Definissez des parametres** (`paramKey`) sur les elements dynamiques
3. **Sauvegardez** en Custom (UUID genere)
4. **Utilisez** le `template_id` + `params` dans vos automatisations

### Recuperer la liste des templates

```yaml
service: peek_it_ha.get_templates
response_variable: result
```

Retourne un dictionnaire par appareil configure :
```json
{
  "TV du salon": {
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

## Automatisations

### Alerte de detection de mouvement

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
            title: "Mouvement detecte !"
            camera_url: "rtsp://192.168.1.50:554/stream1"
          duration: 15000
          animationIn: slide_right
          animationOut: fade
```

### Bulletin meteo du matin

```yaml
automation:
  - alias: "Meteo du matin"
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
          title: "Meteo du jour"
          duration: 10000
          animationIn: fade
```

### Automatisation d'annonce TTS

```yaml
automation:
  - alias: "Alerte TTS sonnette"
    trigger:
      - platform: state
        entity_id: binary_sensor.doorbell
        to: "on"
    action:
      - service: peek_it_ha.tts
        data:
          text: "Quelqu'un est a la porte d'entree"
          lang: "fr"
          speed: 1.25
          volume: 1.0
```

### Notification avec son

```yaml
automation:
  - alias: "Alerte linge termine"
    trigger:
      - platform: state
        entity_id: sensor.washing_machine
        to: "idle"
    action:
      - service: peek_it_ha.notify
        data:
          message: "La machine a laver a termine !"
          title: "Lessive"
          duration: 8000
          sound: "08-notify.mp3"
          soundVolume: 0.7
```

### Boutons interactifs — retour vers HA

Quand un utilisateur appuie sur un bouton dans une notification (via la telecommande TV), un evenement HA est declenche :

```yaml
automation:
  - alias: "Bouton TV - Eteindre lumieres"
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

### Alerte persistante avec bouton de fermeture

```yaml
automation:
  - alias: "Alerte fuite d'eau"
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
          tts: "Attention ! Fuite d'eau detectee !"
          ttsLang: "fr"
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
              content: "FUITE D'EAU DETECTEE"
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
              content: "Compris"
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

### Flux camera RTSP

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

Le flux s'affiche avec une latence ultra-faible (~50ms) grace a une configuration ExoPlayer optimisee.

---

## Reference des services

| Service | Description |
|---------|-------------|
| `peek_it_ha.notify` | Envoyer une notification a tous les appareils configures |
| `peek_it_ha.get_templates` | Recuperer la liste des templates de tous les appareils |
| `peek_it_ha.tts` | Envoyer du TTS a tous les appareils configures |
| `peek_it_ha.tts_stop` | Arreter le TTS sur tous les appareils configures |

---

## Webhooks & evenements

L'integration ecoute un webhook pour recevoir les logs et les actions de boutons depuis la TV.

| Evenement HA | Declencheur | Donnees |
|--------------|-------------|---------|
| `peekit_button_press` | Appui sur un bouton de la TV | `{ "action": "button_id" }` |

Les logs de la TV sont transmis au logger HA avec le prefixe `[PEEK-IT REPORT]`.

---

## Multi-appareils

L'integration prend en charge **plusieurs appareils**. Ajoutez chaque TV comme une integration separee. Les services `peek_it_ha.notify`, `tts`, `tts_stop` et `get_templates` envoient automatiquement a **tous les appareils configures**.

Pour cibler un seul appareil, utilisez l'entite `notify` specifique :

```yaml
service: notify.send_message
target:
  entity_id: notify.tv_du_salon
data:
  message: "Uniquement sur cette TV"
```

---

## Internationalisation

L'integration et l'application Peek-it [TV] prennent en charge **6 langues** :

| Code | Langue |
|------|--------|
| `en` | Anglais (par defaut) |
| `fr` | Francais |
| `de` | Allemand |
| `es` | Espagnol |
| `nl` | Neerlandais |
| `pt` | Portugais |

La langue peut etre configuree dans les parametres du Designer ou sur l'ecran des parametres de l'application Peek-it [TV].

---

## WAF — Le KPI ultime

Le legendaire **WAF** — *Wife Acceptance Factor* (Facteur d'Acceptation Conjugale). Cette metrique non officielle mais absolument cruciale qui mesure la tolerance de votre moitie envers vos experiences domotiques.

### Cas d'usage qui boostent votre WAF

**Linge intelligent** : une notification "Lessive terminee !" apparait discretement pendant le film. Fini les lessives oubliees 3 jours dans le tambour qui sentent le renfermee.

> *(WAF : +23 points)*

**Meteo du matin** : chaque jour a 7h30, la meteo s'affiche sur la TV de la cuisine. Plus besoin de demander a un assistant vocal, ni de chercher son telephone sous l'oreiller.

> *(WAF : +15 points)*

**Camera de la sonnette** : quelqu'un sonne, le flux camera apparait a l'ecran. Deliberation depuis le canape. Personne n'a eu a se lever. La democratie du salon a tranche.

> *(WAF : +38 points)*

**Score sportif** : un discret "2 - 1, 78'" apparait 3 secondes dans le coin superieur droit. Tout le monde est content. Personne n'a change de chaine. La paix du foyer est preservee.

> *(WAF : +52 points)*

### Le cas d'usage qui RUINE votre WAF

**Debogage en production** : vous testez vos notifications a 23h pendant que votre moitie regarde le dernier episode de la saison. Le grand final. Le moment ou tout se joue. Et la : "Test 1", "Lorem ipsum", "AAAA CA MARCHE !", un gros rectangle noir, puis plus rien... puis re-un rectangle noir.

> *(WAF : -347 points. Temps de recuperation estime : 3 semaines de bon comportement. Et un bouquet de fleurs.)*

**Conseil de pro** : testez vos automatisations AVANT 21h. Ou utilisez le bouton **KILL** dans le Designer. Il existe pour une raison. Votre couple vous remerciera.

---

## Depannage

| Probleme | Solution |
|----------|----------|
| Integration introuvable dans HA | Verifiez que le dossier est bien dans `custom_components/peek_it_ha/`. Redemarrez HA. |
| "Impossible de se connecter" a la configuration | Verifiez l'IP et le port. L'application doit tourner sur la TV. Testez `http://IP:8081/api/status` dans un navigateur. |
| Binary sensor toujours "hors ligne" | L'application Peek-it [TV] est-elle en cours d'execution ? Le service demarre-t-il au boot ? |
| La notification ne s'affiche pas | Verifiez la permission d'overlay dans les parametres Android TV. |
| Le Designer ne se connecte pas | Verifiez que vous etes sur le meme reseau. Essayez `http://IP:PORT/` dans votre navigateur. |
| Templates vides dans le menu engrenage | La TV doit etre allumee et joignable. Verifiez l'etat du binary_sensor. |
| Le bouton TV ne declenche pas HA | Configurez le token HA dans le Designer (icone engrenage). Verifiez que `ha_ip` est accessible depuis la TV. |
| Le TTS ne parle pas | Verifiez qu'un moteur TTS est installe sur l'Android TV (Google TTS est generalement pre-installe). |
| Pas de son avec la notification | Verifiez que le fichier son existe (verifiez via les parametres du Designer). Certaines applications de streaming peuvent bloquer le mixage audio. |
| Le menu ne repond pas au D-pad | Assurez-vous que l'element menu a le focus. Definissez `duration: 0` pour que le menu reste ouvert. |

---

## Contribuer

Les contributions sont les bienvenues ! Ouvrez une issue ou une pull request sur le [depot GitHub](https://github.com/jolabs40/peek-it-ha).

## Licence

Ce projet est distribue sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de details.

---

<p align="center">
  Fait avec du cafe, beaucoup trop de fichiers YAML, et un amour deraisonnable pour les overlays.<br/>
  <strong>Peek-it [HA]</strong> — parce que votre TV peut faire bien plus que vous ne le pensez.
</p>
