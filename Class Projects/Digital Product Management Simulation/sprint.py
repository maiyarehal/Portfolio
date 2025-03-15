from datetime import datetime, timedelta
from user_story import UserStory

class Sprint:
    def __init__(self, sprint_name, duration_days):
        self.sprint_name = sprint_name
        self.duration = timedelta(days=duration_days)
        self.start_date = datetime.now()
        self.end_date = self.start_date + self.duration
        self.user_stories = []

    def add_user_story(self, user_story):
        self.user_stories.append(user_story)

    def complete_user_story(self, title):
        for story in self.user_stories:
            if story.title == title:
                story.mark_completed()

    def report(self):
        completed_stories = [story for story in self.user_stories if story.completed]
        report_str = (f"Sprint: {self.sprint_name}\n"
                      f"Duration: {self.duration.days} days\n"
                      f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n"
                      f"End Date: {self.end_date.strftime('%Y-%m-%d')}\n"
                      f"User Stories:\n")
        for story in self.user_stories:
            report_str += str(story) + "\n"
        report_str += f"\nTotal User Stories: {len(self.user_stories)}\n"
        report_str += f"Completed User Stories: {len(completed_stories)}\n"
        return report_str

    def to_dict(self):
        return {
            "sprint_name": self.sprint_name,
            "duration_days": self.duration.days,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "user_stories": [story.to_dict() for story in self.user_stories],
        }

    @staticmethod
    def from_dict(data):
        sprint = Sprint(data['sprint_name'], data['duration_days'])
        sprint.start_date = datetime.fromisoformat(data['start_date'])
        sprint.end_date = datetime.fromisoformat(data['end_date'])
        sprint.user_stories = [UserStory.from_dict(story) for story in data['user_stories']]
        return sprint
