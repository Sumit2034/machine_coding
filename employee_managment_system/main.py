from datetime import datetime, timedelta
import uuid
from model.employee import Employee
from service.employee_service import EmployeeService
from service.meeting_service import MeetingService


def main():
    repo = EmployeeService()
    scheduler = MeetingService()

    # Add employees
    emp1 = Employee(uuid.uuid4(), "Alice")
    emp2 = Employee(uuid.uuid4(), "Bob")
    repo.add_employee(emp1)
    repo.add_employee(emp2)

    # Schedule a meeting
    scheduler.schedule_meeting(emp1, emp2, 30)

    # Check employee's schedule
    slot1 = emp1.calendar.get_available_slot(30)

    print(f"slot for {emp1.name} is {slot1}")

    # Delete a meeting
    first_date = next(iter(emp1.calendar.schedule))
    # Get the first meeting for that date
    first_meeting = emp1.calendar.schedule[first_date][0]
    scheduler.delete_meeting(emp1, first_meeting.meeting_id)

    # Reschedule a meeting
    new_time = datetime.now() + timedelta(hours=1)

    scheduler.schedule_meeting(emp1, emp2, 30)
    reschedule_meeting = emp1.calendar.schedule[first_date][0]
    scheduler.reschedule_meeting(emp1, reschedule_meeting.meeting_id, new_time)


if __name__ == "__main__":
    main()