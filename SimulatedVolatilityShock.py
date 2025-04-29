import numpy as np

def monte_carlo_option_price(S0, K, T, r, sigma, N=10000, M=100, dSigma =1):
    dt = T / M
    payoffs = []

    for _ in range(N):
        S = S0
        for _ in range(1, int(M/2)):
            Z = np.random.normal()
            S = S * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
        for _ in range(int((M/2) +1), M):
            Z = np.random.normal()
            S = S * np.exp((r - 0.5 * (sigma+dSigma)**2) * dt + (sigma+dSigma) * np.sqrt(dt) * Z)
        payoff = max(S - K, 0)  # For call option
        payoffs.append(payoff)

    option_price = np.exp(-r * T) * np.mean(payoffs)
    return option_price
print(monte_carlo_option_price(200,200,	0.5,	0.05,	0.8,	10000,	100, 0.8))
