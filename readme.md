# Sublime AutoFold

### Sublime Text 3 plugin for auto-folding tags and attributes from HTML, XML and other markup language files

Instead of having long URLs in one line like this:
![unfolded](https://raw.githubusercontent.com/fermads/sublime-autofold/master/img/unfolded.png)

You'll have them automatically folded when you save your files:
![folded](https://raw.githubusercontent.com/fermads/sublime-autofold/master/img/folded.png)

## Install

If using [Package Control](https://packagecontrol.io/) for [Sublime Text](sublimetext.com/3), simply install the AutoFold package.

Alternatively, you can clone the repo directly into your Sublime plugin folder.

**Mac:**

```bash
  cd ~/"Library/Application Support/Sublime Text 3/Packages"
  git clone --depth 1 https://github.com/fermads/sublime-autofold.git AutoFold
```

**Windows:**

```bash
  cd "%APPDATA%\Sublime Text 3\Packages"
  git clone --depth 1 https://github.com/fermads/sublime-autofold.git AutoFold
```
`--depth` 1 downloads only the current version to reduce the clone size.

## Usage

Open a markup file (like HTML) with tags containing attributes href or src.

Example:
```html
<html>
<head>
  <link rel="shortcut icon" href="http://url" />
  <script src="//url"></script>
</head>
<body>
  <img src="https://url" />
  <a href="url.html">link</a>
</body>
</html>
```

Save the file. All urls will be folded.

## Config

Default configuration:
```js
{
  "attributes" : [ // attributes to auto-fold
    "href",
    "src"
  ],

  "tags": [ // tags to auto-fold
  ],

  "unfoldCurrentLine": true // auto-unfold tags and attributes on current line
}
```

