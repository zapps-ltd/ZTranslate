# Third-party notices

ZTranslate is licensed under AGPL-3.0-or-later (see LICENSE). Copyright (C) 2026 ZAPPS SOFTWARE LTD.

The portable ZTranslate.exe is built with PyInstaller. It contains the Python runtime, the Python standard library, wxPython (with wxWidgets), pywin32 and comtypes. The online services in the second part are not bundled; ZTranslate only contacts them when you select them.

## Components shipped in or used to build the program

1. Python
   - Author: Python Software Foundation and contributors.
   - Use: the language runtime and standard library (Python 3.14), bundled in the exe. It also carries small third-party libraries of its own (for example zlib, expat, libffi, OpenSSL), each under its own permissive license as listed in the Python license documentation.
   - License: PSF-2.0, Python Software Foundation License Version 2.
   - URL: https://www.python.org

2. wxPython and wxWidgets
   - Author: Robin Dunn, Scott Talbert and the wxPython team; wxWidgets by Julian Smart, Robert Roebling and the wxWidgets developers.
   - Use: all windows, dialogs, the tray icon, the hotkeys and the clipboard access.
   - License: wxWindows Library Licence (a license: LGPL-2.0-or-later with an exception that lets binary versions be distributed under your own terms). SPDX: LicenseRef-wxWindows (WxWindows-exception-3.1 applied to LGPL-2.0-or-later).
   - URL: https://wxpython.org and https://www.wxwidgets.org
   - Verified against: the license file in the installed wxPython 4.3.1 package.

3. pywin32
   - Author: Mark Hammond and contributors.
   - Use: SAPI speech, COM, process information, creating the desktop shortcut.
   - License: PSF-2.0 according to its package metadata; the license files shipped in the package (win32\License.txt and win32com\License.txt) are BSD-3-Clause style texts, which must be kept with copies.
   - URL: https://github.com/mhammond/pywin32
   - Verified against: pywin32 312 package metadata and its license files.

4. comtypes
   - Author: Thomas Heller and the comtypes developers.
   - Use: access to Windows UI Automation.
   - License: MIT, MIT License.
   - URL: https://github.com/enthought/comtypes
   - Verified against: comtypes 1.4.16 license file.

5. PyInstaller (build tool, and its small bootloader that is part of the exe)
   - Author: Hartmut Goebel, Giovanni Bajo, David Vierra, David Cortesi, Martin Zibricky and the PyInstaller Development Team.
   - Use: packs the program into one portable exe.
   - License: GPL-2.0-or-later WITH a special exception that allows the programs it builds to be distributed under any license. The exception applies to the bootloader that is placed in the exe.
   - URL: https://pyinstaller.org
   - Verified against: PyInstaller 6.22.0 package metadata and COPYING.txt.
   - Also used at build time only, not shipped in the exe as separate parts: pyinstaller-hooks-contrib (GPL-2.0-or-later with exception for the hooks, Apache-2.0 for some parts), altgraph (MIT), pefile (MIT), pywin32-ctypes (BSD-3-Clause), packaging (Apache-2.0 OR BSD-2-Clause), setuptools (MIT).

6. UPX (optional)
   - The build settings allow UPX compression of the exe if the UPX tool is installed. UPX is GPL-2.0-or-later with a special exception that allows compressing programs under any license. https://upx.github.io
7. Microsoft Visual C++ runtime (VCRUNTIME140.dll, VCRUNTIME140_1.dll, MSVCP140.dll), by Microsoft, inside the exe.
   - License: Microsoft redistributable terms. https://learn.microsoft.com/cpp/windows/redistributing-visual-cpp-files

## Online services and servers (not bundled)

Each is a service or server under its own terms of use and privacy policy. ZTranslate only sends text to the one you choose.

1. LibreTranslate
   - Project: LibreTranslate community. Use: the Local Offline engine and the LibreTranslate-compatible custom API. You run the server yourself; it is not included. Its server software is AGPL-3.0; it uses Argos Translate (MIT) and its models, with their own licenses.
   - URL: https://libretranslate.com and https://github.com/LibreTranslate/LibreTranslate
2. Google Translate (web endpoint translate.googleapis.com, used without a key)
   - Google LLC. A service under Google's terms. This is an unofficial public endpoint and may change or stop. https://translate.google.com
3. DeepL API
   - DeepL SE. A service under DeepL's terms. Your own key is needed. https://www.deepl.com
4. Microsoft Translator (Azure AI Translator, called Bing Translate in the settings)
   - Microsoft Corporation. A service under Microsoft's terms. Your own key is needed. https://learn.microsoft.com/azure/ai-services/translator/
5. OpenAI API
   - OpenAI. A service under OpenAI's terms. Your own key is needed. https://platform.openai.com
6. Google Gemini API
   - Google LLC. A service under Google's terms. Your own key is needed. https://ai.google.dev
7. OpenRouter
   - OpenRouter, Inc. A service under its terms; it passes your text on to the model provider it routes to. Your own key is needed. https://openrouter.ai
8. Any custom API you enter yourself is under the terms of whoever runs it.

## Notices that must accompany copies

These licenses require their copyright notice and license text to be included with copies of the exe. Keep this file with every copy.

MIT License (comtypes)
- Copyright (c) 2006-2013, Thomas Heller. Copyright (c) 2014, Comtypes Developers. All rights reserved.
- Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: the above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

pywin32
- Copyright (c) 1994-2008, Mark Hammond; Copyright (c) 1996-2008, Greg Stein and Mark Hammond. All rights reserved. Redistribution in source and binary forms is permitted under the BSD-style conditions and disclaimer in pywin32's win32\License.txt, which must accompany copies.

Python
- Copyright (c) 2001 and later Python Software Foundation. All rights reserved. Distributed under the PSF License Agreement; the full text is at https://docs.python.org/3/license.html

wxPython and wxWidgets
- Copyright (c) 1998-2005 Julian Smart, Robert Roebling et al, and later wxWidgets developers; wxPython copyright Robin Dunn and the wxPython team. Distributed under the wxWindows Library Licence, Version 3.1 (full text: https://www.wxwidgets.org/about/licence/). Binary versions may be distributed under the terms of your choice. The library source code is available at https://github.com/wxWidgets/Phoenix and https://github.com/wxWidgets/wxWidgets

PyInstaller
- Copyright (c) 2010-2023, PyInstaller Development Team. Copyright (c) 2005-2009, Giovanni Bajo. Based on previous work under copyright (c) 2002 McMillan Enterprises, Inc. License: GPL-2.0-or-later with the PyInstaller exception for programs it builds; source at https://github.com/pyinstaller/pyinstaller

## Compatibility with AGPL-3.0-or-later

These components keep their own licenses. ZTranslate itself is AGPL-3.0-or-later, and each bundled component can be combined with it:
- MIT (comtypes) and PSF-2.0 (Python, pywin32): permissive and compatible with the GPL family, including AGPL-3.0.
- wxWindows Library Licence (wxPython, wxWidgets): LGPL-2.0-or-later with an exception; it may be combined with GPL-3.0 and AGPL-3.0 works.
- PyInstaller (GPL-2.0-or-later with exception): the "or later" lets it be used under GPL-3.0, and the exception covers the built exe, so it is compatible.
- Nothing bundled is GPL-2.0-only, which would not be compatible with AGPL-3.0. No incompatibility was found.
- LibreTranslate is a separate server you run; it is AGPL-3.0 and is not combined with ZTranslate. The online services are reached over the network under their own terms and are not part of the program.
