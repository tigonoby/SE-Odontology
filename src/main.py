"""
Sistema Experto de Odontología
Punto de entrada principal de la aplicación
"""

import sys
import os

# Añadir el directorio raíz al path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from gui.main_window import main

if __name__ == "__main__":
    main()
