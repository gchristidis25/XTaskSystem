# TO DO LIST
# - Implement Tests


import datetime
import time

class Task:
    """An everyday task that has
    - memo: the text that describes the task
    - priority: how ergent is it to complete the task
    - creation_date: the date the note was created
    - status: shows if the task was completed or not
    - completion_date: the date when the note was completed"""

    def __init__(self, memo: str) -> None:
        self.memo = memo
        self.creation_date = datetime.datetime.now().date()
        self.status = "incomplete"
        self.completion_date = ""

    def set_priority(self) -> None:
        """Sets the priority of a note"""
        priority = int(input("Give a priority to the task (1: urgent, 2: regular, 3: planned): "))
        while True:
            if priority in range(1, 4):
                self.priority = priority
                break
            print(f"Sorry, but {priority} is not allowed.")

    def search(self, filter:str) -> bool:
        """Returns true if the filter is in the memo, else it returns false
         The search is case insensitive """
        return filter.casefold().strip() in self.memo.casefold()
    
    def is_completed(self) -> bool:
        """Returns true if the the task is completed, else it returns false"""
        return self.status == "completed"




if __name__ == "__main__":
    task = Task("do this")
    

          