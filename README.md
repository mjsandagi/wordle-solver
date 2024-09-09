## Wordle Solver

This Python script retrieves the solution for a specific day's Wordle from The New York Times Wordle API.

### Usage

3. Open a terminal.
4. Navigate to the directory containing the python file.
5. Run the program by typing `python solution.py` and press Enter.
6. Enter the date of the Wordle puzzle you want to get the solution for in the format `YYYY-MM-DD` when prompted.

### How it works

1. **API Request**: The code constructs a URL using the provided date and sends a request to the New York Times Wordle API.

3. **Response Handling**: The response is parsed from JSON format, extracting the solution to the Wordle puzzle for that date.

4. **Output**: The solution is displayed to the user.

### Note

Note that solutions for future dates may not be available as they might not have been uploaded yet by The New York Times.
