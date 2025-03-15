from product_management import ProductManagement

if __name__ == "__main__":
    pm = ProductManagement()

    # Load existing sprints or create a new one
    try:
        pm.load_from_file('sprints.json')
    except FileNotFoundError:
        sprint1 = pm.create_sprint("Sprint 1", 14)

        # Adding user stories
        user_story1 = UserStory("As a user, I want to track my expenses", 
                                "Users can input and categorize expenses.", 
                                "User can add, edit, and delete expenses.", 
                                "High")
        user_story2 = UserStory("As a user, I want to view my budget", 
                                "Users can see their budget summary.", 
                                "Budget displays total income and expenses.", 
                                "Medium")

        sprint1.add_user_story(user_story1)
        sprint1.add_user_story(user_story2)

        # Completing a user story
        sprint1.complete_user_story("As a user, I want to track my expenses")

        # Save sprints to file
        pm.save_to_file('sprints.json')

    # Generate report
    print(pm.generate_report())

    # Simulate sprint progress
    pm.simulate_progress(5)
