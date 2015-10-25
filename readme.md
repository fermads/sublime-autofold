# Sublime Auto Fold

### Sublime Text 3 plugin for automatically folding tags, attributes and strings matching regexp patterns

Instead of having long urls cluttering your view like this:
![unfolded](https://raw.githubusercontent.com/fermads/sublime-autofold/master/img/unfolded.png)

Have urls automatically folded when opening or saving files:
![folded](https://raw.githubusercontent.com/fermads/sublime-autofold/master/img/folded.png)

## Install

If using [Package Control](https://packagecontrol.io/)
for [Sublime Text](http://sublimetext.com/3), simply install the Auto Fold package.

Alternatively, clone the repo directly into Sublime Packages folder.

**Windows:**

```bash
  cd "%APPDATA%\Sublime Text 3\Data\Packages"
  git clone --depth 1 https://github.com/fermads/sublime-autofold.git AutoFold
```

**Mac:**

```bash
  cd ~/"Library/Application Support/Sublime Text 3/Data/Packages"
  git clone --depth 1 https://github.com/fermads/sublime-autofold.git AutoFold
```

`--depth` 1 downloads only the current version to reduce the clone size.

*It's the `/Data/Packages` and not `/Packages` folder.

## Usage
Open any HTML file with tags containing attributes `href` or `src`.
These attributes values will be folded. Saving the file will also fold them.

## Settings
Default settings will fold `src` and `href` attributes from HTML and
will fold Markdown urls matching `(http.*?)`.

Settings file is `AutoFold.sublime-settings`

```js
{
  "attributes" : [ // attributes to auto fold
    "href",
    "src"
  ],

  "tags": [ // tags auto fold
    "h1"
  ],

  "regexps": [ // regexps to auto fold
    "(?<=\\()http.*?(?=\\))" // fold markdown urls "(http://..)"
  ],

  "extensions": [  // activate this plugin for extensions:
    "html",
    "xml",
    "md"
  ],

  "runOnLoad": true, // auto fold on load
  "runOnSave": true // auto fold on save
}
```

