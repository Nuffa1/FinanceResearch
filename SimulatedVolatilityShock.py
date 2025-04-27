import numpy as np

def monte_carlo_option_price(S0, K, T, r, sigma, N=10000, M=100):
    dt = T / M
    payoffs = []

    for _ in range(N):
        S = S0
        for _ in range(M):
            Z = np.random.normal()
            S = S * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
        payoff = max(S - K, 0)  # For call option
        payoffs.append(payoff)

    option_price = np.exp(-r * T) * np.mean(payoffs)
    return option_price
print(monte_carlo_option_price(200,220,	1.0,	0.05,	0.8,	10000,	100))
