
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

            
check_entries = read_file()

total_sessions = 0
total_minutes = 0
for entry in check_entries:
    _,_,_,minutes = entry
    total_sessions += 1
    total_minutes += minutes
print(f"Total Sessions: {total_sessions}")
print(f"You have studied a total of {total_minutes} minutes.")
     
def filter_subjects(data, subject):
    filtered_subjects = []
    for entry in data:
        date,day,subjects,minutes = entry
        if subjects.lower() == subject.lower():
            filtered_subjects.append(entry)
    return filtered_subjects

filtered_entries = filter_subjects(check_entries,"Python")

def filter_duration(data, min_duration, max_duration):
    duration_list = []
    for entry in data:
        date,day,subjects,minutes = entry
        if min_duration <= minutes <= max_duration:
            duration_list.append(entry)
    return duration_list

duration = filter_duration(check_entries, 20, 60)

def sort_study_minutes(data):
    return sorted(data, key=lambda entry: entry[3], reverse=True)

sorted_entries = sort_study_minutes(check_entries)