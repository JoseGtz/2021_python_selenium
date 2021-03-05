"""Automatically Tic Tac Toe"""
import random
from selenium.common.exceptions import TimeoutException
from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def winner(wait):
    """Winner Functionality"""
    try:
        locator = (By.XPATH, "//div[@class= 'board win']")
        wait.until(EC.presence_of_element_located(locator))
        return True
    except TimeoutException:
        return False


def select_empty_box(wait):
    """Select an empty box"""
    try:
        locator = (By.CSS_SELECTOR, '.square')
        elements = wait.until(EC.visibility_of_all_elements_located(locator))
        empty = []
        for box in elements:
            cell = box.find_element_by_tag_name('div')
            if not cell.get_attribute('class'):
                empty.append(box)
        print(f'Total boxes: {len(empty)}')
        target = random.choice(empty)
        target.click()
    except TimeoutException as exception:
        raise RuntimeError(f'No empty boxes{exception}')


def print_game_stats(wait: WebDriverWait):
    """Print game stats"""
    player_1_score_loc = (By.CSS_SELECTOR, '.player1 .score')
    player_1_score = wait.until(EC.visibility_of_element_located(player_1_score_loc))

    ties_score_loc = (By.CSS_SELECTOR, '.ties .score')
    ties_score = wait.until(EC.visibility_of_element_located(ties_score_loc))

    player_2_score_loc = (By.CSS_SELECTOR, '.player2 .score')
    player_2_score = wait.until(EC.visibility_of_element_located(player_2_score_loc))

    print(f'Player: {player_1_score.text}, Tie: {ties_score.text}, Computer: {player_2_score.text}')


if __name__ == '__main__':
    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 3)
    my_driver.get("https://playtictactoe.org/")
    while not winner(my_wait):
        select_empty_box(my_wait)
    print_game_stats(my_wait)
    my_driver.quit()
