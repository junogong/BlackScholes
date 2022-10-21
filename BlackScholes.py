import numpy as np
from scipy.stats import norm
from py_vollib.black_scholes import black_scholes as bs
from py_vollib.black_scholes.greeks.analytical import delta, gamma, vega, theta, rho

# Define variables
r = float(input('Annualized risk free interest rate'))
S = float(input('Underlying Price'))
K = float(input('Strike Price'))
T = float(input('Time'))
sigma = float(input('Volatility'))
option = str(input('Put or Call'))

T = T / 365

#Calculate Options price
def blackScholes(r, S, K, T, sigma, type = option):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if option == "c":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif option == "p":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price, bs(option, S, K, T, r, sigma)
    except:
        print("Please confirm the input parameters!")

print("Option Price: ", blackScholes(r, S, K, T, sigma, option))

#Calculate Delta
def delter(r, S, K, T, sigma, type = option):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    try:
        if option == "c":
            delt = norm.cdf(d1, 0, 1)
        elif option == "p":
            delt = -norm.cdf(-d1, 0, 1)
        return delt, delta(option, S, K, T, r, sigma)
    except:
        print("Please confirm the input parameters!")

print("Options Delta: ", delter(r, S, K, T, sigma, option))

#Calculate Gamma
def gammer(r, S, K, T, sigma, type = option):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        gamm = norm.pdf(d1, 0, 1)/(S*sigma*np.sqrt(T))
        return gamm, gamma(option, S, K, T, r, sigma)
    except:
        print("Please confirm the input parameters!")

print("Option Gamma: ", gammer(r, S, K, T, sigma, option))

#Calculate Vega
def vegar(r, S, K, T, sigma, type = option):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        veg = S*norm.pdf(d1, 0, 1) * np.sqrt(T)
        return veg * 0.01, vega(option, S, K, T, r, sigma)
    except:
        print("Please confirm the input parameters!")

print("Option Vega: ", vegar(r, S, K, T, sigma, option))

#Calculate Theta
def theter(r, S, K, T, sigma, type = option):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if option == "c":
            thet = -S*norm.pdf(d1, 0, 1) * sigma/(2*np.sqrt(T)) - r * K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif option == "p":
            thet = -S*norm.pdf(d1, 0, 1) * sigma/(2*np.sqrt(T)) + r * K*np.exp(-r*T)*norm.cdf(-d2, 0, 1)
        return thet/365, theta(option, S, K, T, r, sigma)
    except:
        print("Please confirm the input parameters!")

print("Option Theta: ", theter(r, S, K, T, sigma, option))

#Calculate Rho
def rhor(r, S, K, T, sigma, type = option):
    "Calculate BS price of call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if option == "c":
            rh = K*T*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif option == "p":
            rh = -K*T*np.exp(-r*T)*norm.cdf(-d2, 0, 1)
        return rh * 0.01, rho(option, S, K, T, r, sigma)
    except:
        print("Please confirm the input parameters!")

print("Option Rho: ", rhor(r, S, K, T, sigma, option))
