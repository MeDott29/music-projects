# src/main.py

from song_analysis import identify_drop_section
from song_data import get_song_data

# Get the song data
song_data = get_song_data()

# Identify the drop section
drop_start, drop_end = identify_drop_section(song_data)

# Use the analysis results
if drop_start and drop_end:
    # Perform actions with the drop section, such as extracting or applying effects
    print(f"The drop section starts at {drop_start} and ends at {drop_end}")
else:
    print("No drop section found")
