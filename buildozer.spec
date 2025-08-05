[app]

# (str) Título da aplicação
title = Meu App Teste

# (str) Nome do pacote
package.name = meuappteste

# (str) Domínio do pacote (necessário para Android/iOS)
package.domain = org.henrique.meuappteste

# (str) Diretório fonte da aplicação (onde estão os arquivos)
source.dir = .

# (str) Arquivo fonte da aplicação (incluindo extensão)
source.main = main.py

# (list) Diretórios para incluir
source.include_exts = py,png,jpg,kv,atlas

# (str) Versão da aplicação
version = 0.1

# (list) Dependências da aplicação
# Separadas por vírgulas
requirements = python3,kivy

# (str) Icon da aplicação
#icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash da aplicação
#presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]

# (int) Log level (0 = errors only, 1 = info, 2 = debug - com mais verbose output)
log_level = 2

# (int) Exibe warnings usando o logger padrão do Python
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

[android]

# (list) Permissões
android.permissions = INTERNET

# (int) Target Android API
android.api = 31

# (int) Minimum API que o app irá rodar
android.minapi = 21

# (str) NDK version to use
android.ndk = 25b

# (str) SDK directory
#android.sdk_path = 

# (str) NDK directory
#android.ndk_path = 

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Orientação da tela (landscape, sensorLandscape, portrait, sensorPortrait, all)
orientation = portrait

# (bool) Debug ou release APK
android.debug = True
