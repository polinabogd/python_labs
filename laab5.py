import re
from datetime import datetime


if __name__ == '__main__':
    file_with_logs = open("logfile.txt", "r")

    matches = []
    FIRST_DATE = 1237788064
    SECOND_DATE = 1238197074
    counter_of_matches = 0
    regex_pattern = fr"^.*GET.*200.*\"-\".\"-\".\"-\""

    for i in range(FIRST_DATE, SECOND_DATE):
        date = datetime.fromtimestamp(i)
        date_for_search = date.strftime("%d/%b/%Y:%H:%M:%S")
        for line in file_with_logs:
            if re.findall(regex_pattern, line):
                matches.append(line)
                counter_of_matches += 1
        for line in matches:
            if date_for_search in line:
                print(line)
    print(counter_of_matches)

