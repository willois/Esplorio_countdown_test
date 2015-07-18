from datetime import datetime
import optparse

def main():

    parser = optparse.OptionParser()
    parser.add_option('-d', '--deadline', action="store", dest='deadline', default='2015-12-25', type="str", help="A date in YYYY-MM-DD format")
    parser.add_option('-e', '--event', action="store", dest='event', default='Christmas', type="str", help="The event on such deadline")

    (options, args) = parser.parse_args()

    def deadline_countdown():
            year, month, day = map(int, options.deadline.split('-'))
            deadline = datetime(year, month, day)
            days_till_deadline = deadline - datetime.today()
            if len(options.event) > 0:
                print('{} days until {}'.format(days_till_deadline.days, options.event))
            else:
                print('{} days until {}'.format(days_till_deadline.days, options.deadline))

    deadline_countdown()

main()


