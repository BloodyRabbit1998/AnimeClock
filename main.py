from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty,ObjectProperty
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.picker import MDTimePicker
from kivymd_extensions.akivymd.uix.bottomappbar import AKFloatingRoundedAppbar, AKFloatingRoundedAppbarButtonItem

Builder.load_file('main.kv')

class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    on_delete=ObjectProperty()
    def remove_item(self, instance):
        self.screen.ids.md_list.remove_widget(instance)
class MainScreen(MDScreen):
    pass

class TimeScreen(MDScreen):
    def remove_item(self, instance):
        print("delete")
        self.ids.list_time.remove_widget(instance)
    def save(self,instance,time):
        
        from datetime import datetime
        self.ids.list_time.add_widget(SwipeToDeleteItem(text=str(time),on_delete=lambda x:self.remove_item()))
    def add_alarm(self):		
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.save)
        time_dialog.open()

class AlarmApp(MDApp):

    def remove_item(self, instance):
        print("delete")
        self.mainScreen.ids.list_time.remove_widget(instance)
    def __init__(self, **kwargs):
        super(AlarmApp, self).__init__(**kwargs)
    def build(self):
        self.mainScreen=MainScreen()
        return self.mainScreen


def main():
    AlarmApp().run()


if __name__ == '__main__':
    main()