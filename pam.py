#!/usr/bin/env python2
'''
PAM module for authenticating users via a onelogin email/username and OTP
'''
# import json
import os
import sys
import syslog
import time

def logit(data):
    '''
    Logs data to stderr and syslog
    Args:
        data (*): Data to log
    Returns: None
    '''
    data_str = str(data)
    sys.stderr.write('%s\n' % data_str)
    syslog.syslog(syslog.LOG_ERR, data_str)


def pam_sm_authenticate(pamh, _flags, _argv):
    '''
    Authenticates a user via onelogin email/username and OTP
    '''
    # Load config file and build access token
    # Auth'd login
    return pamh.PAM_SUCCESS

def pam_sm_setcred(pamh, _flags, _argv):
    '''
    Default
    '''
    return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, _flags, _argv):
    '''
    Default
    '''
    return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, _flags, _argv):
    '''
    Default
    '''
    return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, _flags, _argv):
    '''
    Default
    '''
    return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, _flags, _argv):
    '''
    Default
    '''
    return pamh.PAM_SUCCESS