import os
import pandas as pd

pairs=[
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-056.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-056.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-057.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-057.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-058.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-058.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-059.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-059.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-060.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-060.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-061.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-061.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-062.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-062.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-063.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-063.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-064.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-064.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-065.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-065.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-066.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-066.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-067.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-067.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-068.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-068.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-069.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-069.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-070.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-070.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-071.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-071.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-072.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-072.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-073.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-073.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-074.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-074.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-075.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-075.csv'],
    ['TEST_V1_18_16_2021_EN_DmakingLeidy-076.csv','2TEST_V1_18_16_2021_EN_DmakingLeidy-076.csv'],
]

for f1, f2 in pairs:
  df1 = pd.read_csv(f'Behaviour_1/{f1}', header=1, sep=';')
  df2 = pd.read_csv(f'./Behaviour_2/{f2}', header=2, sep=';')


  b1=df1.loc[df1.shape[0]-1].Block
  t1=df1.loc[df1.shape[0]-1].TrialNr
  c1=df1.loc[df1.shape[0]-1].BlockNr
  d1=df1.loc[df1.shape[0]-1].StockSum
  e1=df1.loc[df1.shape[0]-1]['TrialList.Cycle']
  g1=df1.loc[df1.shape[0]-1]['TrialList.Sample']

  
  df2.Block+=b1
  df2.TrialNr+=t1
  df2.BlockNr+=c1
  df2.StockSum+=d1
  df2['TrialList.Cycle']+=e1
  df2['TrialList.Sample']+=g1


  df3=df1.append(df2)

  f3=f'Behaviour_12/{f1}' + '.csv'
  df3.to_csv(f3)

print("Done")