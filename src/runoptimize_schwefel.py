from swarm_schwefel import SwarmSchwefel
from utils import printResult


if __name__ == "__main__":
    iterCount = 300

    dimension = 3
    swarmsize = 2000

    minvalues = [-500.0] * dimension
    maxvalues = [500.0] * dimension

    currentVelocityRatio = 0.5
    localVelocityRatio = 2.0
    globalVelocityRatio = 5.0

    swarm = SwarmSchwefel(
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
