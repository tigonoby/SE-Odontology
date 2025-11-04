#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de Inicio Automático
Verifica dependencias e inicia la aplicación
"""

import sys
import os
import subprocess

def check_python_version():
    """Verifica la versión de Python"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Error: Se requiere Python 3.8 o superior")
        print(f"   Versión actual: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro} - OK")
    return True

def check_dependencies():
    """Verifica que las dependencias estén instaladas"""
    required_packages = {
        'tkinter': 'tkinter',
        'numpy': 'numpy',
        'skfuzzy': 'scikit-fuzzy',
        'reportlab': 'reportlab'
    }
    
    missing = []
    
    for package, pip_name in required_packages.items():
        try:
            if package == 'tkinter':
                __import__(package)
            else:
                __import__(package)
            print(f"✓ {pip_name} - Instalado")
        except ImportError:
            print(f"✗ {pip_name} - NO instalado")
            missing.append(pip_name)
    
    return missing

def install_dependencies(packages):
    """Instala dependencias faltantes"""
    if not packages:
        return True
    
    print("\n📦 Instalando dependencias faltantes...")
    
    for package in packages:
        if package == 'tkinter':
            print("\n⚠️  tkinter no está disponible")
            print("   Windows: Reinstale Python con 'tcl/tk and IDLE'")
            print("   Linux: sudo apt-get install python3-tk")
            print("   Mac: tkinter debería estar incluido")
            continue
        
        try:
            print(f"\nInstalando {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✓ {package} instalado correctamente")
        except Exception as e:
            print(f"✗ Error al instalar {package}: {e}")
            return False
    
    return True

def run_application():
    """Ejecuta la aplicación principal"""
    print("\n" + "="*60)
    print("🦷 Iniciando Sistema Experto de Odontología...")
    print("="*60 + "\n")
    
    # Cambiar al directorio src
    src_dir = os.path.join(os.path.dirname(__file__), 'src')
    
    if os.path.exists(src_dir):
        sys.path.insert(0, os.path.dirname(__file__))
    
    try:
        # Importar y ejecutar
        from src.gui.main_window import main
        main()
    except Exception as e:
        print(f"\n❌ Error al iniciar la aplicación: {e}")
        print("\nDetalles del error:")
        import traceback
        traceback.print_exc()
        input("\nPresione Enter para salir...")
        return False
    
    return True

def main():
    """Función principal"""
    print("\n" + "="*60)
    print("   SISTEMA EXPERTO DE ODONTOLOGÍA - VERIFICACIÓN")
    print("="*60 + "\n")
    
    # Verificar Python
    if not check_python_version():
        input("\nPresione Enter para salir...")
        return
    
    # Verificar dependencias
    print("\n📋 Verificando dependencias...")
    missing = check_dependencies()
    
    if missing:
        print(f"\n⚠️  Se encontraron {len(missing)} dependencias faltantes")
        response = input("\n¿Desea instalarlas automáticamente? (s/n): ")
        
        if response.lower() in ['s', 'si', 'sí', 'y', 'yes']:
            if not install_dependencies(missing):
                print("\n❌ No se pudieron instalar todas las dependencias")
                print("   Ejecute manualmente: pip install -r requirements.txt")
                input("\nPresione Enter para salir...")
                return
            
            # Verificar nuevamente
            print("\n📋 Verificando instalación...")
            missing = check_dependencies()
            
            if missing and 'tkinter' not in [m for m in missing]:
                print("\n❌ Algunas dependencias aún no están instaladas")
                input("\nPresione Enter para salir...")
                return
    
    print("\n✓ Todas las dependencias están listas")
    
    # Ejecutar aplicación
    run_application()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Aplicación interrumpida por el usuario")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\n" + "="*60)
        print("   Gracias por usar el Sistema Experto de Odontología")
        print("="*60)
