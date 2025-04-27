import math
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, q=0.0):
    """
    Black-Scholes Option Pricing Formula

    Parameters:
    S     : Current stock price
    K     : Strike price
    T     : Time to maturity (in years)
    r     : Risk-free interest rate (annual, continuously compounded)
    sigma : Volatility of the underlying asset (annualized)
    q     : Dividend yield (annual, continuously compounded), default is 0

    Returns:
    call_price : Price of the European call option
    put_price  : Price of the European put option
    """

    if T <= 0 or sigma <= 0 or S <= 0 or K <= 0:
        raise ValueError("Inputs must be positive and time to maturity must be > 0")

    d1 = (math.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    call = S * math.exp(-q * T) * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    put  = K * math.exp(-r * T) * norm.cdf(-d2) - S * math.exp(-q * T) * norm.cdf(-d1)

    return round(call, 4), round(put, 4)

# Example usage
if __name__ == "__main__":
    S = 200      # Current stock price
    K = 220      # Strike price
    T = 1.0        # Time to maturity (in years)
    r = 0.05     # Risk-free rate (5%)
    sigma = 0.8  # Volatility (20%)
    q = 0.0      # Dividend yield (0%)

    call_price, put_price = black_scholes(S, K, T, r, sigma, q)
    print(f"Call Price: {call_price}")
    print(f"Put Price: {put_price}")
    
