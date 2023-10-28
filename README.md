# Photon Entanglement Simulator

A python version of the java-based simulator by Kumaresan Ramanathan. 

To run the simulator, experiment with the parameters:

```python
pairPrediction = EntangledPhotonMeasurement(0.707106, 0, 0, 0.707106)
pairPrediction.set_measurement_angles(90, 90)
```

Note that the parameters for EntangledPhotonMeasurement are for the states: `00, 01, 10, 11`

Here they are set to the square root of 2, considering that the probabilities are the square of the parameters.
Hence, in this case this means our superimposed probabilities are: 

```text
Probability of 00 = 0.50
Probability of 01 = 0.00
Probability of 10 = 0.00
Probability of 11 = 0.50
```

To set the measurement apparatus angles:

```python
pairPrediction.set_measurement_angles(90, 90)
```

