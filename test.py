import re, time

t1 = time.time()


re.match(r"^(a+)+$", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaab")




print(time.time() - t1)