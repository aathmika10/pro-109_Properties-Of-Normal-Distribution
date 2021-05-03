import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff

df=pd.read_csv("StudentsPerformance.csv")
readingScore=df["reading score"].to_list()

mean=statistics.mean(readingScore)
median=statistics.median(readingScore)
stdDev=statistics.stdev(readingScore)
mode=statistics.mode(readingScore)

print("mean, median, standard deviation, mode of the reading score is {},{},{},{}".format(mean,median,stdDev,mode))

FirstStart,FirstEnd =mean-stdDev,mean+stdDev
SecondStart,SecondEnd=mean-(2*stdDev),mean+(2*stdDev)
ThirdStart,ThirdEnd=mean-(3*stdDev),mean+(3*stdDev)

listOf1stStdDev=[result for result in readingScore if result >FirstStart and result<FirstEnd]
listOf2ndStdDev=[result for result in readingScore if result >SecondStart and result<SecondEnd ]
listOf3rdStdDev=[result for result in readingScore if result >ThirdStart and result<ThirdEnd]

print("{}% of data lies within 1 standard deviation".format(len(listOf1stStdDev)*100.0/len(readingScore)))
print("{}% of data lies within 2 standard deviation".format(len(listOf2ndStdDev)*100.0/len(readingScore)))
print("{}% of data lies within 3 standard deviation".format(len(listOf3rdStdDev)*100.0/len(readingScore)))

fig=ff.create_distplot([readingScore],["reading score"],show_hist=False)
fig.show()