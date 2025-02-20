from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


class AIPromptGenerator:
    def __init__(self, role, goal, task, adherence="medium"):
        self.role = role
        self.goal = goal
        self.task = task
        self.adherence = adherence

    def generate_prompt(self, user_input):
        structure_templates = {
            "high": (
                f"### Role: {self.role}\n"
                f"### Goal: {self.goal}\n"
                f"### Task: {self.task}\n\n"
                f"### User Input:\n"
                f"{user_input}\n\n"
                "**Instructions:**\n"
                "- Strictly follow the outlined format.\n"
                "- Ensure clarity, accuracy, and completeness.\n"
                "- Maintain professional and structured responses.\n"
                "- Stick to bullet points where applicable.\n"
                "\n**Expected Output Format:**\n"
                "- **Weekly Tasks**\n"
                "- **Monthly Tasks**\n"
                "- **Seasonal Tasks**"
            ),
            "medium": (
                f"You are a {self.role} whose goal is to {self.goal}. "
                f"Your task is to {self.task}. "
                f"Consider the following user input:\n{user_input}\n\n"
                "Follow the given structure, but feel free to adjust details as needed. "
                "Maintain a professional tone, but creativity is allowed."
            ),
            "low": (
                f"Imagine you are a {self.role}. "
                f"Your mission is {self.goal}. "
                f"Here’s your task: {self.task}. "
                f"The user has provided this input:\n{user_input}\n\n"
                "Express yourself freely, without strict structure. "
                "Be engaging and creative while maintaining relevance."
            )
        }

        return structure_templates.get(self.adherence, structure_templates["medium"])


@CrewBase
class HomeMgt():
    """HomeMgt crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def list_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['list_manager'],
            verbose=True
        )

    @task
    def generate_home_mgt_lists_task(self) -> Task:
        return Task(
            description="Help create a structured to-do list based on user input: {user_input}. "
                        "The list should include sections for weekly, monthly, and seasonal tasks.",
            expected_output="A markdown-formatted list of home tasks saved to `home_tasks.md`, "
                            "with sections for weekly, monthly, and seasonal tasks.",
            agent=self.list_manager(),
            output_file="home_tasks.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the HomeMgt crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
