# import os

# def safe_write_to_file(filename, data):
#     backup_name = f"{filename}.backup"
    
#     # Create backup if original file exists
#     if os.path.exists(filename):
#         with open(filename, 'r', encoding='utf-8') as original, \
#              open(backup_name, 'w', encoding='utf-8') as backup:
#                 backup.write(original.read())
#         print(f"Backup created: {backup_name}")
#     else:
#         print("No existing file found. Creating a new one.")
    
#     # Write new data
#     with open(filename, 'w', encoding='utf-8') as file:
#         file.write(data)
#     print(f"New data written to: {filename}")


# # --- Test the function ---

# # Step 1: First save (creates backup if file exists)
# safe_write_to_file('3_notes.txt', "Day 2 - Learned about file backups in Python.\n")

# # Step 2: Second save (will overwrite again, but make another backup)
# safe_write_to_file('3_notes.txt', "Day 3 - Experimented with CSV files and backups.\n")

# --- Extension Task ---
# TODO: Modify this code so that instead of overwriting '3_notes.txt.backup',
# it creates a new backup file each time with a timestamp in its name.
#
# Example:
#     3_notes_2025-10-11_16-30-45.backup
#
# Steps to complete:
# 1. Import the 'datetime' module (already imported above).
# 2. Inside the backup section, generate a timestamp:
#       timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# 3. Create a new backup filename using that timestamp.
# 4. Open the backup file in *append* ('a') mode instead of overwrite ('w')
#    to keep all previous versions together if desired.
#
# Hint: Try printing the backup filename to verify it changes each time you run the program.
#
# Optional Challenge:
#     Add a line at the top of each backup file saying when it was created.
#     Example: "Backup created on 2025-10-11 16:30:45\n"
# 
# Scroll to the bottom to see a possible solution





























import os
from datetime import datetime

def safe_write_to_file(filename, data):
    """
    Writes new data to a file safely.
    If the file already exists, creates a timestamped backup
    before overwriting it.
    """
    if os.path.exists(filename):
        # Generate timestamp for unique backup name
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_name = f"{filename}_{timestamp}.backup"

        # Create timestamped backup
        with open(filename, 'r', encoding='utf-8') as original, \
             open(backup_name, 'w', encoding='utf-8') as backup:
            # Optional header in backup file
            backup.write(f"Backup created on {datetime.now()}\n")
            backup.write(original.read())

        print(f"Backup created: {backup_name}")
    else:
        print("No existing file found. Creating a new one.")
    
    # Write new data to main file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)
    print(f"New data written to: {filename}")


# --- Test the function ---

# Step 1: First save (creates file if not present)
safe_write_to_file('3_notes.txt', "Day 2 - Learned about file backups in Python.\n")

# Step 2: Second save (creates timestamped backup and overwrites main file)
safe_write_to_file('3_notes.txt', "Day 3 - Experimented with CSV files and timestamped backups.\n")

