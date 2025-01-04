import numpy as np

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

    def get_num_c(self) -> int:
        return self._num_c

    def sub_carrier_freqs(self, num_bs: int):
        sc_freqs = self._carrier_freq + np.arange(0, self._num_c) * self._subcarrier_interval
        sc_freqs = sc_freqs.reshape(1,-1)
        sc_freqs = np.concatenate([sc_freqs]*num_bs, 0)
        return sc_freqs