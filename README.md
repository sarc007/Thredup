# Thredup
A project to extract data from the website and do statistical calculations on it
Below is the description of the requirement
=====================================================================================================
Scrape information on thredup.com
=====================================================================================================
Primarily we want to establish an indicator of second hand prices on clothes in relation to retail
price as new. Secondly we want to understand the priced by Thredup to consumers.
First step
Scrape information on
https://www.thredup.com/products/women?department_tags=women
Scrape all items for sale on women’s clothing with the following information by column
• Category. 9 in total, exclude swimwear. Dresses, Tops etc., Listed on the left in the image below
• Brand, presented in bold below each item, e.g. Catherines in the image below
• Sales price, presented in black, in the case of Catherines, $11,99
• Retail price, presented in grey with a line across, in the case of Catherines $60
• Condition: New with tags, Like-New, Gently used, Signs of wear. A search option presented in the
left hand columns further down on the page.
• Marked down or not. A search option presented in the left hand columns further down on the
page.
• New arrival or not. A search option presented in the left hand columns further down on the page.
Second step
Add one column for sourcing price. Multiply the Thredup sales price (eg $11,99) by the indicated
sourcing price in the list below. In this case 5% because it is a standard payout. If it is a LUXEbrand
the sourcing price will be higher. All brands included in the LUXE segment are listed on
https://www.thredup.com/luxe/brands1.pdf.
Deliverables
Short description of your scraping process, how did you go about and how can you be certain that
you got all the information?
All data consolidated in xls or csv including the column for correctly calculated sourcing price.
Answers in plain text
1. What is the average second hand price in percentage of estimated retail price per category (9)
and condition (4)? Presented in a matrix in xls.
2. What is the average second hand price in percentage of estimated retail price for marked down
items per category (9) and condition (4)? Presented in a matrix in xls.
3. How large is the share of marked down products in relation to all scraped items?
4. What is the average second hand price in percentage of estimated retail price for new arrivals?
