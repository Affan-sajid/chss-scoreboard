import os
import django
import time
import random
import datetime

# test


# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoreboard_mine.settings')
django.setup()

from scoreboard.models import Score

def update_scores():
    while True:
        # Generate random scores for demonstration
        curentdate = datetime.datetime.now()
        Red = random.randint(0, 100)
        Orange = random.randint(0, 100)
        Yellow = random.randint(0, 100)
        Green = random.randint(0, 100)
        Blue = random.randint(0, 100)
        
        # Update the database
        Score.objects.create(Red=Red, Orange=Orange,Yellow=Yellow,Green=Green,Blue=Blue,last_updated = curentdate)
        print(f"Updated scores at {curentdate}: Red: {Red}, Orange: {Orange} , Yellow: {Yellow}, Green: {Green}, Blu: {Blue} ")
        
        # Wait for 5 seconds
        time.sleep(5)

if __name__ == "__main__":
    update_scores()
