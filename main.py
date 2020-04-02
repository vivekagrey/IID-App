#nano ~/.kivy/config.ini
from kivy.uix.textinput import TextInput
from kivy.uix.actionbar import ActionItem, ActionView, ActionBar
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from  kivy.lang import Builder
from kivy.uix.settings import SettingsWithSidebar

from settingsjson import settings_json
"""class SearchBar(TextInput, ActionItem):
    def __init__(self, *args, **kwargs):
        super(SearchBar, self).__init__(*args, **kwargs)
        self.hint_text='Search'
        self.size_hint = [1 , .6]
        self.pos_hint={'x': 0, 'center_y':.5}
        self.multiline = False
    def search(self):
        request = self.text
        print(request)
        return str(request)"""
class DroneNewsScreen(Screen):
    pass
class DroneCinemaScreen(Screen):
    pass
class MappingDronesScreen(Screen):
    pass
class AgricultureDronesScreen(Screen):
    pass
class DefenceDronesScreen(Screen):
    pass
class KnowBeforeYouFlyScreen(Screen):
    pass
class DroneGlossaryScreen(Screen):
    pass
class DGCAScreen(Screen):
    pass
class IIDPilotListScreen(Screen):
    pass
class Buttonmain(Button):
    pass
class MyScreenManager(ScreenManager):
    pass
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class DronePilotTrainingScreen(Screen):
    pass
class WeatherScreen(Screen):
    pass
class DroneInsuranceScreen(Screen):
    pass
class OnlineTestScreen(Screen):
    pass
class FlyZonesScreen(Screen):
    pass
class DroneServiceCentreScreen(Screen):
    pass
class DroneStoreScreen(Screen):
    pass
class MoreScreen(Screen):
    pass
class TermsAndConditionsScreen(Screen):
    pass
class AboutUsScreen(Screen):
    pass
class FAQsScreen(Screen):
    pass
class ActionBar1(Screen):
    pass
class ActionBar2(Screen):
    pass
root_widget = Builder.load_file("myiidd.kv")
class MyIIDApp(App):
    def build(self):
        self.use_kivy_settings = False
        self.settings_cls = SettingsWithSidebar
        setting = self.config.get('example', 'boolexample')
        App.destroy_settings(self)
        return root_widget

    def build_config(self, config):
        config.setdefaults('example', {
            'boolexample': True,
            'numericexample': 10,
            'optionsexample': 'option2',
            'stringexample': 'some_string',
            'pathexample': '../iidapp/settingsjson.py'})

    def build_settings(self, settings):
        settings.add_json_panel('Panel Name',self.config,data=settings_json)

    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)
if __name__ == '__main__':
    MyIIDApp().run()
