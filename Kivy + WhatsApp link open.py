from kivy.app import App
from kivy.uix.button import Button
import webbrowser

class MyApp(App):
    def build(self):
        return Button(
            text="Test Button",
            on_press=self.send_message,
        )

    def send_message(self, instance):
        phone_number = "replace this area with your friends phone number "
        message = "Hello from my bot!"
        url = f"https://wa.me/{phone_number}?text={message.replace(' ', '%20')}"
        webbrowser.open(url)

if __name__ == "__main__":
    MyApp().run()
