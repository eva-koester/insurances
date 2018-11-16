with open('beschwerden.csv') as snabb:
  #  print(snabb.readline())
  # print(snabb.readline())
    for line in snabb:
        print("Original:", line)
        print("Splitted:", line.strip().split(","))

    line = snabb.readline().split(',')
    print(line)
        #row = snabb.readline()
   # print(row)
   # for i in range (0, 10):
  #     line = row.split(',')
     #  print(line)


