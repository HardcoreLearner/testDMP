import timeit
from faker import Faker
from dmp import DossierMedical
from patients import Patient

def test_perf_recherche():
    fake = Faker()
    dmp = DossierMedical()
    test_name = "PerfTest_123"  # Nom unique pour le test
    
    # Génération de 10k patients avec 1 patient connu
    for i in range(1, 10001):
        name = test_name if i == 5000 else fake.name()
        dmp.ajouter_patient(Patient(i, name, fake.date_of_birth().strftime('%Y-%m-%d')))
    
    # Mesure sur le nom connu
    temps = timeit.repeat(
        lambda: dmp.rechercher_patient(test_name),
        number=10,
        repeat=5
    )
    
    avg_time = sum(temps) / len(temps) / 10  # Moyenne en secondes
    assert avg_time < 0.1  # 100ms maximum