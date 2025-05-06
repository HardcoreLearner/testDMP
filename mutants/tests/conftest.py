# tests/conftest.py
import sys
import os

# Ajouter le chemin absolu du projet à PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)