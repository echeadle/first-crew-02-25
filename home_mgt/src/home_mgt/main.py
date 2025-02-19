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
    inputs = {
        'topic': 'Opening the deck by removing all covers',
        'current_year': str(datetime.now().year)
    }
    
    try:
        HomeMgt().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == '__main__':
    run()