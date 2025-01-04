from dfrc import DFRC
import numpy as np

CARRIER_FREQ = 5.725e9 # Hz
SUBCARRIER_INTERVAL = 312.5e3 # Hz
OFDM_SYMBOL_PERIOD = 3.2e-6 # Sec
NUM_BS = 4 # Antennas
NUM_C = 8 # Number of Subcarriers
NUM_UE = 4 # Antennas

dfrc = DFRC(CARRIER_FREQ,
            SUBCARRIER_INTERVAL,
            OFDM_SYMBOL_PERIOD,
            NUM_BS,
            NUM_C,
            NUM_UE)

num_c = 3
num_bs = 2
packet = np.random.default_rng().integers(2, size=int(np.power(2, num_c + num_bs)))
dfrc(packet, num_c, num_bs)


