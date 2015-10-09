import sublime, sublime_plugin, re

class AutoFoldListener(sublime_plugin.EventListener):
  settings = False

  def load_settings(self):
    self.settings = sublime.load_settings("AutoFold.sublime-settings")
    if not self.settings:
      print "AutoFold.sublime-settings file is required"

  def on_pre_save_async(self, view):
    if not self.settings:
      self.load_settings()

    attrs = self.settings.get('attributes')
    tags = self.settings.get('tags')

    if attrs:
      self.fold_attributes(view, attrs)

    if tags:
      self.fold_tags(view, tags)

  def fold_tags(self, view, tags):
    for tag in tags:
      result = view.find_all(r"(?<=<" + re.escape(tag) + ">).*?(?=</"
             + re.escape(tag) + ">)", sublime.IGNORECASE)
      view.fold(result)

  def fold_attributes(self, view, attrs):
    for attr in attrs:
      result = view.find_all(r"(?<=" + re.escape(attr)
             + "=\").*?(?=\")", sublime.IGNORECASE)
      view.fold(result)
