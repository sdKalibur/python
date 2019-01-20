#!/usr/bin/env python3

# Running pace converter

def get_dist_run_km():
    print('Enter distance you run in Kilometers')
# try
#    global dist_run_km
    dist_run_km = float(input())
    print('You clean to have run ' + str(dist_run_km) + ' Kilometers' )
    return dist_run_km

def dist_miles(dist_run_km):
#    dist_run_km = float(1.7)
    global dist_run_miles
    dist_run_miles = float(dist_run_km) / 1.609
    print('Distance run in miles is ' + str(dist_run_miles) )
    return dist_run_miles

def get_time_run():
    global time_run_min
    print('Enter time you run in minutes')
    time_run_min = float(input())
    print('You claim to have run for ' + str(time_run_min) + ' minutes')
    print('Enter the number of seconds you run extra to the minutes above, if any. ')
    time_run_secs = int(input())    
    print('You claim to have run for an extra ' + str(time_run_secs) + ' seconds')
    time_run_min = time_run_min + (time_run_secs / 60 )
    return time_run_min

def avg_run_pace_mile(t_min, d_mile):
    print('Your running pace in minutes per miles is:')
    pace_mile = t_min / d_mile
    return pace_mile
    

# get_dist_run_km()
#print('You total run time is ' + str(get_time_run()) + ' minutes')

# print('You ran at a pace of: ' + str(avg_run_pace_mile()) + 'minutes per mile')
# print('You covered ' + str(dist_run_miles) + ' miles ')
#dist_miles() 
#print('You covered ' + str(dist_miles()) + ' miles ')


print(avg_run_pace_mile(get_time_run(), dist_miles(get_dist_run_km())))

# avg_run_pace_mile(float(time_run_min) , float(dist_run_miles))

