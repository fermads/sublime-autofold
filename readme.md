# Sublime Auto Fold

### Sublime Text 3 plugin for automatically folding tags, attributes or any configurable string matching a regular expression

Plugin default settings will:

* fold `rel`, `content` and `type` attributes from HTML files
* fold `<head>` from HTML files
* fold all absolute urls leaving the last path part

Instead of having long urls cluttering your view like this:<br/>
![unfolded](https://raw.githubusercontent.com/fermads/sublime-autofold/master/img/unfolded.png)

Have urls automatically folded when opening or saving files:<br/>
![folded](https://raw.githubusercontent.com/fermads/sublime-autofold/master/img/folded.png)

Or add your own tags, attributes and regular expressions to auto fold.
To change the default settings copy the
[settings file](AutoFold.sublime-settings)
to `[Sublime path]/Data/Packages/User/AutoFold.sublime-settings`
and change it.

## Install

Using [Package Control](https://packagecontrol.io/)
for [Sublime Text](http://sublimetext.com/3), simply install the
`Auto Fold` package.

`ctrl+shift+p` (Win, Linux) or `cmd+shift+p` (OS X) > type/choose: `Install Package` > type/choose: `auto fold`

## Usage

Example 1: open any HTML file with tags containing attributes `rel`, `content`
or `src`. These attribute values will be folded.
Saving the file will also fold them.

Example 2: open any HTML, CSS or Markdown file with absolute urls.
These urls will be folded on open and on save.

