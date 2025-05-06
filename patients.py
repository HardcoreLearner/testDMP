from datetime import datetime
import hashlib

class Patient:
    def __init__(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("Champs obligatoires manquants")
        
        try:
            datetime.strptime(date_naissance, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Format de date invalide (YYYY-MM-DD requis)")
            
        self.id = id
        self.nom = nom
        self.date_naissance = date_naissance
        self.pathologies = pathologies or []
        self.allergies = allergies or []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()

    def _calculate_hash(self):
        return hashlib.sha256(f"{self.id}{self.nom}{self.date_naissance}".encode()).hexdigest()