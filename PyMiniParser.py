# Thomas Medina-Herrera
#
# Theory of Automata - Mini Assignment -
#
# To run program: install python, install BeautifulSoup, install lxml, use command prompt to execute code
# python --version or go to python.org
# python -m pip install beautifulsoup4 or pip install beautifulsoup4
# pip install lxml
# open command prompt, cd (go to file location)
# run: python PyMiniParser.py

from bs4 import BeautifulSoup

# program asks for user input, html file
file_path = input("Enter name html file: ")

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')   # parses through html data

    # searches through credentials, if NOT there, outputs N/A
    name = soup.find('div', class_='name').text if soup.find('div', class_='name') else "N/A"
    title = soup.find('div', class_='first-appointment').text if soup.find('div', class_='first-appointment') else "N/A"
    office = soup.find('div', class_='office').text if soup.find('div', class_='office') else "N/A"
    phone = soup.find('div', class_='phone').text if soup.find('div', class_='phone') else "N/A"
    email = soup.find('div', class_='email').a['href'].replace('mailto:', '') if soup.find('div', class_='email') else "N/A"

    output_content = f"""
        Name: {name.strip()}
        Title: {title.strip()}
        Office: {office.strip()}
        Phone: {phone.strip()}
        Email: {email.strip()}
    """

    # saves credentials .txt file
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(output_content)

    print("Content was written to file output.txt.")

# ERROR if file NOT found
except FileNotFoundError:
    print(f"File'{file_path}' was not found.")
