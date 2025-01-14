# This code is part of the training "Einführung Quantencomputing"
# Author: Andreas Sturm, Fraunhofer IAO

import numpy as np

from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.visualization import plot_bloch_vector, plot_bloch_multivector
from qiskit.visualization.state_visualization import _bloch_multivector_data
from qiskit.quantum_info import Statevector

from qiskit.circuit.library import RXGate, RYGate, RZGate, HGate, XGate, YGate, ZGate, IGate
from qiskit.quantum_info import Statevector

from matplotlib.pyplot import figure

from ipywidgets import interactive, FloatSlider
from ipywidgets import RadioButtons, ToggleButtons

from IPython.display import display


theta = Parameter("$\\theta$")
phi = Parameter("$\\phi$")
circuit = QuantumCircuit(1)
circuit.ry(theta, 0)  # RY gate
circuit.p(phi, 0)     # Phase gate

def show_plot_0(latitude_num_value: float, longitute_num_value: float):
    theta_num_value = 0.5*np.pi - latitude_num_value*np.pi/180
    phi_num_value = longitute_num_value*np.pi/180
    circuit_num_values = circuit.assign_parameters({
        theta: theta_num_value, phi: phi_num_value})
    statevector = Statevector(circuit_num_values)
    display(plot_bloch_multivector(statevector))
    print("Amplitudes:")
    print(f"  a = {statevector[0]:.3f}")
    print(f"  b = {statevector[1]:.3f}")

interactive_bloch_0 = interactive(
    show_plot_0,
    latitude_num_value=FloatSlider(min=-90.0, max=90.0, value=90.0, step=10.0, description='latitude (in °)', readout_format='.0f', continuous_update=True),
    longitute_num_value=FloatSlider(min=-180.0, max=180.0, value=0.0, step=10.0, description='longitude (in °)', readout_format='.0f', continuous_update=True)
)

def show_plot_1(theta_factor: float, phi_factor: float):
    theta_num_value = theta_factor*np.pi
    phi_num_value = phi_factor*np.pi
    circuit_num_values = circuit.assign_parameters({
        theta: theta_num_value, phi: phi_num_value})
    statevector = Statevector(circuit_num_values)
    display(plot_bloch_multivector(statevector))
    # display(circuit_num_values.draw())
    print(f"θ = {theta_factor} π, φ = {phi_factor} π")
    print("Amplitudes:")
    print(f"  a = {statevector[0]:.3f}")
    print(f"  b = {statevector[1]:.3f}")

interactive_bloch_1 = interactive(
    show_plot_1,
    theta_factor=FloatSlider(min=0.0, max=1.0, description=r'$\tfrac{\theta}{\pi}$', readout_format='.2f', continuous_update=True),
    phi_factor=FloatSlider(min=0.0, max=2.0, description=r'$\tfrac{\phi}{\pi}$', readout_format='.2f', continuous_update=True)
)

ket_0 = Statevector.from_label("0")
ket_plus = Statevector.from_label("+")
ket_r = Statevector.from_label("r")
kets = [ket_0, ket_plus, ket_r]

bloch_vectors = list(map(_bloch_multivector_data, kets))
bloch_vectors = [temp[0] for temp in bloch_vectors]

def apply_gate_and_plot_result(gate):
    if gate == "I":
        op = IGate()
    if gate == "X":
        op = XGate()
    elif gate == "Y":
        op = YGate()
    elif gate == "Z":
        op = ZGate()
    elif gate == "H":
        op = HGate()
            
    evolved_kets = list(map(lambda ket: ket.evolve(op), kets))
    evolved_bloch_vectors = list(map(_bloch_multivector_data, evolved_kets))
    evolved_bloch_vectors = [temp[0] for temp in evolved_bloch_vectors]
    
    fig = figure(figsize=(12, 12))
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    plot_bloch_vector(bloch_vectors, ax=ax1, figsize=(10,10), title="original")
    plot_bloch_vector(evolved_bloch_vectors, ax=ax2, figsize=(10,10), title="evolved with "+gate)

interactive_bloch_2 = interactive(
    apply_gate_and_plot_result,
    gate=ToggleButtons(options=["I", "X", "Y", "Z", "H"], description="Gate:", value="I")
)



old_rot_gate = ""
float_slider = FloatSlider(min=0.0, max=2*np.pi, description=r'$\theta$', readout_format='.2f', continuous_update=True)

def apply_rot_gate_and_plot_result(rot_gate, theta_factor):
    global old_rot_gate
    kets = [ket_0, ket_plus, ket_r]
    if old_rot_gate != rot_gate:
        theta_factor = 0
        op = IGate()
    if rot_gate == "RX":
        op = RXGate(theta_factor*np.pi)
    elif rot_gate == "RY":
        op = RYGate(theta_factor*np.pi)
    elif rot_gate == "RZ":
        op = RZGate(theta_factor*np.pi)

    evolved_kets = list(map(lambda ket: ket.evolve(op), kets))
    evolved_bloch_vectors = list(map(_bloch_multivector_data, evolved_kets))
    evolved_bloch_vectors = [temp[0] for temp in evolved_bloch_vectors]
    
    tit = f"evolved with {rot_gate}({theta_factor}π)"
    fig = figure(figsize=(12, 12))
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    plot_bloch_vector(evolved_bloch_vectors, ax=ax1, figsize=(10,10), title=tit)
    
    old_rot_gate = rot_gate
    float_slider.value = theta_factor

interactive_bloch_3 = interactive(
    apply_rot_gate_and_plot_result,
    rot_gate=RadioButtons(options=["RX", "RY", "RZ"], description="Gate:", value="RZ"),
    theta_factor=float_slider
)
