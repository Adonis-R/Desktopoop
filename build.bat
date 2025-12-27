@echo off
echo ========================================
echo   Compilation de Desktopoop en .exe
echo ========================================
echo.

echo [1/3] Installation des dependances...
pip install -r requirements.txt

echo.
echo [2/3] Compilation en cours...
pyinstaller --onefile --noconsole --name "TrollApp" --add-data "assets;assets" src/main.py

echo.
echo [3/3] Nettoyage...
rmdir /s /q build 2>nul
del /q TrollApp.spec 2>nul

echo.
echo ========================================
echo   Compilation terminee !
echo   L'executable se trouve dans : dist\TrollApp.exe
echo ========================================
echo.
pause
