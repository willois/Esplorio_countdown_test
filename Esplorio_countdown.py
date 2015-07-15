from datetime import datetime
def main():
    a = input('Please input a date in YYYY-MM-DD format')
    b = input('Please input the event on such deadline')

    def deadline_countdown(d="2015-12-25", e="Christmas"):
            year, month, day = map(int, a.split('-'))
            deadline = datetime(year, month, day)
            days_till_deadline = deadline - datetime.today()
            if b == ():
                print('{} days until {}'.format(days_till_deadline.days, d))
            else:
                print('{} days until {}'.format(days_till_deadline.days, e))

    deadline_countdown(a, b)
main()


