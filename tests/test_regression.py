from dmp import DossierMedical
from patients import Patient
import hypothesis.strategies as st
from hypothesis import given

class TestNonRegression:
    """Ensemble de tests pour vérifier l'absence de régressions"""
    
    def test_ajout_suppression_historique(self):
        """Vérifie qu'un ajout/suppression ne corrompt pas les données existantes"""
        dmp = DossierMedical()
        p1 = Patient(1, "Test", "2000-01-01")
        p2 = Patient(2, "Another", "1999-12-31")
        
        # Scénario historique qui a causé un bug
        dmp.ajouter_patient(p1)
        dmp.ajouter_patient(p2)
        dmp.supprimer_patient(1)
        
        assert len(dmp.patients) == 1
        assert dmp.patients[0].id == 2  # Regression check

    @given(
        st.integers(min_value=1),
        st.text(min_size=1),
        st.dates().map(lambda d: d.isoformat())
    )
    def test_generation_aleatoire_patients(self, id, nom, date_naissance):
        """Test property-based pour vérifier la stabilité des formats"""
        patient = Patient(id, nom, date_naissance)
        assert patient.date_naissance == date_naissance
        assert patient.nom.strip() == nom.strip()