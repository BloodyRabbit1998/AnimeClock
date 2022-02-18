from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.picker import MDTimePicker
Builder.load_file('main.kv')

class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    def remove_item(self, instance):
        self.screen.ids.md_list.remove_widget(instance)
class MainScreen(MDScreen):
    pass

class TimeScreen(MDScreen):
    def remove_item(self, instance):
        self.screen.ids.list_time.remove_widget(instance)
    def get_time(self,instance,time):
        print(time)
    def save(self,instance,time):
        from datetime import datetime
        self.ids.list_time.add_widget(SwipeToDeleteItem(text=str(time)))
    def add_alarm(self):		
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.save,time=self.get_time)
        time_dialog.open()

class AlarmApp(MDApp):
    def __init__(self, **kwargs):
        super(AlarmApp, self).__init__(**kwargs)
    def build(self):
        return MainScreen()


def main():
    AlarmApp().run()


if __name__ == '__main__':
    main()