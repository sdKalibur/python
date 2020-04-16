# Final Project

## Problem Statement
* inputs:
  * Ticky app syslog file events
    * success
    * error
    * user anme
  * Generate usage stats:

### Desired outcome
Two reports:
  1. ranking of error messeges:
    * sorted by most common
    * total number of events
    * exclude user info
  2. Usage stats
    * list of all users who have used Ticky
    * For each user:
      * INFO events logged
      * ERROR events logged


* regex to parse syslog
* append and modify values in dictionary
* Move files to appropriet directory to use with CSV->HTML  converter

## Research
sample event:
  *May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#6767] (username)*
### Tools, libs, modules
* re - regex modules
* csv - read and write CSV
* python/bash - to run the script(s)


## Planning
* testing:
  * check only 'ticky' app logs are matched i,e correct group/column in log file
  * check for string match
  * check for string match position
  * check for string match among other characters e,g 'ben' NOT 'burdenned'

### Order of operation:
  1. find matching *ticky* events
  2. separate failures and successful events
  3. append to *ticky* events report

###  Report 1 Error rankings:
  - dict of Error Message : number of errors
    Errors = {'Error msg1' : 5 , 'Error msg2' : 34 }
  * Generate a report order by desc by value.

### Report Two: usage stats
  - dict per user with two keys 'Success' and 'errors'
    dict username = {'Successful': 10 , 'Errored': 5 }
* data types:
  1. dictionary
  2. strings
  3. int (values)

## Writing
