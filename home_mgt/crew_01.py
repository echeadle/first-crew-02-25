from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

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
			config=self.tasks_config['generate_home_mgt_lists_task'],
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the HomeMgt crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)