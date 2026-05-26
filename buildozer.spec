[app]
title = ElimuYetApp
package.name = elimuyetapp
package.domain = org.elimuyet
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,plyer,android
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 34
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = True
android.sdk = 34
android.build_tools = 34.0.0
