from selenium import webdriver


def get_score():
    driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
    driver.get("http://localhost:8777")
    score = driver.find_element_by_id("score")
    s = score.text
    driver.close()
    driver.quit()
    return s




def check_score(result):
    if 0 <= int(result) <= 1000:
        return True
    else:
        return False



def main_function():
    result = get_score()
    var = check_score(result)
    if var == True:
      print("Pass")
    else:
        print("Failed")


main_function()






