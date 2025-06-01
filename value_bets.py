
# Simule une détection simple de value bets
def detect_value_bet(odds, probability):
    expected_value = (odds * probability) - 1
    return expected_value > 0
