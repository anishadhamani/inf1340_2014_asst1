#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        if grade in ("A+", "A-", "A", "B+", "B-", "B", "FZ"):
            letter_grade = grade
            print("The grade entered is ", letter_grade)

        else:
            print("Error")
            raise ValueError("Out of range input")

        # remove this line once the code is implemented
        # check that the grade is one of the accepted values
        # assign grade to letter_grade
    elif type(grade) is int:
        print("The grade entered is", grade)

        # remove this line once the code is implemented
        if 100 >= grade >= 0:
            letter_grade = grade
            letter_grade = mark_to_letter(grade)
            #print(letter_grade)
        else:
            print("Error")
            raise ValueError("Out of range input")
        # check that grade is in the accepted range
        # convert the numeric grade to a letter grade
        # assign the value to letter_grade
         # letter_grade = grade
        # hint: letter_grade = mark_to_letter(grade)

    else:
          # raise a TypeError exception
        print("error")
        raise TypeError("Invalid type passed as parameter")

    # write a long if-statement to convert letter_grade
    # assign the value to gpa
    if letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A+":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    elif letter_grade == "FZ":
        gpa = 0.0
    print("The corresponding gpa is ", gpa)
    return gpa


def mark_to_letter(grade):
    letter_grade = ""
    if 100 >= grade >= 90:
        letter_grade = "A+"
    elif 89 >= grade >= 85:
        letter_grade = "A"
    elif 84 >= grade >= 80:
        letter_grade = "A-"
    elif 79 >= grade >= 77:
        letter_grade = "B+"
    elif 76 >= grade >= 73:
        letter_grade = "B"
    elif 72 >= grade >= 70:
        letter_grade = "B-"
    elif 69 >= grade >= 0:
        letter_grade = "FZ"
    return letter_grade

