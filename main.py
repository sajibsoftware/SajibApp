from kivy.app import App
from kivy.uix.label import Label

class SajibApp(App):
    def build(self):
        return Label(text="Welcome to SajibApp")

SajibApp().run()
