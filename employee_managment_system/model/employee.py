from service.calender_service import CalendarService


class Employee:

    def __init__(self, id, name) -> None:
        self.name = name
        self.employee_id = id
        self.calendar = CalendarService()

    