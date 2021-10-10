import json 
import os 
from math import exp 
team = "Chennai Super Kings"
directory_for_data = ###
def get_data(): 
  dataset = []
  for filename in os.listdir(directory_for_data):
    if filename.endswith(".json"):
        f = open(os.path.join(directory_for_data, filename), 'r')
        file = json.load(f)
        total_5overs = 0 
        total_20overs = 0 
        wickets_5overs = 0 
        try:
         for h in range(2):
          for i in range(6): 
            for j in range(6): 
              if file["info"]["outcome"]["winner"] == team:
                win_or_loss = 1 
              if file["info"]["outcome"]["winner"] != team:
                win_or_loss = 0
              if file["innings"][h]["team"] == team:
                total_5overs += file["innings"][h]["overs"][i]["deliveries"][j]["runs"]["total"] 
                try:
                  if file["innings"][h]["overs"][i]["deliveries"][j]["wickets"]:
                    wickets_5overs += 1 
                except:
                  continue 
        except:
          continue
        try: 
         for h in range(2):
          for i in range(20): 
            for j in range(6): 
              if file["innings"][h]["team"] == team:
                total_20overs += file["innings"][h]["overs"][i]["deliveries"][j]["runs"]["total"] 
        except:
          continue
        list_for_dataset = [total_5overs, wickets_5overs, total_20overs, win_or_loss]
        dataset.append(list_for_dataset)
  return dataset 

def mean(values):
    return sum(values) / float(len(values))

def variance(values, mean):
    return sum([(value - mean) ** 2 for value in values]) 
  
def covariance(x,mean_x,y,mean_y):
    covar = 0.0
    for i in range(len(x)):
     covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar  

def coefficients(dataset):
    x1 = [data[0] for data in dataset] 
    x2 = [data[1] for data in dataset]
    y = [data[2] for data in dataset] 
    x1_mean, x2_mean, y_mean = mean(x1), mean(x2), mean(y)
    b1 = covariance(x1, x1_mean, y, y_mean) / variance(x1, x1_mean) 
    b2 = covariance(x2, x2_mean, y, y_mean) / variance(x2, x2_mean) 
    b0 = y_mean - b1 * x1_mean - b2 * x2_mean
    return b0, b1, b2
 
def linear_regression(train, inp):
  	b0, b1, b2 = coefficients(train) 
  	y_pred = b0 + b1 * inp[0] + b2 * inp[1]
  	return y_pred 
  	
def main():
  print("\n*****SCORE PREDICTOR*****\n")
  dataset = get_data()
  current_score = int(input("What's the score at 5 overs ? \n\n")) 
  print("\n")
  current_wicket = int(input("How many wickets at 5 overs ? \n\n")) 
  print("\n")
  inp_for_score_prediction = [current_score, current_wicket]
  predicted_score = linear_regression(dataset, inp_for_score_prediction) 
  print("From the calculations with previous match records, Maximum score might be,\n")
  print("\n")
  print(round(predicted_score)) 
  print("\n")
if __name__ == '__main__':
  main()
