import csv
import requests
from bs4 import BeautifulSoup  # HTML data structure
import os
dir_path=os.path.dirname(os.path.realpath(__file__))
# Done - 'shorts','dresses','tops','sweaters','outerwear', 'skirts','activewear' ,'jeans','pants'
# To Do  - 'sweaters','outerwear', 'skirts','activewear' ,'jeans','pants'
listcategory =['sweaters','outerwear', 'skirts'] # coats & jackets are know as outer wear
listcondition = [1,2,3,4,5,6,7] # 1,2,3,4,5,6,7
noOftries=3
new_with_tags = False
like_new = False
gently_used = False
signs_of_wear = False
mark_down = False
new_arrival = False
luxe = False
sourcing_price = 0

headerrow = ['item_number', 'description', 'Category', 'Brand', 'Sales_Price', 'Retail_Price', 'New with Tags',
             'Like-New', 'Gently Used', 'Signs of Wear', 'Mark Down', 'New Arrival', 'LUXE', 'sourcing price']
for category in listcategory:
    for booleancondition in listcondition:
        consterror = 60
        nexterrorpage = 0
        errorpage = ''
        if booleancondition==1:
            new_with_tags = False
            like_new = False
            gently_used = False
            signs_of_wear = False
            mark_down = False
            new_arrival = False
        if booleancondition==2:
            new_with_tags = True
            like_new = False
            gently_used = False
            signs_of_wear = False
            mark_down = False
            new_arrival = False
        if booleancondition==3:
            new_with_tags = False
            like_new = True
            gently_used = False
            signs_of_wear = False
            mark_down = False
            new_arrival = False
        if booleancondition==4:
            new_with_tags = False
            like_new = False
            gently_used = True
            signs_of_wear = False
            mark_down = False
            new_arrival = False
        if booleancondition==5:
            new_with_tags = False
            like_new = False
            gently_used = False
            signs_of_wear = True
            mark_down = False
            new_arrival = False
        if booleancondition==6:
            new_with_tags = False
            like_new = False
            gently_used = False
            signs_of_wear = False
            mark_down = True
            new_arrival = False
        if booleancondition==7:
            new_with_tags = False
            like_new = False
            gently_used = False
            signs_of_wear = False
            mark_down = False
            new_arrival = True
        csvfilename = category + str(new_with_tags) + str(like_new) + str(gently_used) + str(signs_of_wear) + str(
            mark_down) + str(new_arrival)
        j = 0  # Counter for records


        with open(dir_path+'/data/'+csvfilename+'.csv', 'w') as f1:
            writer = csv.writer(f1,delimiter='|',  lineterminator='\n' )
            writer.writerow(headerrow)
            attemptedtries = 0
            for page in range(1, 100000):
                if not mark_down and not new_with_tags and not like_new and not gently_used and not signs_of_wear and not new_arrival :
                    page_url = "https://www.thredup.com/products/women/"+category+"?department_tags=women&page=" + str(
                    page) + "&search_tags=women-"+category+"&sort=Newest+First"
                if mark_down and not new_with_tags and not like_new and not gently_used and not signs_of_wear and not new_arrival:
                    page_url = "https://www.thredup.com/products/women/"+category+"?department_tags=women&page=" + str(
                        page) + "&search_tags=women-"+category+"&sort=Newest+First&clearance=true"
                if not mark_down and not new_with_tags and not like_new and not gently_used and not signs_of_wear and new_arrival:
                    page_url = "https://www.thredup.com/products/women/"+category+"?department_tags=women&page=" + str(
                        page) + "&search_tags=women-"+category+"&sort=Newest+First&listed_days=7"
                if not mark_down and new_with_tags and not like_new and not gently_used and not signs_of_wear and not new_arrival:
                     page_url = "https://www.thredup.com/products/women/"+category+"?department_tags=women&page=" + str(
                            page) + "&search_tags=women-"+category+"&sort=Newest+First&condition=q1_nwt"
                if not mark_down and not new_with_tags and like_new and not gently_used and not signs_of_wear and not new_arrival:
                    page_url = "https://www.thredup.com/products/women/"+category+"?department_tags=women&page=" + str(
                        page) + "&search_tags=women-"+category+"&sort=Newest+First&condition=q1_only"
                if not mark_down and not new_with_tags and not like_new and gently_used and not signs_of_wear and not new_arrival:
                    page_url = "https://www.thredup.com/products/women/"+category+"?department_tags=women&page=" + str(
                        page) + "&search_tags=women-"+category+"&sort=Newest+First&condition=q2_only"
                if not mark_down and not new_with_tags and not like_new and not gently_used and signs_of_wear and not new_arrival:
                    page_url = "https://www.thredup.com/products/women/"+category+"?department_tags=women&page=" + str(
                        page) + "&search_tags=women-"+category+"&sort=Newest+First&condition=q3_only"

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
                    for attemptedtries in range(1,noOftries):
                        scrappage = requests.get(page_url)
                        html_doc = scrappage.text
                        page_soup = BeautifulSoup(html_doc, 'lxml')
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
                i = 0  # counter for record on the page
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

                    sales_price = sales_price_soup.find("div", {"class": "formatted-prices"}).find("span", {"class": "formatted-price price-color--regular with-promo"})
                    # print(sales_price_value)

                    if sales_price is None:
                        sales_price=sales_price_soup.find("div", {"class": "formatted-prices"}).find("span", {"class": "formatted-price price-color--sale with-promo"})
                    if sales_price is None:
                        sales_price=sales_price_soup.find("div", {"class": "formatted-prices"}).find("span", {"class": "formatted-price price-color--regular"})
                    if sales_price is None:
                        sales_price=sales_price_soup.find("div", {"class": "formatted-prices"}).find("span", {"class": "formatted-price price-color--sale"})

                    retail_price_soup = BeautifulSoup(str(container), 'lxml')
                    retail_price = retail_price_soup.find("div", {"class": "formatted-prices"}).find("span", {
                        "class": "formatted-msrp"})

                    try:
                        item_brand_value = item_brand[0].text
                        item_description_value = item_card_bottom[1].get('href').rsplit('/', 2)[-2]
                        item_number_value = item_card_bottom[1].get('href').rsplit('/', 1)[-1] # 43919419
                        try:
                            sales_price.text
                            sales_price_value=sales_price.text
                        except NameError:
                            sales_price_value=0
                        try:
                            retail_price.text
                            retail_price_value=retail_price.text
                        except :
                            retail_price_value=0
                        if retail_price is None:
                            retail_price_value=0
                    except:
                        file = open(dir_path+'/logs/'+csvfilename+'.log', 'a+')
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
                    print(category+' - '+str(booleancondition)+' - '+str(j)+' - '+str(i) + ' - ' + item_number_value)
            file = open(dir_path+'/logs/'+csvfilename+'.log', 'a+')
            file.write(errorpage + '\n')
            file.close()
