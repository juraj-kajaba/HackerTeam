""" Day 28: RegEx, Patterns, and Intro to Databases """

import re


def getEmailDomain(email:str):
    pat = re.compile(r"^([a-z\.]+)@([a-z\.]+)$")
    m = pat.match(email)

    if m:
        groups = m.groups()
        if len(groups) == 2:
           return groups[1]

    return None


def getGmailUsers(users):
    """
    Input array is list of tupples where first agrument of tupple is name and the second one is email address.
    Function returns only these names where email has domain gmail.com in alphabetical order.    
    """
    out = []

    for usr in users:
        if getEmailDomain(usr[1]) == "gmail.com":
            out.append(usr[0])

    return sorted(out)


# Read the names
# N = int(input())
# names = []

# for N_itr in range(N):
#     firstNameEmailID = input().split()

#     firstName = firstNameEmailID[0]
#     emailID = firstNameEmailID[1]

#     names.append([firstName, emailID])


# # Print an alphabetically-ordered list of first names for every user 
# # with a gmail account. Each name must be printed on a new line.
# o = getGmailUsers(names)
# for u in o:
#     print(u)


