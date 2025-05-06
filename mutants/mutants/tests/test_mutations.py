import os
import subprocess

def test_mutations():
    # S'assure que pytest et mutmut voient dmp.py/patients.py à la racine
    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd()

    # 1) lance Mutmut ; renvoie 0 si *aucun* mutant n'a survécu
    result = subprocess.run(
        ["mutmut", "run"],
        capture_output=True,
        text=True,
        env=env
    )
    assert result.returncode == 0, (
        "🤖 Des mutants ont survécu ! Détail mutmut:\n"
        f"{result.stdout}\n{result.stderr}"
    )
