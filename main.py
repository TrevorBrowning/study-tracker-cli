
def read_file():
    file_data = []
    with open("study_data.txt") as data:
        for line in data:
            stripped_line = line.strip()
            if stripped_line == "":
                continue
            parts = stripped_line.split(",")
            if len(parts) != 4:
                continue
            date, day, subjects, minutes_str = parts
            try:
                minutes = int(minutes_str)
            except:
                continue
            combined_lines = (date, day, subjects, minutes)

            file_data.append(combined_lines)
        return file_data

            
check_entries = read_file()
count = 0
for entry in check_entries:
    count += 1
print(f"Total Sessions: {count}")
            
