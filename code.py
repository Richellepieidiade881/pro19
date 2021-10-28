import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv 
import pandas as pd 
df=pd.read_csv("StudentsPerformance.csv")
score_list=df["reading score" ].to_list()
score_mean=statistics.mean(score_list)
score_median=statistics.median(score_list)
score_mode=statistics.mode(score_list)
score_sd=statistics.stdev(score_list)
print(score_mean,score_median,score_mode,score_sd)
score_fsds , score_fsde=score_mean - score_sd,score_mean + score_sd
score_ssds , score_ssd=score_mean - (2 * score_sd) , score_mean +(2*score_sd)
score_tsds , score_tsd=score_mean - (3* score_sd) , score_mean +(2* score_sd)
score_data_fsd=[result for result in score_list if result > score_fsds and result < score_fsde]
score_data_ssd=[result for result in score_list if result > score_ssds and result < score_ssd]
score_data_tsd=[result for result in score_list if result > score_tsds and result < score_tsd]
print(format(len(score_data_fsd) * 100 /len (score_list)))
print(format(len(score_data_ssd)*100/len(score_list)))
print(format(len(score_data_tsd)*100/len(score_list)))
