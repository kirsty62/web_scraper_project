#   Web Scraper for vacancymail.co.zw Jobs

    This Python program scrapes job listings from [https://vacancymail.co.zw/jobs/](https://vacancymail.co.zw/jobs/), extracts relevant information, and saves it to a CSV file. [cite: 1, 2, 3, 4, 5]

    ##   Table of Contents

    1.  [Objective](#objective)
    2.  [Requirements](#requirements)
        * [Input](#input)
        * [Processing](#processing)
        * [Output](#output)
        * [Automation & Scheduling](#automation--scheduling)
        * [Error Handling & Logging](#error-handling--logging)
    3.  [Implementation Guidelines](#implementation-guidelines)
    4.  [Submission Requirements](#submission-requirements)
    5.  [Grading Rubric](#grading-rubric)
    6.  [Installation](#installation)
    7.  [Usage](#usage)
    8.  [Dependencies](#dependencies)

    ##   1. Objective <a name="objective"></a>

    The objective of this project is to develop a Python program that scrapes data from [https://vacancymail.co.zw/jobs/](https://vacancymail.co.zw/jobs/), consolidates the extracted data into a structured format (CSV), and optionally schedules the scraping task. [cite: 1, 2] This assignment reinforces fundamentals of programming taught during the crash course while exposing students to web scraping, data handling, and automation skills. [cite: 2]

    ##   2. Requirements <a name="requirements"></a>

    ###   Input <a name="input"></a>

    * Extract the 10 most recently posted jobs from [https://vacancymail.co.zw/jobs/](https://vacancymail.co.zw/jobs/) [cite: 3]
    * Extract relevant data such as: Job title, company, location, expiry date and job description. [cite: 3]

    ###   Processing <a name="processing"></a>

    * Store scraped data in a structured format:
        * CSV: Use pandas to save structured data. [cite: 4]
    * Implement data cleaning (e.g., removing duplicates, formatting dates). [cite: 5]

    ###   Output <a name="output"></a>

    * Generate an output file (`scraped_data.csv`). [cite: 5]

    ###   Automation & Scheduling <a name="automation--scheduling"></a>

    * Provide an option to schedule scraping at regular intervals (e.g., daily, hourly) using `schedule` or cron. [cite: 6]

    ###   Error Handling & Logging <a name="error-handling--logging"></a>

    * Implement exception handling for request failures, parsing errors, and connectivity issues. [cite: 7]
    * Log key events and errors using the `logging` module. [cite: 8]

    ##   3. Implementation Guidelines <a name="implementation-guidelines"></a>

    1.  Use `requests` for making HTTP requests. [cite: 8]
    2.  Use `BeautifulSoup` for parsing HTML (or Selenium if necessary). [cite: 9]
    3.  Use `pandas` for data storage and formatting. [cite: 9]
    4.  Use `schedule` (or cron for Linux/macOS) to automate scraping. [cite: 10]
    5.  Implement logging and error handling. [cite: 10]

    ##   4. Submission Requirements <a name="submission-requirements"></a>

    * A Python script (`web_scraper.py`) [cite: 11]
    * Sample output file (`scraped_data.csv`) [cite: 11]
    * A README file with setup instructions, dependencies, and usage guide [cite: 11]

    ##   5. Grading Rubric <a name="grading-rubric"></a>

    |   Criteria                   |   Excellent (10 pts)                                          |   Good (7 pts)                                        |   Satisfactory (5 pts)                                    |   Needs Improvement (2 pts)                                        |
    |   :------------------------- |   :---------------------------------------------------------- |   :-------------------------------------------------- |   :------------------------------------------------------ |   :------------------------------------------------------------- |
    |   Web Scraping               |   Scrapes data efficiently from multiple pages                 |   Scrapes correctly from a single page                 |   Scrapes but misses key data                          |   Fails to scrape correctly                                     |
    |   Data Storage               |   Saves clean data in multiple formats (CSV, Excel, DB)         |   Saves data in one format correctly                   |   Saves data but with formatting issues                  |   Does not save structured data correctly                      |
    |   Automation                   |   Implements a working scheduling mechanism                 |   Implements scheduling with minor issues               |   Scheduling partially works                              |   No scheduling feature implemented                              |
    |   Error Handling & Logging   |   Proper exception handling and logs key events                |   Handles most errors with basic logging               |   Some errors cause crashes                              |   No error handling implemented                                  |
    |   Code Structure & Readability |   Clean, modular code with comments                         |   Mostly well-structured but lacks comments           |   Some structure issues, lacks comments                  |   Poorly structured, difficult to read                          |
    |   Submission Completeness      |   All required files submitted and well-documented             |   Missing minor components                             |   Missing major components                               |   Submission incomplete                                          |

    ##   6. Installation <a name="installation"></a>

    Before you begin, ensure you have Python 3.6 or later installed on your system. You can download it from [python.org](https://www.python.org/).

    1.  Clone the repository:

        ```bash
        git clone <your_repository_url>
        cd <your_project_directory>
        ```

        * Replace `<your_repository_url>` with the actual URL of your Git repository.
        * Replace `<your_project_directory>` with the name of the directory where the project files are located
    2.  (Optional) Create a virtual environment (recommended):

        ```bash
        python3 -m venv venv # Create a virtual environment
        source venv/bin/activate # Activate it (Linux/macOS)
        # venv\Scripts\activate  (Windows)
        ```

    3.  Install the required Python packages:

        ```bash
        pip install -r requirements.txt
        ```

        * It's excellent practice to have a `requirements.txt` file in your project, listing all the dependencies. You can create it using:

            ```bash
            pip freeze > requirements.txt
            ```

        * If you don't have a `requirements.txt`, you can list the dependencies directly:

            ```bash
            pip install requests beautifulsoup4 pandas schedule
            ```

    ##   7. Usage <a name="usage"></a>

    1.  To run the web scraper:

        ```bash
        python web_scraper.py
        ```

    2.  The scraped data will be saved to a CSV file named `scraped_data.csv` in the same directory as the script.

    3.  (Optional) To enable scheduling:

        * Uncomment the scheduling lines in the `web_scraper.py` file.
        * Modify the schedule interval as needed. For example, to run the scraper daily at 9:00 AM:

            ```python
            schedule.every().day.at("09:00").do(job_runner)
            ```

        * Ensure your system is set up to run Python scripts at scheduled times (e.g., using cron on Linux/macOS or Task Scheduler on Windows).

    ##   8. Dependencies <a name="dependencies"></a>

    This project uses the following Python libraries:

    * [requests](https://pypi.org/project/requests/): For making HTTP requests.
    * [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/): For parsing HTML.
    * [pandas](https://pypi.org/project/pandas/): For data manipulation and CSV output.
    * [schedule](https://pypi.org/project/schedule/): (Optional) For scheduling the scraping.
    * [logging](https://docs.python.org/3/library/logging.html): For logging errors and events.