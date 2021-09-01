from datetime import date

weekdays = {'1':'Monday', '2':'Tuesday', '3':'Wednesday', '4':'Thursday',
            '5':'Friday', '6':'Saturday', '7':'Sunday'}
Y = 2009
D, M = map(int, input().split())

day = date(Y, M, D).isoweekday()

print(weekdays[f'{day}'])