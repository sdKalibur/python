def avg_run_pace_mile(w, h):
#    try:
        pace_mile = w / h
        return pace_mile
 #   except IncorrectInputValueTypeError:
 #       print('You\'ve entered an incorrect value type please enter only numberic data')
q = 10
z = 5
try:
    print(avg_run_pace_mile(q, z))
except ZeroDivisionError:
     print('You\'ve entered an incorrect value type please enter only numberic data')
    
