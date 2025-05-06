from datetime import datetime
from patients import Patient
from collections import defaultdict

class DossierMedical:
    def __init__(self):
        self.patients = []
        self._nom_index = defaultdict(list)  # Index pour la recherche rapide
        self._access_log = []
        self._id_set = set()
    
    @property
    def access_log(self):
        """Accès RGPD-compatible aux logs"""
        return [entry.copy() for entry in self._access_log]

    def _log_access(self, action, patient_id=None):
        """Journalisation RGPD améliorée"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": f"{action} {patient_id}" if patient_id else action,
            "patient_id": patient_id
        }
        self._access_log.append(entry)
    
    def ajouter_patient(self, patient):
        # Validation ID unique (O(1) grâce au set)
        if patient.id in self._id_set:
            raise ValueError(f"ID {patient.id} existe déjà")
        
        # Validation format ID
        if not isinstance(patient.id, int) or patient.id <= 0:
            raise ValueError("ID doit être un entier positif")
        
        # Mise à jour des structures de données
        self.patients.append(patient)
        self._nom_index[patient.nom].append(patient)
        self._id_set.add(patient.id)
        
        # Journalisation
        self._log_access("AJOUT", patient.id)

    def rechercher_patient(self, nom):
        # Journalisation avec le nom recherché
        self._log_access("RECHERCHE", nom)
        
        # Recherche via l'index (O(1) en temps constant)
        return self._nom_index.get(nom, []).copy()  # Retourne une copie pour l'immutabilité
    
    def ajouter_pathologie(self, id_patient, pathologie):
        patient = next((p for p in self.patients if p.id == id_patient), None)
        if not patient:
            raise ValueError(f"Patient {id_patient} non trouvé")
        
        patient.pathologies.append(pathologie)
        self._log_access("Ajout pathologie", id_patient)
    
    def supprimer_patient(self, id_patient):
        initial_count = len(self.patients)
        self.patients = [p for p in self.patients if p.id != id_patient]
        
        if len(self.patients) == initial_count:
            raise ValueError(f"Patient {id_patient} inexistant")
        
        self._log_access("Suppression patient", id_patient)
    
    def verifier_integrite(self, patient):
        """Vérifie l'intégrité des données patient"""
        return patient._calculate_hash() == patient._integrity_hash