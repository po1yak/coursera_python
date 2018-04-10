import sys

num_steps = cur_step = int(sys.argv[1])
cur_str = ''

while cur_step > 0:
    for i in range(1,cur_step):
        cur_str = cur_str + " "
    for i in range(cur_step,num_steps + 1):
        cur_str = cur_str + "#"
    cur_step -= 1
    print(cur_str)
    cur_str = ""
