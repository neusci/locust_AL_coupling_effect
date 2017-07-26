file_head="""#! /use/bin/env fish
# written by python script: generate_run_sh.py
\n
"""

execfile("../slow/slow_analy_head.py")

for c in range(couple_number): # which couple  range(50)
    file_ob = open('run_a_couple_%d.sh'%c, 'w')
    file_ob.write(file_head)
    for s in shift_list:
        for t in range(trial_number): # how many trials
            file_ob.write("mkdir -p %s%d/shift%d_trial%d\n"%(datadir,c,s,t))
            file_ob.write("cd %s%d/shift%d_trial%d; cp %sprcw .; ./prcw -m=%d -o=%d -r=%d > output.txt &\n"%(datadir,c,s,t,datadir,c,s,(10000*c+100*s+t)))
        file_ob.write("\n")
    file_ob.close()


'''   #previous
for c in range(couple_number): # which couple  range(50)
    file_ob = open('run_a_couple_%d.sh'%c, 'w')
    file_ob.write(file_head)
    for s in shift_list:
        for t in range(5): # range(trial_number): # how many trials
            file_ob.write("mkdir -p %s%d/shift%d_trial%d\n"%(datadir,c,s,t))
            file_ob.write("cd %s%d/shift%d_trial%d; cp %sprcw .; ./prcw -m=%d -o=%d -r=%d > output.txt &\n"%(datadir,c,s,t,datadir,c,s,(10000*c+100*s+t)))
        file_ob.write("\n")
    file_ob.close()


for c in range(couple_number): # which couple  range(50)
    file_ob = open('run_b_couple_%d.sh'%c, 'w')
    file_ob.write(file_head)
    for s in shift_list:
        for t in range(5,10): # range(trial_number): # how many trials
            file_ob.write("mkdir -p %s%d/shift%d_trial%d\n"%(datadir,c,s,t))
            file_ob.write("cd %s%d/shift%d_trial%d; cp %sprcw .; ./prcw -m=%d -o=%d -r=%d > output.txt &\n"%(datadir,c,s,t,datadir,c,s,(10000*c+100*s+t)))
        file_ob.write("\n")
    file_ob.close()


for c in range(couple_number):
    file_ob = open('run_c_couple_%d.sh'%c, 'w')
    file_ob.write(file_head)
    for s in range(1,shift_list[1]-shift_list[0]):
        for t in range(10): # range(trial_number): # how many trials
            file_ob.write("mkdir -p %s%d/shift%d_trial%d\n"%(datadir,c,s,t))
            file_ob.write("cd %s%d/shift%d_trial%d; cp %sprcw .; ./prcw -m=%d -o=%d -r=%d > output.txt &\n"%(datadir,c,s,t,datadir,c,s,(10000*c+100*s+t)))
        file_ob.write("\n")
        file_ob.close()
'''


print("done")
