def regex_test(line):
  import re
  try:
    print re.search(r'(\w+\.)(\w+\.?)*([a-zA-Z])+\(?\)?', line).group().replace(" ","").replace("(","").replace(")","")
  except:
    pass

def parse(file_name):
  lines = open(file_name,'r')
  for line in lines:
    regex_test(line)

parse("test.txt")
