@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
set "PY_SCRIPT=%SCRIPT_DIR%img2mtrx.py"
if "%~1"=="" (
  echo 请将图片拖到此图标上运行。
  pause
  exit /b 1
)
python "%PY_SCRIPT%" "%~1"
pause
