
# Simule une détection d'arbitrage entre deux cotes
def detect_arbitrage(odds1, odds2):
    return (1/odds1 + 1/odds2) < 1
