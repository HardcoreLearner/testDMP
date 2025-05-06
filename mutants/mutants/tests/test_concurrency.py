import threading
from dmp import DossierMedical
from patients import Patient
import pytest

def test_acces_concurrent():
    dmp = DossierMedical()
    patient = Patient(1, "Concurrent", "2000-01-01")
    dmp.ajouter_patient(patient)
    
    def modifier_pathologie():
        for _ in range(100):
            dmp.ajouter_pathologie(1, "Allergie")

    threads = [threading.Thread(target=modifier_pathologie) for _ in range(10)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    assert len(dmp.patients[0].pathologies) == 1000