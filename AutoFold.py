import sublime, sublime_plugin, re

class AutoFoldListener(sublime_plugin.EventListener):
  settings = False
  active = False
  debug = True

  def log(self, str):
    if self.debug:
      print("[AutoFold] "+ str)


  def activate(self, view):
    self.settings = sublime.load_settings("AutoFold.sublime-settings")
    syntax = view.settings().get("syntax").lower()
    files = self.settings.get('files')

    if not files:
      self.log("AutoFold.sublime-settings file missing")
      return False

    # run only on specific files
    for type in files:
      if type in syntax:
        self.log("Activated for file type "+ type + " syntax "+ syntax)
        return True

    self.log("Not activated for syntax "+ syntax)


  def execute(self, view):
    attrs = self.settings.get('attributes')
    tags = self.settings.get('tags')

    if attrs:
      self.fold_attributes(view, attrs)

    if tags:
      self.fold_tags(view, tags)


  def on_load(self, view):
    self.active = self.activate(view)

    if self.active and self.settings.get('runOnLoad'):
      self.execute(view)


  def on_pre_save_async(self, view):
    if self.active and self.settings.get('runOnSave'):
      self.execute(view)


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
