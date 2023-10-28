import math
import random
from decimal import Decimal, ROUND_HALF_UP

class EntangledPhotonMeasurement:
    def __init__(self, i00, i01, i10, i11):
        # Initialize the state probabilities for the photons
        self.p00 = i00
        self.p01 = i01
        self.p10 = i10
        self.p11 = i11

        # Check if probabilities add up to approximately 1 (within a small range)
        check = self.p00 ** 2 + self.p01 ** 2 + self.p10 ** 2 + self.p11 ** 2
        if check > 1.01 or check < 0.99:
            print("Error: Probabilities must add up to 1")

    def format_number(self, value):
        # Format a number to two decimal places
        return str(Decimal(value).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))

    def square(self, value):
        # Calculate the square of a value
        return value * value

    def set_independent_photon_angles(self, angle1, angle2):
        # Set the photon state based on independent angles
        r1 = math.radians(angle1)
        r2 = math.radians(angle2)
        self.p00 = math.cos(r1) * math.cos(r2)
        self.p01 = math.cos(r1) * math.sin(r2)
        self.p10 = math.sin(r1) * math.cos(r2)
        self.p11 = math.sin(r1) * math.sin(r2)

    def set_measurement_angles(self, angle1, angle2):
        # Set the measurement angles for the photons
        self.m1angle = angle1
        self.m2angle = angle2
        r1 = math.radians(angle1)
        r2 = math.radians(angle2)
        self.m00 = math.cos(r1) * math.cos(r2)
        self.m01 = math.cos(r1) * math.sin(r2)
        self.m10 = math.sin(r1) * math.cos(r2)
        self.m11 = math.sin(r1) * math.sin(r2)

    def report_measurement_probability(self):
        # Compute and print measurement probabilities

        # Store original measurement angles
        original_p1angle = self.m1angle
        original_p2angle = self.m2angle

        # Calculate probability for measuring 11
        prob11 = self.square((self.p00 * self.m00) + (self.p01 * self.m01) + (self.p10 * self.m10) + (self.p11 * self.m11))

        # Set measurement angles for 01
        self.set_measurement_angles(90 + original_p1angle, original_p2angle)
        prob01 = self.square((self.p00 * self.m00) + (self.p01 * self.m01) + (self.p10 * self.m10) + (self.p11 * self.m11))

        # Set measurement angles for 10
        self.set_measurement_angles(original_p1angle, original_p2angle + 90)
        prob10 = self.square((self.p00 * self.m00) + (self.p01 * self.m01) + (self.p10 * self.m10) + (self.p11 * self.m11))

        # Set measurement angles for 00
        self.set_measurement_angles(90 + original_p1angle, 90 + original_p2angle)
        prob00 = self.square((self.p00 * self.m00) + (self.p01 * self.m01) + (self.p10 * self.m10) + (self.p11 * self.m11))

        # Reset to original measurement angles
        self.set_measurement_angles(original_p1angle, original_p2angle)

        # Print the probabilities
        print("Probability of 00 =", self.format_number(prob00))
        print("Probability of 01 =", self.format_number(prob01))
        print("Probability of 10 =", self.format_number(prob10))
        print("Probability of 11 =", self.format_number(prob11))

        too_small = 0.00001
        if prob01 + prob11 > too_small:
            print("Probability of Photon1 measured to be 1, given that Photon2 was measured to be 1 =", self.format_number(prob11 / (prob01 + prob11)))
        if prob10 + prob00 > too_small:
            print("Probability of Photon1 measured to be 1, given that Photon2 was measured to be 0 =", self.format_number(prob10 / (prob10 + prob00)))
        if prob01 + prob11 > too_small:
            print("Probability of Photon1 measured to be 0, given that Photon2 was measured to be 1 =", self.format_number(prob01 / (prob01 + prob11)))
        if prob10 + prob00 > too_small:
            print("Probability of Photon1 measured to be 0, given that Photon2 was measured to be 0 =", self.format_number(prob00 / (prob10 + prob00)))

        if prob10 + prob11 > too_small:
            print("Probability of Photon2 measured to be 1, given that Photon1 was measured to be 1 =", self.format_number(prob11 / (prob10 + prob11)))
        if prob01 + prob00 > too_small:
            print("Probability of Photon2 measured to be 1, given that Photon1 was measured to be 0 =", self.format_number(prob01 / (prob01 + prob00)))
        if prob10 + prob11 > too_small:
            print("Probability of Photon2 measured to be 0, given that Photon1 was measured to be 1 =", self.format_number(prob10 / (prob10 + prob11)))
        if prob01 + prob00 > too_small:
            print("Probability of Photon2 measured to be 0, given that Photon1 was measured to be 0 =", self.format_number(prob00 / (prob01 + prob00)))

    def perform_measurement(self):
        # Perform a measurement and update the photon states

        # Store original measurement angles
        original_p1angle = self.m1angle
        original_p2angle = self.m2angle

        # Calculate probability for measuring 11
        prob11 = self.square((self.p00 * self.m00) + (self.p01 * self.m01) + (self.p10 * self.m10) + (self.p11 * self.m11))

        # Set measurement angles for 01
        self.set_measurement_angles(90 + original_p1angle, original_p2angle)
        prob01 = self.square((self.p00 * self.m00) + (self.p01 * self.m01) + (self.p10 * self.m10) + (self.p11 * self.m11))

        # Set measurement angles for 10
        self.set_measurement_angles(original_p1angle, original_p2angle + 90)
        prob10 = self.square((self.p00 * self.m00) + (self.p01 * self.m01) + (self.p10 * self.m10) + (self.p11 * self.m11))

        # Set measurement angles for 00
        self.set_measurement_angles(90 + original_p1angle, 90 + original_p2angle)
        prob00 = self.square((self.p00 * self.m00) + (self.p01 * self.m01) + (self.p10 * self.m10) + (self.p11 * self.m11))

        # Reset to original measurement angles
        self.set_measurement_angles(original_p1angle, original_p2angle)

        # Generate a random number to simulate measurement outcome
        rand = random.random()

        if rand < prob00:
            angle1 = self.m1angle + 90
            angle2 = self.m2angle + 90
            self.set_independent_photon_angles(angle1, angle2)
            print("-------------------------------------------------------")
            print("Measured 00")
            print("After measurement, the photon angles are", self.format_number(angle1), "and", self.format_number(angle2), "and the photon state is", self.format_number(self.p00), self.format_number(self.p01), self.format_number(self.p10), self.format_number(self.p11))
        elif rand < prob00 + prob01:
            angle1 = self.m1angle + 90
            angle2 = self.m2angle
            self.set_independent_photon_angles(angle1, angle2)
            print("-------------------------------------------------------")
            print("Measured 01")
            print("After measurement, the photon angles are", self.format_number(angle1), "and", self.format_number(angle2), "and the photon state is", self.format_number(self.p00), self.format_number(self.p01), self.format_number(self.p10), self.format_number(self.p11))
        elif rand < prob00 + prob01 + prob10:
            angle1 = self.m1angle
            angle2 = self.m2angle + 90
            self.set_independent_photon_angles(angle1, angle2)
            print("-------------------------------------------------------")
            print("Measured 10")
            print("After measurement, the photon angles are", self.format_number(angle1), "and", self.format_number(angle2), "and the photon state is", self.format_number(self.p00), self.format_number(self.p01), self.format_number(self.p10), self.format_number(self.p11))
        else:
            angle1 = self.m1angle
            angle2 = self.m2angle
            self.set_independent_photon_angles(angle1, angle2)
            print("-------------------------------------------------------")
            print("Measured 11")
            print("After measurement, the photon angles are", self.format_number(angle1), "and", self.format_number(angle2), "and the photon state is", self.format_number(self.p00), self.format_number(self.p01), self.format_number(self.p10), self.format_number(self.p11))

if __name__ == "__main__":
    # Compute probabilities. But we don't make any measurement. So the Photon state is not changed.
    pairPrediction = EntangledPhotonMeasurement(0.707106, 0, 0, 0.707106)
    pairPrediction.set_measurement_angles(90, 90)
    pairPrediction.report_measurement_probability()

    # Perform some measurements. Measurements will change the photon states.
    for i in range(100):
        pairExperiment = EntangledPhotonMeasurement(0.707106, 0, 0, 0.707106)
        pairExperiment.set_measurement_angles(90, 90)
        pairExperiment.perform_measurement()
