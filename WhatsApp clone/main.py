from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase
from kivymd.theming import ThemeManager
from kivymd.uix.menu import MDDropdownMenu

from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder

class Tab(FloatLayout, MDTabsBase):
	pass

class MainApp(MDApp):

	def build(self):
		self.theme_cls.primary_palette = 'Teal'
		self.theme_cls.primary_hue = '800'
		return Builder.load_file('main.kv')

	def demo(self):
		print(self.screen.ids.toolbar.right_action_items[1])

	def change_screen(self, screen_name, curr = None, title = None):
		self.root.ids.screen_manager.current = screen_name
		if curr is not None:
			self.root.ids.screen_manager.transition.direction = 'right'
		else:
			self.root.ids.screen_manager.transition.direction = 'left'
		if title is not None:
			self.set_title(title)

	def set_title(self, title):
		self.root.ids.toolbar_chat_screen.title = title

if __name__ == '__main__':
	MainApp().run()