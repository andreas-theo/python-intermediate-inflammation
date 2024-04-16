"""Tests for the Patient model."""
from inflammation.models import Patient


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_create_doctor():
    from inflammation.models import Doctor, Patient

    patients = [Patient(name='Alice'), Patient(name='Bob')]
    name = 'House'
    doctor = Doctor(name=name, patients=patients)
    assert doctor.name == name


def test_doctor_is_person():
    from inflammation.models import Doctor, Person

    doctor = Doctor(name='Alice', patients=[Patient(name='Bob')])
    assert isinstance(doctor, Person)


def test_add_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)
    value = 5
    day = 2
    p.add_observation(value, day)
    assert p.observations[0].day == day
    assert p.observations[0].value == value
