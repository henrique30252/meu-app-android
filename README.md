# Aplicativo Android em Python - Teste APK

Este projeto demonstra como criar um aplicativo Android simples usando Python e Kivy, e como convertê-lo em um arquivo APK.

## Arquivos do Projeto

- `main.py`: Código principal do aplicativo
- `buildozer.spec`: Arquivo de configuração para gerar o APK
- `requirements.txt`: Lista de dependências Python

## Funcionalidades do App

O aplicativo possui:
- Um título
- Campo de entrada de texto
- Botão interativo
- Área para exibir resultados

## Como Testar Localmente

Execute o aplicativo no seu computador:

```bash
python main.py
```

## Como Gerar o APK

### Opção 1: Usando Buildozer (Linux/macOS/WSL)

**IMPORTANTE**: Buildozer funciona melhor em sistemas Linux. No Windows, recomenda-se usar WSL (Windows Subsystem for Linux).

```bash
# Instalar buildozer
pip install buildozer

# Inicializar (primeira vez)
buildozer android debug

# Para builds subsequentes
buildozer android debug
```

O APK será gerado na pasta `bin/`.

### Opção 2: Usando GitHub Actions (Recomendado para Windows)

1. Suba seu código para um repositório GitHub
2. Configure GitHub Actions com workflow para Android build
3. O APK será gerado automaticamente

### Opção 3: Usando Replit ou Google Colab

1. Faça upload dos arquivos para Replit/Colab
2. Execute o processo de build na nuvem

### Opção 4: Usando BeeWare (Alternativa)

BeeWare é outra opção para criar apps móveis em Python:

```bash
pip install briefcase
briefcase new
```

## Dependências Necessárias para Build

Para gerar APK localmente, você precisa:

1. **Java Development Kit (JDK)**
2. **Android SDK**
3. **Android NDK**
4. **Python 3.x**
5. **Cython**

## Limitações no Windows

- Buildozer não funciona nativamente no Windows
- Use WSL, Docker, ou serviços de build na nuvem
- Considere usar BeeWare como alternativa

## Próximos Passos

1. Teste o app localmente com `python main.py`
2. Configure um ambiente Linux (WSL/VM/Cloud)
3. Use Buildozer para gerar o APK
4. Instale o APK no dispositivo Android

## Debugging

Se encontrar problemas:
- Verifique se todas as dependências estão instaladas
- Use `buildozer android debug -v` para output detalhado
- Consulte logs na pasta `.buildozer/`

## Estrutura Final do APK

O APK final será:
- Nome: Meu App Teste
- Pacote: org.henrique.meuappteste
- Versão: 0.1
- API mínima: Android 5.0 (API 21)
