# Photon Simulator

A python version of the java-based simulator by Kumaresan Ramanathan for learning the principles of quantum computing.

## Entanglement Simulator

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

## Polarization Measurement Simulator

Set the polarization of the photon via:

```python
photon = PhotonPolarizationMeasurement(0)
```

And set the measurement angle (filter angle) via:

```python
photon.measure_polarization(90)
```

The output will give the probability of polarization and the standard deviation.
For angles like those given above `(0, 90)`, the output should be deterministic behavior:

```
MEAN: 0.0
Standard Deviation: 0.0
```

But for a photo/measurement angle like, say, `(0, 45)`, it would be probabilistic and something like close to `0.5`:

```
MEAN: 0.491
Standard Deviation: 0.4999189934379369
```

