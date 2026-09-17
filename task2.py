schedule = {
    "Mon": [
        "Administration of Operating Systems and Computer Networks",
        "Programming",
        "Ukrainian Language for Professional Purposes"
    ],

    "Tue": [
        "Databases in Information Systems",
        "Programming",
        "IT Law"
    ],

    "Wed": [
        "Web Development",
        "Foreign Language for Professional Purposes",
        "Web Development / Databases in Information Systems"
    ],

    "Thu": [
        "Administration of Operating Systems and Computer Networks",
        "Programming",
        "Web Development"
    ],

    "Fri": [
        "IT Law",
        "Foreign Language for Professional Purposes",
        "Databases in Information Systems"
    ]
}

print("WEEKLY SCHEDULE")
print("-" * 100)
print(f"{'Day':<10} {'Number of classes':<20} Subjects")
print("-" * 100)

for day, subjects in schedule.items():
    print(f"{day:<10} {len(subjects):<20} {', '.join(subjects)}")

print("-" * 100)


total_classes = sum(len(subjects) for subjects in schedule.values())

print(f"\nTotal classes per week: {total_classes}")


max_day = max(schedule, key=lambda day: len(schedule[day]))

print(
    f"Day with the most classes: "
    f"{max_day} ({len(schedule[max_day])} classes)"
)


all_subjects = set()

for subjects in schedule.values():
    for subject in subjects:
        if " / " in subject:
            parts = subject.split(" / ")
            all_subjects.update(parts)
        else:
            all_subjects.add(subject)

print("\nAll unique subjects:")
for subject in sorted(all_subjects):
    print("-", subject)

print("Number of unique subjects:", len(all_subjects))


monday_subjects = set(schedule["Mon"])
wednesday_subjects = set()

for subject in schedule["Wed"]:
    if " / " in subject:
        wednesday_subjects.update(subject.split(" / "))
    else:
        wednesday_subjects.add(subject)

print("\nSubjects on both Monday and Wednesday:")
print(monday_subjects & wednesday_subjects)


print("\nSubjects on Monday but not on Wednesday:")
print(monday_subjects - wednesday_subjects)


def count_subjects(schedule):
    subject_counts = {}

    for subjects in schedule.values():
        for subject in subjects:

            if " / " in subject:
                parts = subject.split(" / ")

                for part in parts:
                    subject_counts[part] = subject_counts.get(part, 0) + 1

            else:
                subject_counts[subject] = subject_counts.get(subject, 0) + 1

    return subject_counts


subject_counts = count_subjects(schedule)


print("\nSubject counts:")

for subject, count in subject_counts.items():
    print(f"{subject}: {count}")


rating = sorted(
    subject_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nSUBJECT RATING:")

for number, (subject, count) in enumerate(rating, start=1):
    print(f"{number}. {subject} — {count} classes")