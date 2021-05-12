import datetime
import pandas
import matplotlib.pyplot as plt

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

    if (league == "Heist"):
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