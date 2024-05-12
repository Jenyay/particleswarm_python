import numpy as np

from particleswarm.swarm import Swarm


class SwarmSchwefel(Swarm):
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
        function = 418.9829 * len(position) - sum(position * np.sin(np.sqrt(np.abs(position))))
        penalty = self._getPenalty(position, 10000.0)
        return function + penalty
