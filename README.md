# Pokémon Palette Scraper

## Overview
The Pokémon Palette Scraper is a tool designed to extract color palettes for Pokémon from a specific website (pokemon palette). The scraper collects hex codes representing the colors for each Pokémon, which can be used in various projects such as visualizations, websites, or data analysis. This project aims to make it easier to access and utilize color information for Pokémon in a structured format.

## Features
- Scrapes color palette information for each Pokémon.
- Outputs color palettes as hex codes per Pokémon.
- Saves the data in a structured format (e.g., sqlite3 DB) for easy integration with other projects.
- Interactive tool menu for managing scraping and database operations.

## Installation

### Prerequisites
- Python 3.8 or higher
- Required Python packages (listed in `requirements.txt`)
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Recon1991/pk-palette-scraper.git
   cd pokemon-palette-scraper
   ```

2. **Create a Virtual Environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Install ChromeDriver**:
   - Download ChromeDriver from [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
   - Make sure the version matches your installed Google Chrome version.
   - Add the path to ChromeDriver to your system's PATH environment variable, or place it in the project directory.

## Usage

1. **Run the Scraper Tool**:
   ```bash
   python palette-tool.py
   ```

   The tool provides an interactive menu with the following options:
   
   - **1. Non-Shiny Scraping**: Scrapes the color palettes for non-shiny Pokémon and saves them to the database.
   - **2. Shiny Scraping**: Scrapes the color palettes for shiny Pokémon and saves them to the database.
   - **3. Merge Non-Shiny and Shiny Databases**: Merges the non-shiny and shiny color palette databases into a single database.
   - **4. Exit**: Exits the tool.

2. **Modify Parameters**:
   You can modify the script to target different URLs or adjust scraping behavior by editing the `scraper.py` or `shiny_scraper.py` files.

## Output
- The scraped data will be saved in an SQLite database (`pokemon_palettes_base.db` and `pokemon_palettes_shiny.db`), and the merged data will be saved as `pokemon_palettes_merged.db`.
- Each database contains the Pokémon's name and its corresponding color palette (nine hex codes).

## Project Structure
- `scraper.py`: The script that scrapes non-shiny Pokémon color palettes.
- `shiny_scraper.py`: The script that scrapes shiny Pokémon color palettes.
- `pokemon_palette_db_merger.py`: The script that merges the non-shiny and shiny databases.
- `palette-tool.py`: The interactive tool that provides an easy-to-use menu for managing the scraping and merging processes.
- `requirements.txt`: List of dependencies required to run the scraper.
- `README.md`: Documentation for the project.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Any improvements, such as additional features or optimizations, are welcome.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Disclaimer
Please note that the scraping process can take a considerable amount of time to complete, depending on the number of Pokémon and the website's response time. It is recommended to be patient and avoid interrupting the process once started.
 Be mindful of the website's terms of service, and avoid overwhelming the server with too many requests.

## Contact
For any questions or feedback, feel free to open an issue or contact the project maintainer.
