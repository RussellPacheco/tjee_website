from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re
import os
import time


class Meetup:
    def __init__(self):
        ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
        DRIVER_PATH = None

        if os.name == "nt":
            DRIVER_PATH = os.path.join(ROOT_PATH, "resources/chromedriver.exe")
        elif os.name == "posix":
            DRIVER_PATH = os.path.join(ROOT_PATH, "resources/chromedriver")

        OPTIONS = Options()
        OPTIONS.headless = True
        OPTIONS.add_argument("--incognito")

        self.driver = webdriver.Chrome(options=OPTIONS, service=Service(DRIVER_PATH))

    def close(self):
        self.driver.close()

    def _scroll_down(self):
        """A method for scrolling the page."""

        # Get scroll height.
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:

            # Scroll down to the bottom.
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load the page.
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height.
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

    def login(self, email: str, password: str) -> BeautifulSoup:
        self.driver.get("https://www.meetup.com/login")

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "email")))

        emailInput = self.driver.find_element(By.ID, "email")
        emailInput.send_keys(email)
        passwordInput = self.driver.find_element(By.ID, "current-password")
        passwordInput.send_keys(password + Keys.ENTER)

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_any_elements_located(
            (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/main/div[1]/div/div[2]/div[2]/div/div/div/div/a")))

    def _get_total_members(self) -> list:
        # list_data = soup.find_all('li', class_=re.compile("member-item"))

        large_pictures = self._get_large_pictures()

        self.driver.get("https://www.meetup.com/ja-JP/TJEE-Tokyo-Japanese-English-exchange/members/")
        self._scroll_down()
        soup = BeautifulSoup(self.driver.page_source)

        members_list = soup.find("ul", class_="list--infinite-scroll groupMembersList list")
        images = members_list.find_all("img", class_="avatar-print")
        members = members_list.find_all('h4', class_="text--bold text--ellipsisOneLine")
        new_members = []

        for member in members:
            new_member = {}
            split_name = member.contents[0].split(" ")
            firstname = True

            for name in split_name:
                if len(split_name) == 1:
                    new_member["firstname"] = name
                    new_members.append(new_member)
                else:
                    if firstname:
                        firstname = False
                        new_member["firstname"] = name
                    else:
                        new_member["lastname"] = name
                        if new_member not in new_members:
                            new_members.append(new_member)

        for image in images:
            link = image["src"]
            alt = image["alt"]
            fullname = alt.split(" ")
            firstname = fullname[0]
            lastname = ""
            if len(fullname) == 2:
                lastname = fullname[1]

            exists = False
            for member in new_members:
                if member["firstname"] == firstname:
                    member["thumbnail"] = link
                    exists = True

            if not exists:
                new_members.append({"firstname": firstname, "lastname": lastname, "thumbnail": link})

        return new_members

    def _find_large_picture_tag(self, tag):
        prog = re.compile(".*highres.*")
        if tag.has_attr('src'):
            if prog.match(tag['src']) and tag.name == "img":
                return True
        return False

    def _get_large_pictures(self):
        self.driver.get("https://www.meetup.com/ja-JP/TJEE-Tokyo-Japanese-English-exchange/members/")
        self._scroll_down()

        soup = BeautifulSoup(self.driver.page_source, features="html.parser")

        # WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located({By.CLASS_NAME: 'list--infinite-scroll groupMembersList list'}))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located([By.TAG_NAME, 'ul']))

        list_tag = self.driver.find_element(By.CLASS_NAME, 'groupMembersList')
        all_lists = list_tag.find_elements(By.CLASS_NAME, "member-item")

        group_member_list = soup.find(class_="groupMembersList")
        a_tag = group_member_list.find_all("li")

        members = []

        for tag in a_tag:
            link = "https://www.meetup.com" + tag.find("a")["href"]
            self.driver.get(link)
            soup = BeautifulSoup(self.driver.page_source, features="html.parser")
            img_tag = soup.find_all(self._find_large_picture_tag)

            if len(img_tag) == 1:
                print(f"THIS IS IMAGE {img_tag}")
                print(f"THIS IS THE IMAGE TAG: {img_tag[0]}")
                fullname = img_tag[0]['alt'].split(" ")
                firstname = fullname[0]
                lastname = ""
                if len(fullname) == 2:
                    lastname = fullname[1]
                link = img_tag[0]['src']

                member_obj = {"firstname": firstname, "lastname": lastname, "highres": link}
                members.append(member_obj)
                self.driver.back()

        return members

    def _merge_objects(self, obj1, obj2):

        merged_list = []

        for i in obj1:
            exists = False
            for e in obj2:
                if i["firstname"] == e["firstname"]:
                    exists = True
                    i.update(e)
                    merged_list.append(i)

            if not exists:
                merged_list.append(i)

        return merged_list

    def get_member_objects(self):
        members = self._get_total_members()
        highres_obj = self._get_large_pictures()

        return self._merge_objects(members, highres_obj)

    def quit(self):
        self.driver.quit()


soup = Meetup()
soup.login(email="languageexchange.tjee@gmail.com", password="Y8Z43cmYj3")
items = soup.get_member_objects()
soup.quit()


print(items)