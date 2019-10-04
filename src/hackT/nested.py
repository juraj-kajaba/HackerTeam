""" Day 26: Nested Logic """

def getFine(dayDue : int, monthDue : int, yearDue : int, dayAct : int, monthAct : int, yearAct) -> int:
    fine = 0

    if yearAct > yearDue:
        fine = 10000
    elif yearAct == yearDue:
        if monthAct > monthDue:
            fine = 500 * (monthAct - monthDue)
        elif monthAct == monthDue and dayAct > dayDue:
            fine = 15 * (dayAct - dayDue)

    return fine            

