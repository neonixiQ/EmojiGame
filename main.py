from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class EmojiApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Emoji", halign="center")


EmojiApp().run()