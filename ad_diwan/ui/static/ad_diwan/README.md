# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd ad_diwan/ad_diwan/static/ui
```

To generate the styles:

```console
npm install
cd ad_diwan/ui/static/ad_diwan
npx @tailwindcss/cli -i ../static/ad_diwan/css/app.css -o ../static/ad_diwan/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
