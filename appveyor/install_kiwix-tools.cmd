REM ========================================================
REM Install kiwix-tools
curl -fsSL -O https://download.kiwix.org/release/kiwix-tools/kiwix-tools_win-i686-2.1.0.zip || exit /b 1
7z e kiwix-tools_win-i686-2.1.0.zip -o%EXTRA_DIR%\bin kiwix-serve.exe || exit /b 1
