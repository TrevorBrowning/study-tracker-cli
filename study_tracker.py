
def read_file():
    file_data = []
    with open("study_data.txt") as data:
        for line in data:
            stripped_line = line.strip()
            if stripped_line == "":
                continue
            parts = stripped_line.split(",")
            clean_parts = []
            for i in parts:
                clean_item = i.strip()
                clean_parts.append(clean_item)
            if len(clean_parts) != 4:
                continue
            date, day, subjects, minutes_str = clean_parts
            try:
                minutes = int(minutes_str)
            except:
                continue
            combined_lines = (date, day, subjects, minutes)

            file_data.append(combined_lines)
        return file_data

            


def filter_subjects(data, subject):
    filtered_subjects = []
    for entry in data:
        date,day,subjects,minutes = entry
        if subjects.lower() == subject.lower():
            filtered_subjects.append(entry)
    return filtered_subjects

def filter_duration(data, min_duration, max_duration):
    duration_list = []
    for entry in data:
        date,day,subjects,minutes = entry
        if min_duration <= minutes <= max_duration:
            duration_list.append(entry)
    return duration_list


def sort_study_minutes(data):
    return sorted(data, key=lambda entry: entry[3], reverse=True)


def display_data(data):
    for entry in data:
        date, day, subject, minutes = entry
        print(f"{date} | {day} | {subject} | {minutes} min")
    print("----------------------")



def main():
    check_entries = read_file()

    SEPARATOR = "-" * 22
    
    while True:
        print("\n" * 2)
        print("Study Session Analyzer")
        print(SEPARATOR)
        print("1. Show all sessions")
        print("2. Show total sessions and duration")
        print("3. Filter by subject")
        print("4. Filter by duration")
        print("5. Show Longest Sessions")
        print("6. Exit")
        menu_choice = input("Enter your choice: ")
        if menu_choice == "1":
            print("\n")
            print("All Sessions:")
            print(SEPARATOR)

            display_data(check_entries)
            input("Press Enter to return to menu...")

        elif menu_choice == "2":
            total_sessions = 0
            total_minutes = 0
            for entry in check_entries:
                _,_,_,minutes = entry
                total_sessions += 1
                total_minutes += minutes
            print("\n" * 2)
            print(SEPARATOR)
            print("Session & Minute Totals:")
            print(f"Total Sessions: {total_sessions}")
            print(f"You have studied a total of {total_minutes} minutes.")
            print(SEPARATOR)
            input("Press Enter to return to menu...")

        elif menu_choice == "3":
            subject_choice = input("Enter subject: ")
            subject_filt = filter_subjects(check_entries, subject_choice)
            print("\n" * 2)
            print(f"{subject_choice.capitalize()} Sessions:")
            print(SEPARATOR)
            if subject_filt == []:
                print("No sessions found")
            else:
                display_data(subject_filt)
            input("Press Enter to return to menu...")

        elif menu_choice == "4":
            min_choice = int(input("Enter minimum duration: "))
            max_choice = int(input("Enter maximum duration "))
            duration_filt = filter_duration(check_entries, min_choice, max_choice)
            print("\n" * 2)
            print(f"Sorted by Duration (Min-{min_choice}/Max-{max_choice}):")
            print(SEPARATOR)
            if duration_filt == []:
                print("No sessions found")
            else:
                display_data(duration_filt)
            input("Press Enter to return to menu...")

        elif menu_choice == "5":
            sorted_entries = sort_study_minutes(check_entries)
            print("\n" * 2)
            print(f"Sorted by Longest Duration:")
            print(SEPARATOR)
            display_data(sorted_entries)
            input("Press Enter to return to menu...")

        elif menu_choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()