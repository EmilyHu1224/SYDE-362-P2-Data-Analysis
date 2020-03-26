import csv
refFile = 'control_test_failures/Control Test-100-0.csv'
resFile = 'res.csv'

ref = []
with open(refFile) as csvfile:
  r = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in r:
    f = row[2]
    if f == 'Delay':
      continue
    
    ref.append(f[0])

res = []
with open(resFile) as csvfile:
  r = csv.reader(csvfile, delimiter=',', quotechar='|')
  
  skippedFirstRow = False
  for row in r:
    if not skippedFirstRow:
      skippedFirstRow = True
      continue

    f = row[1]
    res.append(f)

error_count = 0

if len(res) != len(ref):
  print("Result length doesn't match: {} :((".format(len(res)))
else:
  for i in range(len(res)):
    if res[i] != ref[i]:
    	error_count += 1
    	print("Result type doesn't match at index {}: ref = {}, res = {}".format(i, ref[i], res[i]))

total_count = len(res)
correct_count = total_count - error_count
accuracy = 1. * correct_count / total_count * 100
print("Accuracy: {}/{} = {}%".format(correct_count, total_count, accuracy))