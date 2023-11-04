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

Entanglement is a fundamental phenomenon in quantum mechanics where two or more particles become correlated in such a way that the state of one particle is directly related to the state of the other, regardless of the distance between them.

Measurement breaks Entanglement: the act of observing or measuring one of the entangled particles. When you measure an entangled particle, its state collapses to a definite value, and due to the entanglement, the state of the other particle also becomes definite. However, this act of measurement effectively breaks the entanglement between the particles.

The effect of entanglement is reflected in the measurement: even though the act of measurement breaks the entanglement, the outcomes of the measurements on both particles will still be correlated because of their previous entangled state. For instance, if two particles are entangled in such a way that if one is measured to be in state A, the other will be in state B, and vice versa, then measuring one and finding it in state A will instantly tell us that the other is in state B, even if they are light-years apart.


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

# Q-Sharp Kitchen Sink

I added a Q# kitchen sink from Kumaresan's course, but updated to use latest Q# syntax and language features. His program from his teaching materials no longer works as it uses deprecated language features.

I left most of the experiments uncommented, but they need to be selectively used to get the desired quantum effects.

[Code](kitchen_sink_q_sharp.qs)