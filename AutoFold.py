import sublime, sublime_plugin, re

class AutoFoldListener(sublime_plugin.EventListener):
  s = False

  def loadSettings(self):
    print("loading settings")
    self.s = sublime.load_settings("AutoFold.sublime-settings")

  def on_pre_save_async(self, view):
    if not self.s:
      self.loadSettings()

    attrs = self.s.get('foldAttributes')
    tags = self.s.get('foldTags')

    if attrs:
      self.fold_attributes(view, attrs)

    if tags:
      self.fold_tags(view, tags)

    print("OK, saved")

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


  # def on_post_save_async(self, view):
  #   if not self.s:
  #     self.loadSettings()
  #   if self.s.get('attributes'):
  #     print(self.s.get('attributes')[0])
      # view.run_command('git_annotate')


  # def run(self, edit):
  #   # (https?|file|mailto)://(?:[^\s]+)+
  #   result = self.view.find_all(r"(?<=\").*?(?=\")",sublime.IGNORECASE)
  #   self.view.fold(result)
  #   print(result)
  #   # self.view.insert(edit, 0, "Hello, World!")
