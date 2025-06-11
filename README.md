# 🧠 Job Scraper Bot

This Python-based job scraper collects listings from **Naukri**, **Glassdoor**, and **ZipRecruiter**, uses **proxy rotation** to avoid detection, and uploads the results to **Google Sheets**. It's fully compatible with **GitHub Actions** for automated scheduling.

---

## 🚀 Features

- 🔎 **Multi-platform scraping** from:
  - Naukri
  - Glassdoor
  - ZipRecruiter
- 🔁 **Rotating proxies** via `proxies.txt`
- 📤 **Auto-upload** to Google Sheets
- ⏱️ **GitHub Actions** for daily automation
- 🎭 **Headless browsing** with Playwright
- 🛡️ **Detection avoidance** with proxy rotation

---

## 🛠️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 2. Configure Environment

Create a `.env` file in the root directory:

```env
# .env
SHEET_ID=your_google_sheet_id_here
```

Save your Google Sheets service account JSON as:
```
google-creds.json
```

**Important:** Make sure your Google Sheet is shared with the service account email.

---

## 🤖 Run the Scraper Locally

```bash
python main.py
```

---

## ⚙️ GitHub Actions Setup (Optional)

### Step 1: Add Secrets

In your GitHub repository:
1. Go to **Settings** → **Secrets and variables** → **Actions** → **New repository secret**
2. Add the following secrets:

**GOOGLE_CREDS_JSON:** Paste the contents of `google-creds.json`

**ENV_FILE:** Paste contents of your `.env` file, e.g.:
```env
SHEET_ID=your_google_sheet_id_here
```

### Step 2: GitHub Workflow File

Create `.github/workflows/scrape.yml`:

```yaml
# .github/workflows/scrape.yml
name: Daily Job Scraper

on:
  schedule:
    - cron: '0 9 * * *'  # Every day at 9 AM UTC
  workflow_dispatch:

jobs:
  scrape:
    runs-on: ubuntu-latest
    
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v3
        
      - name: 🐍 Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          
      - name: 💾 Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          python -m playwright install
          
      - name: 🔐 Set up environment
        run: echo "${{ secrets.ENV_FILE }}" > .env
        
      - name: 🔑 Save Google credentials
        run: echo "${{ secrets.GOOGLE_CREDS_JSON }}" > google-creds.json
        
      - name: 🚀 Run scraper
        run: python main.py
```

---

## 📁 Project Structure

```
.
├── main.py
├── naukri_scraper.py
├── glassdoor_scraper.py
├── ziprecruiter_scraper.py
├── google_sheets.py
├── proxy_utils.py
├── .env
├── proxies.txt
├── requirements.txt
├── google-creds.json
└── .github/
    └── workflows/
        └── scrape.yml
```

---

## 🌐 Proxy Configuration

Create `proxies.txt` and add one proxy per line:

```txt
http://123.456.78.9:8080
http://89.23.45.67:3128
socks5://proxy.example.com:1080
```

**Note:** If the file is empty or missing, the scraper will run without a proxy.

---

## 📦 Requirements

Create `requirements.txt` with the following dependencies:

```txt
pandas
playwright
google-api-python-client
google-auth
python-dotenv
```

---

## 📊 Google Sheets Setup

1. **Create a Google Cloud Project:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one

2. **Enable Google Sheets API:**
   - Navigate to APIs & Services → Library
   - Search for "Google Sheets API" and enable it

3. **Create Service Account:**
   - Go to APIs & Services → Credentials
   - Click "Create Credentials" → "Service Account"
   - Download the JSON key file and rename it to `google-creds.json`

4. **Share Your Google Sheet:**
   - Open your Google Sheet
   - Click "Share" and add the service account email with "Editor" permissions
   - Copy the Sheet ID from the URL

---

## 🚀 Usage

### Local Development
```bash
# Clone the repository
git clone <your-repo-url>
cd job-scraper-bot

# Install dependencies
pip install -r requirements.txt
playwright install

# Configure environment
cp .env.example .env
# Edit .env with your Google Sheet ID

# Add your Google credentials
# Save google-creds.json in the root directory

# Run the scraper
python main.py
```

### Automated Scheduling
Once you've set up GitHub Actions, the scraper will:
- Run automatically every day at 9 AM UTC
- Can be manually triggered via GitHub's "Run workflow" button
- Upload results directly to your Google Sheet

---

## 📌 Important Notes

- **Playwright** runs in headless mode for better performance
- **Proxy rotation** helps avoid IP blocking and rate limiting
- **Google Sheet** must be shared with the service account email
- **Manual triggers** available in GitHub Actions for testing
- **Error handling** included for robust operation
- **Rate limiting** implemented to respect website policies

---

## 🔧 Troubleshooting

### Common Issues:

1. **Google Sheets Permission Error:**
   - Ensure the Google Sheet is shared with the service account email
   - Verify the `SHEET_ID` in your `.env` file

2. **Proxy Connection Issues:**
   - Check if proxies in `proxies.txt` are active
   - Remove or update non-working proxies

3. **Playwright Installation:**
   - Run `playwright install` after installing requirements
   - Ensure you have sufficient disk space

4. **GitHub Actions Failures:**
   - Verify all secrets are properly set
   - Check the Actions logs for specific error messages

---

## 📈 Future Enhancements

- [ ] Add more job sites (Indeed, LinkedIn, etc.)
- [ ] Implement job deduplication
- [ ] Add email notifications for new jobs
- [ ] Create a web dashboard for results
- [ ] Add filtering options for job criteria
- [ ] Implement database storage option

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ⚠️ Disclaimer

This tool is for educational and personal use only. Please respect the terms of service of the websites being scraped and use appropriate delays between requests. The authors are not responsible for any misuse of this tool.