
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
import hashlib

class Patient:
    def xǁPatientǁ__init____mutmut_orig(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
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
    def xǁPatientǁ__init____mutmut_1(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if  all([id, nom, date_naissance]):
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
    def xǁPatientǁ__init____mutmut_2(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("XXChamps obligatoires manquantsXX")
        
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
    def xǁPatientǁ__init____mutmut_3(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("Champs obligatoires manquants")
        
        try:
            datetime.strptime(None, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Format de date invalide (YYYY-MM-DD requis)")
            
        self.id = id
        self.nom = nom
        self.date_naissance = date_naissance
        self.pathologies = pathologies or []
        self.allergies = allergies or []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_4(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("Champs obligatoires manquants")
        
        try:
            datetime.strptime(date_naissance, "XX%Y-%m-%dXX")
        except ValueError:
            raise ValueError("Format de date invalide (YYYY-MM-DD requis)")
            
        self.id = id
        self.nom = nom
        self.date_naissance = date_naissance
        self.pathologies = pathologies or []
        self.allergies = allergies or []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_5(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("Champs obligatoires manquants")
        
        try:
            datetime.strptime( "%Y-%m-%d")
        except ValueError:
            raise ValueError("Format de date invalide (YYYY-MM-DD requis)")
            
        self.id = id
        self.nom = nom
        self.date_naissance = date_naissance
        self.pathologies = pathologies or []
        self.allergies = allergies or []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_6(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("Champs obligatoires manquants")
        
        try:
            datetime.strptime(date_naissance, "%Y-%m-%d")
        except ValueError:
            raise ValueError("XXFormat de date invalide (YYYY-MM-DD requis)XX")
            
        self.id = id
        self.nom = nom
        self.date_naissance = date_naissance
        self.pathologies = pathologies or []
        self.allergies = allergies or []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_7(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("Champs obligatoires manquants")
        
        try:
            datetime.strptime(date_naissance, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Format de date invalide (YYYY-MM-DD requis)")
            
        self.id = None
        self.nom = nom
        self.date_naissance = date_naissance
        self.pathologies = pathologies or []
        self.allergies = allergies or []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_8(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("Champs obligatoires manquants")
        
        try:
            datetime.strptime(date_naissance, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Format de date invalide (YYYY-MM-DD requis)")
            
        self.id = id
        self.nom = None
        self.date_naissance = date_naissance
        self.pathologies = pathologies or []
        self.allergies = allergies or []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_9(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("Champs obligatoires manquants")
        
        try:
            datetime.strptime(date_naissance, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Format de date invalide (YYYY-MM-DD requis)")
            
        self.id = id
        self.nom = nom
        self.date_naissance = None
        self.pathologies = pathologies or []
        self.allergies = allergies or []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_10(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("Champs obligatoires manquants")
        
        try:
            datetime.strptime(date_naissance, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Format de date invalide (YYYY-MM-DD requis)")
            
        self.id = id
        self.nom = nom
        self.date_naissance = date_naissance
        self.pathologies = pathologies and []
        self.allergies = allergies or []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_11(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
        if not all([id, nom, date_naissance]):
            raise ValueError("Champs obligatoires manquants")
        
        try:
            datetime.strptime(date_naissance, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Format de date invalide (YYYY-MM-DD requis)")
            
        self.id = id
        self.nom = nom
        self.date_naissance = date_naissance
        self.pathologies = None
        self.allergies = allergies or []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_12(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
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
        self.allergies = allergies and []
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_13(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
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
        self.allergies = None
        self.contacts_urgence = contacts_urgence or []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_14(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
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
        self.contacts_urgence = contacts_urgence and []
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_15(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
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
        self.contacts_urgence = None
        self._integrity_hash = self._calculate_hash()
    def xǁPatientǁ__init____mutmut_16(self, id, nom, date_naissance, pathologies=None, allergies=None, contacts_urgence=None):
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
        self._integrity_hash = None

    xǁPatientǁ__init____mutmut_mutants = {
    'xǁPatientǁ__init____mutmut_1': xǁPatientǁ__init____mutmut_1, 
        'xǁPatientǁ__init____mutmut_2': xǁPatientǁ__init____mutmut_2, 
        'xǁPatientǁ__init____mutmut_3': xǁPatientǁ__init____mutmut_3, 
        'xǁPatientǁ__init____mutmut_4': xǁPatientǁ__init____mutmut_4, 
        'xǁPatientǁ__init____mutmut_5': xǁPatientǁ__init____mutmut_5, 
        'xǁPatientǁ__init____mutmut_6': xǁPatientǁ__init____mutmut_6, 
        'xǁPatientǁ__init____mutmut_7': xǁPatientǁ__init____mutmut_7, 
        'xǁPatientǁ__init____mutmut_8': xǁPatientǁ__init____mutmut_8, 
        'xǁPatientǁ__init____mutmut_9': xǁPatientǁ__init____mutmut_9, 
        'xǁPatientǁ__init____mutmut_10': xǁPatientǁ__init____mutmut_10, 
        'xǁPatientǁ__init____mutmut_11': xǁPatientǁ__init____mutmut_11, 
        'xǁPatientǁ__init____mutmut_12': xǁPatientǁ__init____mutmut_12, 
        'xǁPatientǁ__init____mutmut_13': xǁPatientǁ__init____mutmut_13, 
        'xǁPatientǁ__init____mutmut_14': xǁPatientǁ__init____mutmut_14, 
        'xǁPatientǁ__init____mutmut_15': xǁPatientǁ__init____mutmut_15, 
        'xǁPatientǁ__init____mutmut_16': xǁPatientǁ__init____mutmut_16
    }

    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPatientǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁPatientǁ__init____mutmut_mutants"), *args, **kwargs)
        return result 

    __init__.__signature__ = _mutmut_signature(xǁPatientǁ__init____mutmut_orig)
    xǁPatientǁ__init____mutmut_orig.__name__ = 'xǁPatientǁ__init__'



    def xǁPatientǁ_calculate_hash__mutmut_orig(self):
        return hashlib.sha256(f"{self.id}{self.nom}{self.date_naissance}".encode()).hexdigest()

    xǁPatientǁ_calculate_hash__mutmut_mutants = {

    }

    def _calculate_hash(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPatientǁ_calculate_hash__mutmut_orig"), object.__getattribute__(self, "xǁPatientǁ_calculate_hash__mutmut_mutants"), *args, **kwargs)
        return result 

    _calculate_hash.__signature__ = _mutmut_signature(xǁPatientǁ_calculate_hash__mutmut_orig)
    xǁPatientǁ_calculate_hash__mutmut_orig.__name__ = 'xǁPatientǁ_calculate_hash'


