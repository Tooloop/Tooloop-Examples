# Bundle structure

ZIP file containing:

`APP_NAME-VERSION.zip`

```
./
|- app.definition
|- preview_image.jpg (320 × 180 px)
|- README.md
|- LICENSE.md
|
+- scripts/
|   |- install.sh
|   |- uninstall.sh
|
+- presentation/
|   |- start-presentation.sh
|   |- stop-presentation.sh
|   |- ...
|
+- data/ (optional)
|   |- ...
|
+- settings/ (optional)
    |- controller.py
    |- settings_panel.html
    |- dashboard_widget.html
```

# App info file

`app.definition`

```
{
  "name": "Awesome Super Trooper",
  "description": "256 characters short description",
  "media": [
    {
      "type": "video",
      "url": "https://youtu.be/GynFoGzOWds",
      "description": "Description of video 1"
    }, {
      "type": "image",
      "url": "https://www.cool-dude.com/awesome-super-trooper/img/app-preview-1.jpg",
      "description": "Description of image 1"
    }, {
      "type": "image",
      "url": "https://www.cool-dude.com/awesome-super-trooper/img/app-preview-2.jpg",
      "description": "Description of image 2"
    }, {
      "type": "video",
      "url": "https://vimeo.com/6912147",
      "description": "Description of video 2"
    }
  ],
  "version": "1.0",
  "last_updated": "2017-01-22",
  "license": "Commercial",
  "category": "Tools",
  "tags": ["examples"],
  "developer": "Cool dude",
  "support_url": "http://www.cool-dude.com/awesome-super-trooper/",
  "compatibility": {
    "s": "False",
    "m": "True",
    "l": "True"
    "xl": "True"
  }
}
```
