from time import time, localtime, strftime

current_time = time()

print("Seconds since January 1, 1970: {0:,.4f} or {0:.2e} \
in scientific notation".format(current_time))

print(strftime( "%b %d %Y" ,localtime(current_time)) )
