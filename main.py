﻿from crewai import Crew, Agent, Task
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class CrewAIProject:
    def __init__(self):
        self.agents = self.create_agents()
        self.tasks = self.create_tasks()
        self.crew = self.create_crew()

    def create_agents(self):
        researcher = Agent(
            role='Researcher',
            goal='Conduct thorough research',
            backstory='An expert researcher with years of experience',
            verbose=True
        )
        return [researcher]

    def create_tasks(self):
        research_task = Task(
            description='Perform comprehensive research on a given topic',
            agent=self.agents[0],
            expected_output='A detailed research report'
        )
        return [research_task]

    def create_crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=2
        )

    def run(self):
        result = self.crew.kickoff()
        return result

def main():
    project = CrewAIProject()
    result = project.run()
    print(result)

if __name__ == "__main__":
    main()
