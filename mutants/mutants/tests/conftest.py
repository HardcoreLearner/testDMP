# tests/conftest.py
import sys
import os

# 1) Détermine le dossier 'mutants/' ou la racine du projet sandboxé
#    __file__ peut être ".../mutants/tests/conftest.py" ou ".../tests/conftest.py"
root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# 2) Ajoute ce dossier en tête de sys.path
if root not in sys.path:
    sys.path.insert(0, root)
