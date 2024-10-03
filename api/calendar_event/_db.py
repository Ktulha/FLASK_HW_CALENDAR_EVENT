from api.calendar_event._storage import Calendar_Events_Storage


class Calendar_Events_DB:
  def __init__(self):
    self._storage=Calendar_Events_Storage