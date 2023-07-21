

class Decay:

    @staticmethod
    def calculate_decay(decay_factor, observation_period=100, normalize=True):
        unnormalized_decay = []
        normalized_decay = []
        for i in range(observation_period):
            unnormalized_decay.append((1-decay_factor) * decay_factor ** i)

        if normalize:
            total = sum(unnormalized_decay)
            for decay in unnormalized_decay:
                normalized_decay.append(decay /total)
            return normalized_decay

        return unnormalized_decay

