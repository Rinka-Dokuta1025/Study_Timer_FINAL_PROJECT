import time
from datetime import datetime

# -----------------------------------------------------------
# FUNCTION: get_positive_int
# PURPOSE: Ask the user for a number and make sure it is
#          a whole number (integer) greater than zero.
# WHY IT'S HERE: This prevents the program from breaking
#                if the user types something invalid.
# -----------------------------------------------------------
def get_positive_int(prompt):
    while True:
        txt = input(prompt).strip()   # Ask the user for input
        try:
            val = int(txt)            # Try to turn the input into an integer
            if val > 0:               # Make sure the number is positive
                return val
            print("Please enter a number greater than zero.")
        except ValueError:
            # This happens if the user types something like "hello" or "3.5"
            print("That isn't a whole number. Try again.")


# -----------------------------------------------------------
# FUNCTION: get_optional_int
# PURPOSE: Allow the user to either type a number OR just 
#          press Enter to choose a default value.
# EXAMPLE: If default = 30 minutes, the user can just press Enter.
# -----------------------------------------------------------
def get_optional_int(prompt, default_val):
    txt = input(f"{prompt} (press Enter for {default_val}): ").strip()

    # If they press Enter, use the default
    if txt == "":
        return default_val

    # Otherwise, try to convert what they typed into a number
    try:
        val = int(txt)
        if val > 0:
            return val
        print("Using default because value must be > 0.")
        return default_val
    except ValueError:
        # User typed something invalid
        print("Using default because that wasn't a valid number.")
        return default_val


# -----------------------------------------------------------
# FUNCTION: beep
# PURPOSE: Make a small alert sound when a timer finishes.
# NOTE: Not all computers support sound, so this may fall back
#       to printing a bell character.
# -----------------------------------------------------------
def beep():
    try:
        # Windows computers use winsound
        import winsound
        winsound.Beep(880, 300)
    except Exception:
        # For Mac/Linux/others, this may or may not make a sound
        print('\a', end='')


# -----------------------------------------------------------
# FUNCTION: countdown
# PURPOSE: Show a timer counting down on the screen.
# HOW IT WORKS: Prints minutes and seconds, updates every second.
# -----------------------------------------------------------
def countdown(total_seconds, label):
    while total_seconds > 0:
        mins = total_seconds // 60   # How many minutes left?
        secs = total_seconds % 60    # How many seconds left?
        
        # Print time like: Study: 05:12 remaining
        print(f"{label}: {mins:02d}:{secs:02d} remaining", end="\r")
        
        time.sleep(1)                # Wait for 1 second
        total_seconds -= 1           # Remove 1 second from the timer

    # Clear the line when countdown finishes
    print(" " * 60, end="\r")


# -----------------------------------------------------------
# MAIN PROGRAM
# PURPOSE: This is the main part of the program that runs
#          the study/break loops, interacts with the user,
#          and displays motivational messages.
# -----------------------------------------------------------
def main():
    print("==== Study Timer ====")
    print("This program helps you schedule study and break sessions.\n")

    # Ask for the user's name to personalize the program
    name = input("Enter your name (optional): ").strip()

    # Ask if the user wants test mode
    # Test mode is fast: 1 minute = 1 second
    print("\nTest mode runs FAST (1 minute = 1 second).")
    fast = input("Enable test mode? (y/n): ").strip().lower() == "y"

    # If test mode is on, scale = 1 second per "minute"
    # If off, scale = 60 seconds per real minute
    scale = 1 if fast else 60

    # Ask how many loops the user wants to study
    loops = get_positive_int("\nHow many study loops do you want to complete? ")

    # Ask how long study and break times should be
    study_mins = get_optional_int("Study minutes per loop", 30)
    break_mins = get_optional_int("Break minutes per loop", 10)

    # A list of motivational messages (meets requirement: list)
    messages = [
        "Nice focus! Keep it up.",
        "You're doing great—keep pushing!",
        "Awesome job! Stay consistent!",
        "Small sessions add up to big wins."
    ]

    # Show a summary of the user's plan
    print("\nSummary of your plan:")
    print(f"  Loops: {loops}")
    print(f"  Study per loop: {study_mins} minutes")
    print(f"  Break per loop: {break_mins} minutes")
    print(f"  Mode: {'TEST (fast)' if fast else 'NORMAL (real time)'}\n")

    # Track how long the full session took
    started_at = datetime.now()

    # Keeps track of how many loops the user finishes
    completed_loops = 0

    # -----------------------------------------------------------
    # MAIN LOOP: Runs once for each study session
    # -----------------------------------------------------------
    for i in range(1, loops + 1):

        # STUDY PHASE
        print(f"--- Loop {i} of {loops}: STUDY ---")
        countdown(study_mins * scale, "Study")   # Run countdown
        beep()                                    # Make alert sound
        print("\nStudy time is up! Take a break.")

        # Motivational message from the list
        print(messages[(i - 1) % len(messages)])
        print()

        # BREAK PHASE (skip after last loop)
        if i < loops:
            print(f"--- Loop {i} of {loops}: BREAK ---")
            countdown(break_mins * scale, "Break")
            beep()
            print("\nBreak time is over! Get ready for the next study session.\n")

        completed_loops += 1

    # Calculate total time spent
    finished_at = datetime.now()
    duration = finished_at - started_at

    # End message
    print("🎉 All study loops complete! Great job!")
    if name:
        print(f"Nice work, {name}!")
    print(f"Total loops completed: {completed_loops}")
    print(f"Total elapsed time: {duration}")


# This line makes the program run only if you run THIS file
if __name__ == "__main__":
    main()
