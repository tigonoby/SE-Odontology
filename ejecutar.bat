@echo off
chcp 65001 >nul
title Sistema Experto de Odontología
color 0B

echo ============================================================
echo    🦷 SISTEMA EXPERTO DE ODONTOLOGÍA
echo    Universidad - Proyecto de Sistemas Expertos
echo ============================================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Python no está instalado o no está en el PATH
    echo.
    echo Por favor, instale Python desde: https://www.python.org/downloads/
    echo Asegúrese de marcar "Add Python to PATH" durante la instalación
    echo.
    pause
    exit /b 1
)

echo ✓ Python encontrado
python --version
echo.

REM Verificar si existe requirements.txt
if not exist "requirements.txt" (
    echo ⚠️  ADVERTENCIA: No se encontró requirements.txt
    echo    El sistema puede no funcionar correctamente
    echo.
)

REM Preguntar si desea instalar dependencias
echo ¿Desea verificar/instalar dependencias? (Recomendado en la primera ejecución)
echo [S] Sí - Instalar/actualizar dependencias
echo [N] No - Ejecutar directamente
echo.
choice /C SN /N /M "Seleccione una opción (S/N): "

if %errorlevel% equ 1 (
    echo.
    echo 📦 Instalando dependencias...
    echo ============================================================
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo ❌ Error al instalar dependencias
        pause
        exit /b 1
    )
    echo.
    echo ✓ Dependencias instaladas correctamente
    echo.
)

REM Ejecutar la aplicación
echo ============================================================
echo 🚀 Iniciando Sistema Experto de Odontología...
echo ============================================================
echo.
echo Si la ventana no aparece, verifique la consola para errores.
echo Presione Ctrl+C para detener la aplicación.
echo.

REM Opción 1: Usar el script run.py
if exist "run.py" (
    python run.py
) else (
    REM Opción 2: Ejecutar directamente
    if exist "src\main.py" (
        python src\main.py
    ) else (
        echo ❌ ERROR: No se encontró el archivo principal
        echo    Verifique que src\main.py exista
        pause
        exit /b 1
    )
)

if %errorlevel% neq 0 (
    echo.
    echo ============================================================
    echo ❌ La aplicación terminó con errores
    echo ============================================================
    echo.
    echo Posibles soluciones:
    echo 1. Ejecute: pip install -r requirements.txt
    echo 2. Verifique que Python 3.8+ esté instalado
    echo 3. Consulte los logs en la carpeta 'logs\'
    echo 4. Revise el archivo INSTALACION.md
    echo.
) else (
    echo.
    echo ============================================================
    echo ✓ Aplicación cerrada correctamente
    echo ============================================================
)

echo.
pause
