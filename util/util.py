def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    import sys
    import os
    python = sys.executable
    os.execl(python, python, * sys.argv)


def clear_screen():
    """Clears the screen"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')