import datetime
import pandas
import matplotlib.pyplot as plt

# Just using main.py now to rewrite the csv files to include the 'daysIntoLeague' column

# Helper function that takes the date and converts it to the corresponding day of the league (Ex: 2021-01-15 -> Day 1 of ritual league)
def adjustDate(league, date):
    if (league == "Ritual"):
        if (date == datetime.datetime.strptime("2021-01-15", "%Y-%m-%d")):
            return 1
        elif (date == datetime.datetime.strptime("2021-01-16", "%Y-%m-%d")):
            return 2
        elif (date == datetime.datetime.strptime("2021-01-17", "%Y-%m-%d")):
            return 3
        elif (date == datetime.datetime.strptime("2021-01-18", "%Y-%m-%d")):
            return 4
        elif (date == datetime.datetime.strptime("2021-01-19", "%Y-%m-%d")):
            return 5
        elif (date == datetime.datetime.strptime("2021-01-20", "%Y-%m-%d")):
            return 6
        elif (date == datetime.datetime.strptime("2021-01-21", "%Y-%m-%d")):
            return 7
        elif (date == datetime.datetime.strptime("2021-01-22", "%Y-%m-%d")):
            return 8
        elif (date == datetime.datetime.strptime("2021-01-23", "%Y-%m-%d")):
            return 9
        elif (date == datetime.datetime.strptime("2021-01-24", "%Y-%m-%d")):
            return 10
        elif (date == datetime.datetime.strptime("2021-01-25", "%Y-%m-%d")):
            return 11
        elif (date == datetime.datetime.strptime("2021-01-26", "%Y-%m-%d")):
            return 12
        elif (date == datetime.datetime.strptime("2021-01-27", "%Y-%m-%d")):
            return 13
        elif (date == datetime.datetime.strptime("2021-01-28", "%Y-%m-%d")):
            return 14
        elif (date == datetime.datetime.strptime("2021-01-29", "%Y-%m-%d")):
            return 15
        elif (date == datetime.datetime.strptime("2021-01-30", "%Y-%m-%d")):
            return 16
        elif (date == datetime.datetime.strptime("2021-01-31", "%Y-%m-%d")):
            return 17
        elif (date == datetime.datetime.strptime("2021-02-01", "%Y-%m-%d")):
            return 18
        elif (date == datetime.datetime.strptime("2021-02-02", "%Y-%m-%d")):
            return 19
        elif (date == datetime.datetime.strptime("2021-02-03", "%Y-%m-%d")):
            return 20
        elif (date == datetime.datetime.strptime("2021-02-04", "%Y-%m-%d")):
            return 21
        elif (date == datetime.datetime.strptime("2021-02-05", "%Y-%m-%d")):
            return 22
        elif (date == datetime.datetime.strptime("2021-02-06", "%Y-%m-%d")):
            return 23
        elif (date == datetime.datetime.strptime("2021-02-07", "%Y-%m-%d")):
            return 24
        elif (date == datetime.datetime.strptime("2021-02-08", "%Y-%m-%d")):
            return 25
        elif (date == datetime.datetime.strptime("2021-02-09", "%Y-%m-%d")):
            return 26
        elif (date == datetime.datetime.strptime("2021-02-10", "%Y-%m-%d")):
            return 27
        elif (date == datetime.datetime.strptime("2021-02-11", "%Y-%m-%d")):
            return 28
        elif (date == datetime.datetime.strptime("2021-02-12", "%Y-%m-%d")):
            return 29
        elif (date == datetime.datetime.strptime("2021-02-13", "%Y-%m-%d")):
            return 30
        elif (date == datetime.datetime.strptime("2021-02-14", "%Y-%m-%d")):
            return 31
        elif (date == datetime.datetime.strptime("2021-02-15", "%Y-%m-%d")):
            return 32
        elif (date == datetime.datetime.strptime("2021-02-16", "%Y-%m-%d")):
            return 33
        elif (date == datetime.datetime.strptime("2021-02-17", "%Y-%m-%d")):
            return 34
        elif (date == datetime.datetime.strptime("2021-02-18", "%Y-%m-%d")):
            return 35
        elif (date == datetime.datetime.strptime("2021-02-19", "%Y-%m-%d")):
            return 36
        elif (date == datetime.datetime.strptime("2021-02-20", "%Y-%m-%d")):
            return 37
        elif (date == datetime.datetime.strptime("2021-02-21", "%Y-%m-%d")):
            return 38
        elif (date == datetime.datetime.strptime("2021-02-22", "%Y-%m-%d")):
            return 39
        elif (date == datetime.datetime.strptime("2021-02-23", "%Y-%m-%d")):
            return 40
        elif (date == datetime.datetime.strptime("2021-02-24", "%Y-%m-%d")):
            return 41
        elif (date == datetime.datetime.strptime("2021-02-25", "%Y-%m-%d")):
            return 42
        elif (date == datetime.datetime.strptime("2021-02-26", "%Y-%m-%d")):
            return 43
        elif (date == datetime.datetime.strptime("2021-02-27", "%Y-%m-%d")):
            return 44
        elif (date == datetime.datetime.strptime("2021-02-28", "%Y-%m-%d")):
            return 45
        elif (date == datetime.datetime.strptime("2021-03-01", "%Y-%m-%d")):
            return 46
        elif (date == datetime.datetime.strptime("2021-03-02", "%Y-%m-%d")):
            return 47
        elif (date == datetime.datetime.strptime("2021-03-03", "%Y-%m-%d")):
            return 48
        elif (date == datetime.datetime.strptime("2021-03-04", "%Y-%m-%d")):
            return 49
        elif (date == datetime.datetime.strptime("2021-03-05", "%Y-%m-%d")):
            return 50
        elif (date == datetime.datetime.strptime("2021-03-06", "%Y-%m-%d")):
            return 51
        elif (date == datetime.datetime.strptime("2021-03-07", "%Y-%m-%d")):
            return 52
        elif (date == datetime.datetime.strptime("2021-03-08", "%Y-%m-%d")):
            return 53
        elif (date == datetime.datetime.strptime("2021-03-09", "%Y-%m-%d")):
            return 54
        elif (date == datetime.datetime.strptime("2021-03-10", "%Y-%m-%d")):
            return 55
        elif (date == datetime.datetime.strptime("2021-03-11", "%Y-%m-%d")):
            return 56
        elif (date == datetime.datetime.strptime("2021-03-12", "%Y-%m-%d")):
            return 57
        elif (date == datetime.datetime.strptime("2021-03-13", "%Y-%m-%d")):
            return 58
        elif (date == datetime.datetime.strptime("2021-03-14", "%Y-%m-%d")):
            return 59
        elif (date == datetime.datetime.strptime("2021-03-15", "%Y-%m-%d")):
            return 60
        elif (date == datetime.datetime.strptime("2021-03-16", "%Y-%m-%d")):
            return 61
        elif (date == datetime.datetime.strptime("2021-03-17", "%Y-%m-%d")):
            return 62
        elif (date == datetime.datetime.strptime("2021-03-18", "%Y-%m-%d")):
            return 63
        elif (date == datetime.datetime.strptime("2021-03-19", "%Y-%m-%d")):
            return 64
        elif (date == datetime.datetime.strptime("2021-03-20", "%Y-%m-%d")):
            return 65
        elif (date == datetime.datetime.strptime("2021-03-21", "%Y-%m-%d")):
            return 66
        elif (date == datetime.datetime.strptime("2021-03-22", "%Y-%m-%d")):
            return 67
        elif (date == datetime.datetime.strptime("2021-03-23", "%Y-%m-%d")):
            return 68
        elif (date == datetime.datetime.strptime("2021-03-24", "%Y-%m-%d")):
            return 69
        elif (date == datetime.datetime.strptime("2021-03-25", "%Y-%m-%d")):
            return 70
        elif (date == datetime.datetime.strptime("2021-03-26", "%Y-%m-%d")):
            return 71
        elif (date == datetime.datetime.strptime("2021-03-27", "%Y-%m-%d")):
            return 72
        elif (date == datetime.datetime.strptime("2021-03-28", "%Y-%m-%d")):
            return 73
        elif (date == datetime.datetime.strptime("2021-03-29", "%Y-%m-%d")):
            return 74
        elif (date == datetime.datetime.strptime("2021-03-30", "%Y-%m-%d")):
            return 75
        elif (date == datetime.datetime.strptime("2021-03-31", "%Y-%m-%d")):
            return 76
        elif (date == datetime.datetime.strptime("2021-04-01", "%Y-%m-%d")):
            return 77
        elif (date == datetime.datetime.strptime("2021-04-02", "%Y-%m-%d")):
            return 78
        elif (date == datetime.datetime.strptime("2021-04-03", "%Y-%m-%d")):
            return 79
        elif (date == datetime.datetime.strptime("2021-04-04", "%Y-%m-%d")):
            return 80
        elif (date == datetime.datetime.strptime("2021-04-05", "%Y-%m-%d")):
            return 81
        elif (date == datetime.datetime.strptime("2021-04-06", "%Y-%m-%d")):
            return 82
        elif (date == datetime.datetime.strptime("2021-04-07", "%Y-%m-%d")):
            return 83
        elif (date == datetime.datetime.strptime("2021-04-08", "%Y-%m-%d")):
            return 84
        elif (date == datetime.datetime.strptime("2021-04-09", "%Y-%m-%d")):
            return 85
        elif (date == datetime.datetime.strptime("2021-04-10", "%Y-%m-%d")):
            return 86
        elif (date == datetime.datetime.strptime("2021-04-11", "%Y-%m-%d")):
            return 87
        elif (date == datetime.datetime.strptime("2021-04-12", "%Y-%m-%d")):
            return 88
    elif (league == "Heist"):
        if (date == datetime.datetime.strptime("2020-09-18", "%Y-%m-%d")):
            return 1
        elif (date == datetime.datetime.strptime("2020-09-19", "%Y-%m-%d")):
            return 2
        elif (date == datetime.datetime.strptime("2020-09-20", "%Y-%m-%d")):
            return 3
        elif (date == datetime.datetime.strptime("2020-09-21", "%Y-%m-%d")):
            return 4
        elif (date == datetime.datetime.strptime("2020-09-22", "%Y-%m-%d")):
            return 5
        elif (date == datetime.datetime.strptime("2020-09-23", "%Y-%m-%d")):
            return 6
        elif (date == datetime.datetime.strptime("2020-09-24", "%Y-%m-%d")):
            return 7
        elif (date == datetime.datetime.strptime("2020-09-25", "%Y-%m-%d")):
            return 8
        elif (date == datetime.datetime.strptime("2020-09-26", "%Y-%m-%d")):
            return 9
        elif (date == datetime.datetime.strptime("2020-09-27", "%Y-%m-%d")):
            return 10
        elif (date == datetime.datetime.strptime("2020-09-28", "%Y-%m-%d")):
            return 11
        elif (date == datetime.datetime.strptime("2020-09-29", "%Y-%m-%d")):
            return 12
        elif (date == datetime.datetime.strptime("2020-09-30", "%Y-%m-%d")):
            return 13
        elif (date == datetime.datetime.strptime("2020-10-01", "%Y-%m-%d")):
            return 14
        elif (date == datetime.datetime.strptime("2020-10-02", "%Y-%m-%d")):
            return 15
        elif (date == datetime.datetime.strptime("2020-10-03", "%Y-%m-%d")):
            return 16
        elif (date == datetime.datetime.strptime("2020-10-04", "%Y-%m-%d")):
            return 17
        elif (date == datetime.datetime.strptime("2020-10-05", "%Y-%m-%d")):
            return 18
        elif (date == datetime.datetime.strptime("2020-10-06", "%Y-%m-%d")):
            return 19
        elif (date == datetime.datetime.strptime("2020-10-07", "%Y-%m-%d")):
            return 20
        elif (date == datetime.datetime.strptime("2020-10-08", "%Y-%m-%d")):
            return 21
        elif (date == datetime.datetime.strptime("2020-10-09", "%Y-%m-%d")):
            return 22
        elif (date == datetime.datetime.strptime("2020-10-10", "%Y-%m-%d")):
            return 23
        elif (date == datetime.datetime.strptime("2020-10-11", "%Y-%m-%d")):
            return 24
        elif (date == datetime.datetime.strptime("2020-10-12", "%Y-%m-%d")):
            return 25
        elif (date == datetime.datetime.strptime("2020-10-13", "%Y-%m-%d")):
            return 26
        elif (date == datetime.datetime.strptime("2020-10-14", "%Y-%m-%d")):
            return 27
        elif (date == datetime.datetime.strptime("2020-10-15", "%Y-%m-%d")):
            return 28
        elif (date == datetime.datetime.strptime("2020-10-16", "%Y-%m-%d")):
            return 29
        elif (date == datetime.datetime.strptime("2020-10-17", "%Y-%m-%d")):
            return 30
        elif (date == datetime.datetime.strptime("2020-10-18", "%Y-%m-%d")):
            return 31
        elif (date == datetime.datetime.strptime("2020-10-19", "%Y-%m-%d")):
            return 32
        elif (date == datetime.datetime.strptime("2020-10-20", "%Y-%m-%d")):
            return 33
        elif (date == datetime.datetime.strptime("2020-10-21", "%Y-%m-%d")):
            return 34
        elif (date == datetime.datetime.strptime("2020-10-22", "%Y-%m-%d")):
            return 35
        elif (date == datetime.datetime.strptime("2020-10-23", "%Y-%m-%d")):
            return 36
        elif (date == datetime.datetime.strptime("2020-10-24", "%Y-%m-%d")):
            return 37
        elif (date == datetime.datetime.strptime("2020-10-25", "%Y-%m-%d")):
            return 38
        elif (date == datetime.datetime.strptime("2020-10-26", "%Y-%m-%d")):
            return 39
        elif (date == datetime.datetime.strptime("2020-10-27", "%Y-%m-%d")):
            return 40
        elif (date == datetime.datetime.strptime("2020-10-28", "%Y-%m-%d")):
            return 41
        elif (date == datetime.datetime.strptime("2020-10-29", "%Y-%m-%d")):
            return 42
        elif (date == datetime.datetime.strptime("2020-10-30", "%Y-%m-%d")):
            return 43
        elif (date == datetime.datetime.strptime("2020-10-31", "%Y-%m-%d")):
            return 44
        elif (date == datetime.datetime.strptime("2020-11-01", "%Y-%m-%d")):
            return 45
        elif (date == datetime.datetime.strptime("2020-11-02", "%Y-%m-%d")):
            return 46
        elif (date == datetime.datetime.strptime("2020-11-03", "%Y-%m-%d")):
            return 47
        elif (date == datetime.datetime.strptime("2020-11-04", "%Y-%m-%d")):
            return 48
        elif (date == datetime.datetime.strptime("2020-11-05", "%Y-%m-%d")):
            return 49
        elif (date == datetime.datetime.strptime("2020-11-06", "%Y-%m-%d")):
            return 50
        elif (date == datetime.datetime.strptime("2020-11-07", "%Y-%m-%d")):
            return 51
        elif (date == datetime.datetime.strptime("2020-11-08", "%Y-%m-%d")):
            return 52
        elif (date == datetime.datetime.strptime("2020-11-09", "%Y-%m-%d")):
            return 53
        elif (date == datetime.datetime.strptime("2020-11-10", "%Y-%m-%d")):
            return 54
        elif (date == datetime.datetime.strptime("2020-11-11", "%Y-%m-%d")):
            return 55
        elif (date == datetime.datetime.strptime("2020-11-12", "%Y-%m-%d")):
            return 56
        elif (date == datetime.datetime.strptime("2020-11-13", "%Y-%m-%d")):
            return 57
        elif (date == datetime.datetime.strptime("2020-11-14", "%Y-%m-%d")):
            return 58
        elif (date == datetime.datetime.strptime("2020-11-15", "%Y-%m-%d")):
            return 59
        elif (date == datetime.datetime.strptime("2020-11-16", "%Y-%m-%d")):
            return 60
        elif (date == datetime.datetime.strptime("2020-11-17", "%Y-%m-%d")):
            return 61
        elif (date == datetime.datetime.strptime("2020-11-18", "%Y-%m-%d")):
            return 62
        elif (date == datetime.datetime.strptime("2020-11-19", "%Y-%m-%d")):
            return 63
        elif (date == datetime.datetime.strptime("2020-11-20", "%Y-%m-%d")):
            return 64
        elif (date == datetime.datetime.strptime("2020-11-21", "%Y-%m-%d")):
            return 65
        elif (date == datetime.datetime.strptime("2020-11-22", "%Y-%m-%d")):
            return 66
        elif (date == datetime.datetime.strptime("2020-11-23", "%Y-%m-%d")):
            return 67
        elif (date == datetime.datetime.strptime("2020-11-24", "%Y-%m-%d")):
            return 68
        elif (date == datetime.datetime.strptime("2020-11-25", "%Y-%m-%d")):
            return 69
        elif (date == datetime.datetime.strptime("2020-11-26", "%Y-%m-%d")):
            return 70
        elif (date == datetime.datetime.strptime("2020-11-27", "%Y-%m-%d")):
            return 71
        elif (date == datetime.datetime.strptime("2020-11-28", "%Y-%m-%d")):
            return 72
        elif (date == datetime.datetime.strptime("2020-11-29", "%Y-%m-%d")):
            return 73
        elif (date == datetime.datetime.strptime("2020-11-30", "%Y-%m-%d")):
            return 74
        elif (date == datetime.datetime.strptime("2020-12-01", "%Y-%m-%d")):
            return 75
        elif (date == datetime.datetime.strptime("2020-12-02", "%Y-%m-%d")):
            return 76
        elif (date == datetime.datetime.strptime("2020-12-03", "%Y-%m-%d")):
            return 77
        elif (date == datetime.datetime.strptime("2020-12-04", "%Y-%m-%d")):
            return 78
        elif (date == datetime.datetime.strptime("2020-12-05", "%Y-%m-%d")):
            return 79
        elif (date == datetime.datetime.strptime("2020-12-06", "%Y-%m-%d")):
            return 80
        elif (date == datetime.datetime.strptime("2020-12-07", "%Y-%m-%d")):
            return 81
        elif (date == datetime.datetime.strptime("2020-12-08", "%Y-%m-%d")):
            return 82
        elif (date == datetime.datetime.strptime("2020-12-09", "%Y-%m-%d")):
            return 83
        elif (date == datetime.datetime.strptime("2020-12-10", "%Y-%m-%d")):
            return 84
        elif (date == datetime.datetime.strptime("2020-12-11", "%Y-%m-%d")):
            return 85
        elif (date == datetime.datetime.strptime("2020-12-12", "%Y-%m-%d")):
            return 86
        elif (date == datetime.datetime.strptime("2020-12-13", "%Y-%m-%d")):
            return 87
        elif (date == datetime.datetime.strptime("2020-12-14", "%Y-%m-%d")):
            return 88
        elif (date == datetime.datetime.strptime("2020-12-15", "%Y-%m-%d")):
            return 89
        elif (date == datetime.datetime.strptime("2020-12-16", "%Y-%m-%d")):
            return 90
        elif (date == datetime.datetime.strptime("2020-12-17", "%Y-%m-%d")):
            return 91
        elif (date == datetime.datetime.strptime("2020-12-18", "%Y-%m-%d")):
            return 92
        elif (date == datetime.datetime.strptime("2020-12-19", "%Y-%m-%d")):
            return 93
        elif (date == datetime.datetime.strptime("2020-12-20", "%Y-%m-%d")):
            return 94
        elif (date == datetime.datetime.strptime("2020-12-21", "%Y-%m-%d")):
            return 95
        elif (date == datetime.datetime.strptime("2020-12-22", "%Y-%m-%d")):
            return 96
        elif (date == datetime.datetime.strptime("2020-12-23", "%Y-%m-%d")):
            return 97
        elif (date == datetime.datetime.strptime("2020-12-24", "%Y-%m-%d")):
            return 98
        elif (date == datetime.datetime.strptime("2020-12-25", "%Y-%m-%d")):
            return 99
        elif (date == datetime.datetime.strptime("2020-12-26", "%Y-%m-%d")):
            return 100
        elif (date == datetime.datetime.strptime("2020-12-27", "%Y-%m-%d")):
            return 101
        elif (date == datetime.datetime.strptime("2020-12-28", "%Y-%m-%d")):
            return 102
        elif (date == datetime.datetime.strptime("2020-12-29", "%Y-%m-%d")):
            return 103
        elif (date == datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")):
            return 104
        elif (date == datetime.datetime.strptime("2020-12-31", "%Y-%m-%d")):
            return 105
        elif (date == datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")):
            return 106
        elif (date == datetime.datetime.strptime("2021-01-02", "%Y-%m-%d")):
            return 107
        elif (date == datetime.datetime.strptime("2021-01-03", "%Y-%m-%d")):
            return 108
        elif (date == datetime.datetime.strptime("2021-01-04", "%Y-%m-%d")):
            return 109
        elif (date == datetime.datetime.strptime("2021-01-05", "%Y-%m-%d")):
            return 110
        elif (date == datetime.datetime.strptime("2021-01-06", "%Y-%m-%d")):
            return 111
        elif (date == datetime.datetime.strptime("2021-01-07", "%Y-%m-%d")):
            return 112
        elif (date == datetime.datetime.strptime("2021-01-08", "%Y-%m-%d")):
            return 113
        elif (date == datetime.datetime.strptime("2021-01-09", "%Y-%m-%d")):
            return 114
        elif (date == datetime.datetime.strptime("2021-01-10", "%Y-%m-%d")):
            return 115
        elif (date == datetime.datetime.strptime("2021-01-11", "%Y-%m-%d")):
            return 116
    elif (league == "Metamorph"):
        if (date == datetime.datetime.strptime("2019-12-13", "%Y-%m-%d")):
            return 1
        elif (date == datetime.datetime.strptime("2019-12-14", "%Y-%m-%d")):
            return 2
        elif (date == datetime.datetime.strptime("2019-12-15", "%Y-%m-%d")):
            return 3
        elif (date == datetime.datetime.strptime("2019-12-16", "%Y-%m-%d")):
            return 4
        elif (date == datetime.datetime.strptime("2019-12-17", "%Y-%m-%d")):
            return 5
        elif (date == datetime.datetime.strptime("2019-12-18", "%Y-%m-%d")):
            return 6
        elif (date == datetime.datetime.strptime("2019-12-19", "%Y-%m-%d")):
            return 7
        elif (date == datetime.datetime.strptime("2019-12-20", "%Y-%m-%d")):
            return 8
        elif (date == datetime.datetime.strptime("2019-12-21", "%Y-%m-%d")):
            return 9
        elif (date == datetime.datetime.strptime("2019-12-22", "%Y-%m-%d")):
            return 10
        elif (date == datetime.datetime.strptime("2019-12-23", "%Y-%m-%d")):
            return 11
        elif (date == datetime.datetime.strptime("2019-12-24", "%Y-%m-%d")):
            return 12
        elif (date == datetime.datetime.strptime("2019-12-25", "%Y-%m-%d")):
            return 13
        elif (date == datetime.datetime.strptime("2019-12-26", "%Y-%m-%d")):
            return 14
        elif (date == datetime.datetime.strptime("2019-12-27", "%Y-%m-%d")):
            return 15
        elif (date == datetime.datetime.strptime("2019-12-28", "%Y-%m-%d")):
            return 16
        elif (date == datetime.datetime.strptime("2019-12-29", "%Y-%m-%d")):
            return 17
        elif (date == datetime.datetime.strptime("2019-12-30", "%Y-%m-%d")):
            return 18
        elif (date == datetime.datetime.strptime("2019-12-31", "%Y-%m-%d")):
            return 19
        elif (date == datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")):
            return 20
        elif (date == datetime.datetime.strptime("2020-01-02", "%Y-%m-%d")):
            return 21
        elif (date == datetime.datetime.strptime("2020-01-03", "%Y-%m-%d")):
            return 22
        elif (date == datetime.datetime.strptime("2020-01-04", "%Y-%m-%d")):
            return 23
        elif (date == datetime.datetime.strptime("2020-01-05", "%Y-%m-%d")):
            return 24
        elif (date == datetime.datetime.strptime("2020-01-06", "%Y-%m-%d")):
            return 25
        elif (date == datetime.datetime.strptime("2020-01-07", "%Y-%m-%d")):
            return 26
        elif (date == datetime.datetime.strptime("2020-01-08", "%Y-%m-%d")):
            return 27
        elif (date == datetime.datetime.strptime("2020-01-09", "%Y-%m-%d")):
            return 28
        elif (date == datetime.datetime.strptime("2020-01-10", "%Y-%m-%d")):
            return 29
        elif (date == datetime.datetime.strptime("2020-01-11", "%Y-%m-%d")):
            return 30
        elif (date == datetime.datetime.strptime("2020-01-12", "%Y-%m-%d")):
            return 31
        elif (date == datetime.datetime.strptime("2020-01-13", "%Y-%m-%d")):
            return 32
        elif (date == datetime.datetime.strptime("2020-01-14", "%Y-%m-%d")):
            return 33
        elif (date == datetime.datetime.strptime("2020-01-15", "%Y-%m-%d")):
            return 34
        elif (date == datetime.datetime.strptime("2020-01-16", "%Y-%m-%d")):
            return 35
        elif (date == datetime.datetime.strptime("2020-01-17", "%Y-%m-%d")):
            return 36
        elif (date == datetime.datetime.strptime("2020-01-18", "%Y-%m-%d")):
            return 37
        elif (date == datetime.datetime.strptime("2020-01-19", "%Y-%m-%d")):
            return 38
        elif (date == datetime.datetime.strptime("2020-01-20", "%Y-%m-%d")):
            return 39
        elif (date == datetime.datetime.strptime("2020-01-21", "%Y-%m-%d")):
            return 40
        elif (date == datetime.datetime.strptime("2020-01-22", "%Y-%m-%d")):
            return 41
        elif (date == datetime.datetime.strptime("2020-01-23", "%Y-%m-%d")):
            return 42
        elif (date == datetime.datetime.strptime("2020-01-24", "%Y-%m-%d")):
            return 43
        elif (date == datetime.datetime.strptime("2020-01-25", "%Y-%m-%d")):
            return 44
        elif (date == datetime.datetime.strptime("2020-01-26", "%Y-%m-%d")):
            return 45
        elif (date == datetime.datetime.strptime("2020-01-27", "%Y-%m-%d")):
            return 46
        elif (date == datetime.datetime.strptime("2020-01-28", "%Y-%m-%d")):
            return 47
        elif (date == datetime.datetime.strptime("2020-01-29", "%Y-%m-%d")):
            return 48
        elif (date == datetime.datetime.strptime("2020-01-30", "%Y-%m-%d")):
            return 49
        elif (date == datetime.datetime.strptime("2020-01-31", "%Y-%m-%d")):
            return 50
        elif (date == datetime.datetime.strptime("2020-02-01", "%Y-%m-%d")):
            return 51
        elif (date == datetime.datetime.strptime("2020-02-02", "%Y-%m-%d")):
            return 52
        elif (date == datetime.datetime.strptime("2020-02-03", "%Y-%m-%d")):
            return 53
        elif (date == datetime.datetime.strptime("2020-02-04", "%Y-%m-%d")):
            return 54
        elif (date == datetime.datetime.strptime("2020-02-05", "%Y-%m-%d")):
            return 55
        elif (date == datetime.datetime.strptime("2020-02-06", "%Y-%m-%d")):
            return 56
        elif (date == datetime.datetime.strptime("2020-02-07", "%Y-%m-%d")):
            return 57
        elif (date == datetime.datetime.strptime("2020-02-08", "%Y-%m-%d")):
            return 58
        elif (date == datetime.datetime.strptime("2020-02-09", "%Y-%m-%d")):
            return 59
        elif (date == datetime.datetime.strptime("2020-02-10", "%Y-%m-%d")):
            return 60
        elif (date == datetime.datetime.strptime("2020-02-11", "%Y-%m-%d")):
            return 61
        elif (date == datetime.datetime.strptime("2020-02-12", "%Y-%m-%d")):
            return 62
        elif (date == datetime.datetime.strptime("2020-02-13", "%Y-%m-%d")):
            return 63
        elif (date == datetime.datetime.strptime("2020-02-14", "%Y-%m-%d")):
            return 64
        elif (date == datetime.datetime.strptime("2020-02-15", "%Y-%m-%d")):
            return 65
        elif (date == datetime.datetime.strptime("2020-02-16", "%Y-%m-%d")):
            return 66
        elif (date == datetime.datetime.strptime("2020-02-17", "%Y-%m-%d")):
            return 67
        elif (date == datetime.datetime.strptime("2020-02-18", "%Y-%m-%d")):
            return 68
        elif (date == datetime.datetime.strptime("2020-02-19", "%Y-%m-%d")):
            return 69
        elif (date == datetime.datetime.strptime("2020-02-20", "%Y-%m-%d")):
            return 70
        elif (date == datetime.datetime.strptime("2020-02-21", "%Y-%m-%d")):
            return 71
        elif (date == datetime.datetime.strptime("2020-02-22", "%Y-%m-%d")):
            return 72
        elif (date == datetime.datetime.strptime("2020-02-23", "%Y-%m-%d")):
            return 73
        elif (date == datetime.datetime.strptime("2020-02-24", "%Y-%m-%d")):
            return 74
        elif (date == datetime.datetime.strptime("2020-02-25", "%Y-%m-%d")):
            return 75
        elif (date == datetime.datetime.strptime("2020-02-26", "%Y-%m-%d")):
            return 76
        elif (date == datetime.datetime.strptime("2020-02-27", "%Y-%m-%d")):
            return 77
        elif (date == datetime.datetime.strptime("2020-02-28", "%Y-%m-%d")):
            return 78
        elif (date == datetime.datetime.strptime("2020-02-29", "%Y-%m-%d")):
            return 79
        elif (date == datetime.datetime.strptime("2020-03-01", "%Y-%m-%d")):
            return 80
        elif (date == datetime.datetime.strptime("2020-03-02", "%Y-%m-%d")):
            return 81
        elif (date == datetime.datetime.strptime("2020-03-02", "%Y-%m-%d")):
            return 82
        elif (date == datetime.datetime.strptime("2020-03-03", "%Y-%m-%d")):
            return 83
        elif (date == datetime.datetime.strptime("2020-03-04", "%Y-%m-%d")):
            return 84
        elif (date == datetime.datetime.strptime("2020-03-05", "%Y-%m-%d")):
            return 85
        elif (date == datetime.datetime.strptime("2020-03-06", "%Y-%m-%d")):
            return 86
        elif (date == datetime.datetime.strptime("2020-03-07", "%Y-%m-%d")):
            return 87
        elif (date == datetime.datetime.strptime("2020-03-08", "%Y-%m-%d")):
            return 88
        elif (date == datetime.datetime.strptime("2020-03-09", "%Y-%m-%d")):
            return 89
    elif(league == "Delirium"):
        if (date == datetime.datetime.strptime("2020-03-13", "%Y-%m-%d")):
            return 1
        elif (date == datetime.datetime.strptime("2020-03-14", "%Y-%m-%d")):
            return 2
        elif (date == datetime.datetime.strptime("2020-03-15", "%Y-%m-%d")):
            return 3
        elif (date == datetime.datetime.strptime("2020-03-16", "%Y-%m-%d")):
            return 4
        elif (date == datetime.datetime.strptime("2020-03-17", "%Y-%m-%d")):
            return 5
        elif (date == datetime.datetime.strptime("2020-03-18", "%Y-%m-%d")):
            return 6
        elif (date == datetime.datetime.strptime("2020-03-19", "%Y-%m-%d")):
            return 7
        elif (date == datetime.datetime.strptime("2020-03-20", "%Y-%m-%d")):
            return 8
        elif (date == datetime.datetime.strptime("2020-03-21", "%Y-%m-%d")):
            return 9
        elif (date == datetime.datetime.strptime("2020-03-22", "%Y-%m-%d")):
            return 10
        elif (date == datetime.datetime.strptime("2020-03-23", "%Y-%m-%d")):
            return 11
        elif (date == datetime.datetime.strptime("2020-03-24", "%Y-%m-%d")):
            return 12
        elif (date == datetime.datetime.strptime("2020-03-25", "%Y-%m-%d")):
            return 13
        elif (date == datetime.datetime.strptime("2020-03-26", "%Y-%m-%d")):
            return 14
        elif (date == datetime.datetime.strptime("2020-03-27", "%Y-%m-%d")):
            return 15
        elif (date == datetime.datetime.strptime("2020-03-28", "%Y-%m-%d")):
            return 16
        elif (date == datetime.datetime.strptime("2020-03-29", "%Y-%m-%d")):
            return 17
        elif (date == datetime.datetime.strptime("2020-03-30", "%Y-%m-%d")):
            return 18
        elif (date == datetime.datetime.strptime("2020-03-31", "%Y-%m-%d")):
            return 19
        elif (date == datetime.datetime.strptime("2020-04-01", "%Y-%m-%d")):
            return 20
        elif (date == datetime.datetime.strptime("2020-04-02", "%Y-%m-%d")):
            return 21
        elif (date == datetime.datetime.strptime("2020-04-03", "%Y-%m-%d")):
            return 22
        elif (date == datetime.datetime.strptime("2020-04-04", "%Y-%m-%d")):
            return 23
        elif (date == datetime.datetime.strptime("2020-04-05", "%Y-%m-%d")):
            return 24
        elif (date == datetime.datetime.strptime("2020-04-06", "%Y-%m-%d")):
            return 25
        elif (date == datetime.datetime.strptime("2020-04-07", "%Y-%m-%d")):
            return 26
        elif (date == datetime.datetime.strptime("2020-04-08", "%Y-%m-%d")):
            return 27
        elif (date == datetime.datetime.strptime("2020-04-09", "%Y-%m-%d")):
            return 28
        elif (date == datetime.datetime.strptime("2020-04-10", "%Y-%m-%d")):
            return 29
        elif (date == datetime.datetime.strptime("2020-04-11", "%Y-%m-%d")):
            return 30
        elif (date == datetime.datetime.strptime("2020-04-12", "%Y-%m-%d")):
            return 31
        elif (date == datetime.datetime.strptime("2020-04-13", "%Y-%m-%d")):
            return 32
        elif (date == datetime.datetime.strptime("2020-04-14", "%Y-%m-%d")):
            return 33
        elif (date == datetime.datetime.strptime("2020-04-15", "%Y-%m-%d")):
            return 34
        elif (date == datetime.datetime.strptime("2020-04-16", "%Y-%m-%d")):
            return 35
        elif (date == datetime.datetime.strptime("2020-04-17", "%Y-%m-%d")):
            return 36
        elif (date == datetime.datetime.strptime("2020-04-18", "%Y-%m-%d")):
            return 37
        elif (date == datetime.datetime.strptime("2020-04-19", "%Y-%m-%d")):
            return 38
        elif (date == datetime.datetime.strptime("2020-04-20", "%Y-%m-%d")):
            return 39
        elif (date == datetime.datetime.strptime("2020-04-21", "%Y-%m-%d")):
            return 40
        elif (date == datetime.datetime.strptime("2020-04-22", "%Y-%m-%d")):
            return 41
        elif (date == datetime.datetime.strptime("2020-04-23", "%Y-%m-%d")):
            return 42
        elif (date == datetime.datetime.strptime("2020-04-24", "%Y-%m-%d")):
            return 43
        elif (date == datetime.datetime.strptime("2020-04-25", "%Y-%m-%d")):
            return 44
        elif (date == datetime.datetime.strptime("2020-04-26", "%Y-%m-%d")):
            return 45
        elif (date == datetime.datetime.strptime("2020-04-27", "%Y-%m-%d")):
            return 46
        elif (date == datetime.datetime.strptime("2020-04-28", "%Y-%m-%d")):
            return 47
        elif (date == datetime.datetime.strptime("2020-04-29", "%Y-%m-%d")):
            return 48
        elif (date == datetime.datetime.strptime("2020-04-30", "%Y-%m-%d")):
            return 49
        elif (date == datetime.datetime.strptime("2020-05-01", "%Y-%m-%d")):
            return 50
        elif (date == datetime.datetime.strptime("2020-05-02", "%Y-%m-%d")):
            return 51
        elif (date == datetime.datetime.strptime("2020-05-03", "%Y-%m-%d")):
            return 52
        elif (date == datetime.datetime.strptime("2020-05-04", "%Y-%m-%d")):
            return 53
        elif (date == datetime.datetime.strptime("2020-05-05", "%Y-%m-%d")):
            return 54
        elif (date == datetime.datetime.strptime("2020-05-06", "%Y-%m-%d")):
            return 55
        elif (date == datetime.datetime.strptime("2020-05-07", "%Y-%m-%d")):
            return 56
        elif (date == datetime.datetime.strptime("2020-05-08", "%Y-%m-%d")):
            return 57
        elif (date == datetime.datetime.strptime("2020-05-09", "%Y-%m-%d")):
            return 58
        elif (date == datetime.datetime.strptime("2020-05-10", "%Y-%m-%d")):
            return 59
        elif (date == datetime.datetime.strptime("2020-05-11", "%Y-%m-%d")):
            return 60
        elif (date == datetime.datetime.strptime("2020-05-12", "%Y-%m-%d")):
            return 61
        elif (date == datetime.datetime.strptime("2020-05-13", "%Y-%m-%d")):
            return 62
        elif (date == datetime.datetime.strptime("2020-05-14", "%Y-%m-%d")):
            return 63
        elif (date == datetime.datetime.strptime("2020-05-15", "%Y-%m-%d")):
            return 64
        elif (date == datetime.datetime.strptime("2020-05-16", "%Y-%m-%d")):
            return 65
        elif (date == datetime.datetime.strptime("2020-05-17", "%Y-%m-%d")):
            return 66
        elif (date == datetime.datetime.strptime("2020-05-18", "%Y-%m-%d")):
            return 67
        elif (date == datetime.datetime.strptime("2020-05-19", "%Y-%m-%d")):
            return 68
        elif (date == datetime.datetime.strptime("2020-05-20", "%Y-%m-%d")):
            return 69
        elif (date == datetime.datetime.strptime("2020-05-21", "%Y-%m-%d")):
            return 70
        elif (date == datetime.datetime.strptime("2020-05-22", "%Y-%m-%d")):
            return 71
        elif (date == datetime.datetime.strptime("2020-05-23", "%Y-%m-%d")):
            return 72
        elif (date == datetime.datetime.strptime("2020-05-24", "%Y-%m-%d")):
            return 73
        elif (date == datetime.datetime.strptime("2020-05-25", "%Y-%m-%d")):
            return 74
        elif (date == datetime.datetime.strptime("2020-05-26", "%Y-%m-%d")):
            return 75
        elif (date == datetime.datetime.strptime("2020-05-27", "%Y-%m-%d")):
            return 76
        elif (date == datetime.datetime.strptime("2020-05-28", "%Y-%m-%d")):
            return 77
        elif (date == datetime.datetime.strptime("2020-05-29", "%Y-%m-%d")):
            return 78
        elif (date == datetime.datetime.strptime("2020-05-30", "%Y-%m-%d")):
            return 79
        elif (date == datetime.datetime.strptime("2020-05-31", "%Y-%m-%d")):
            return 80
        elif (date == datetime.datetime.strptime("2020-06-01", "%Y-%m-%d")):
            return 81
        elif (date == datetime.datetime.strptime("2020-06-02", "%Y-%m-%d")):
            return 82
        elif (date == datetime.datetime.strptime("2020-06-03", "%Y-%m-%d")):
            return 83
        elif (date == datetime.datetime.strptime("2020-06-04", "%Y-%m-%d")):
            return 84
        elif (date == datetime.datetime.strptime("2020-06-05", "%Y-%m-%d")):
            return 85
        elif (date == datetime.datetime.strptime("2020-06-06", "%Y-%m-%d")):
            return 86
        elif (date == datetime.datetime.strptime("2020-06-07", "%Y-%m-%d")):
            return 87
        elif (date == datetime.datetime.strptime("2020-06-08", "%Y-%m-%d")):
            return 88
        elif (date == datetime.datetime.strptime("2020-06-09", "%Y-%m-%d")):
            return 89
        elif (date == datetime.datetime.strptime("2020-06-10", "%Y-%m-%d")):
            return 90
        elif (date == datetime.datetime.strptime("2020-06-11", "%Y-%m-%d")):
            return 91
        elif (date == datetime.datetime.strptime("2020-06-12", "%Y-%m-%d")):
            return 92
        elif (date == datetime.datetime.strptime("2020-06-13", "%Y-%m-%d")):
            return 93
        elif (date == datetime.datetime.strptime("2020-06-14", "%Y-%m-%d")):
            return 94
        elif (date == datetime.datetime.strptime("2020-06-15", "%Y-%m-%d")):
            return 95
    elif (league == "Harvest"):
        if (date == datetime.datetime.strptime("2020-06-19", "%Y-%m-%d")):
            return 1
        elif (date == datetime.datetime.strptime("2020-06-20", "%Y-%m-%d")):
            return 2
        elif (date == datetime.datetime.strptime("2020-06-21", "%Y-%m-%d")):
            return 3
        elif (date == datetime.datetime.strptime("2020-06-22", "%Y-%m-%d")):
            return 4
        elif (date == datetime.datetime.strptime("2020-06-23", "%Y-%m-%d")):
            return 5
        elif (date == datetime.datetime.strptime("2020-06-24", "%Y-%m-%d")):
            return 6
        elif (date == datetime.datetime.strptime("2020-06-25", "%Y-%m-%d")):
            return 7
        elif (date == datetime.datetime.strptime("2020-06-26", "%Y-%m-%d")):
            return 8
        elif (date == datetime.datetime.strptime("2020-06-27", "%Y-%m-%d")):
            return 9
        elif (date == datetime.datetime.strptime("2020-06-28", "%Y-%m-%d")):
            return 10
        elif (date == datetime.datetime.strptime("2020-06-29", "%Y-%m-%d")):
            return 11
        elif (date == datetime.datetime.strptime("2020-06-30", "%Y-%m-%d")):
            return 12
        elif (date == datetime.datetime.strptime("2020-07-01", "%Y-%m-%d")):
            return 13
        elif (date == datetime.datetime.strptime("2020-07-02", "%Y-%m-%d")):
            return 14
        elif (date == datetime.datetime.strptime("2020-07-03", "%Y-%m-%d")):
            return 15
        elif (date == datetime.datetime.strptime("2020-07-04", "%Y-%m-%d")):
            return 16
        elif (date == datetime.datetime.strptime("2020-07-05", "%Y-%m-%d")):
            return 17
        elif (date == datetime.datetime.strptime("2020-07-06", "%Y-%m-%d")):
            return 18
        elif (date == datetime.datetime.strptime("2020-07-07", "%Y-%m-%d")):
            return 19
        elif (date == datetime.datetime.strptime("2020-07-08", "%Y-%m-%d")):
            return 20
        elif (date == datetime.datetime.strptime("2020-07-09", "%Y-%m-%d")):
            return 21
        elif (date == datetime.datetime.strptime("2020-07-10", "%Y-%m-%d")):
            return 22
        elif (date == datetime.datetime.strptime("2020-07-11", "%Y-%m-%d")):
            return 23
        elif (date == datetime.datetime.strptime("2020-07-12", "%Y-%m-%d")):
            return 24
        elif (date == datetime.datetime.strptime("2020-07-13", "%Y-%m-%d")):
            return 25
        elif (date == datetime.datetime.strptime("2020-07-14", "%Y-%m-%d")):
            return 26
        elif (date == datetime.datetime.strptime("2020-07-15", "%Y-%m-%d")):
            return 27
        elif (date == datetime.datetime.strptime("2020-07-16", "%Y-%m-%d")):
            return 28
        elif (date == datetime.datetime.strptime("2020-07-17", "%Y-%m-%d")):
            return 29
        elif (date == datetime.datetime.strptime("2020-07-18", "%Y-%m-%d")):
            return 30
        elif (date == datetime.datetime.strptime("2020-07-19", "%Y-%m-%d")):
            return 31
        elif (date == datetime.datetime.strptime("2020-07-20", "%Y-%m-%d")):
            return 32
        elif (date == datetime.datetime.strptime("2020-07-21", "%Y-%m-%d")):
            return 33
        elif (date == datetime.datetime.strptime("2020-07-22", "%Y-%m-%d")):
            return 34
        elif (date == datetime.datetime.strptime("2020-07-23", "%Y-%m-%d")):
            return 35
        elif (date == datetime.datetime.strptime("2020-07-24", "%Y-%m-%d")):
            return 36
        elif (date == datetime.datetime.strptime("2020-07-25", "%Y-%m-%d")):
            return 37
        elif (date == datetime.datetime.strptime("2020-07-26", "%Y-%m-%d")):
            return 38
        elif (date == datetime.datetime.strptime("2020-07-27", "%Y-%m-%d")):
            return 39
        elif (date == datetime.datetime.strptime("2020-07-28", "%Y-%m-%d")):
            return 40
        elif (date == datetime.datetime.strptime("2020-07-29", "%Y-%m-%d")):
            return 41
        elif (date == datetime.datetime.strptime("2020-07-30", "%Y-%m-%d")):
            return 42
        elif (date == datetime.datetime.strptime("2020-07-31", "%Y-%m-%d")):
            return 43
        elif (date == datetime.datetime.strptime("2020-08-01", "%Y-%m-%d")):
            return 44
        elif (date == datetime.datetime.strptime("2020-08-02", "%Y-%m-%d")):
            return 45
        elif (date == datetime.datetime.strptime("2020-08-03", "%Y-%m-%d")):
            return 46
        elif (date == datetime.datetime.strptime("2020-08-04", "%Y-%m-%d")):
            return 47
        elif (date == datetime.datetime.strptime("2020-08-05", "%Y-%m-%d")):
            return 48
        elif (date == datetime.datetime.strptime("2020-08-06", "%Y-%m-%d")):
            return 49
        elif (date == datetime.datetime.strptime("2020-08-07", "%Y-%m-%d")):
            return 50
        elif (date == datetime.datetime.strptime("2020-08-08", "%Y-%m-%d")):
            return 51
        elif (date == datetime.datetime.strptime("2020-08-09", "%Y-%m-%d")):
            return 52
        elif (date == datetime.datetime.strptime("2020-08-10", "%Y-%m-%d")):
            return 53
        elif (date == datetime.datetime.strptime("2020-08-11", "%Y-%m-%d")):
            return 54
        elif (date == datetime.datetime.strptime("2020-08-12", "%Y-%m-%d")):
            return 55
        elif (date == datetime.datetime.strptime("2020-08-13", "%Y-%m-%d")):
            return 56
        elif (date == datetime.datetime.strptime("2020-08-14", "%Y-%m-%d")):
            return 57
        elif (date == datetime.datetime.strptime("2020-08-15", "%Y-%m-%d")):
            return 58
        elif (date == datetime.datetime.strptime("2020-08-16", "%Y-%m-%d")):
            return 59
        elif (date == datetime.datetime.strptime("2020-08-17", "%Y-%m-%d")):
            return 60
        elif (date == datetime.datetime.strptime("2020-08-18", "%Y-%m-%d")):
            return 61
        elif (date == datetime.datetime.strptime("2020-08-19", "%Y-%m-%d")):
            return 62
        elif (date == datetime.datetime.strptime("2020-08-20", "%Y-%m-%d")):
            return 63
        elif (date == datetime.datetime.strptime("2020-08-21", "%Y-%m-%d")):
            return 64
        elif (date == datetime.datetime.strptime("2020-08-22", "%Y-%m-%d")):
            return 65
        elif (date == datetime.datetime.strptime("2020-08-23", "%Y-%m-%d")):
            return 66
        elif (date == datetime.datetime.strptime("2020-08-24", "%Y-%m-%d")):
            return 67
        elif (date == datetime.datetime.strptime("2020-08-25", "%Y-%m-%d")):
            return 68
        elif (date == datetime.datetime.strptime("2020-08-26", "%Y-%m-%d")):
            return 69
        elif (date == datetime.datetime.strptime("2020-08-27", "%Y-%m-%d")):
            return 70
        elif (date == datetime.datetime.strptime("2020-08-28", "%Y-%m-%d")):
            return 71
        elif (date == datetime.datetime.strptime("2020-08-29", "%Y-%m-%d")):
            return 72
        elif (date == datetime.datetime.strptime("2020-08-30", "%Y-%m-%d")):
            return 73
        elif (date == datetime.datetime.strptime("2020-08-31", "%Y-%m-%d")):
            return 74
        elif (date == datetime.datetime.strptime("2020-09-01", "%Y-%m-%d")):
            return 75
        elif (date == datetime.datetime.strptime("2020-09-02", "%Y-%m-%d")):
            return 76
        elif (date == datetime.datetime.strptime("2020-09-03", "%Y-%m-%d")):
            return 77
        elif (date == datetime.datetime.strptime("2020-09-04", "%Y-%m-%d")):
            return 78
        elif (date == datetime.datetime.strptime("2020-09-05", "%Y-%m-%d")):
            return 79
        elif (date == datetime.datetime.strptime("2020-09-06", "%Y-%m-%d")):
            return 80
        elif (date == datetime.datetime.strptime("2020-09-07", "%Y-%m-%d")):
            return 81
        elif (date == datetime.datetime.strptime("2020-09-08", "%Y-%m-%d")):
            return 82
        elif (date == datetime.datetime.strptime("2020-09-09", "%Y-%m-%d")):
            return 83
        elif (date == datetime.datetime.strptime("2020-09-10", "%Y-%m-%d")):
            return 84
        elif (date == datetime.datetime.strptime("2020-09-11", "%Y-%m-%d")):
            return 85
        elif (date == datetime.datetime.strptime("2020-09-12", "%Y-%m-%d")):
            return 86
        elif (date == datetime.datetime.strptime("2020-09-13", "%Y-%m-%d")):
            return 87
        elif (date == datetime.datetime.strptime("2020-09-14", "%Y-%m-%d")):
            return 88

# Update harvest league dataset
# df_harvestCurrency = pandas.read_csv("Data/Harvest.2020-06-19.2020-09-14.currency.csv", sep=';', parse_dates=['Date'])
# df_harvestCurrency['daysIntoLeague'] = 0
# for index, row_series in df_harvestCurrency.iterrows():
#     df_harvestCurrency.at[index, 'daysIntoLeague'] = adjustDate(row_series['League'], row_series['Date'])
# df_harvestCurrency.to_csv(r'ComputerPathHere\Data\updatedHarvest.csv', index=False)

# Update delirium league dataset
# df_deliriumCurrency = pandas.read_csv("Data/Delirium.2020-03-13.2020-06-15.currency.csv", sep=';', parse_dates=['Date'])
# df_deliriumCurrency['daysIntoLeague'] = 0
# for index, row_series in df_deliriumCurrency.iterrows():
#     df_deliriumCurrency.at[index, 'daysIntoLeague'] = adjustDate(row_series['League'], row_series['Date'])
# df_deliriumCurrency.to_csv(r'ComputerPathHere\Data\updatedDelirium.csv', index=False)

# Update metamorph league dataset
# df_metamorphCurrency = pandas.read_csv("Data/Metamorph.2019-12-13.2020-03-09.currency.csv", sep=';', parse_dates=['Date'])
# df_metamorphCurrency['daysIntoLeague'] = 0
# for index, row_series in df_metamorphCurrency.iterrows():
#     df_metamorphCurrency.at[index, 'daysIntoLeague'] = adjustDate(row_series['League'], row_series['Date'])
# df_metamorphCurrency.to_csv(r'ComputerPathHere\Data\updatedMetamorph.csv', index=False)

########################################################################################################################
# df_heistItems = pandas.read_csv("Data/Heist.2020-09-18.2021-01-11.items.csv", sep=';', parse_dates=['Date'])
# print("read heistItems csv file")
#
# df_heistItems['daysIntoLeague'] = 0
# print('added daysIntoLeague')
#
# for index, row_series in df_heistItems.iterrows():
#     df_heistItems.at[index, 'daysIntoLeague'] = adjustDate(row_series['League'], row_series['Date'])
# print("set daysIntoLeague values")
#
# df_heistItems.to_csv(r'ComputerPathHere\Data\updatedHeist_Items.csv', index=False)
# print("saved the updated csv file")

# df_ritualItems = pandas.read_csv("Data/Ritual.2021-01-15.2021-04-12.items.csv", sep=';', parse_dates=['Date'])
# print("read ritualItems csv file")
#
# df_ritualItems['daysIntoLeague'] = 0
# print('added daysIntoLeague')
#
# for index, row_series in df_ritualItems.iterrows():
#     df_ritualItems.at[index, 'daysIntoLeague'] = adjustDate(row_series['League'], row_series['Date'])
# print("set daysIntoLeague values")
#
# df_ritualItems.to_csv(r'ComputerPathHere\Data\updatedRitual_Items.csv', index=False)
# print("saved the updated csv file")

########################################################################################################################
# Update csv files with daysIntoLeague column

# df_heistCurrency = pandas.read_csv("Data/Heist.2020-09-18.2021-01-11.currency.csv", sep=';', parse_dates=['Date'])
# df_ritualCurrency = pandas.read_csv("Data/Ritual.2021-01-15.2021-04-12.currency.csv", sep=';', parse_dates=['Date'])
#
# print(df_ritualCurrency.head())
# Add a new column in the dataset for adjusted dates (to allow for overlapping of separate leagues on the same graph)
# df_ritualCurrency['daysIntoLeague'] = 0
# df_heistCurrency['daysIntoLeague'] = 0
# print(df_ritualCurrency.head())
#
# for index, row_series in df_ritualCurrency.iterrows():
#     df_ritualCurrency.at[index, 'daysIntoLeague'] = adjustDate(row_series['League'], row_series['Date'])
#
# for index, row_series in df_heistCurrency.iterrows():
#     df_heistCurrency.at[index, 'daysIntoLeague'] = adjustDate(row_series['League'], row_series['Date'])
# print(df_ritualCurrency.head())
# print("date adjusting done")
#
# df_ritualCurrency.to_csv(r'ComputerPathHere\Data\updatedRitual.csv', index=False)
# df_heistCurrency.to_csv(r'ComputerPathHere\Data\updatedHeist.csv', index=False)