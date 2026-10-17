from pathlib import Path


def test_files_exist():
    expected = [
        "Basic.py",
        "Task-01.py",
        "Task-02.py",
        "Task-03.py",
        "Task-04.py",
        "Task-05.py",
        "Task-06.py",
        "class-student.py",
        "polymorphishm.py",
        "2-digits.py",
        "3-digits.py",
        "Inheritence.py",
    ]
    for f in expected:
        assert Path(f).exists(), f"{f} is missing from the repository root"


def test_pytest_sanity():
    # Basic sanity test so pytest never reports "collected 0 items" in CI
    assert 1 + 1 == 2
