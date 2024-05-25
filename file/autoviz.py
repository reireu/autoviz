import pandas as pd
import numpy as np
from autoviz.AutoViz_Class import AutoViz_Class

df = pd.read_csv("./data/coordinate.csv")
df.head()

autoviz = AutoViz_Class().AutoViz("./data/Boston.csv")
