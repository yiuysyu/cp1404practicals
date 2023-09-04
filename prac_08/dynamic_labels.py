from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Construct the main app."""
        super().__init__(**kwargs)
        # List names
        self.names = ["Amy", "Ella", "Elsie", "Bob", "William"]

    def build(self):
        """Build the GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
