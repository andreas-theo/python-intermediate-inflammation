"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

from functools import reduce
import numpy as np


class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)


class Person:
    """A person."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Patient(Person):
    """A patient in an inflammation study."""

    def __init__(self, name, observations=None):
        super().__init__(name)
        self.observations = []
        if observations is not None:
            self.observations = observations

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation

    def __str__(self):
        return self.name


class Doctor(Person):
    """A doctor in an inflammation study."""

    def __init__(self, name, patients):
        super().__init__(name)
        self.patients = patients

    def add_patient(self, name):
        if name in set(self.patients):
            raise ValueError(f'Patient {name} already exists')
        new_patient = Patient(name)
        self.patients.append(new_patient)
        return new_patient

    def add_patients(self, names):
        map(self.add_patient, names)

    def __str__(self):
        return self.name


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: An array containing the inflammation data.
    :return: A daily mean of the inflammation data."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: An array containing the inflammation data.
    :return: A daily max of the inflammation data."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: An array containing the inflammation data.
    :return: A daily min of the inflammation data."""
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    data_max = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / data_max[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised


def daily_std(data):
    """Calculate the daily standard deviation of a 2D inflammation data array.

    :param data: An array containing the inflammation data.
    :return: A daily standard deviation of the inflammation data."""
    return np.std(data, axis=0)


def daily_above_threshold(patient_row, data, threshold):
    """Find the daily values that are above a threshold for a given patient.

    :param patient_row: Row index corresponding to a patient.
    :param data: An array containing the inflammation data.
    :param threshold: Threshold for the patient.
    :return: A list of booleans describing whether each value if above the threshold."""
    above_threshold = map(lambda daily_value: daily_value > threshold, data[patient_row])
    nr_above_threshold = reduce(lambda a, b: a + 1 if b else a, above_threshold, 0)
    return nr_above_threshold


def attach_names(patient_matrix, patient_names):
    # Check that the rows in the matrix are as many as the names
    assert patient_matrix.shape[0] == len(patient_names)
    list_of_names_and_data = []
    for name, data in zip(patient_names, patient_matrix):
        list_of_names_and_data.append({'name': name, 'data': data})
    return list_of_names_and_data
