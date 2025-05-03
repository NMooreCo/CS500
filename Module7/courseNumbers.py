# Course numbers and their rooms numbers
course_numbers_with_rooms = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
}
# Course numbers and their instructors
course_numbers_with_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}
# Course numbers and their meeting times
course_numbers_with_meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}
# Function to get course information
def get_course_info(course_number) -> tuple:
    course_number = course_number.strip().upper()
    room = course_numbers_with_rooms.get(course_number, "Room not found")
    instructor = course_numbers_with_instructors.get(course_number, "Instructor not found")
    meeting_time = course_numbers_with_meeting_times.get(course_number, "Meeting time not found")
    
    return room, instructor, meeting_time

# Main program
course_number = input("Enter a course number (CSC101): ")
room, instructor, meeting_time = get_course_info(course_number)
print(f"Course Number: {course_number}")
print(f"Room Number: {room}")
print(f"Instructor: {instructor}")
print(f"Meeting Time: {meeting_time}")

