from datetime import datetime
import pytest
from dmp import DossierMedical
from patients import Patient

class TestPatient:
    def test_creation_patient_valide(self):
        p = Patient(1, "Dupont", "2000-01-01")
        assert p.id == 1
        assert "Dupont" in p.nom

    def test_controle_champs_obligatoires(self):
        with pytest.raises(ValueError):
            Patient(None, "Nom", "2000-01-01")
        
        with pytest.raises(ValueError):
            Patient(1, "", "2000-01-01")

    def test_format_date_naissance(self):
        with pytest.raises(ValueError):
            Patient(1, "Nom", "date-invalide")