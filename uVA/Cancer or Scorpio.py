import datetime

def zodiac(m, d):
    date = (m, d)
    if (1, 21) <= date <= (2, 19):
        return "aquarius"
    if (2, 20) <= date <= (3, 20):
        return "pisces"
    if (3, 21) <= date <= (4, 20):
        return "aries"
    if (4, 21) <= date <= (5, 21):
        return "taurus"
    if (5, 22) <= date <= (6, 21):
        return "gemini"
    if (6, 22) <= date <= (7, 22):
        return "cancer"
    if (7, 23) <= date <= (8, 21):
        return "leo"
    if (8, 22) <= date <= (9, 23):
        return "virgo"
    if (9, 24) <= date <= (10, 23):
        return "libra"
    if (10, 24) <= date <= (11, 22):
        return "scorpio"
    if (11, 23) <= date <= (12, 22):
        return "sagittarius"
    return "capricorn"
    
n = int(input())
for i in range(n):
    s = input()
    d = s[2 : 4]
    m = s[0:2]
    y = s[4:]
    date_1 = datetime.datetime.strptime(m + "/" + d + "/" + y, "%m/%d/%Y")
    end_date = date_1 + datetime.timedelta(weeks = 40)
    end_date = str(end_date)[0 : 10]
    end_date = end_date.split('-')
    print(i + 1, end_date[1] + "/" + end_date[2] + "/" + end_date[0], zodiac(int(end_date[1]), int(end_date[2])))
    