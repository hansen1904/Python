from selenium import webdriver

url = input('Type URL: ')

if "https://" not in url:
    url = "https://" + url
elif "http://" not in url:
    url = "https://" + url

driver = webdriver.Chrome('I:\chromedriver.exe')
driver.get('https://magnus-hansen.dk/')

titler = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']

print('')

for i in titler:

    elem = driver.find_elements_by_tag_name(i)

    if len(elem) > 1:
        print(i + " titler")

        for y in elem:
            print(y.text)
        print('')

    elif len(elem) == 1:

        print(i,"titler")
        print(elem[0].text)
        print('')

driver.close()
