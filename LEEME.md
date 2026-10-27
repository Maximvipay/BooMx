# Repodrusca -> APK (Capacitor)

Requisitos: Node.js 18+, Android Studio (con SDK) y Java 17.

## Pasos
1. En esta carpeta:  `npm install`
2. `npm run setup`   (crea la carpeta android, parchea permisos y sincroniza)
3. `npm run open`    (abre Android Studio)
4. En Android Studio: Build > Build Bundle(s) / APK(s) > Build APK(s)
   El APK queda en android/app/build/outputs/apk/debug/

## Si cambias index.html o el MP3
Edítalos en `www/` y corre `npm run sync`.

## Notas
- Android 13+ pide permiso de notificaciones; el servicio en primer plano muestra una notificación fija mientras suena.
- Algunas marcas (Xiaomi, Huawei, Samsung) matan apps en segundo plano: en el teléfono, desactiva la optimización de batería para la app.
- Verifica nombres de clases del servicio en el README del plugin si la versión cambia.

## Compilar con GitHub (sin computadora)
1. Sube TODO el contenido de esta carpeta a un repositorio nuevo (incluida .github/workflows/build.yml, www/, package.json, capacitor.config.json y patch_manifest.py).
2. En el repo: pestaña Actions > "Build APK" > Run workflow.
3. Al terminar (5-10 min), entra a la ejecución y descarga "Repodrusca-APK" en Artifacts.
