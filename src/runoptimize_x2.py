import numpy as np

from swarm_x2 import SwarmX2
from utils import printResult


if __name__ == "__main__":
    iterCount = 300

    dimension = 5
    swarmsize = 200

    minvalues = np.array([-100] * dimension)
    maxvalues = np.array([100] * dimension)

    currentVelocityRatio = 0.1
    localVelocityRatio = 1.0
    globalVelocityRatio = 5.0

    swarm = SwarmX2(
        swarmsize,
        minvalues,
        maxvalues,
        currentVelocityRatio,
        localVelocityRatio,
        globalVelocityRatio,
    )

    for n in range(iterCount):
        print("Position", swarm[0].position)
        print("Velocity", swarm[0].velocity)
        print(printResult(swarm, n))

        swarm.nextIteration()
