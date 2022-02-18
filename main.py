from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen

Builder.load_file('main.kv')

class MainScreen(MDScreen):
    pass

class TimeScreen(MDScreen):
    pass

class AlarmApp(MDApp):
    def __init__(self, **kwargs):
        super(AlarmApp, self).__init__(**kwargs)
    def build(self):
        return MainScreen()


def main():
    AlarmApp().run()


if __name__ == '__main__':
    main()