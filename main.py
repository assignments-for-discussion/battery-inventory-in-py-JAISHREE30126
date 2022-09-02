
def count_batteries_by_usage(cycles):
  #create a dict to store value of each count
  count_dict={
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }
  for cycle in cycles:
    if(cycle<400):
      count_dict["lowCount"]+=1
    elif(cycle<920):
      count_dict["mediumCount"]+=1
    else:
      count_dict["highCount"]+=1
  return count_dict

def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
