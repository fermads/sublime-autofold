# Sublime Auto Fold

### Sublime Text 3 plugin for automatically folding tags, attributes or any configurable string matching a regular expression

Plugin default settings will:

* fold `src` and `href` attributes from HTML and XML files
* fold all `url(*)` from CSS files, including base64 data
* fold all `urls (http*)` from Markdown files (.md and .mkd extensions)

Instead of having long urls cluttering your view like this:<br/>
![unfolded](https://raw.githubusercontent.com/fermads/sublime-autofold/master/img/unfolded.png)

Have urls automatically folded when opening or saving files:<br/>
![folded](https://raw.githubusercontent.com/fermads/sublime-autofold/master/img/folded.png)

Or add your own tags, attributes and regular expressions to auto fold changing
the `[settings file]/Data/Packages/User/AutoFold.sublime-settings`

## Install

Using [Package Control](https://packagecontrol.io/)
for [Sublime Text](http://sublimetext.com/3), simply install the
`Auto Fold` package.

`ctrl+shift+p` (Win, Linux) or `cmd+shift+p` (OS X) > type/choose: `Install Package` > type/choose: `auto fold`

## Usage

Example 1: open any HTML file with tags containing attributes `href` or `src`.
These attribute values will be folded. Saving the file will also fold them.

Example 2: open any CSS file with a url(...) as a value of a property.
These urls will be folded on open and on save.

## Settings

To change the default settings copy the
[settings file](AutoFold.sublime-settings)
to `[your Sublime path]/Data/Packages/User/AutoFold.sublime-settings`
and change it.
