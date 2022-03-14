from replit import db


def add_algo():
  db["linear search"] = ["psedo code", "O(n)", "O(1)"]
  db["binary search"] = ["psedo code",  "O(log n)", "O(1)"]
  db["jump search"] = ["psedo code", "O(n^-2)", "O(1)"]
  db["interpolation search"] = ["psedo code", "O(n)", "O(1)"]
  db["exponential search"] = ["psedo code", "time complexity", "space complexity"]
  db["ternary search"] = ["psedo code","O(log3 n)", "O(1)"]

  db["selection sort"] = ["psedo code", "O(n^2)", "O(1)"]
  db["bubble search"] = ["psedo code", "O(n^2)", "O(1)"]
  db["insertion sort"] = ["psedo code", "O(n^2)", "O(1)"]
  db["merge sort"] = ["psedo code", "O(nlog n)", "O(1)"]
  db["heap sort"] = ["psedo code", "time complexity", "space complexity"]
  db["quick sort"] = ["psedo code", "O(nlog n)", "O(n)"]
  db["radix sort"] = ["psedo code", "O(nd)", "O(n+2^d)"]
  db["counting sort"] = ["psedo code", "O(n+k)", "O(n+r)"]
  db["bucket sort"] = ["psedo code", "O(n^2)", "O(n+k)"]
  db["shell sort"] = ["psedo code", "O(n^2)", "O(1)"]
  db["comb sort"] = ["psedo code", "O(n^2)", "O(1)"]
  db["pigeonhole sort"] = ["psedo code", "O(n+2^k)", "O(2^k)"]
  db["cycle sort"] = ["psedo code", "O(n^2)", "O(1)"]

  
def clear_db():
  del db["algos"]