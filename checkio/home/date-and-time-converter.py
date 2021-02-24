"""
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.

![](https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/e65e2763db7549fa88f7a7f335abfb56/example_1.png)

Input: Date and time as a string

Output: The same date and time, but in a more readable format

Example:

    date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
    date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
    # NB: words "hour" and "minute" are used only when time is 01:mm (1 hour) or hh:01 (1 minute).
    # In other cases it should be used "hours" and "minutes".

How it is used: To improve the understanding between computers and humans.

Precondition:
0 < date <= 31
0 < month <= 12
0 < year <= 3000
0 < hours < 24
0 < minutes < 60
"""

mounth_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


# def date_time(time: str) -> str:
#     s1, s2 = time.split(' ')
#     d, m, y = s1.split('.')
#     h, _m = s2.split(':')
#     return f"{int(d)} {mounth_list[int(m) - 1]} {y} year {int(h)} {'hour' if int(s[3]) == 1 else 'hours'} {int(_m)} {'minute' if int(s[4]) == 1 else 'minutes'}"

def date_time(time: str) -> str:
    import re
    m = re.search(r'(\d*)\.(\d*)\.(\d*) (\d*):(\d*)', time)
    s = m.groups()
    return f"{int(s[0])} {mounth_list[int(s[1]) - 1]} {s[2]} year {int(s[3])} {'hour' if int(s[3]) == 1 else 'hours'} {int(s[4])} {'minute' if int(s[4]) == 1 else 'minutes'}"

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
