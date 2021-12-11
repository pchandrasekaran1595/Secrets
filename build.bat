@echo off
setlocal enabledelayedexpansion

echo.
echo ******************************
echo *        Exe Builder         *
echo ******************************
echo.

echo pyinstaller main.py --onefile --clean --log-level DEBUG --name secrets --console
pyinstaller main.py --onefile --clean --log-level DEBUG --name secrets --console

echo.
echo ******************************
echo *    Exe Build Complete      *
echo ******************************
echo.

