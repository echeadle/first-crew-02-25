# What is prompt adhearence

ChatGPT said:
Prompt Adherence in CrewAI refers to how strictly an agent follows the provided instructions, constraints, and structure of the prompt when executing a task. It determines whether the agent should stick closely to the given guidance or have some flexibility in interpreting it.

How It Works in CrewAI
In CrewAI, prompt adherence can be controlled using different settings when defining agents or tasks. Some tasks might require strict adherence (e.g., structured reports with exact formats), while others might allow for more creativity.

Example Use Case
Imagine you have an agent writing news summaries. If prompt adherence is high, the agent will strictly follow the expected format and length. If prompt adherence is low, the agent might summarize the news more freely, potentially deviating from the format.

Would you like a practical example in CrewAI code? 🚀

You said:
based off of that, please create me a prompt generator that  you feel would work best in an ai agent framework like crewai.

Prompt Generator for AI Agents in CrewAI
A good prompt generator for CrewAI should:
✅ Allow flexibility for different agent roles
✅ Support different levels of prompt adherence
✅ Ensure clear instructions, constraints, and goals

Here's a Python script that dynamically generates structured prompts based on agent roles, goals, and adherence levels:

    ```python

    import random

    class AIPromptGenerator:
        def __init__(self, role, goal, task, adherence="medium"):
            """
            Initializes the prompt generator.
            
            :param role: The role of the AI agent (e.g., "Researcher", "Writer").
            :param goal: The agent's main objective.
            :param task: The specific task assigned.
            :param adherence: How strictly the agent should follow the prompt (low, medium, high).
            """
            self.role = role
            self.goal = goal
            self.task = task
            self.adherence = adherence

        def generate_prompt(self):
            """
            Generates a structured prompt based on adherence level.
            """
            structure_templates = {
                "high": (
                    f"### Role: {self.role}\n"
                    f"### Goal: {self.goal}\n"
                    f"### Task: {self.task}\n\n"
                    "**Instructions:**\n"
                    "- Strictly follow the outlined format.\n"
                    "- Ensure clarity, accuracy, and completeness.\n"
                    "- Maintain professional and structured responses.\n"
                    "- Stick to bullet points where applicable.\n"
                    "\n**Expected Output Format:**\n"
                    "- Introduction (2-3 sentences)\n"
                    "- Key Points (bullet format)\n"
                    "- Conclusion (1-2 sentences)"
                ),
                "medium": (
                    f"You are a {self.role} whose goal is to {self.goal}. "
                    f"Your task is to {self.task}. "
                    "Follow the given structure, but feel free to adjust details as needed. "
                    "Maintain a professional tone, but creativity is allowed."
                ),
                "low": (
                    f"Imagine you are a {self.role}. "
                    f"Your mission is {self.goal}. "
                    f"Here’s your task: {self.task}. "
                    "Express yourself freely, without strict structure. "
                    "Be engaging and creative while maintaining relevance."
                )
            }

            return structure_templates.get(self.adherence, structure_templates["medium"])




        # Example Usage
        if __name__ == "__main__":
            # Example: Generating a prompt for a Researcher Agent
            prompt_generator = AIPromptGenerator(
                role="Senior AI Researcher",
                goal="Analyze emerging AI trends",
                task="Provide a detailed breakdown of the top 3 AI trends in 2025.",
                adherence="high"
            )

            print(prompt_generator.generate_prompt())

    ```

### **Prompt Generator for AI Agents in CrewAI**  
A good **prompt generator** for CrewAI should:  
✅ Allow flexibility for different agent roles  
✅ Support different levels of **prompt adherence**  
✅ Ensure clear instructions, constraints, and goals  

Here's a **Python script** that dynamically generates structured prompts based on **agent roles, goals, and adherence levels**:

---

### **Code: AI Prompt Generator for CrewAI**
```python
import random

class AIPromptGenerator:
    def __init__(self, role, goal, task, adherence="medium"):
        """
        Initializes the prompt generator.
        
        :param role: The role of the AI agent (e.g., "Researcher", "Writer").
        :param goal: The agent's main objective.
        :param task: The specific task assigned.
        :param adherence: How strictly the agent should follow the prompt (low, medium, high).
        """
        self.role = role
        self.goal = goal
        self.task = task
        self.adherence = adherence

    def generate_prompt(self):
        """
        Generates a structured prompt based on adherence level.
        """
        structure_templates = {
            "high": (
                f"### Role: {self.role}\n"
                f"### Goal: {self.goal}\n"
                f"### Task: {self.task}\n\n"
                "**Instructions:**\n"
                "- Strictly follow the outlined format.\n"
                "- Ensure clarity, accuracy, and completeness.\n"
                "- Maintain professional and structured responses.\n"
                "- Stick to bullet points where applicable.\n"
                "\n**Expected Output Format:**\n"
                "- Introduction (2-3 sentences)\n"
                "- Key Points (bullet format)\n"
                "- Conclusion (1-2 sentences)"
            ),
            "medium": (
                f"You are a {self.role} whose goal is to {self.goal}. "
                f"Your task is to {self.task}. "
                "Follow the given structure, but feel free to adjust details as needed. "
                "Maintain a professional tone, but creativity is allowed."
            ),
            "low": (
                f"Imagine you are a {self.role}. "
                f"Your mission is {self.goal}. "
                f"Here’s your task: {self.task}. "
                "Express yourself freely, without strict structure. "
                "Be engaging and creative while maintaining relevance."
            )
        }

        return structure_templates.get(self.adherence, structure_templates["medium"])

# Example Usage
if __name__ == "__main__":
    # Example: Generating a prompt for a Researcher Agent
    prompt_generator = AIPromptGenerator(
        role="Senior AI Researcher",
        goal="Analyze emerging AI trends",
        task="Provide a detailed breakdown of the top 3 AI trends in 2025.",
        adherence="high"
    )

    print(prompt_generator.generate_prompt())
```

### **Why This Works Well for CrewAI**
1. **Role-Based Prompting** – Adapts to different **agent personas**  
2. **Dynamic Adherence Control** – Supports **strict, balanced, or creative** interpretations  
3. **Structured Outputs** – Ensures **consistent task execution**  

Would you like an integration example where this generator works directly inside a CrewAI `Task`? 🚀