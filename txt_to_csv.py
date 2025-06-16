from collections import defaultdict
import pandas as pd

def converter():
  with open("data.txt", "r") as f:
    data = f.read()
    blocks = data.split("*** Circuit ***") # splits the data into a list of blocks for each unique circuit

    stats = defaultdict(list)  # list of lists for each statistic that grows as needed
    i = 0  # index of each statistic

    for block in blocks[1:]:
      index = block.find("Communication time (s)")
      block = block[index:-2]

      lines = block.split('\n')
      block = [line.lstrip() for line in lines]

      for statistic in block:
        colon_index = statistic.find(":")
        statistic = statistic[colon_index + 1:]
        stats[i].append(statistic)
        i += 1

      i = 0

    # call your dataframes here
    circuit2575, circuit5050, circuit7525 = ltmPorts(stats)
    link_width = linkWidth(stats)
    noc_clock = nocClock(stats)

    # add your dataframes to df_list
    df_list = [circuit2575, circuit5050, circuit7525, link_width, noc_clock]
    plain_text = toPlainText(df_list)
  
  with open("data.csv", "w") as f:
    f.write(plain_text)

# generates default table of each statistic
def buildTable(stats, start, end):
  table = {
      "Communication time (s)": stats[0][start:end + 1],
      "EPR pair generation time (s)": stats[1][start:end + 1],
      "EPR pair distribution time (s)": stats[2][start:end + 1],
      "Pre-processing time (s)": stats[3][start:end + 1],
      "Classical transfer time (s)": stats[4][start:end + 1],
      "Post-processing time (s)": stats[5][start:end + 1],
      "Computation time (s)": stats[6][start:end + 1],
      "Fetch time (s)": stats[7][start:end + 1],
      "Decode time (s)": stats[8][start:end + 1],
      "Dispatch time (s)": stats[9][start:end + 1],
      "Execution time (s)": stats[10][start:end + 1],
      "Coherence (%)": stats[11][start:end + 1]
  }
  return table

# converts dataframes to plain text for csv file
def toPlainText(df_list):
  plain_text = ""
  for df in df_list:
    text = df.to_csv(index=False)
    plain_text += "\n" + text + "\n"
  return plain_text

'''
to analyze another parameter, add a function similar to the ones below:
  - call buildTable() with the corresponding start and end indices in your blocks of data
  - define your variable parameter as a dictionary and add it to the dictionary returned by buildTable()
  - convert the dictionary to a dataframe and return it
'''

def ltmPorts(stats):
  table1 = buildTable(stats, 0, 4)
  table2 = buildTable(stats, 5, 9)
  table3 = buildTable(stats, 10, 14)
  param = {"LTM Ports": [1, 2, 3, 4, 5]}
  new_table1 = {**param, **table1}
  new_table2 = {**param, **table2}
  new_table3 = {**param, **table3}
  df1 = pd.DataFrame(new_table1)
  df2 = pd.DataFrame(new_table2)
  df3 = pd.DataFrame(new_table3)
  return df1, df2, df3

def linkWidth(stats):
  table = buildTable(stats, 15, 19)
  param = {"Link width (bits)": [2, 4, 6, 8, 10]}
  new_table = {**param, **table}
  df = pd.DataFrame(new_table)
  return df

def nocClock(stats):
  table = buildTable(stats, 20, 29)
  param = {"NoC Clock Speed (MHz)" : [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]}
  new_table = {**param, **table}
  df = pd.DataFrame(new_table)
  return df

if __name__ == "__main__":
  converter()