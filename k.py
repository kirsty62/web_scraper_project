import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
import logging
import os

# === Logging Setup ===
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename='logs/scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# === Step 6: Fetch Job Listings Page ===
def fetch_jobs_page():
    try:
        url = "https://vacancymail.co.zw/jobs/"
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"❌ Failed to fetch jobs page: {e}")
        return None

# === Step 7: Parse Jobs ===
def parse_jobs(html):
    soup = BeautifulSoup(html, 'html.parser')
    jobs = []

    job_details = soup.find_all('div', class_='job-listing-details')
    job_footers = soup.find_all('div', class_='job-listing-footer')

    for i in range(min(len(job_details), len(job_footers))):
        detail_div = job_details[i]
        footer_div = job_footers[i]

        # Job title
        title_tag = detail_div.find('h4')
        title = title_tag.text.strip() if title_tag else detail_div.get_text(strip=True)[:100]

        # Company name
        company_tag = detail_div.find('span')
        company = company_tag.text.strip() if company_tag else ''

        # **Extract job link**
        link_tag = detail_div.find('a')
        job_url = link_tag['href'] if link_tag and 'href' in link_tag.attrs else None

        # Description (will be updated later)
        description = detail_div.get_text(strip=True)

        # Footer info
        footer_text = footer_div.get_text(strip=True)
        location = "Harare" if "Harare" in footer_text else "Unknown"

        # Try to extract expiry date
        expiry = ''
        for word in footer_text.split():
            if word.lower() in ["expires", "deadline", "closing"]:
                index = footer_text.lower().split().index(word)
                if index + 1 < len(footer_text.split()):
                    expiry = footer_text.split()[index + 1]
                break

        jobs.append({
            'Job Title': title,
            'Company': company,
            'Location': location,
            'Expiry Date': expiry,
            'Description': description,  # This will be the short description for now
            'Job URL': job_url  # Add the job URL
        })

    return jobs

# === Step 8: Save to CSV ===
def save_to_csv(jobs, filename='scraped_data.csv'):
    if not jobs:
        logging.warning("No job data to save.")
        return

    try:
        df = pd.DataFrame(jobs)

        if 'Expiry Date' in df.columns:
            df['Expiry Date'] = pd.to_datetime(df['Expiry Date'], errors='coerce')

        df.drop_duplicates(inplace=True)
        df.to_csv(filename, index=False)

        logging.info(f"✅ Saved {len(df)} job posts to {filename}")
        print(f"✅ Saved {len(df)} job posts to {filename}")
    except Exception as e:
        logging.error(f"Error saving to CSV: {e}")
        print(f"❌ Error saving to CSV: {e}")

# === Step 9: Main Workflow ===
def main():
    html = fetch_jobs_page()
    if html:
        jobs = parse_jobs(html)
        print(f"✅ Parsed {len(jobs)} job posts.")
        for job in jobs:
            print(job)
        save_to_csv(jobs)
    else:
        print("❌ Failed to fetch jobs page.")

# === Step 10: Scheduled Runner ===
def job_runner():
    logging.info("⏰ Scheduled job started.")
    main()

# === Step 11: Scheduling Logic ===
if __name__ == "__main__":
    # Run once daily at 9:00 AM
    # schedule.every().day.at("09:00").do(job_runner)
    schedule.every(1).minutes.do(job_runner)

    print("⏳ Waiting for scheduled jobs... (Press Ctrl + C to stop)")

    while True:
        schedule.run_pending()
        time.sleep(1)