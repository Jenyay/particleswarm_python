import numpy as np

from swarm_rastrigin import SwarmRastrigin
from utils import printResult


if __name__ == "__main__":
    iterCount = 300

    dimension = 4
    swarmsize = 2000

    minvalues = np.array([-5.12] * dimension)
    maxvalues = np.array([5.12] * dimension)

    currentVelocityRatio = 0.5
    localVelocityRatio = 2.0
    globalVelocityRatio = 5.0

    swarm = SwarmRastrigin(
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
