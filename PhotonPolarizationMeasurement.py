import math
import random

class PhotonPolarizationMeasurement:
    def __init__(self, angle):
        self.polarization_angle = angle

    # Measurement returns True for "aligned" and False for "anti-aligned"
    # Qubit value 1 = Aligned (True)
    # Qubit value 0 = Anti-Aligned (False)
    # Observe how measurement causes the state to change
    def measure_polarization(self, angle):
        diff_angle = angle - self.polarization_angle
        cos_diff_angle = math.cos(math.radians(diff_angle))
        probability_align = cos_diff_angle * cos_diff_angle
        probability_anti_align = 1 - probability_align

        if random.random() < probability_align:
            self.polarization_angle = angle
            return True  # True means "Aligned"
        else:
            self.polarization_angle = angle + 90
            return False  # False means "Anti-Aligned"

if __name__ == "__main__":
    # Experiment 1 (comment out Experiment 2 when enabling Experiment 1)
    # photon = PhotonPolarizationMeasurement(90)
    # for i in range(5):
    #     print(photon.measure_polarization(45))

    # Experiment 2
    true_count = 0
    false_count = 0

    for _ in range(1000):
        photon = PhotonPolarizationMeasurement(0)
        if photon.measure_polarization(90):
            true_count += 1
        else:
            false_count += 1

    # Mapping: True to 1, and False to 0
    mean = (1.0 * true_count + 0 * false_count) / (true_count + false_count)
    variance = ((1.0 - mean) ** 2 * true_count + mean ** 2 * false_count) / (true_count + false_count)
    standard_deviation = math.sqrt(variance)
    
    print(f"MEAN: {mean}\nStandard Deviation: {standard_deviation}")
