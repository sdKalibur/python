#! /usr/bin/env python3

import os, requests

feedback_dir = '/data/feedback'
url = 'http://34.67.208.199/feedback'
#print(os.listdir(feedback_dir))

feedback_files = os.listdir('/data/feedback') 
all_feedback = []

for file in feedback_files :
    with open( feedback_dir + '/' + file, 'r') as f:    
        #print(f.readlines())
        fd = f.readlines()
        all_feedback.append({'title':fd[0], 'name':fd[1], 'date':fd[2], 'feeback':fd[3]})
    f.close()

print(all_feedback)

request.post(url, all_feedback)

