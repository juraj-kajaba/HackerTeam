""" Day 12: Inheritance test"""

from hackT import inheritance


def test_1():
    s = inheritance.Student("Heraldo", "Memelli", '8135627', [100, 80])
    assert s.calculate() == 'O'

def test_2():
    s = inheritance.Student("Jozko", "Mrkvicka", '8135627', [100, 80, 40, 60, 55])
    assert s.calculate() == 'P'

def test_3():
    s = inheritance.Student("Janko", "Ferko", '8135627', [10, 80, 20, 40])
    assert s.calculate() == 'T'    
