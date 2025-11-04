# Manual de Instalación y Ejecución

## Requisitos del Sistema

### Software Necesario
- **Python 3.8 o superior** (Recomendado: Python 3.10+)
- **Sistema Operativo**: Windows, macOS o Linux
- **Espacio en disco**: Mínimo 100 MB
- **RAM**: Mínimo 512 MB

### Verificar Instalación de Python

Abra PowerShell o CMD y ejecute:
```powershell
python --version
```

Debería ver algo como: `Python 3.10.x`

Si no tiene Python instalado, descárguelo de: https://www.python.org/downloads/

---

## Instalación Paso a Paso

### 1. Navegar al Directorio del Proyecto

```powershell
cd "C:\Proyecto Universidad\Odontologia-proyect"
```

### 2. Crear Entorno Virtual (Recomendado)

Un entorno virtual mantiene las dependencias aisladas:

```powershell
python -m venv venv
```

### 3. Activar el Entorno Virtual

**En Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**En Windows CMD:**
```cmd
venv\Scripts\activate.bat
```

**En Linux/Mac:**
```bash
source venv/bin/activate
```

Verá `(venv)` al inicio de la línea de comandos.

### 4. Instalar Dependencias

```powershell
pip install -r requirements.txt
```

Esto instalará:
- scikit-fuzzy (lógica difusa)
- numpy (operaciones numéricas)
- reportlab (generación de PDF)
- matplotlib (gráficos)
- Pillow (manejo de imágenes)

**Nota sobre tkinter**: Tkinter viene incluido con Python, no necesita instalación adicional.

### 5. Verificar Instalación

```powershell
python -c "import tkinter; import skfuzzy; import reportlab; print('✓ Todas las dependencias instaladas correctamente')"
```

---

## Ejecutar la Aplicación

### Método 1: Desde la Raíz del Proyecto

```powershell
python src/main.py
```

### Método 2: Desde el Directorio src

```powershell
cd src
python main.py
```

### Método 3: Usando el módulo GUI directamente

```powershell
python -m src.gui.main_window
```

---

## Solución de Problemas Comunes

### Error: "No module named 'tkinter'"

**Solución para Windows:**
Tkinter debería venir con Python. Si no, reinstale Python y marque "tcl/tk and IDLE" durante la instalación.

**Solución para Linux:**
```bash
sudo apt-get install python3-tk
```

**Solución para Mac:**
Tkinter debería estar incluido. Si no:
```bash
brew install python-tk
```

### Error: "No module named 'skfuzzy'"

**Solución:**
```powershell
pip install scikit-fuzzy
```

### Error: "No module named 'reportlab'"

**Solución:**
```powershell
pip install reportlab
```

### Error al Generar PDF

Si hay problemas al generar PDFs, verifique:
```powershell
pip install --upgrade reportlab Pillow
```

### La Ventana no Aparece

1. Verifique que no haya errores en la consola
2. Intente ejecutar con:
```powershell
python -u src/main.py
```

### Error: "Import could not be resolved"

Asegúrese de estar en el directorio correcto:
```powershell
cd "C:\Proyecto Universidad\Odontologia-proyect"
python src/main.py
```

---

## Actualizar el Proyecto

Si descarga una versión actualizada:

```powershell
# Activar entorno virtual
.\venv\Scripts\Activate.ps1

# Actualizar dependencias
pip install -r requirements.txt --upgrade

# Ejecutar
python src/main.py
```

---

## Desinstalar

Para desinstalar el proyecto:

1. Desactivar entorno virtual:
```powershell
deactivate
```

2. Eliminar el directorio completo:
```powershell
cd ..
Remove-Item -Recurse -Force "Odontologia-proyect"
```

---

## Crear Ejecutable (Opcional)

Para crear un ejecutable standalone usando PyInstaller:

### 1. Instalar PyInstaller

```powershell
pip install pyinstaller
```

### 2. Generar Ejecutable

```powershell
pyinstaller --onefile --windowed --name="SistemaOdontologia" src/main.py
```

El ejecutable estará en la carpeta `dist/`

### 3. Ejecutar

```powershell
.\dist\SistemaOdontologia.exe
```

**Nota**: El ejecutable puede ser grande (50-100 MB) porque incluye Python y todas las dependencias.

---

## Ejecutar Pruebas

Para validar que todo funciona correctamente:

```powershell
# Activar entorno virtual
.\venv\Scripts\Activate.ps1

# Ejecutar pruebas
python tests/test_diagnosis.py
```

Debería ver:
```
=== EJECUTANDO PRUEBAS DEL SISTEMA EXPERTO ===
✓ Test pasado
✓ Test pasado
...
✓ TODAS LAS PRUEBAS PASARON EXITOSAMENTE
```

---

## Estructura de Archivos Generados

Durante el uso, el sistema generará:

```
Odontologia-proyect/
├── logs/
│   └── sistema_YYYYMMDD.log    # Logs diarios
├── reports/
│   └── diagnostico_*.pdf        # Reportes generados
└── venv/                        # Entorno virtual (si se creó)
```

---

## Comandos Útiles

### Ver Logs
```powershell
Get-Content logs/sistema_*.log -Tail 50
```

### Limpiar Archivos Temporales
```powershell
Remove-Item -Recurse __pycache__
Remove-Item -Recurse src/__pycache__
Remove-Item -Recurse src/*/__pycache__
```

### Listar Paquetes Instalados
```powershell
pip list
```

### Actualizar pip
```powershell
python -m pip install --upgrade pip
```

---

## Contacto y Soporte

Si encuentra problemas:

1. Revise la sección de solución de problemas
2. Verifique los logs en `logs/`
3. Consulte la documentación en `docs/`
4. Contacte al desarrollador

---

© 2025 - Sistema Experto de Odontología - Proyecto Universidad
