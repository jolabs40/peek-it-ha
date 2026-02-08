# peek-it TV — Integration Home Assistant

<p align="center">
  <img src="peek_it_tv/icon@2x.png" alt="peek-it TV" width="128"/>
</p>

<p align="center">
  <strong>Transformez votre Android TV en panneau de notifications intelligent.</strong><br/>
  Alertes, cameras, dashboards, messages — directement en overlay sur votre TV.
</p>

<p align="center">
  <a href="#-installation">Installation</a> •
  <a href="#-utilisation">Utilisation</a> •
  <a href="#-le-designer--votre-meilleur-ami">Designer</a> •
  <a href="#-templates--parametres">Templates</a> •
  <a href="#-automations">Automations</a> •
  <a href="#-waf--wife-acceptance-factor">WAF</a> •
  <a href="README.md">English Version</a>
</p>

---

## Pourquoi peek-it TV ?

Votre NVIDIA Shield, Chromecast, Xiaomi Mi Box ou tout autre appareil Android TV est branche 24h/24 sur votre TV. Et si on en profitait ?

**peek-it TV** affiche des **notifications riches en overlay** par-dessus n'importe quelle application. Netflix en cours ? Un flux camera s'affiche 5 secondes en haut a droite. Match de foot ? Le score s'actualise en temps reel. Le facteur sonne ? La camera du portail s'affiche instantanement.

### Ce que vous pouvez afficher

| Type | Exemple |
|------|---------|
| **Texte riche** | Titres, messages, compteurs, meteo |
| **Images** | Photos, captures, logos, QR codes |
| **Flux video RTSP** | Cameras de surveillance en direct, ultra basse latence |
| **Pages web** | Dashboards HA, graphiques Grafana, widgets meteo |
| **SVG** | Icones vectorielles, schemas, jauges |
| **Formes** | Rectangles, ellipses, lignes, fleches — pour composer des layouts complets |
| **Boutons interactifs** | Controlables a la telecommande, declenchent des actions HA |

### Points forts

- **Zero latence** — overlay natif Android, pas de streaming ni de cast
- **Fonctionne avec tout** — Netflix, Plex, Kodi, YouTube, jeux... l'overlay passe par-dessus
- **Designer visuel** — creez vos notifications en drag & drop depuis un navigateur
- **Templates reutilisables** — creez une fois, reutilisez avec des parametres dynamiques
- **7 animations** — fade, slide, pop... entrees et sorties independantes
- **Boutons interactifs** — la telecommande TV declenche des automations HA
- **Multi-box** — gerez plusieurs TV depuis une seule instance HA

---

## Prerequis

1. **Un appareil Android TV** (NVIDIA Shield, Chromecast avec Google TV, Xiaomi Mi Box, etc.)
2. **L'application peek-it TV** installee sur l'appareil
3. **Home Assistant** installe et fonctionnel
4. Les deux appareils sur le **meme reseau local**

### Installer l'application Android TV

> L'application n'est pas (encore) sur le Play Store. Installez-la via sideload.

