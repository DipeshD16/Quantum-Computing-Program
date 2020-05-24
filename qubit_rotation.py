import pennylane as qml
from pennylane import numpy as np
dev1 = qml.device("default.qubit", wires=1)
@qml.qnode(dev1)
def circuit(params):
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=0)
    return qml.expval(qml.PauliZ(0))
print(circuit([0.54,0.12]))
dcircuit = qml.grad(circuit, argnum=0)
print(dcircuit([0.54, 0.12]))

def cost(x):
    return circuit(x)
init_params = np.array([0.11, 0.12])
print(cost(init_params))
opt = qml.GradientDescentOptimizer(stepsize=0.4)
steps = 100
params = init_params
for i in range(steps):
    params = opt.step(cost, params)
    if (i+1)%5==0:
        print("Cost after step {:5d}: {: .7f}".format(i+1, cost(params)))
print("optimized rotation angle: {}".format(params))
