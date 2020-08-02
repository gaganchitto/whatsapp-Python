from selenium import webdriver

driver=webdriver.Chrome('chromedriver.exe') # Enter Chrome Driver path
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

while(True):
    name=input("Enter the name :") #enter the name of the person exaclty same as you save in your Phone
    if(name=="stop" or name=="Stop"): #type stop if you want to stop bombing
        break
    msg=input("Enter Your Message :")  # Enter the message you want to send
    count=int(input("Enter Number of times you want to send msg :"))  #Enter ho many time you wanna send that msg
    input("Scan the QR code and Enter any key")

    user=driver.find_element_by_xpath(f"//span[@title='{name}']")  
    user.click()

    msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

    for i in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

    print("Message has been Sent Successfully")
