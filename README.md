
# AI News Scraper

AI News Scraper is a Python-based project that leverages CrewAI tools to scrape and save the latest news articles from the web. Users can specify topics of interest, and the scraper dynamically fetches relevant news from reputable websites, storing them in a structured format.

## Features
- **Customizable Topics**: Specify the topics of interest to scrape targeted news.
- **Timestamped Organization**: Saves news articles with timestamps for better categorization.
- **CrewAI Integration**: Utilizes `SerperDevTool` and `ScrapeWebsiteTool` from CrewAI for efficient scraping.
- **Automated Task Management**: Automatically interpolates tasks and agents for a seamless scraping experience.

## File Structure
```plaintext
ai_news/
├── src/
│   ├── ai_news/
│   │   ├── config/
│   │   │   ├── agents.yaml   # Configuration for scraping agents
│   │   │   ├── tasks.yaml    # Configuration for scraping tasks
│   │   ├── tools/
│   │   │   ├── crew.py       # CrewAI setup and initialization
│   │   │   ├── main.py       # Entry point to run the scraper
├── tests/                    # Unit tests for project components
├── news/                     # Output folder for saved news articles
├── .env                      # Environment variables (e.g., API keys)
├── .gitignore                # Ignored files for Git
├── pyproject.toml            # Dependency and project configuration
├── README.md                 # This documentation
```

## Installation

1. **Clone the Repository**
   ```bash
   git clone <https://github.com/Prahaladha-Reddy/Ai_News_Scrapper>
   cd ai_news
   ```

2. **Set Up Environment**
   - Create a `.env` file in the project root and configure it with the necessary secrets (e.g., API keys).
   - Example:
     ```env
     SERPER_API_KEY=your_api_key
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Edit `main.py`**
   - Specify the topic you want to scrape and the timestamp format:
     ```python
     inputs = {
         'topic': 'openai',
         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
     }
     ```

2. **Run the Script**
   ```bash
   python src/ai_news/tools/main.py
   ```

3. **View Results**
   - The scraped news articles are saved in the `news/` directory, with filenames based on the timestamp.

## Technologies Used
- **Python**: Core programming language for the project.
- **CrewAI Tools**:
  - `SerperDevTool`: For precise web scraping.
  - `ScrapeWebsiteTool`: To extract structured data from news websites.
- **Dependency Management**: Managed via `pyproject.toml`.


