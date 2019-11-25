import calendar
import datetime
from dateutil import parser


class CalendarPractice:
    def find_week_day(self, date_string):
        switcher = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
        }
        month, day, year = map(int, date_string.split())
        res_week_day = calendar.weekday(year, month, day)
        return switcher[res_week_day].upper()

    def time_delta_1(self, d1, d2):
        return abs(int((d2 - d1).total_seconds()))

    def time_delta_2(self, t1, t2):
        t1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
        t2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
        return str(int((abs(t1 - t2)).total_seconds()))


if __name__ == '__main__':
    print(calendar.TextCalendar(firstweekday=6).formatyear(2020))
    print(
        "Return a header containing abbreviated weekday names.\nn specifies the width in characters for one weekday:\n{}"
        .format(calendar.weekheader(6)))
    print(
        "Returns weekday of first day of the month and number of days in month,\nfor the specified year and month:\n{}"
        .format(calendar.monthrange(2015, 8)))
    print("Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).:\n{}"
          .format(calendar.weekday(2015, 8, 5)))

    c = CalendarPractice()
    print(c.find_week_day("08 05 2015"))

    case1 = ["Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"]
    case1_date1 = parser.parse(case1[0].strip())
    case1_date2 = parser.parse(case1[1].strip())
    print("The absolute difference (t1 - t2) in seconds:\n{}".format(c.time_delta_1(case1_date1, case1_date2)))

    case2 = ["Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"]
    case2_date1 = parser.parse(case2[0].strip())
    case2_date2 = parser.parse(case2[1].strip())
    print("The absolute difference (t1 - t2) in seconds:\n{}".format(c.time_delta_1(case2_date1, case2_date2)))

    print("The absolute difference (t1 - t2) in seconds:\n{}".format(c.time_delta_2(case1[0], case1[1])))
    print("The absolute difference (t1 - t2) in seconds:\n{}".format(c.time_delta_2(case2[0], case2[1])))
