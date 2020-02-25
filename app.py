import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
import sys


# TO DO, get combinations 'year/code' and generate GRAPHS... Only 3 graphs to show an example atm...      
GRAPHS = [
  {
    'year':'1891',
    'code': 'MA0'
  },
  {
    'year':'1891',
    'code': 'MA1'
  },
  {
    'year':'1891',
    'code': 'MA2'
  }
]


#
# EXAMPLE BELOW :
#
# 'EVENT_CODE': {
#   'cols' : [index of names column, index of perfs column, index of date column],
#   'title' : 'Discipline Human readable name'
# }
#
# TO DO : put that fuckin long dictionnary in a json file bruh pliz
CODES = {
  'MA0': {
    'cols' : [2,4,8],
    'title': '100y - Hommes'
  },
  'MA1': {
    'cols' : [2,4,8],
    'title': '100m - Hommes'
  },
  'MA2': {
    'cols' : [2,4,8],
    'title': '200m - Hommes'
  },
  'MA3': {
    'cols' : [2,4,8],
    'title': '400m - Hommes'
  },
  'MA4': {
    'cols' : [2,4,8],
    'title': '800m - Hommes'
  },
  'MA5': {
    'cols' : [2,4,8],
    'title': '1500m - Hommes'
  },
  'MA6': {
    'cols' : [2,4,8],
    'title': '1Mile - Hommes'
  },
  'MA7': {
    'cols' : [2,4,8],
    'title': '5000m - Hommes'
  },
  'MA8': {
    'cols' : [2,4,8],
    'title': '10000m - Hommes'
  },
  'MA9': {
    'cols' : [2,4,8],
    'title': 'Marathon - Hommes'
  },
  'MB1': {
    'cols' : [2,4,8],
    'title': '110m Haies - Hommes'
  },
  'MB2': {
    'cols' : [2,4,8],
    'title': '400m Haies - Hommes'
  },
  'MB3': {
    'cols' : [2,4,8],
    'title': '3000m Course d\'obstacles à cheval - Hommes'
  },
  'MC1': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'MC2': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'MC3': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'ME1': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'ME2': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'MF1': {
    'cols' : [2,4,8],
    'title': 'Saut en hauteur - Hommes'
  },
  'MF2': {
    'cols' : [2,4,8],
    'title': 'Saut à la perche - Hommes'
  },
  'MF3': {
    'cols' : [2,4,8],
    'title': 'Saut en longueur - Hommes'
  },
  'MF4': {
    'cols' : [2,4,8],
    'title': 'Triple saut - Hommes'
  },
  'MF5': {
    'cols' : [2,4,8],
    'title': 'Lancer de poids - Hommes'
  },
  'MF6': {
    'cols' : [2,4,8],
    'title': 'Lancer de disque - Hommes'
  },
  'MF7': {
    'cols' : [2,4,8],
    'title': 'Lancer de marteau - Hommes'
  },
  'MF8': {
    'cols' : [2,4,8],
    'title': 'Lancer de javelot - Hommes'
  },
  'MF9': {
    'cols' : [2,4,8],
    'title': 'Decathlon - Hommes'
  },
  'WA1': {
    'cols' : [2,4,8],
    'title': '100m - Femmes'
  },
  'WA2': {
    'cols' : [2,4,8],
    'title': '200m - Femmes'
  },
  'WA3': {
    'cols' : [2,4,8],
    'title': '400m - Femmes'
  },
  'WA4': {
    'cols' : [2,4,8],
    'title': '800m - Femmes'
  },
  'WA5': {
    'cols' : [2,4,8],
    'title': '1500m - Femmes'
  },
  'WA6': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'WA7': {
    'cols' : [2,4,8],
    'title': '5000m - Femmes'
  },
  'WA8': {
    'cols' : [2,4,8],
    'title': '10000m - Femmes'
  },
  'WA9': {
    'cols' : [2,4,8],
    'title': 'Marathon - Femmes'
  },
  'WB1': {
    'cols' : [2,4,8],
    'title': '110m Haies - Femmes'
  },
  'WB2': {
    'cols' : [2,4,8],
    'title': '400m Haies - Femmes'
  },
  'WB3': {
    'cols' : [2,4,8],
    'title': '3000m Course d\'obstacles à cheval - Femmes'
  },
  'WC1': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'WC2': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'WC3': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'WE1': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'WE2': {
    'cols' : [2,4,8],
    'title': '?'
  },
  'WF1': {
    'cols' : [2,4,8],
    'title': 'Saut en hauteur - Femmes'
  },
  'WF2': {
    'cols' : [2,4,8],
    'title': 'Saut à la perche - Femmes'
  },
  'WF3': {
    'cols' : [2,4,8],
    'title': 'Saut en longueur - Femmes'
  },
  'WF4': {
    'cols' : [2,4,8],
    'title': 'Triple saut - Femmes'
  },
  'WF5': {
    'cols' : [2,4,8],
    'title': 'Lancer de poids - Femmes'
  },
  'WF6': {
    'cols' : [2,4,8],
    'title': 'Lancer de disque - Femmes'
  },
  'WF7': {
    'cols' : [2,4,8],
    'title': 'Lancer de marteau - Femmes'
  },
  'WF8': {
    'cols' : [2,4,8],
    'title': 'Lancer de javelot - Femmes'
  },
  'WF9': {
    'cols' : [2,4,8],
    'title': 'Pentathlon/Heptathlon - Femmes'
  }
}

