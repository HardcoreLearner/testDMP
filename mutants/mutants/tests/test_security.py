import pytest
from dmp import DossierMedical
from patients import Patient

def test_suppression_definitive():
    dmp = DossierMedical()
    patient = Patient(1, "Test", "2000-01-01")
    
    dmp.ajouter_patient(patient)
    dmp.supprimer_patient(1)
    
    # Vérification suppression
    assert not any(p.id == 1 for p in dmp.patients)
    
    # Vérification présence dans les logs
    assert any(
        "Suppression patient 1" in entry['action']
        for entry in dmp.access_log
    )