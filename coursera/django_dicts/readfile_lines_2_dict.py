#! /usr/bin/env python3

import os, requests

feedback_dir = '/data/feedback'
url = 'http://35.223.29.59/feedback/'
#print(os.listdir(feedback_dir))

feedback_files = os.listdir('/data/feedback') 
all_feedback = []

for file in feedback_files :
    with open( feedback_dir + '/' + file, 'r') as f:    
        #print(f.readlines())
        fd = f.readlines()
        #print(fd)
        all_feedback.append({'title':fd[0].strip(), 'name':fd[1].strip(), 'date':fd[2].strip(), 'feedback':fd[3].strip()})
    f.close()

#print(all_feedback)

for i in all_feedback:
    print('Will post : {}'.format(i))
    post = requests.post(url, data = i)
    print(post.status_code)
#requests.post(url, all_feedback)
