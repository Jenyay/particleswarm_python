from particleswarm import Swarm


class SwarmX2(Swarm):
    def __init__(
        self,
        swarmsize: int,
        minvalues: list[float],
        maxvalues: list[float],
        currentVelocityRatio: float,
        localVelocityRatio: float,
        globalVelocityRatio: float,
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
