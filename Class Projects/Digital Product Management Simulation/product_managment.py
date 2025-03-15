import json
from sprint import Sprint

class ProductManagement:
    def __init__(self):
        self.sprints = []

    def create_sprint(self, sprint_name, duration_days):
        sprint = Sprint(sprint_name, duration_days)
        self.sprints.append(sprint)
        return sprint

    def generate_report(self):
        report = "Product Management Report\n"
        report += "=" * 30 + "\n"
        for sprint in self.sprints:
            report += sprint.report()
        return report

    def save_to_file(self, filename):
        data = {"sprints": [sprint.to_dict() for sprint in self.sprints]}
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.sprints = [Sprint.from_dict(sprint) for sprint in data['sprints']]

    def simulate_progress(self, days_passed):
        for sprint in self.sprints:
            for day in range(days_passed):
                if datetime.now() >= sprint.end_date:
                    print(f"Sprint '{sprint.sprint_name}' has ended.")
                    break
                for story in sprint.user_stories:
                    if not story.completed and story.priority == "High":
                        story.mark_completed()
                        print(f"Completed: {story.title} on day {day + 1}")
