from matplotlib import pyplot
import os
import re
import csv


def get_files():
    all_files = os.listdir("./")
    daily_files = []
    for file in all_files:
        match = re.fullmatch("[0-9]+-[0-9]+-[0-9]+.csv", file)
        if match:
            daily_files.append(match.string)
    return daily_files


def get_data_from_files(daily_files, search_terms, populations):
    all_daily_counts = []
    for i in range(len(search_terms)):
        search_term_counts = []
        for file in daily_files:
            with open(file, newline='') as csvfile:
                reader = csv.reader(csvfile)
                daily_count = 0
                for row in reader:
                    if search_terms[i] in row:
                        if len(row) < 9:
                            daily_count += int(row[3])
                        else:
                            daily_count += int(row[7])
                search_term_counts.append(daily_count/populations[i])
        all_daily_counts.append(search_term_counts)
    return all_daily_counts


def get_new_cases(all_daily_cases):
    all_new_cases = []
    for daily_cases in all_daily_cases:
        new_cases = []
        for i in range(1, len(daily_cases)):
            #if daily_cases[i] - daily_cases[i-1] != 0:
                new_cases.append(daily_cases[i] - daily_cases[i-1])
        all_new_cases.append(new_cases)
    return all_new_cases


def show_graph(all_daily_cases, searches):
    for i in range(len(all_daily_cases)):
        pyplot.plot([x for x in range(1, len(all_daily_cases[i])+1)], all_daily_cases[i], label=searches[i])
    pyplot.legend()
    pyplot.show()


def main():
    searches = ["Montana", "Italy", "US", "New York"]
    populations = [1068778, 60317116, 328239523, 19453561]
    show_graph(get_new_cases(get_data_from_files(get_files(), searches, populations)), searches)


if __name__ == "__main__":
    main()
