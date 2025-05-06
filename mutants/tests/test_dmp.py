import pytest
from dmp import DossierMedical
from patients import Patient

class TestDMPUnit:
    def test_ajout_suppression(self):
        dmp = DossierMedical()
        patient = Patient(1, "Test", "2000-01-01")
        
        dmp.ajouter_patient(patient)
        assert len(dmp.patients) == 1
        
        dmp.supprimer_patient(1)
        assert len(dmp.patients) == 0

    def test_recherche_inexistant(self):
        dmp = DossierMedical()
        assert len(dmp.rechercher_patient("Inconnu")) == 0

    def test_ajout_pathologie_validation(self):
        dmp = DossierMedical()
        dmp.ajouter_patient(Patient(1, "Test", "2000-01-01"))
        
        dmp.ajouter_pathologie(1, "Diabète")
        assert "Diabète" in dmp.patients[0].pathologies
        
        with pytest.raises(ValueError):
            dmp.ajouter_pathologie(999, "Invalid")