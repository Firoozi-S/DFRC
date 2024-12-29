import numpy as np


VALID_MODES = {
    'single_subcarrier': 1,
    'uniform_distribution': 2,
    'uniform_extraction': 3,
    'random_distribution': 4,
    'all_subcarrier': 5
}

class _OFDM():
    def __init__(self,
                 num_c: int,
                 ofdm_symbol_period: float,
                 subcarrier_interval: float,
                 carrier_freq: float
                 ) -> None:
        
        if num_c <= 0:
            return
        
        if carrier_freq <= 0 or subcarrier_interval <= 0 or ofdm_symbol_period <= 0:
            return
        
        self._num_c = num_c
        self._ofdm_symbol_period = ofdm_symbol_period
        self._subcarrier_interval = subcarrier_interval
        self._carrier_freq = carrier_freq
        pass

    def sub_carrier_freqs(self, num_bs: int):

        antenna_index = np.concatenate([np.arange(0, num_bs).reshape(-1,1)]* self._num_c,
                                        axis=1)
        current_sc = np.concatenate([np.arange(1, self._num_c + 1).reshape(1,-1)]*num_bs, 
                                    axis=0)

        sc_freqs = self._carrier_freq + (antenna_index * self._num_c + current_sc) * self._subcarrier_interval

        print(VALID_MODES['all_subcarrier'])
        return sc_freqs