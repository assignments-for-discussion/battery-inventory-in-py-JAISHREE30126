
def count_batteries_by_usage(cycles):
  #create a dict to store value of each count
  dict={
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }
  for i in cycles:
    if(i<400):
      dict["lowCount"]+=1
    elif(i<920):
      dict["mediumCount"]+=1
    else:
      dict["highCount"]+=1
  return dict

def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
