from SigmoidBoostCalcs import userBoost

# Makes CSV File and prints data to screen
# ---------------------------------------
import csv
f = open('test.csv', 'w', newline='')
writer = csv.writer(f)
#make CSV(.01 day increments)
for x in range(0, 18001, 1):
    print(f"{x/100},{userBoost(x/100)}")
    writer.writerow([x/100, userBoost(x/100)])
f.close()
