import dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re
import os
import time

dotenv.load_dotenv()


class Meetup:
    def __init__(self):
        ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
        DRIVER_PATH = None

        print(f"""
            
            The logged in user is {os.getlogin()}

            The os name is {os.name}

        """)

        if os.name != "posix":
            print(f"""

            The uname is {os.uname()}

            """)

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

    def _scroll_up(self):
        """"A method for scrolling the page."""
        self.driver.execute_script("window.scrollTo(0, 0);")

    def login(self, email: str, password: str):
        self.driver.get("https://www.meetup.com/login")

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "email")))
        emailInput = self.driver.find_element(By.ID, "email")
        emailInput.send_keys(email)
        passwordInput = self.driver.find_element(By.ID, "current-password")
        passwordInput.send_keys(password + Keys.ENTER)

        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_any_elements_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/main/div[1]/div/div[2]/div[2]/div/div/div/div/a")))
        except Exception as e:
            print(f"There was an exception: {e}")
            pass

    def get_pending_members(self) -> list:
        self.driver.get("https://www.meetup.com/ja-JP/TJEE-Tokyo-Japanese-English-exchange/members/?op=pending")
        self._scroll_down()
        soup = BeautifulSoup(self.driver.page_source, features="html.parser")
        pending_member_list = soup.find("ul", class_="groupMembersList")
        individual_list = pending_member_list.find_all("li")

        pending_members = []

        for li in individual_list:
            link = f"https://www.meetup.com{li.find('a').get('href')}"
            pending_members_name = li.find("h4").text
            pending_members_date = li.find("div", class_="member-item-subtitle").text
            date_array = re.findall("\d{1,5}", pending_members_date)

            pending_member = {
                "meetup_id": re.search("\d{2,}", link)[0],
                "meetup_name": pending_members_name,
                "app_date": f"{date_array[0]}/{date_array[1]}/{date_array[2]}",
                "link": link
            }

            pending_members.append(pending_member)

        return pending_members

    def get_pending_member_detail(self, member_obj):
        self.driver.get(member_obj["link"])
        soup = BeautifulSoup(self.driver.page_source, features="html.parser")
        member_info_card = soup.find_all("div", class_="_memberInfoCard-module_card__7_JXK")

        answers = {"answer_one": None, "answer_two": None, "answer_three": None}
        counter = 0
        for detail in member_info_card:
            qa = detail.find_all("p")

            if counter == 0:
                answers["answer_one"] = qa[1].text
            elif counter == 1:
                answers["answer_two"] = qa[1].text
            else:
                answers["answer_three"] = qa[1].text

            counter += 1

        member_obj["answers"] = answers

        return member_obj

    def approve_pending_member(self, member_obj, text="Welcome to TJEE!"):
        self.driver.get("https://www.meetup.com/ja-JP/TJEE-Tokyo-Japanese-English-exchange/members/?op=pending")
        member_list = self.driver.find_element(By.CLASS_NAME, f"member-item--{member_obj['meetup_id']}")
        approve_button = member_list.find_element(By.CLASS_NAME, "approveButton")
        approve_button.click()
        view_modal = self.driver.find_element(By.CLASS_NAME, "view--modal")
        name = view_modal.find_element(By.CLASS_NAME, "text--bold").text
        if member_obj['meetup_name'] == name:
            text_input = view_modal.find_element(By.TAG_NAME, "textarea")
            text_input.clear()
            text_input.send_keys(text)
            buttons = view_modal.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if button.text == "メンバーを承認":
                    button.click()
                    pass

    def deny_pending_member(self, member_obj, text):
        self.driver.get("https://www.meetup.com/ja-JP/TJEE-Tokyo-Japanese-English-exchange/members/?op=pending")
        member_list = self.driver.find_element(By.CLASS_NAME, f"member-item--{member_obj['meetup_id']}")
        decline_button = member_list.find_element(By.CLASS_NAME, "declineButton")
        decline_button.click()
        view_modal = self.driver.find_element(By.CLASS_NAME, "view--modal")
        name = view_modal.find_element(By.CLASS_NAME, "text--bold").text
        if member_obj['meetup_name'] == name:
            text_input = view_modal.find_element(By.TAG_NAME, "textarea")
            text_input.clear()
            text_input.send_keys(text)
            buttons = view_modal.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if button.text == "メンバーの申請を断る":
                    button.click()
                    pass

    def _get_total_members(self) -> list:
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

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located([By.TAG_NAME, 'ul']))

        group_member_list = soup.find(class_="groupMembersList")
        a_tag = group_member_list.find_all("li")

        members = []

        for tag in a_tag:
            link = "https://www.meetup.com" + tag.find("a")["href"]
            self.driver.get(link)
            soup = BeautifulSoup(self.driver.page_source, features="html.parser")
            img_tag = soup.find_all(self._find_large_picture_tag)

            if len(img_tag) == 1:
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
