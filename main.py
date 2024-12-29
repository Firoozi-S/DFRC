from dfrc import DFRC

CARRIER_FREQ = 5.725e9 # Hz
SUBCARRIER_INTERVAL = 312.5e3 # Hz
OFDM_SYMBOL_PERIOD = 3.2e-6 # Sec
NUM_BS = 16 # Antennas
NUM_C = 4 # Number of Subcarriers
NUM_UE = 4 # Antennas

dfrc = DFRC(CARRIER_FREQ,
            SUBCARRIER_INTERVAL,
            OFDM_SYMBOL_PERIOD,
            NUM_BS,
            NUM_C,
            NUM_UE)

dfrc('None')


