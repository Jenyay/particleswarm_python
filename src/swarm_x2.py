from particleswarm.swarm import Swarm


class SwarmX2(Swarm):
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
        penalty = self._getPenalty(position, 10000.0)
        finalfunc = sum(position * position)

        return finalfunc + penalty
