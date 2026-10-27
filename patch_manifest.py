# Agrega permisos y servicio al AndroidManifest.xml generado por Capacitor
p = "android/app/src/main/AndroidManifest.xml"
s = open(p, encoding="utf-8").read()

perms = """    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
"""
service = """        <service
            android:name="io.capawesome.capacitorjs.plugins.foregroundservice.AndroidForegroundService"
            android:foregroundServiceType="mediaPlayback" />
        <receiver android:name="io.capawesome.capacitorjs.plugins.foregroundservice.NotificationActionBroadcastReceiver" />
"""
if "FOREGROUND_SERVICE_MEDIA_PLAYBACK" not in s:
    s = s.replace("</manifest>", perms + "</manifest>")
if "AndroidForegroundService" not in s:
    s = s.replace("</application>", service + "    </application>")
open(p, "w", encoding="utf-8").write(s)
print("Manifest actualizado")
