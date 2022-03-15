from replit import db


def addAlgo(algo_name):
  algo_name = algo_name.lower()
  if algo_name in db.keys():
    return "Algorithm already in database"
  else:
    db[algo_name] = {"time_complexity" : "", "space_complexity" : ""}
    return "Algorithm added."


def addTimeComplexity(algo_name, time_complexity):
  db[algo_name]["time_complexity"] = time_complexity
  return "Time complexity added"

def addSpaceComplexity(algo_name, space_complexity):
  db[algo_name]["space_complexity"] = space_complexity
  return "Space complexity added."

  
def delDb():
  for i in db:
    del db[i]
  return "Database deleted."

def delAlgo(algo_name):
  del db[algo_name]
  return "Algorithm deleted."