""" Day 28: RegEx, Patterns, and Intro to Databases test """


from hackT import re_ex

def test_1():           
    # test data
    arr = [
        'riya riya@gmail.com'.split(' '),
        'julia julia@julia.me'.split(' '),
        'julia sjulia@gmail.com'.split(' '),
        'julia julia@gmail.com'.split(' '),
        'samantha samantha@gmail.com'.split(' '),
        'tanya tanya@gmail.com'.split(' ')]

    o = re_ex.getGmailUsers(arr)

    assert o == ['julia', 'julia', 'riya', 'samantha', 'tanya']

test_1()