def get_csv_data(name):
  dir_path = os.path.dirname(os.path.realpath(__file__)) + '/data'
  csv = os.path.join(dir_path, name)
  data = pd.read_csv(csv + '.csv', encoding="utf-8", sep=";") 
  return data

def get_clean_data(title):
  data = get_csv_data(title)
  indexes = CODES[title.split('_')[1]]['cols']
  df = format_to_ndc(data, indexes, title.split('_')[0])
  return df

def format_to_ndc(data, indexes, year): # Outputs name, date, perf columns
  names = data.iloc[0:len(data.index),indexes[0]]
  perfs = data.iloc[0:len(data.index),indexes[1]]
  date = data.iloc[0:len(data.index),indexes[2]]
  df = pd.DataFrame({
    'name':names,
    'date':date + ' ' + year,
    'perf':perfs,
  })
  df = df.dropna()
  df['date'] = df['date'].apply(lambda dat: dat.split()[0] + ' 01 ' + dat.split()[1] if not isinstance(dat, float) and len(dat.split()) == 2 else dat)
  df['date'] = pd.to_datetime(df['date'], format='%b %d %Y')
  return df.sort_values(by ='date')

def plot_line_graph(graph_dict):
  title = graph_dict['year'] + '_' + graph_dict['code']
  human_title = CODES[graph_dict['code']]['title'] + ' (année ' + graph_dict['year']+ ')'
  df = get_clean_data(title)
  return dcc.Graph(
      id = title,
      figure = {
          'data': [
              {'x': df['date'], 'y': df['perf'], 'type': 'line', 'name': 'Performances'},
          ],
          'layout': {
              'title': human_title,
              'yaxis': {
                  'range': [min(df['perf']),max(df['perf'])]
              }
          }
      }
  )

layout_arr = [
    html.H1(children="Athlétisme - Performances")
]

for graph in GRAPHS:
  layout_arr.append(plot_line_graph(graph))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(children=layout_arr)

if __name__ == '__main__':
    app.run_server(debug=True)


#   _____            _            _              _                  
#  |  __ \          | |          (_)            | |                 
#  | |  | | __ _ ___| |__         _ ___       __| | ___  _ __   ___ 
#  | |  | |/ _` / __| '_ \       | / __|     / _` |/ _ \| '_ \ / _ \
#  | |__| | (_| \__ \ | | |      | \__ \    | (_| | (_) | |_) |  __/
#  |_____/ \__,_|___/_| |_|      |_|___/     \__,_|\___/| .__/ \___|
#                                                       | |         
#                                                       |_|        
