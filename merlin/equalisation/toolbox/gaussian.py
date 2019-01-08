import numpy as np


class Gaus:
    """Class for generating a Gaussian on the form Gaus.equation() with
        norm 1 times area, mean at mu and standard deviation of sigma.
        x is a numpy.ndarray of arbitrary size, respective y values for
        the generated gaussian can be accessed through Gaus.y.
    """

    def __init__(self, x, area: float, mu: float, sigma: float):
        self.x = x
        self.area = area
        self.mu = mu
        self.sigma = sigma
        self.y = self.area/np.sqrt(2*np.pi*self.sigma**2) * \
            np.exp(-(self.x-self.mu)**2/(2*self.sigma**2))

    def equation(self):
        return 'f(x)=area/sqrt(2 pi sigma^2) exp(-(x-mu)^2/(2 sigma^2))'

    def generate(self):
        self.y = self.area/np.sqrt(2*np.pi*self.sigma**2) * \
            np.exp(-(self.x-self.mu)**2/(2*self.sigma**2))