1. Telechargez le fichier APK depuis la [page Releases](https://gitlab.com/jolabs40/peek-it/releases)
2. Transferez-le sur votre appareil (cle USB, `adb install`, ou un file manager)
3. Lancez l'application — elle demande la permission d'overlay (affichage par-dessus les autres apps)
4. Accordez la permission — le service demarre automatiquement
5. Notez l'**adresse IP** affichee sur l'ecran principal (ex: `192.168.1.42`)
6. Le port par defaut est **8081** (modifiable dans l'app)

> **Astuce** : le service demarre automatiquement au boot de l'appareil. Branchez, oubliez.

<!-- SCREENSHOT: Ecran principal de l'app Android TV montrant l'IP, le port et le statut du service -->

---

## Installation

### Methode 1 : HACS (recommandee)

1. Ouvrez HACS dans Home Assistant
2. Allez dans **Integrations** > menu 3 points > **Custom repositories**
3. Ajoutez l'URL du depot : `https://gitlab.com/jolabs40/peek-it`
4. Categorie : **Integration**
5. Cliquez sur **peek-it TV** > **Telecharger**
6. **Redemarrez Home Assistant**

### Methode 2 : Installation manuelle

1. Copiez le dossier `peek_it_tv/` dans votre repertoire `custom_components/` :
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
2. **Redemarrez Home Assistant**

### Ajout de l'integration

1. Allez dans **Parametres** > **Appareils et services** > **Ajouter une integration**
2. Cherchez **peek-it TV**
3. Renseignez :
   - **Adresse IP** : l'IP de votre appareil Android TV (affichee dans l'app)
   - **Port** : `8081` (par defaut)
   - **Nom** : un nom pour identifier votre TV (ex: "TV Salon")
4. Validez — l'integration teste la connexion et se configure automatiquement

<!-- SCREENSHOT: Formulaire d'ajout de l'integration dans HA (IP, port, nom) -->

### Ce qui est cree automatiquement

| Entite | Type | Description |
|--------|------|-------------|
| `binary_sensor.tv_salon_status` | Binary Sensor | Etat de connexion (online/offline), poll toutes les 30s |
| `notify.tv_salon` | Notify | Entite d'envoi de notifications |

L'entite `binary_sensor` expose aussi un attribut `designer_url` avec le lien direct vers le Designer web.

---

## Options de l'integration (engrenage)

Cliquez sur l'**icone engrenage** de la carte peek-it TV pour acceder a 3 menus :

### Parametres

Modifiez l'IP, le port ou le nom de votre appareil. L'integration se recharge automatiquement apres validation.

<!-- SCREENSHOT: Formulaire Parametres dans le menu engrenage -->

### Templates

Consultez la liste de tous les templates disponibles sur votre Box TV, classes par categorie :

- **Officiels** — templates integres, fournis avec l'application
- **Custom** — vos templates finalises, avec un UUID unique
- **Brouillons** — travaux en cours, pas encore d'ID

Chaque template affiche son **nom**, son **ID** (copiable) et ses **parametres** disponibles.

<!-- SCREENSHOT: Liste des templates dans le menu engrenage avec IDs et params -->

### Designer

Lien direct pour ouvrir le Designer web dans un nouvel onglet. Pratique pour editer vos templates sans quitter HA.

---

## Utilisation

### Mode 1 : Message simple

Le plus rapide — envoyez un message texte qui s'affiche en bas de l'ecran avec un fond sombre.

```yaml
service: peek_it_tv.notify
data:
  message: "Le lave-linge a termine !"
  title: "Maison"
  duration: 8000
```

Resultat : un bandeau sombre en bas de l'ecran avec le titre en bleu et le message en blanc.

<!-- SCREENSHOT: Notification message simple sur la TV avec titre et message -->

### Mode 2 : Template + parametres

Le plus pratique — reutilisez un template existant en injectant des valeurs dynamiques.

```yaml
service: peek_it_tv.notify
data:
  template_id: "70c3f0c7-ac0c-4b09-838a-e116ce9c9a11"
  params:
    titre: "Alerte Securite"
    message: "Mouvement detecte dans le jardin"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 15000
  animationIn: slide_right
  animationOut: fade
```

Le serveur charge le template, remplace les `{{placeholders}}` par les valeurs de `params`, et affiche le resultat.

**Comment trouver le template_id ?**
- Dans le Designer : cliquez sur le badge vert "ID" d'un template dans la bibliotheque
- Dans HA : engrenage > Templates > copiez l'ID affiche
- Via le service : `peek_it_tv.get_templates` retourne la liste complete

### Mode 3 : Elements bruts (JSON complet)

Le plus flexible — definissez chaque widget manuellement.

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
      content: "http://192.168.1.10:8123/local/camera_jardin.jpg"
      style:
        left: 62
        top: 7
        width: 34
        height: 22
    - type: text
      content: "Camera Jardin"
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
service: peek_it_tv.notify
data:
  action: CLOSE
```

### Notification persistante (infinie)

```yaml
service: peek_it_tv.notify
data:
  message: "En attente de confirmation..."
  duration: 0
```

Duree `0` = la notification reste affichee jusqu'a un `CLOSE` explicite ou l'appui sur un bouton d'action.

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

### Animations disponibles

| Nom | Effet |
|-----|-------|
| `none` | Instantane, pas d'animation |
| `fade` | Fondu (entree/sortie) |
| `slide_right` | Glissement depuis/vers la droite |
| `slide_left` | Glissement depuis/vers la gauche |
| `slide_top` | Glissement depuis/vers le haut |
| `slide_bottom` | Glissement depuis/vers le bas |
| `pop` | Effet de zoom (scale) |

### Types de widgets

| Type | Description | Contenu (`content`) |
|------|-------------|---------------------|
| `text` | Texte statique | Le texte a afficher |
| `button` | Bouton interactif (telecommande TV) | Texte du bouton |
| `box` | Rectangle / conteneur | — |
| `circle` | Cercle | — |
| `ellipse` | Ellipse / ovale | — |
| `image` | Image (PNG, JPG, URL) | URL de l'image |
| `video` | Flux video RTSP / HTTP | URL du flux |
| `webview` | Page web embarquee | URL de la page |
| `svg` | Image vectorielle SVG | URL ou chemin SVG |
| `line` | Ligne horizontale | — |
| `arrow` | Fleche (pointe a droite) | — |

### Proprietes de style

| Propriete | Type | Description |
|-----------|------|-------------|
| `left` | float | Position X en % de l'ecran (0-100) |
| `top` | float | Position Y en % de l'ecran (0-100) |
| `width` | float | Largeur en % de l'ecran |
| `height` | float | Hauteur en % de l'ecran |
| `color` | string | Couleur du texte (hex, ex: `#FFFFFF`) |
| `bgColor` | string | Couleur de fond (hex avec alpha, ex: `#CC000000`) |
| `size` | int | Taille de police |
| `font` | string | Police (Roboto, sans-serif, etc.) |
| `weight` | string | Graisse (`normal`, `bold`) |
| `align` | string | Alignement (`left`, `center`, `right`) |
| `opacity` | float | Opacite (0.0 a 1.0) |
| `radius` | int | Arrondi des coins (pixels) |
| `borderWidth` | int | Epaisseur de bordure (pixels) |
| `borderColor` | string | Couleur de bordure (hex) |
| `angle` | int | Rotation en degres (0-360) |
| `focusColor` | string | Couleur de bordure au focus |
| `focusBgColor` | string | Couleur de fond au focus |

### Proprietes d'interaction (boutons)

| Propriete | Type | Description |
|-----------|------|-------------|
| `focusable` | bool | Le widget recoit le focus telecommande |
| `directFocus` | bool | Le widget recoit le focus des l'affichage |
| `action` | string | `CLOSE` pour fermer, ou un ID custom pour webhook |
| `paramKey` | string | Lie le contenu a un parametre de template |
| `actionParamKey` | string | Lie l'action a un parametre de template |

---

## Le Designer — votre meilleur ami

Le Designer est un **editeur visuel web** embarque dans l'application Android TV. Vous y accedez depuis n'importe quel navigateur sur votre reseau local.

**URL** : `http://<IP_TV>:<PORT>/` (ex: `http://192.168.1.42:8081/`)

Vous pouvez aussi y acceder via :
- L'attribut `designer_url` du binary_sensor dans HA
- Le menu engrenage > Designer de l'integration

<!-- SCREENSHOT: Vue d'ensemble du Designer avec un template en cours d'edition -->

### Interface

```
┌─────────────────────────────────────────────────────────────┐
│  Header : animations, duree, fond d'ecran, envoi           │
├──────┬──────────────────────────────────┬───────────────────┤
│ Barre│  Zone de travail                 │ Panneau lateral   │
│ d'ou-│  ┌──────────────────────────┐    │ - Layers (calques)│
│ tils │  │                          │    │ - Contenu         │
│      │  │    Ecran TV simule       │    │ - Texte           │
│      │  │    (ratio 16/9 calibre)  │    │ - Apparence       │
│      │  │                          │    │ - Action & Focus  │
│      │  └──────────────────────────┘    │                   │
└──────┴──────────────────────────────────┴───────────────────┘
│  Footer : apercu JSON en temps reel                         │
└─────────────────────────────────────────────────────────────┘
```

### Barre d'outils (gauche)

11 types de widgets disponibles en un clic :

| Icone | Type | Usage |
|-------|------|-------|
| Aa | `text` | Texte, titres, labels |
| Bouton | `button` | Boutons interactifs (telecommande) |
| Image | `image` | Photos, logos (URL) |
| Cercle | `circle` | Forme circulaire |
| Rectangle | `box` | Conteneur, fond, separateur |
| Camera | `video` | Flux RTSP en direct |
| Globe | `webview` | Page web, dashboard HA |
| Crayon | `svg` | Image vectorielle |
| Ovale | `ellipse` | Forme elliptique |
| Trait | `line` | Ligne de separation |
| Fleche | `arrow` | Indicateur de direction |

### Manipulation des widgets

| Action | Geste |
|--------|-------|
| **Deplacer** | Cliquer-glisser |
| **Redimensionner** | Poignees Nord/Sud/Est/Ouest |
| **Multi-selection** | Ctrl + clic |
| **Desactiver l'aimantation** | Alt + glisser |
| **Supprimer** | Touche Suppr |
| **Dupliquer** | Bouton dans le panneau |
| **Ordre Z** | 4 boutons (premier/arriere, monter/descendre) |

### Panneau lateral (droite)

#### Calques (Layers)
Liste de tous les widgets avec leur type et nom. Cliquez pour selectionner. L'ordre = l'ordre d'empilement (z-index).

#### Contenu
- **content** — texte ou URL selon le type de widget
- **paramKey** — nom du parametre dynamique (badge jaune sur le canvas)

#### Texte
- **Police** : Regular, Medium, Black, Light, Condensed
- **Taille** : en pixels
- **Couleur** : selecteur couleur
- **Alignement** : gauche / centre / droite

#### Apparence
- Couleur de fond, bordure, opacite
- Arrondi des coins (radius)
- Epaisseur de bordure
- Angle de rotation (0-360)
- Case "Transparent" (supprime le fond)

#### Action & Focus
- **directFocus** — le widget recoit le focus au lancement (un seul par notification)
- **focusable** — navigable a la telecommande
- **CLOSE** — ferme la notification au clic
- **action** — ID custom (declenche un evenement HA)
- Couleurs de focus personnalisables

### Gestion des templates

#### Sauvegarder
1. Cliquez sur l'icone de sauvegarde
2. Donnez un nom au template
3. Choisissez :
   - **Brouillon** — travail en cours, pas d'ID attribue
   - **Custom (Fini)** — template finalise, UUID genere automatiquement

#### Charger
1. Cliquez sur l'icone de chargement
2. Parcourez les 3 categories :
   - **OFFICIAL** (cadenas) — templates integres, lecture seule
   - **DRAFT** (jaune) — brouillons editables
   - **CUSTOM** (etoile) — vos templates finalises

#### Operations sur les templates
- **Badge vert "ID"** — cliquez pour copier l'UUID dans le presse-papier
- **Icone telechargement** — exporte le template en JSON sur votre PC
- **Icone crayon** — renommer (draft/custom uniquement)
- **Icone poubelle** — supprimer avec confirmation

#### Importer un template
Bouton **IMPORT PC** : importez un fichier `.json` depuis votre ordinateur. Le template est place en brouillon.

### Envoi et test

- **Bouton ENVOYER** (bleu) — envoie le layout actuel sur la TV immediatement
- **Bouton KILL** (rouge) — ferme la notification en cours
- **Apercu JSON** (footer) — voyez le payload exact qui sera envoye

### Calibrage automatique

Au chargement, le Designer interroge `/api/status` pour recuperer la resolution reelle de votre TV. Le ratio du canvas s'adapte automatiquement (16:9, 21:9, etc.). Un badge vert confirme la connexion et la resolution detectee.

<!-- SCREENSHOT: Designer avec badge de calibrage vert "1920x1080" -->

### Configuration HA dans le Designer

Cliquez sur l'icone **engrenage** dans le header du Designer pour :
- Saisir votre **token Home Assistant** (necessaire pour les retours webhook)
- Le token est sauvegarde sur l'appareil, jamais expose en clair

<!-- SCREENSHOT: Modal de configuration token HA dans le Designer -->

---

## Templates & parametres

### Concept

Un template est un layout de notification reutilisable. Au lieu d'envoyer 15 lignes de JSON a chaque fois, vous :

1. **Creez** le layout dans le Designer (drag & drop)
2. **Definissez des parametres** (`paramKey`) sur les elements dynamiques
3. **Sauvegardez** en Custom (UUID genere)
4. **Utilisez** le `template_id` + `params` dans vos automations

### Exemple concret

#### Dans le Designer

Creez un template "Alerte Camera" avec :
- Un fond sombre (`box`)
- Un titre texte avec `paramKey: titre`
- Un flux video avec `paramKey: camera_url`
- Un bouton "Fermer" avec action `CLOSE`

Sauvegardez en Custom. Notez l'UUID : `a1b2c3d4-...`

#### Dans Home Assistant

```yaml
service: peek_it_tv.notify
data:
  template_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
  params:
    titre: "Mouvement detecte - Jardin"
    camera_url: "rtsp://192.168.1.50:554/stream1"
  duration: 20000
  priority: urgent
  animationIn: slide_right
```

Le resultat : votre template s'affiche avec le titre et la camera injectes dynamiquement. Vous reutilisez le meme template pour toutes vos cameras — seul le `params` change.

### Recuperer la liste des templates

```yaml
service: peek_it_tv.get_templates
```

Retourne un dictionnaire par box configuree :
```json
{
  "TV Salon": {
    "official": [
      { "filename": "demo.json", "id": "70c3f0c7-...", "params": ["titre", "message"] }
    ],
    "custom": [
      { "filename": "alerte_camera.json", "id": "a1b2c3d4-...", "params": ["titre", "camera_url"] }
    ],
    "draft": ["brouillon_test.json"]
  }
}
```

---

## Automations

### Notification sur evenement

```yaml
automation:
  - alias: "Alerte mouvement jardin"
    trigger:
      - platform: state
        entity_id: binary_sensor.mouvement_jardin
        to: "on"
    action:
      - service: peek_it_tv.notify
        data:
          template_id: "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
          params:
            titre: "Mouvement detecte !"
            camera_url: "rtsp://192.168.1.50:554/stream1"
          duration: 15000
          animationIn: slide_right
          animationOut: fade
```

### Notification meteo le matin

```yaml
automation:
  - alias: "Meteo du matin"
    trigger:
      - platform: time
        at: "07:30:00"
    condition:
      - condition: state
        entity_id: binary_sensor.tv_salon_status
        state: "on"
    action:
      - service: peek_it_tv.notify
        data:
          message: "{{ states('weather.maison') }} — {{ state_attr('weather.maison', 'temperature') }}°C"
          title: "Meteo du jour"
          duration: 10000
          animationIn: fade
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
          area_id: salon
```

Pour que ca fonctionne, dans le Designer, creez un bouton avec :
- `focusable` : active
- `action` : `lights_off` (l'ID que vous voulez)

L'utilisateur navigue avec les fleches de la telecommande et valide avec OK. L'evenement `peekit_button_press` est emis dans HA avec l'`action` correspondante.

<!-- SCREENSHOT: Template avec boutons interactifs dans le Designer + exemple d'automation HA -->

### Notification persistante avec bouton de fermeture

```yaml
automation:
  - alias: "Alerte fuite d'eau"
    trigger:
      - platform: state
        entity_id: binary_sensor.fuite_eau
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
              content: "J'ai compris"
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

La notification reste affichee (`duration: 0`) jusqu'a ce que quelqu'un appuie sur "J'ai compris" a la telecommande.

### Afficher un dashboard HA en overlay

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

### Flux camera RTSP

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

Le flux s'affiche avec une latence ultra basse (~50ms) grace a ExoPlayer optimise. Ideal pour les sonnettes et cameras de securite.

---

## Service `peek_it_tv.get_templates`

Recupere la liste complete des templates de toutes les box configurees. Utile dans les scripts et automations pour construire des interfaces dynamiques.

```yaml
service: peek_it_tv.get_templates
response_variable: result
```

La variable `result` contient un dictionnaire cle = nom de la box, valeur = templates.

---

## Webhook & evenements

L'integration ecoute un webhook pour recevoir les logs et les actions bouton de la Box TV.

| Evenement HA | Declencheur | Donnees |
|--------------|-------------|---------|
| `peekit_button_press` | Appui bouton sur la TV | `{ "action": "id_du_bouton" }` |

Les logs de la box sont egalement remontes dans le logger HA avec le prefixe `[BOX TV REPORT]`.

---

## Multi-box

L'integration supporte **plusieurs appareils**. Ajoutez chaque TV comme une integration separee. Les services `peek_it_tv.notify` et `get_templates` envoient automatiquement a **toutes les box configurees**.

Pour cibler une seule box, utilisez l'entite `notify` specifique :

```yaml
service: notify.send_message
target:
  entity_id: notify.tv_salon
data:
  message: "Seulement sur cette TV"
```

---

## WAF — Wife Acceptance Factor

Ah, le fameux **WAF**. Ce KPI non officiel mais absolument critique qui mesure la tolerance de votre conjoint(e) face a vos projets domotiques. Avec peek-it TV, votre score WAF va exploser. Voici pourquoi.

### Avant peek-it

> **Vous** : "Cheeeeri(e), y'a quelqu'un a la porte !"
> *(en train de consulter frenetiquement votre telephone, Grafana ouvert sur 3 dashboards)*
>
> **Votre moitie** : "...Tu pourrais juste regarder par la fenetre comme tout le monde ?"

### Apres peek-it

La camera du portail s'affiche **directement sur la TV**, en overlay, pendant que Netflix continue en arriere-plan. Votre moitie n'a meme pas eu a bouger du canape.

> **Votre moitie** : "Oh, c'est le livreur ! Pratique ce truc."
>
> *(WAF : +47 points)*

### Les cas d'usage qui font grimper le WAF

**Le lave-linge intelligent** : une notification "Linge termine !" apparait discretement pendant le film. Fini les lessives oubliees qui marinent 3 jours.

> *(WAF : +23 points, -12 points pour le linge oublie la semaine d'avant)*

**La meteo du matin** : chaque jour a 7h30, la meteo s'affiche sur la TV de la cuisine. Votre moitie sait enfin s'il faut un parapluie sans avoir a demander "Dis Google, quel temps fait-il ?".

> *(WAF : +15 points)*

**L'alerte ecole** : "Le bus arrive dans 5 minutes !" s'affiche en overlay. Les enfants sont (presque) a l'heure. Presque.

> *(WAF : +31 points, enfants : -200 points)*

**Le score du match** : votre moitie regarde sa serie, vous attendez le score. Un discret "PSG 2 - 1, 78'" apparait 3 secondes en haut a droite. Tout le monde est content. Personne n'a change de chaine. La paix du foyer est preservee.

> *(WAF : +52 points, neutralite diplomatique atteinte)*

### Le cas d'usage qui fait PLONGER le WAF

**Le debug en prod** : vous testez vos notifications a 23h. "Test 1", "Test 2", "Lorem ipsum", "AAAA CA MARCHE !" s'affichent en boucle sur la TV pendant que votre moitie essaie de regarder un film.

> **Votre moitie** : "Si je vois encore un rectangle noir s'afficher sur MON episode, ta box va dormir au garage."
>
> *(WAF : -347 points. Recuperation estimee : 3 semaines de bon comportement.)*

**Conseil de pro** : testez vos automations AVANT 21h. Ou mieux : utilisez le bouton **KILL** du Designer. Il existe pour une raison.

---

## Depannage

| Probleme | Solution |
|----------|----------|
| Integration introuvable dans HA | Verifiez que le dossier est bien dans `custom_components/peek_it_tv/`. Redemarrez HA. |
| "Impossible de se connecter" a l'ajout | Verifiez l'IP et le port. L'app doit etre lancee sur la TV. Testez `http://IP:8081/api/status` dans un navigateur. |
| Binary sensor toujours "offline" | L'app Android TV est-elle en cours d'execution ? Le service se lance-t-il au boot ? |
| Notification ne s'affiche pas | Verifiez la permission d'overlay dans les parametres Android TV. |
| Le Designer ne se connecte pas | Verifiez que vous etes sur le meme reseau. Essayez `http://IP:PORT/` dans votre navigateur. |
| Templates vides dans l'engrenage | La Box TV doit etre allumee et accessible. Verifiez le statut du binary_sensor. |
| Bouton TV ne declenche rien dans HA | Configurez le token HA dans le Designer (engrenage). Verifiez que `ha_ip` est accessible depuis la TV. |

---

## Captures d'ecran a realiser

Pour illustrer cette documentation, voici les captures recommandees :

1. **App Android TV** — ecran principal avec IP, port et statut du service
2. **Ajout integration HA** — formulaire IP/port/nom
3. **Carte integration** — avec icone engrenage, binary sensor online
4. **Menu engrenage** — les 3 options (Parametres, Templates, Designer)
5. **Liste templates** — affichage avec IDs et params dans l'engrenage
6. **Designer vue d'ensemble** — canvas avec un template en cours d'edition
7. **Designer sidebar** — panneau de proprietes avec un widget selectionne
8. **Designer bibliotheque** — modale de chargement avec les 3 categories
9. **Designer modal settings** — configuration du token HA
10. **Notification simple** — message texte sur la TV (overlay sur Netflix ou autre)
11. **Notification camera** — flux RTSP en overlay
12. **Notification boutons** — template avec boutons interactifs
13. **Automation HA** — exemple dans l'editeur d'automations

---

## Contribuer

Les contributions sont les bienvenues ! Ouvrez une issue ou une pull request sur le [depot GitHub](https://gitlab.com/jolabs40/peek-it).

## Licence

Ce projet est distribue sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de details.
