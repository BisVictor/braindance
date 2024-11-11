from game import *
from lobby import *
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(browser, by, value, timeout=10):
    return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((by, value)))

def wait_for_clickable(browser, by, value, timeout=10):
     return WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((by, value)))

def execute_steps(browser, filename):
    with open(filename, 'r') as file:
        steps = json.load(file)
    
    for step in steps:
        step_type = step['type']
        payload = step.get('payload', {})        
        if step_type == "create_game":
            if payload.get('private'):
                private_game_flag = True
            else:
                private_game_flag = False
            if payload.get('go_to_play'):
                go_to_play_falg = True
            else:
                go_to_play_falg = False
            create_game(browser, private_game=private_game_flag, go_to_game=go_to_play_falg)
        elif step_type == "enter_game":
            if payload.get('nickname') != None:
                nick_name_json = payload.get('nickname')
            if payload.get('role') == "owner" or "Owner":
                role_falg = "owner"
            elif payload.get('role') == "visitor" or "Visitor":
                role_falg = "visitor"
            if payload.get('skip'):
                skip_flag = True
            else:
                skip_flag = False
            enter_game(browser, nickname=nick_name_json, role=role_falg, skip=skip_flag)
        elif step_type == "create_turn" and payload.get('type') == "picture":
            if payload.get('header_text') != None:
                header_text_flag = payload.get('header_text')
            if payload.get('image_url') != None:
                image_url_flag = payload.get('image_url')
            if payload.get('text') != None:
                text_flag = payload.get('text')
            create_turn_picture(browser, header_text=header_text_flag, image_url=image_url_flag, text=text_flag)
        elif step_type == "create_turn" and payload.get('type') == "video":
            if payload.get('header_text') != None:
                header_text_flag = payload.get('header_text')
            if payload.get('video_url') != None:
                video_url_flag = payload.get('image_url')
            if payload.get('text') != None:
                text_flag = payload.get('text')
            create_turn_picture(browser, header_text=header_text_flag, video_url=video_url_flag, text=text_flag)
        elif step_type == "save_field":
            save_field(browser)
        elif step_type == "go_to_lobby":
            get_lobby(browser)
     