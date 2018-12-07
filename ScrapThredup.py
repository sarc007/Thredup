import csv
import requests
from bs4 import BeautifulSoup  # HTML data structure

consterror = 250
nexterrorpage = 0
errorpage = ''
category = 'Short'
new_with_tags = False
like_new = False
gently_used = False
signs_of_wear = False
mark_down = False
new_arrival = False
luxe = False
sourcing_price = 0
csvfilename = category + str(new_with_tags) + str(like_new) + str(gently_used) + str(signs_of_wear) + str(
    mark_down) + str(new_arrival) + '.csv'
headerrow = ['item_number', 'description', 'Category', 'Brand', 'Sales_Price', 'Retail_Price', 'New with Tags',
             'Like-New', 'Gently Used', 'Signs of Wear', 'Mark Down', 'New Arrival', 'LUXE', 'sourcing price']
j = 0  # Counter for records
i = 0  # counter for record on the page
with open(csvfilename, 'w') as f1:
    writer = csv.writer(f1, lineterminator='\n', )
    writer.writerow(headerrow)
    for page in range(1, 10000000):

        page_url = "https://www.thredup.com/products/women/shorts?department_tags=women&page=" + str(
            page) + "&search_tags=women-shorts&sort=Newest+First"
        #		uClient = uReq(page_url)
        print(page_url)
        scrappage = requests.get(page_url)
        html_doc = scrappage.text
        page_soup = BeautifulSoup(html_doc, 'lxml')
        # parses html into a soup data structure to traverse html
        # as if it were a json data type.
        # page_soup = BeautifulSoup(uClient.read(), "html.parser")
        # print(page_soup.prettify())
        errtxt1 = page_soup.encode("utf-8")
        errtxt = page_soup.prettify()
        errfound = False
        errfound1 = False
        if errtxt.find('Try removing some filters to see more items.') >= 0:
            errfound = True
        if errtxt.find('We couldn\'t find anything matching your search.') >= 0:
            errfound1 = True

        if errfound and errfound1:
            errorpage = errorpage + '\n' + 'Error or no data found Record No : ' + str(j) + ' Page No : ' + str(page)
            nexterrorpage = nexterrorpage + 1
        if nexterrorpage > consterror:
            print(errorpage)
            break
        # 	print("The ERROR IS RAISED")
        # 		errorpage = errorpage+'\n'+'Error or no data found'+ str(page)
        # 		nexterrorpage=nexterrorpage+1
        # 		if nexterrorpage > consterror :
        # 			break
        # 	# opens the connection and downloads html page from url
        # 	uClient = uReq(page_url)
        # 	print (page_url)
        #
        # parses html into a soup data structure to traverse html
        # as if it were a json data type.

        # print(page_soup.prettify())

        # finds each product from the store page
        containers = page_soup.findAll("div", {"class": "results-grid-item"})
        # print(containers)

        for container in containers:
            item_card_bottom_soup = BeautifulSoup(str(container), 'lxml')
            item_card_bottom = item_card_bottom_soup.find("div", {"class": "item-card-bottom"}).findAll("a")
            #	container("div", {"class":"brand-name link"})
            # method1 = soup.find('div').text
            # method2 = soup.find('div').find('span').text
            # method3 = soup.find('span', class_='value-frame').text
            item_brand_soup = BeautifulSoup(str(container), 'lxml')
            item_brand = item_brand_soup.findAll("div", {"class": "brand-name link"})
            # item_brand_soup = BeautifulSoup(item_card_bottom, 'lxml')
            i = i + 1
            j = j + 1

            # print(item_number_value)
            # print(item_description_value)
            sales_price_soup = BeautifulSoup(str(container), 'lxml')
            sales_price = sales_price_soup.find("div", {"class": "formatted-prices"}).find("span", {
                "class": "formatted-price price-color--regular with-promo"})
            # print(sales_price_value)
            retail_price_soup = BeautifulSoup(str(container), 'lxml')
            retail_price = retail_price_soup.find("div", {"class": "formatted-prices"}).find("span", {
                "class": "formatted-msrp"})

            try:
                item_brand_value = item_brand[0].text
                item_description_value = item_card_bottom[1].get('href').rsplit('/', 2)[-2]
                item_number_value = item_card_bottom[1].get('href').rsplit('/', 1)[-1]
                sales_price_value = sales_price.text
                retail_price_value = retail_price.text
            except:
                file = open('testfile.txt', 'a+')
                file.write(
                    str(j) + ' - ' + item_description_value + ' - ' + item_number_value + ' - ' + str(i) + ' - ' + str(
                        page) + '\n')
                file.close()
            #	retail_price_value=0
            # print(retail_price_value)
            # for itemdetail in itemdetails:
            #	itemdetail.div.select()
            # brand = container.div.select("a")[1].text
            # print("brand: " + brand)

            # SalesPrice_RetailPrice = container.div.select("a")[2].text
            # print("SalesPrice_RetailPrice: " + SalesPrice_RetailPrice)
            row = [item_number_value, item_description_value, category, item_brand_value, sales_price_value,
                   retail_price_value, new_with_tags, like_new, gently_used, signs_of_wear, mark_down, new_arrival,
                   luxe, sourcing_price]
            # print(brand)
            # print(SalesPrice_RetailPrice)
            writer.writerow(row)
            print(str(i) + ' - ' + item_number_value)
    file = open('testfile.txt', 'a+')
    file.write(errorpage + '\n')
    file.close()
