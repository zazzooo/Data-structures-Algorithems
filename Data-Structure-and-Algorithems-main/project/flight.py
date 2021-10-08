import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from nams import load_data as cf
pass_air_data = cf.load_airports_data()

pass_air_data.head()
