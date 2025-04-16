import requests  # To fetch the website
from bs4 import BeautifulSoup  # To parse the website's HTML
import pandas as pd  # To store data in a table (like a spreadsheet)
import logging  # To keep track of any errors or important events
import os  # To interact with the operating system (like creating folders)

# --- 1. Setup Logging ---
# This creates a folder named "logs" (if it doesn't exist) and sets up logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/scraper.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# --- 2. Fetch the Web Page ---
def get_web_page(url):
    """
    Fetches the content of a web page.

    Args:
        url (str): The URL of the page to fetch.

    Returns:
        str: The HTML content of the page, or None if there was an error.
    """
    try:
        response = requests.get(url)  # Get the page
        response.raise_for_status()  # Raise an error for bad status codes (like 404)
        return response.text  # Return the page content as text
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to get page: {e}")  # Log the error
        return None


# --- 3. Extract Job Details ---
def extract_job_details(html):
    """
    Extracts job details (title, company, etc.) from the HTML.

    Args:
        html (str): The HTML content of the page.

    Returns:
        list: A list of dictionaries, where each dictionary represents a job.
    """

    soup = BeautifulSoup(html, "html.parser")  # Create a BeautifulSoup object to parse HTML
    jobs = []  # List to store the extracted job data

    job_elements = soup.find_all("div", class_="job-listing-details")  # Find all job detail sections
    for job_element in job_elements:
        title = job_element.find("h4").text.strip() if job_element.find("h4") else "N/A"  # Extract title
        company = job_element.find("span").text.strip() if job_element.find("span") else "N/A"  # Extract company
        link = job_element.find("a")['href'] if job_element.find("a") else "N/A" # Extract link
        description = job_element.get_text(strip=True) # Extract description
        jobs.append(
            {
                "Job Title": title,
                "Company": company,
                "Job URL": link,
                "Description": description,
            }
        )
    return jobs


# --- 4. Save Data to CSV ---
def save_jobs_to_csv(jobs, filename="jobs.csv"):
    """
    Saves the extracted job data to a CSV file.

    Args:
        jobs (list): The list of job dictionaries.
        filename (str, optional): The name of the CSV file. Defaults to "jobs.csv".
    """
    if not jobs:
        logging.warning("No jobs to save.")
        return

    try:
        df = pd.DataFrame(jobs)  # Create a pandas DataFrame from the job list
        df.drop_duplicates(inplace=True)  # Remove duplicate jobs
        df.to_csv(filename, index=False)  # Save to CSV (without the index)
        logging.info(f"Saved {len(df)} jobs to {filename}")
        print(f"Saved {len(df)} jobs to {filename}")
    except Exception as e:
        logging.error(f"Error saving to CSV: {e}")
        print(f"Error saving to CSV: {e}")


# --- 5. Main Function ---
def main():
    """
    Main function to orchestrate the scraping process.
    """

    url = "https://vacancymail.co.zw/jobs/"  # The website to scrape
    html = get_web_page(url)  # Fetch the HTML
    if html:
        jobs = extract_job_details(html)  # Extract job details
        save_jobs_to_csv(jobs)  # Save to CSV
    else:
        print("Could not get the web page.")


# --- 6. Run the Script ---
if __name__ == "__main__":
    main() # Run the main function