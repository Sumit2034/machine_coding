from model.meeting import Meeting


class MeetingService:

    def schedule_meeting(self, employee_x, employee_y, duration):
        slot_x = employee_x.calendar.get_available_slot(duration)
        slot_y = employee_y.calendar.get_available_slot(duration)
        if slot_x and slot_y:
            slot = max(slot_x, slot_y)
            meeting = Meeting("Meeting", [employee_x, employee_y], slot, duration)
            employee_x.calendar.add_meeting(meeting)
            employee_y.calendar.add_meeting(meeting)
            print(f"Meeting scheduled between {employee_x.name} and {employee_y.name} at {slot}")

    def delete_meeting(self, employee, meeting_id):
        employee.calendar.remove_meeting(meeting_id)

    def reschedule_meeting(self, employee, meeting_id, new_time):
        employee.calendar.reschedule_meeting(meeting_id, new_time)