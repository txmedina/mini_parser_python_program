# HTML Credential Mini Parser

A simple Python script that extracts personal credential information from an HTML file using BeautifulSoup.

# Description

This script reads an HTML file and extracts the following fields if they exist within the system:
- Name
- Title
- Office
- Phone
- Email

The parsed information is then written to `output.txt` on he user machine.

# 🛠 Requirements

- Python 3.x
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [lxml](https://pypi.org/project/lxml/)

# 💾 Installation

Install the required libraries using pip:

```bash
pip install beautifulsoup4 lxml
```

# How to Run Program

1. HTML file must be saved locally to user machine.
2. Open desired command prompt or terminal.
3. Navigate (`cd`) to the directory where `PyMiniParser.py` is located.
4. Run the script:

```bash
python PyMiniParser.py
```

5. Enter exact name of the HTML file when prompted.
6. Contents will be saved to `output.txt` on user machine

# Example Input HTML

```html
<div class="name">Jon Smith</div>
<div class="first-appointment">Professor of CS</div>
<div class="office">Room 512, CS Building</div>
<div class="phone">512-5555</div>
<div class="email"><a href="mailto:jdoe@example.com">jsmith@example.com</a></div>
```

# Output

```txt
Name: Jon Smith
Title: Professor of CS
Office: Room 512, CS Building
Phone: 512-5555
Email: jsmith@example.com
```

## 👨‍💻 Author

**Thomas Medina-Herrera**  
📧 tamedin02@gmail.com
