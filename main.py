from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivy.utils import platform

# Rangi za Serikali ya Tanzania
Window.clearcolor = (0, 0.36, 0.58, 1) # Blue ya bendera

class ElimuYetApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        # Screen kuu
        screen = MDScreen()
        
        # Layout kuu
        layout = MDBoxLayout(orientation='vertical', spacing=20, padding=40)
        
        # Kichwa
        title = MDLabel(
            text="ELIMU YETU",
            halign="center",
            font_style="H3",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            bold=True
        )
        
        # Card ya maelezo
        card = MDCard(
            orientation="vertical",
            padding=20,
            spacing=10,
            size_hint=(1, None),
            height="200dp",
            md_bg_color=(1, 1, 1, 1),
            radius=[20,]
        )
        
        maelezo = MDLabel(
            text="Karibu kwenye App ya Elimu Yetu\n\nTovuti rasmi ya masomo kwa wanafunzi wa Tanzania",
            halign="center",
            theme_text_color="Primary",
            font_style="Body1"
        )
        
        # Button ya kuanza
        btn = MDRaisedButton(
            text="ANZA KUSOMA",
            size_hint=(1, None),
            height="50dp",
            md_bg_color=(0, 0.6, 0.2, 1), # Green ya bendera**SAWA MKUU 🙏 PUMUA KWANZA**

**Tumemaliza mateso. Hizi ndio code safi kabisa za mwisho. Copy-paste tu.**

---

### **1. `buildozer.spec` - HII NDIYO SAHIHI**

```ini
[app]
title = ElimuYetApp
package.name = elimuyetapp
package.domain = org.elimuyet
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,pillow,plyer,android
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.accept_sdk_license = True
