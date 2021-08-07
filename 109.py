import random
import statistics
import plotly.figure_factory as ff
import pandas as pd
import csv

df=pd.read.csv("perform.csv")
math_list=df["math score"].tolist()
math_mean=statistics.mean(math_list)
math_mode=statistics.mode(math_list)
math_median=statistics.median(math_list)

