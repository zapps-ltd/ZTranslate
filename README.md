# ZTranslate

ZTranslate is a portable Windows tool that translates the text you select or focus in any program, speaks the translation aloud and can copy it to the clipboard. It is driven by global hotkeys, has no main window, and speaks through the Windows speech engine (SAPI) directly, so it works the same with NVDA, JAWS, Narrator or no screen reader at all. It is written in Python with wxPython.

Version 0.1.1. By the zapps.ltd developers, Harith and Mesar.

## Why it exists

Screen readers and browsers each have their own way of reading and translating text, and many programs expose no usable text selection. ZTranslate gives every Windows user one hotkey that works in any program: select text, press the hotkey, hear the translation. It was built with screen-reader users first in mind, with sighted users given equal priority, and it can run entirely offline if you use a local translation server.

## Features

Getting the text
- Translates the text currently selected in the focused program, read through Windows UI Automation.
- If no selection is found through UI Automation, it translates the text that is on the clipboard. This is the "select, copy, then translate" way that works in web browsers.
- If that finds nothing, it translates the short text (up to 500 characters) of the focused edit field, such as a search box.
- As a last step it sends a Ctrl+C to the active program and uses what was copied.
- Text that is only a web address (starting with http:// or https://) is not translated; you are told so.
- It does not re-translate its own previous clipboard output.
- A repeated press within a short moment is ignored.

Translation engines
- Local Offline: a LibreTranslate-compatible server, by default at http://127.0.0.1:5000/translate (the address can be changed). The server is not included.
- Google Translate (no key needed).
- DeepL (API key; free and paid keys are both recognised).
- Bing Translate, the Microsoft Azure Translator service (API key, optional region).
- OpenAI (API key).
- Google Gemini (API key).
- OpenRouter (API key).
- Custom APIs, as many as you like: either an OpenAI-compatible chat endpoint or a LibreTranslate-compatible endpoint, each with its own name, address and optional key.
- The default engine is Local Offline. Nothing is sent over the internet unless you choose another engine or point a custom API at an internet address.
- If an engine fails, you hear a short message. A failed result is never remembered, so a later try with another engine is not blocked.

Languages
- The target language is set by its code (for example en, es, fr) in Settings.
- The source language is found automatically by the engine. Locally, ZTranslate recognises Arabic, Russian, Chinese, Japanese, Korean, Hebrew, Thai and Hindi by their writing system.
- Exclusion list: a list of 37 languages that you can tick so they are never translated even when detected. Because detection works by writing system, this only separates the scripts above; it cannot tell Latin-script languages (French, Spanish and so on) apart.
- If the result equals the original, you hear "Already in target language."
- Swap: temporarily set the target to the language of the last translated text, for a quick reverse translation. Revert returns to your default. Saving settings also resets the swap.

Speech
- Translations are spoken through SAPI, with any installed SAPI voice (for example Microsoft voices or third-party voices).
- Voice, rate (-10 to 10) and volume (0 to 100) are set in Settings.
- Status messages ("No text found", "Translation failed" and so on) can use the same voice or their own voice and rate.
- A stop-speech hotkey silences speech at once, which is useful for long texts.

Clipboard
- Optional copying of the result to the clipboard, either the translation only or the original followed by the translation.

Cache
- Translations are remembered in memory per source program, so repeating a translation is instant and does not contact the engine again.
- One press of the clear-cache hotkey clears the cache of the current program; two quick presses clear it for all programs. The cache is never written to disk and is gone when the program closes.

Hotkeys (all can be changed or disabled in Settings; changes apply when you save, with no restart)
- Translate: Shift+Win+F1
- Swap target language: Shift+Win+F2
- Revert target language: Shift+Win+F3
- Clear cache: Shift+Win+F5
- Open settings: Shift+Win+F6
- Stop speech: Pause
- Settings warn you at once if two actions share the same hotkey. If Windows or another program already uses a hotkey, ZTranslate cannot register it; choose another in Settings.

Settings, tray and first run
- Settings dialog with tabs: Engine, Voice, Clipboard, Exclusions and Hotkeys, plus an About button.
- A system tray icon is always shown. Its menu has Open Settings, Revert target language to default, About ZTranslate and Quit. A double click on the icon opens Settings.
- On first run a welcome dialog offers to create a desktop shortcut, then opens Settings.
- The About page opens in your default browser. It loads nothing from the internet.
- A short debug log is written on each run (see Privacy).

## Accessibility

- It speaks through SAPI itself and does not depend on any screen reader, so it works with NVDA, JAWS, Narrator or none.
- All settings are standard Windows controls (tabs, edit fields, lists, check boxes, buttons) with keyboard shortcuts on the labels, built with wxPython.
- Everything can be done from the keyboard. There is no main window to find; use the hotkeys or the tray icon.
- API key fields are masked.
- Error and status messages are spoken, not only shown.
- The About page is a plain web page that follows the system light or dark setting and the high-contrast mode.
- Limitation: Windows has no way to read back what a screen reader last said, so ZTranslate translates selected, copied or focused text, not the screen reader's last spoken phrase.
- Limitation: a program running as administrator may ignore the simulated Ctrl+C from a normal ZTranslate. Copy the text yourself first and press the translate hotkey.

## Privacy

- ZTranslate has no account, no analytics, no advertising and no update check.
- Text is sent only when you press the translate hotkey, and only to the engine you chose in Settings:
  - Local Offline: to the server address you set (by default on your own PC, 127.0.0.1). Nothing leaves the PC unless you point it to another machine.
  - Google Translate: the text, the target language and the source language go to translate.googleapis.com.
  - DeepL: the text and target language, with your key, go to api.deepl.com or api-free.deepl.com.
  - Bing Translate: the text and target language, with your key, go to api.cognitive.microsofttranslator.com.
  - OpenAI: the text and an instruction to translate, with your key, go to api.openai.com.
  - Google Gemini: the same, with your key, to generativelanguage.googleapis.com.
  - OpenRouter: the same, with your key, to openrouter.ai.
  - A custom API: to the address you entered.
- Those services have their own terms and privacy policies. ZTranslate does not control what they do with your text. Choose the Local Offline engine if the text must not leave your PC.
- Because the clipboard is one of the sources of text, whatever text is on the clipboard when you press the translate hotkey may be translated, and so sent to your chosen engine.
- Settings, including API keys, are stored as plain text in the file config.json in the ZTranslate folder inside your Windows application data folder (%AppData%). Anyone with access to your account can read it.
- A debug log named debug.log in the same folder records what ZTranslate does, including the text it reads and the translation. It stays on your PC, is emptied each time the program starts, and is never sent anywhere. Delete it whenever you wish.
- The About page is written to the same folder and is opened in your browser. It makes no network requests; its links open only if you click them.

## Requirements

- Windows 10 or Windows 11.
- At least one speech voice installed (Windows includes some).
- For offline translation, a LibreTranslate server that you run yourself. For online engines, an internet connection and, for most, your own API key.
- To run from source: Python 3.14 (the version the project is built and tested with) and the packages wxPython, pywin32 and comtypes.

## Running ZTranslate

Running a build
- Download the release, unpack it and start ZTranslate.exe in the ZTranslate folder. The folder is portable; no installer is needed. You can keep it anywhere, including a USB drive. Settings stay in your application data folder, so moving the folder does not lose them.

Running from source
- Install Python, then the packages: pip install wxPython pywin32 comtypes
- In the project folder run: python run.py

## Folder layout

- run.py: the start-up file.
- ztranslate/: the program.
  - main.py: start-up, hotkeys and the translate action.
  - engines.py: the translation engines and custom APIs.
  - ui_automation.py: reading selected, copied or focused text.
  - speech.py: SAPI speech.
  - settings_dialog.py: the Settings dialog.
  - hotkeys.py: hotkey parsing and conflict checks.
  - config.py: loading and saving settings.
  - cache.py: the in-memory translation cache.
  - lang_detect.py: script-based language detection.
  - tray_icon.py: the tray icon and menu.
  - first_run_dialog.py: the welcome dialog.
  - about_page.py: the About page.
  - debug_log.py: the debug log.
- LICENSE: the license text.
- THIRD_PARTY_NOTICES.md: components used and their licenses.

## Interface languages

The interface of ZTranslate is in English only for now.

## Reporting problems and contact

- Please report bugs and ideas by email to support@zapps.ltd or through the contact page of https://zapps.ltd. Pull requests are not accepted.
- When you report a bug, say which program the text came from, which engine you used and what you heard.

## License

ZTranslate is free software, licensed under the GNU Affero General Public License, version 3 or (at your option) any later version (AGPL-3.0-or-later). The full text is in the file LICENSE. In short: you may use, study, change and share it, but every copy and every modified version, including one that other people use over a network, must stay under the same license, must come with its complete source code, and must keep the copyright notices and the credits below. Nobody can make a closed version of it. Copyright (C) 2026 ZAPPS SOFTWARE LTD.

## Third-party software and credits

ZTranslate is built using the software below. The full list, with licenses and the notices that must accompany copies, is in THIRD_PARTY_NOTICES.md.

- Python (Python Software Foundation License) and its standard library.
- wxPython and wxWidgets (wxWindows Library Licence).
- pywin32 by Mark Hammond and others (PSF license in its metadata, BSD-style license files).
- comtypes by Thomas Heller and the comtypes developers (MIT License).
- PyInstaller (GPL-2.0-or-later with a special exception), used to build the portable program.
- Translation services you may choose to use, under their own terms and not bundled: LibreTranslate, Google Translate, DeepL, Microsoft Translator, OpenAI, Google Gemini and OpenRouter.

Copyright (C) 2026 ZAPPS SOFTWARE LTD. Made by the zapps.ltd developers, Harith and Mesar.
