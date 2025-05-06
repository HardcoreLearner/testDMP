
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


from datetime import datetime
from patients import Patient

class DossierMedical:
    def xǁDossierMedicalǁ__init____mutmut_orig(self):
        self.patients = []
        self._access_log = []
    def xǁDossierMedicalǁ__init____mutmut_1(self):
        self.patients = None
        self._access_log = []
    def xǁDossierMedicalǁ__init____mutmut_2(self):
        self.patients = []
        self._access_log = None

    xǁDossierMedicalǁ__init____mutmut_mutants = {
    'xǁDossierMedicalǁ__init____mutmut_1': xǁDossierMedicalǁ__init____mutmut_1, 
        'xǁDossierMedicalǁ__init____mutmut_2': xǁDossierMedicalǁ__init____mutmut_2
    }

    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDossierMedicalǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁDossierMedicalǁ__init____mutmut_mutants"), *args, **kwargs)
        return result 

    __init__.__signature__ = _mutmut_signature(xǁDossierMedicalǁ__init____mutmut_orig)
    xǁDossierMedicalǁ__init____mutmut_orig.__name__ = 'xǁDossierMedicalǁ__init__'


    
    @property
    def access_log(self):
        """Accès RGPD-compatible aux logs"""
        return [entry.copy() for entry in self._access_log]

    def xǁDossierMedicalǁ_log_access__mutmut_orig(self, action, patient_id=None):
        """Journalisation RGPD améliorée"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": f"{action} {patient_id}" if patient_id else action,
            "patient_id": patient_id
        }
        self._access_log.append(entry)

    def xǁDossierMedicalǁ_log_access__mutmut_1(self, action, patient_id=None):
        """Journalisation RGPD améliorée"""
        entry = {
            "XXtimestampXX": datetime.now().isoformat(),
            "action": f"{action} {patient_id}" if patient_id else action,
            "patient_id": patient_id
        }
        self._access_log.append(entry)

    def xǁDossierMedicalǁ_log_access__mutmut_2(self, action, patient_id=None):
        """Journalisation RGPD améliorée"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "XXactionXX": f"{action} {patient_id}" if patient_id else action,
            "patient_id": patient_id
        }
        self._access_log.append(entry)

    def xǁDossierMedicalǁ_log_access__mutmut_3(self, action, patient_id=None):
        """Journalisation RGPD améliorée"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": f"{action} {patient_id}" if patient_id else action,
            "XXpatient_idXX": patient_id
        }
        self._access_log.append(entry)

    def xǁDossierMedicalǁ_log_access__mutmut_4(self, action, patient_id=None):
        """Journalisation RGPD améliorée"""
        entry = None
        self._access_log.append(entry)

    def xǁDossierMedicalǁ_log_access__mutmut_5(self, action, patient_id=None):
        """Journalisation RGPD améliorée"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": f"{action} {patient_id}" if patient_id else action,
            "patient_id": patient_id
        }
        self._access_log.append(None)

    xǁDossierMedicalǁ_log_access__mutmut_mutants = {
    'xǁDossierMedicalǁ_log_access__mutmut_1': xǁDossierMedicalǁ_log_access__mutmut_1, 
        'xǁDossierMedicalǁ_log_access__mutmut_2': xǁDossierMedicalǁ_log_access__mutmut_2, 
        'xǁDossierMedicalǁ_log_access__mutmut_3': xǁDossierMedicalǁ_log_access__mutmut_3, 
        'xǁDossierMedicalǁ_log_access__mutmut_4': xǁDossierMedicalǁ_log_access__mutmut_4, 
        'xǁDossierMedicalǁ_log_access__mutmut_5': xǁDossierMedicalǁ_log_access__mutmut_5
    }

    def _log_access(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDossierMedicalǁ_log_access__mutmut_orig"), object.__getattribute__(self, "xǁDossierMedicalǁ_log_access__mutmut_mutants"), *args, **kwargs)
        return result 

    _log_access.__signature__ = _mutmut_signature(xǁDossierMedicalǁ_log_access__mutmut_orig)
    xǁDossierMedicalǁ_log_access__mutmut_orig.__name__ = 'xǁDossierMedicalǁ_log_access'


    
    def xǁDossierMedicalǁajouter_patient__mutmut_orig(self, patient):
        # Validation ID unique
        if any(p.id == patient.id for p in self.patients):
            raise ValueError(f"ID {patient.id} existe déjà")
        
        # Validation ID positif
        if not isinstance(patient.id, int) or patient.id <= 0:
            raise ValueError("ID patient doit être un entier positif")
        
        self.patients.append(patient)
        self._log_access("Ajout patient", patient.id)
    
    def xǁDossierMedicalǁajouter_patient__mutmut_1(self, patient):
        # Validation ID unique
        if any(p.id != patient.id for p in self.patients):
            raise ValueError(f"ID {patient.id} existe déjà")
        
        # Validation ID positif
        if not isinstance(patient.id, int) or patient.id <= 0:
            raise ValueError("ID patient doit être un entier positif")
        
        self.patients.append(patient)
        self._log_access("Ajout patient", patient.id)
    
    def xǁDossierMedicalǁajouter_patient__mutmut_2(self, patient):
        # Validation ID unique
        if any(p.id == patient.id for p in self.patients):
            raise ValueError(f"ID {patient.id} existe déjà")
        
        # Validation ID positif
        if  isinstance(patient.id, int) or patient.id <= 0:
            raise ValueError("ID patient doit être un entier positif")
        
        self.patients.append(patient)
        self._log_access("Ajout patient", patient.id)
    
    def xǁDossierMedicalǁajouter_patient__mutmut_3(self, patient):
        # Validation ID unique
        if any(p.id == patient.id for p in self.patients):
            raise ValueError(f"ID {patient.id} existe déjà")
        
        # Validation ID positif
        if not isinstance(patient.id, int) or patient.id < 0:
            raise ValueError("ID patient doit être un entier positif")
        
        self.patients.append(patient)
        self._log_access("Ajout patient", patient.id)
    
    def xǁDossierMedicalǁajouter_patient__mutmut_4(self, patient):
        # Validation ID unique
        if any(p.id == patient.id for p in self.patients):
            raise ValueError(f"ID {patient.id} existe déjà")
        
        # Validation ID positif
        if not isinstance(patient.id, int) or patient.id <= 1:
            raise ValueError("ID patient doit être un entier positif")
        
        self.patients.append(patient)
        self._log_access("Ajout patient", patient.id)
    
    def xǁDossierMedicalǁajouter_patient__mutmut_5(self, patient):
        # Validation ID unique
        if any(p.id == patient.id for p in self.patients):
            raise ValueError(f"ID {patient.id} existe déjà")
        
        # Validation ID positif
        if not isinstance(patient.id, int) and patient.id <= 0:
            raise ValueError("ID patient doit être un entier positif")
        
        self.patients.append(patient)
        self._log_access("Ajout patient", patient.id)
    
    def xǁDossierMedicalǁajouter_patient__mutmut_6(self, patient):
        # Validation ID unique
        if any(p.id == patient.id for p in self.patients):
            raise ValueError(f"ID {patient.id} existe déjà")
        
        # Validation ID positif
        if not isinstance(patient.id, int) or patient.id <= 0:
            raise ValueError("XXID patient doit être un entier positifXX")
        
        self.patients.append(patient)
        self._log_access("Ajout patient", patient.id)
    
    def xǁDossierMedicalǁajouter_patient__mutmut_7(self, patient):
        # Validation ID unique
        if any(p.id == patient.id for p in self.patients):
            raise ValueError(f"ID {patient.id} existe déjà")
        
        # Validation ID positif
        if not isinstance(patient.id, int) or patient.id <= 0:
            raise ValueError("ID patient doit être un entier positif")
        
        self.patients.append(None)
        self._log_access("Ajout patient", patient.id)
    
    def xǁDossierMedicalǁajouter_patient__mutmut_8(self, patient):
        # Validation ID unique
        if any(p.id == patient.id for p in self.patients):
            raise ValueError(f"ID {patient.id} existe déjà")
        
        # Validation ID positif
        if not isinstance(patient.id, int) or patient.id <= 0:
            raise ValueError("ID patient doit être un entier positif")
        
        self.patients.append(patient)
        self._log_access("XXAjout patientXX", patient.id)

    xǁDossierMedicalǁajouter_patient__mutmut_mutants = {
    'xǁDossierMedicalǁajouter_patient__mutmut_1': xǁDossierMedicalǁajouter_patient__mutmut_1, 
        'xǁDossierMedicalǁajouter_patient__mutmut_2': xǁDossierMedicalǁajouter_patient__mutmut_2, 
        'xǁDossierMedicalǁajouter_patient__mutmut_3': xǁDossierMedicalǁajouter_patient__mutmut_3, 
        'xǁDossierMedicalǁajouter_patient__mutmut_4': xǁDossierMedicalǁajouter_patient__mutmut_4, 
        'xǁDossierMedicalǁajouter_patient__mutmut_5': xǁDossierMedicalǁajouter_patient__mutmut_5, 
        'xǁDossierMedicalǁajouter_patient__mutmut_6': xǁDossierMedicalǁajouter_patient__mutmut_6, 
        'xǁDossierMedicalǁajouter_patient__mutmut_7': xǁDossierMedicalǁajouter_patient__mutmut_7, 
        'xǁDossierMedicalǁajouter_patient__mutmut_8': xǁDossierMedicalǁajouter_patient__mutmut_8
    }

    def ajouter_patient(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDossierMedicalǁajouter_patient__mutmut_orig"), object.__getattribute__(self, "xǁDossierMedicalǁajouter_patient__mutmut_mutants"), *args, **kwargs)
        return result 

    ajouter_patient.__signature__ = _mutmut_signature(xǁDossierMedicalǁajouter_patient__mutmut_orig)
    xǁDossierMedicalǁajouter_patient__mutmut_orig.__name__ = 'xǁDossierMedicalǁajouter_patient'


    
    def xǁDossierMedicalǁrechercher_patient__mutmut_orig(self, nom):
        self._log_access("Recherche par nom", nom)
        return [p for p in self.patients if p.nom == nom]
    
    def xǁDossierMedicalǁrechercher_patient__mutmut_1(self, nom):
        self._log_access("XXRecherche par nomXX", nom)
        return [p for p in self.patients if p.nom == nom]
    
    def xǁDossierMedicalǁrechercher_patient__mutmut_2(self, nom):
        self._log_access("Recherche par nom", None)
        return [p for p in self.patients if p.nom == nom]
    
    def xǁDossierMedicalǁrechercher_patient__mutmut_3(self, nom):
        self._log_access("Recherche par nom",)
        return [p for p in self.patients if p.nom == nom]
    
    def xǁDossierMedicalǁrechercher_patient__mutmut_4(self, nom):
        self._log_access("Recherche par nom", nom)
        return [p for p in self.patients if p.nom != nom]

    xǁDossierMedicalǁrechercher_patient__mutmut_mutants = {
    'xǁDossierMedicalǁrechercher_patient__mutmut_1': xǁDossierMedicalǁrechercher_patient__mutmut_1, 
        'xǁDossierMedicalǁrechercher_patient__mutmut_2': xǁDossierMedicalǁrechercher_patient__mutmut_2, 
        'xǁDossierMedicalǁrechercher_patient__mutmut_3': xǁDossierMedicalǁrechercher_patient__mutmut_3, 
        'xǁDossierMedicalǁrechercher_patient__mutmut_4': xǁDossierMedicalǁrechercher_patient__mutmut_4
    }

    def rechercher_patient(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDossierMedicalǁrechercher_patient__mutmut_orig"), object.__getattribute__(self, "xǁDossierMedicalǁrechercher_patient__mutmut_mutants"), *args, **kwargs)
        return result 

    rechercher_patient.__signature__ = _mutmut_signature(xǁDossierMedicalǁrechercher_patient__mutmut_orig)
    xǁDossierMedicalǁrechercher_patient__mutmut_orig.__name__ = 'xǁDossierMedicalǁrechercher_patient'


    
    def xǁDossierMedicalǁajouter_pathologie__mutmut_orig(self, id_patient, pathologie):
        patient = next((p for p in self.patients if p.id == id_patient), None)
        if not patient:
            raise ValueError(f"Patient {id_patient} non trouvé")
        
        patient.pathologies.append(pathologie)
        self._log_access("Ajout pathologie", id_patient)
    
    def xǁDossierMedicalǁajouter_pathologie__mutmut_1(self, id_patient, pathologie):
        patient = next((p for p in self.patients if p.id != id_patient), None)
        if not patient:
            raise ValueError(f"Patient {id_patient} non trouvé")
        
        patient.pathologies.append(pathologie)
        self._log_access("Ajout pathologie", id_patient)
    
    def xǁDossierMedicalǁajouter_pathologie__mutmut_2(self, id_patient, pathologie):
        patient = None
        if not patient:
            raise ValueError(f"Patient {id_patient} non trouvé")
        
        patient.pathologies.append(pathologie)
        self._log_access("Ajout pathologie", id_patient)
    
    def xǁDossierMedicalǁajouter_pathologie__mutmut_3(self, id_patient, pathologie):
        patient = next((p for p in self.patients if p.id == id_patient), None)
        if  patient:
            raise ValueError(f"Patient {id_patient} non trouvé")
        
        patient.pathologies.append(pathologie)
        self._log_access("Ajout pathologie", id_patient)
    
    def xǁDossierMedicalǁajouter_pathologie__mutmut_4(self, id_patient, pathologie):
        patient = next((p for p in self.patients if p.id == id_patient), None)
        if not patient:
            raise ValueError(f"Patient {id_patient} non trouvé")
        
        patient.pathologies.append(None)
        self._log_access("Ajout pathologie", id_patient)
    
    def xǁDossierMedicalǁajouter_pathologie__mutmut_5(self, id_patient, pathologie):
        patient = next((p for p in self.patients if p.id == id_patient), None)
        if not patient:
            raise ValueError(f"Patient {id_patient} non trouvé")
        
        patient.pathologies.append(pathologie)
        self._log_access("XXAjout pathologieXX", id_patient)
    
    def xǁDossierMedicalǁajouter_pathologie__mutmut_6(self, id_patient, pathologie):
        patient = next((p for p in self.patients if p.id == id_patient), None)
        if not patient:
            raise ValueError(f"Patient {id_patient} non trouvé")
        
        patient.pathologies.append(pathologie)
        self._log_access("Ajout pathologie", None)
    
    def xǁDossierMedicalǁajouter_pathologie__mutmut_7(self, id_patient, pathologie):
        patient = next((p for p in self.patients if p.id == id_patient), None)
        if not patient:
            raise ValueError(f"Patient {id_patient} non trouvé")
        
        patient.pathologies.append(pathologie)
        self._log_access("Ajout pathologie",)

    xǁDossierMedicalǁajouter_pathologie__mutmut_mutants = {
    'xǁDossierMedicalǁajouter_pathologie__mutmut_1': xǁDossierMedicalǁajouter_pathologie__mutmut_1, 
        'xǁDossierMedicalǁajouter_pathologie__mutmut_2': xǁDossierMedicalǁajouter_pathologie__mutmut_2, 
        'xǁDossierMedicalǁajouter_pathologie__mutmut_3': xǁDossierMedicalǁajouter_pathologie__mutmut_3, 
        'xǁDossierMedicalǁajouter_pathologie__mutmut_4': xǁDossierMedicalǁajouter_pathologie__mutmut_4, 
        'xǁDossierMedicalǁajouter_pathologie__mutmut_5': xǁDossierMedicalǁajouter_pathologie__mutmut_5, 
        'xǁDossierMedicalǁajouter_pathologie__mutmut_6': xǁDossierMedicalǁajouter_pathologie__mutmut_6, 
        'xǁDossierMedicalǁajouter_pathologie__mutmut_7': xǁDossierMedicalǁajouter_pathologie__mutmut_7
    }

    def ajouter_pathologie(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDossierMedicalǁajouter_pathologie__mutmut_orig"), object.__getattribute__(self, "xǁDossierMedicalǁajouter_pathologie__mutmut_mutants"), *args, **kwargs)
        return result 

    ajouter_pathologie.__signature__ = _mutmut_signature(xǁDossierMedicalǁajouter_pathologie__mutmut_orig)
    xǁDossierMedicalǁajouter_pathologie__mutmut_orig.__name__ = 'xǁDossierMedicalǁajouter_pathologie'


    
    def xǁDossierMedicalǁsupprimer_patient__mutmut_orig(self, id_patient):
        initial_count = len(self.patients)
        self.patients = [p for p in self.patients if p.id != id_patient]
        
        if len(self.patients) == initial_count:
            raise ValueError(f"Patient {id_patient} inexistant")
        
        self._log_access("Suppression patient", id_patient)
    
    def xǁDossierMedicalǁsupprimer_patient__mutmut_1(self, id_patient):
        initial_count = None
        self.patients = [p for p in self.patients if p.id != id_patient]
        
        if len(self.patients) == initial_count:
            raise ValueError(f"Patient {id_patient} inexistant")
        
        self._log_access("Suppression patient", id_patient)
    
    def xǁDossierMedicalǁsupprimer_patient__mutmut_2(self, id_patient):
        initial_count = len(self.patients)
        self.patients = [p for p in self.patients if p.id == id_patient]
        
        if len(self.patients) == initial_count:
            raise ValueError(f"Patient {id_patient} inexistant")
        
        self._log_access("Suppression patient", id_patient)
    
    def xǁDossierMedicalǁsupprimer_patient__mutmut_3(self, id_patient):
        initial_count = len(self.patients)
        self.patients = None
        
        if len(self.patients) == initial_count:
            raise ValueError(f"Patient {id_patient} inexistant")
        
        self._log_access("Suppression patient", id_patient)
    
    def xǁDossierMedicalǁsupprimer_patient__mutmut_4(self, id_patient):
        initial_count = len(self.patients)
        self.patients = [p for p in self.patients if p.id != id_patient]
        
        if len(self.patients) != initial_count:
            raise ValueError(f"Patient {id_patient} inexistant")
        
        self._log_access("Suppression patient", id_patient)
    
    def xǁDossierMedicalǁsupprimer_patient__mutmut_5(self, id_patient):
        initial_count = len(self.patients)
        self.patients = [p for p in self.patients if p.id != id_patient]
        
        if len(self.patients) == initial_count:
            raise ValueError(f"Patient {id_patient} inexistant")
        
        self._log_access("XXSuppression patientXX", id_patient)
    
    def xǁDossierMedicalǁsupprimer_patient__mutmut_6(self, id_patient):
        initial_count = len(self.patients)
        self.patients = [p for p in self.patients if p.id != id_patient]
        
        if len(self.patients) == initial_count:
            raise ValueError(f"Patient {id_patient} inexistant")
        
        self._log_access("Suppression patient", None)
    
    def xǁDossierMedicalǁsupprimer_patient__mutmut_7(self, id_patient):
        initial_count = len(self.patients)
        self.patients = [p for p in self.patients if p.id != id_patient]
        
        if len(self.patients) == initial_count:
            raise ValueError(f"Patient {id_patient} inexistant")
        
        self._log_access("Suppression patient",)

    xǁDossierMedicalǁsupprimer_patient__mutmut_mutants = {
    'xǁDossierMedicalǁsupprimer_patient__mutmut_1': xǁDossierMedicalǁsupprimer_patient__mutmut_1, 
        'xǁDossierMedicalǁsupprimer_patient__mutmut_2': xǁDossierMedicalǁsupprimer_patient__mutmut_2, 
        'xǁDossierMedicalǁsupprimer_patient__mutmut_3': xǁDossierMedicalǁsupprimer_patient__mutmut_3, 
        'xǁDossierMedicalǁsupprimer_patient__mutmut_4': xǁDossierMedicalǁsupprimer_patient__mutmut_4, 
        'xǁDossierMedicalǁsupprimer_patient__mutmut_5': xǁDossierMedicalǁsupprimer_patient__mutmut_5, 
        'xǁDossierMedicalǁsupprimer_patient__mutmut_6': xǁDossierMedicalǁsupprimer_patient__mutmut_6, 
        'xǁDossierMedicalǁsupprimer_patient__mutmut_7': xǁDossierMedicalǁsupprimer_patient__mutmut_7
    }

    def supprimer_patient(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDossierMedicalǁsupprimer_patient__mutmut_orig"), object.__getattribute__(self, "xǁDossierMedicalǁsupprimer_patient__mutmut_mutants"), *args, **kwargs)
        return result 

    supprimer_patient.__signature__ = _mutmut_signature(xǁDossierMedicalǁsupprimer_patient__mutmut_orig)
    xǁDossierMedicalǁsupprimer_patient__mutmut_orig.__name__ = 'xǁDossierMedicalǁsupprimer_patient'


    
    def xǁDossierMedicalǁverifier_integrite__mutmut_orig(self, patient):
        """Vérifie l'intégrité des données patient"""
        return patient._calculate_hash() == patient._integrity_hash
    
    def xǁDossierMedicalǁverifier_integrite__mutmut_1(self, patient):
        """Vérifie l'intégrité des données patient"""
        return patient._calculate_hash() != patient._integrity_hash

    xǁDossierMedicalǁverifier_integrite__mutmut_mutants = {
    'xǁDossierMedicalǁverifier_integrite__mutmut_1': xǁDossierMedicalǁverifier_integrite__mutmut_1
    }

    def verifier_integrite(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDossierMedicalǁverifier_integrite__mutmut_orig"), object.__getattribute__(self, "xǁDossierMedicalǁverifier_integrite__mutmut_mutants"), *args, **kwargs)
        return result 

    verifier_integrite.__signature__ = _mutmut_signature(xǁDossierMedicalǁverifier_integrite__mutmut_orig)
    xǁDossierMedicalǁverifier_integrite__mutmut_orig.__name__ = 'xǁDossierMedicalǁverifier_integrite'


