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

Contact us at john.doe@service.co.uk or hello@domain.com.  
Call us on (123) 456-7890 or 123-456-7890 or 123.456.7890.  
Visit https://www.example.com or http://blog.site.org/post.  
Payment via 1234-5678-9012-3456 or 1234 5678 9012 3456.  
Meetings at 2:45 PM, 14:30, 23:59, and 02:00 AM.  
HTML tags: <body class="main">, <img src="x.jpg">, <html>.  
Trending: #PythonRocks and #TechNews.  
Prices: $19.99 and $1,234.56.

    📤 Sample Output

Email Addresses:

john.doe@service.co.uk

hello@domain.com

Phone Numbers:

(123) 456-7890

123-456-7890

123.456.7890

URLs:

https://www.example.com

http://blog.site.org/post

Credit Card Numbers:

1234-5678-9012-3456

1234 5678 9012 3456

Times:

2:45 PM

14:30

23:59

02:00 AM

HTML Tags:

<body class="main">
<img src="x.jpg">
<html>
Hashtags:

#PythonRocks

#TechNews

Currency Amounts:

$19.99

$1,234.56

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
