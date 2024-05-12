import numpy as np

from particleswarm.swarm import Swarm


class SwarmRastrigin(Swarm):
    def __init__(
        self,
        swarmsize,
        minvalues,
        maxvalues,
        currentVelocityRatio,
        localVelocityRatio,
        globalVelocityRatio,
    ):
        super().__init__(
            swarmsize,
            minvalues,
            maxvalues,
            currentVelocityRatio,
            localVelocityRatio,
            globalVelocityRatio,
        )

    def _finalFunc(self, position):
        function = 10.0 * len(self.minvalues) + sum(
            position * position - 10.0 * np.cos(2 * np.pi * position)
        )
        penalty = self._getPenalty(position, 10000.0)

        return function + penalty
