from datetime import datetime, timedelta


class CalendarService:

    def __init__(self):
        self.schedule = {}

    def get_available_slot(self, duration):
        now = datetime.now()
        for day, meetings in self.schedule.items():
            if len(meetings) == 1:
                available_time = (meetings[0].end_time - now).total_seconds() / 60
                if available_time >= duration:
                    return meetings[0].end_time
            for i in range(len(meetings) - 1):
                available_time = (meetings[i+1].start_time - meetings[i].end_time).total_seconds() / 60
                if available_time >= duration:
                    return meetings[i].end_time
        # If no available slot found, suggest the next day or next available time
        return now

    def add_meeting(self, meeting):
        date = meeting.start_time.date()
        if date not in self.schedule:
            self.schedule[date] = []
        self.schedule[date].append(meeting)

    def remove_meeting(self, meeting_id):
        for date, meetings in self.schedule.items():
            self.schedule[date] = [m for m in meetings if m.meeting_id != meeting_id]

    def reschedule_meeting(self, meeting_id, new_time):
        for date, meetings in self.schedule.items():
            for meeting in meetings:
                if meeting.meeting_id == meeting_id:
                    meeting.start_time = new_time
                    meeting.end_time = new_time + timedelta(minutes=meeting.get_duration())
                    return
