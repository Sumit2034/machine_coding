from datetime import timedelta
import uuid


class Meeting:
    def __init__(self, title, participants, start_time, duration):
        self.meeting_id = uuid.uuid4()
        self.title = title
        self.participants = participants
        self.start_time = start_time
        self.end_time = start_time + timedelta(minutes=duration)

    def get_duration(self):
        return int((self.end_time - self.start_time).total_seconds() / 60)

    def is_conflict(self, other_meeting):
        return not (self.end_time <= other_meeting.start_time or self.start_time >= other_meeting.end_time)
