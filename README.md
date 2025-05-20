ALU Regex Data Extraction
This project is a Python tool that uses regular expressions to extract different types of information from a large body of text (e.g., from web responses).

🔍 What It Extracts

✅ Email addresses

✅ URLs

✅ Phone numbers (in multiple formats)

✅ Credit card numbers

✅ Times (12-hour and 24-hour)

✅ HTML tags

✅ Hashtags

✅ Currency amounts
  
  🧪 Sample Input 

Emails: hello@domain.com, john.doe@service.co.uk

Websites: https://www.example.com, http://blog.site.org/post

Phones: (123) 456-7890, 123-456-7890, 123.456.7890

Cards: 1234 5678 9012 3456, 1234-5678-9012-3456

Times: 14:30, 2:45 PM, 02:00 AM, 23:59

Tags: <html>, <body class="main">, <img src="x.jpg">

Trending: #TechNews, #PythonRocks

Prices: $19.99, $1,234.56

    📤 Sample Output

Email Addresses:

 - hello@domain.com
 - john.doe@service.co.uk

URLs:

 - https://www.example.com,
 - http://blog.site.org/post

Phone Numbers:

 - 123.456.7890
 - 123-456-7890
 - (123) 456-7890

Credit Card Numbers:

 - 1234-5678-9012-3456
 - 1234 5678 9012 3456

Times:

 - 14:30
 - 23:59
 - 2:45 PM
 - 02:00 AM

HTML Tags:

 - <img src="x.jpg">
 - <body class="main">
 - <html> 

Hashtags:
 - #PythonRocks
 - #TechNews

Currency Amounts:
 - $1,234.56
 - $19.99



  📦 Setup Instructions

1. Clone this repository:

  git clone https://github.com/yourusername/alu_regex-data-extraction-yourusername

cd alu_regex-data-extraction-yourusername

2. Make sure Python 3 is installed 

3. Run the script:

    python runner.py

📂 File Structure

regex_extractors.py: Contains all regex functions.

runner.py: Loads data, calls extractors, and prints results.

sample_input.txt: Contains example data to test.

README.md: Project documentation.

🎯 Created for educational use. Customize or expand as needed.
