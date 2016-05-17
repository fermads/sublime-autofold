# Sublime Auto Fold

### Sublime Text 3 plugin for automatically folding tags, attributes or any configurable string matching a regular expression

Instead of having long urls cluttering your view like this:<br/>
![unfolded](https://raw.githubusercontent.com/fermads/sublime-autofold/master/img/unfolded.png)

Have urls automatically folded when opening or saving files:<br/>
![folded](https://raw.githubusercontent.com/fermads/sublime-autofold/master/img/folded.png)

Or add your own tags, attributes and regular expressions to auto fold.

Defaults are:
* fold `src` and `href` attributes from HTML and XML files
* fold all `url(*)` from CSS files, including base64 data
* fold all `urls (http*)` from Markdown files (.md and .mkd extensions)

## Install

If using [Package Control](https://packagecontrol.io/)
for [Sublime Text](http://sublimetext.com/3), simply install the
`Auto Fold` package.

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
Example: open any HTML file with tags containing attributes `href` or `src`.
These attribute values will be folded. Saving the file will also fold them.

## Settings
To change the default settings copy the
[settings file](AutoFold.sublime-settings)
to `[your Sublime path]/Data/Packages/User/AutoFold.sublime-settings`
and change it.
