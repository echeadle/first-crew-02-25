#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from crew import HomeMgt
from dotenv import load_dotenv

load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    user_inputs = []  # Store all user inputs
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        user_inputs.append(user_input)  # Store input

    combined_input = " ".join(user_inputs)  # Combine all inputs

    try:
        HomeMgt().crew().kickoff(inputs={"user_input": combined_input})  # Properly pass user input
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == '__main__':
    run()
