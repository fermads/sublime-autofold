import sublime, sublime_plugin, re

class AutoFoldListener(sublime_plugin.EventListener):
  settings = False
  active = False
  debug = True

  def log(self, str):
    if self.debug:
      print('[AutoFold] '+ str)


  def activate(self, view):
    self.settings = sublime.load_settings('AutoFold.sublime-settings')
    syntax = view.settings().get('syntax').lower()
    extensions = self.settings.get('extensions')
    file_name = view.file_name()

    if not extensions:
      self.log('AutoFold.sublime-settings extensions missing')
      return False

    # run only for selected file extensions
    for ext in extensions:
      if file_name.endswith(ext):
        self.log('Activated for file '+ file_name)
        return True

  def execute(self, view):
    attrs = self.settings.get('attributes')
    tags = self.settings.get('tags')
    regexps = self.settings.get('regexps')

    if attrs:
      self.fold_attributes(view, attrs)

    if tags:
      self.fold_tags(view, tags)

    if regexps:
      self.fold_regexp(view, regexps)

  def on_load_async(self, view):
    self.active = self.activate(view)

    if self.active and self.settings.get('runOnLoad'):
      self.execute(view)


  def on_pre_save_async(self, view):
    if self.active and self.settings.get('runOnSave'):
      self.execute(view)


  def fold_regexp(self, view, regexps):
    for regexp in regexps:
      result = view.find_all(regexp, sublime.IGNORECASE)
      view.fold(result)


  def fold_tags(self, view, tags):
    for tag in tags:
      result = view.find_all(r'(?<=<' + re.escape(tag) + '>)(.|\n)*?(?=</'
             + re.escape(tag) + '>)', sublime.IGNORECASE)
      view.fold(result)


  def fold_attributes(self, view, attrs):
    for attr in attrs:
      result = view.find_all(r'(?<=' + re.escape(attr)
             + '=").*?(?=")', sublime.IGNORECASE)
      view.fold(result)
