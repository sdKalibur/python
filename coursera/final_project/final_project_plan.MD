# Final Project

## Problem Statement
* inputs:
  * Ticky app syslog file events
    * success
    * error
  * Generate usage stats:

### Desired outcome
* regex to parse syslog
* append and modify values in dictionary
* Move files to appropriet directory to use with CSV->HTML  converter

## Research



## Planning
* testing:
  * check only 'ticky' app logs are matched i,e correct group/column in log file
  * check for string match
  * check for string match position
  * check for string match among other characters e,g 'ben' NOT 'burdenned'
* Order of operation:
  1. find matching *ticky* events
  2. separate failures and successful events
  3. append to *ticky* events report
## Writing
