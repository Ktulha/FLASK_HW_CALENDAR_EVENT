"""
Class representing a calendar event.

The CalendarEvent class is used to store information about a specific event, including its date, topic, and content.

Attributes:
    _id (str): Unique identifier for the calendar event.
    date (str): Date of the calendar event.
    topic (str): Topic or title of the calendar event.
    content (str): Detailed content or description of the calendar event.
"""
class CalendarEvent:
    _id:str
    date:str
    topic:str
    content:str