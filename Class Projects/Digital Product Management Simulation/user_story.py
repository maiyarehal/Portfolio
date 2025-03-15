from datetime import datetime

class UserStory:
    def __init__(self, title, description, acceptance_criteria, priority):
        self.title = title
        self.description = description
        self.acceptance_criteria = acceptance_criteria
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()

    def mark_completed(self):
        self.completed = True
        self.completed_at = datetime.now()

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "acceptance_criteria": self.acceptance_criteria,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed else None,
        }

    @staticmethod
    def from_dict(data):
        story = UserStory(data['title'], data['description'], data['acceptance_criteria'], data['priority'])
        story.completed = data['completed']
        story.created_at = datetime.fromisoformat(data['created_at'])
        if data['completed_at']:
            story.completed_at = datetime.fromisoformat(data['completed_at'])
        return story
