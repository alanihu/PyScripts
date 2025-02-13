import requests
from bs4 import BeautifulSoup


def fetch_text_from_google_doc(url):
    try:
        response = requests.get(url, timeout=10)  
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the document: {e}")
        return None

    return BeautifulSoup(response.text, "html.parser")  
    
def get_message(html):

    headers = []
    rows = []
        
    #find the table rows and columns and saving in a list
    for i,row in enumerate(html.find_all('tr')):
        cols = [col.text.strip() for col in row.find_all('td')]
        if i == 0:
            headers=cols
        else:
            x,char,y = int(cols[0]),cols[1], int(cols[2])
            rows.append((x,char,y))


    #set max x,y points of the print matrix
    max_x =max(item[0] for item in rows)
    max_y =max(item[2] for item in rows)

    #create a matrix to print out the ccharacters

    matrix = [[' ' for _ in range(int(max_x) + 1)] for _ in range(int(max_y) + 1)]

    # Populate the matrix with characters from the list
    for x, char, y  in rows:
        matrix[y][x] = char  # Use (y, x) indexing

    return matrix

def print_matrix(matrix):
    """Prints the matrix with inverted y-coordinates."""
    if matrix is None:
        print("No message to display.")
        return

    for row in reversed(matrix):  # Invert y-axis
        print(''.join(row))

#url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
#Fetch and debug the data
doc_content = fetch_text_from_google_doc(url)
message = get_message(doc_content)

#Print to screen 
print_matrix(message)

# Developed by Alan
