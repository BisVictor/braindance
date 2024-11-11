from game import *
from lobby import *
import json

def execute_steps(browser, filename):
    with open(filename, 'r') as file:
        steps = json.load(file)
    
    for step in steps:
        step_type = step['type']
        payload = step.get('payload', {})

        if step_type == "create_game":
            private_game_flag = payload.get('private', False)
            go_to_play_flag = payload.get('go_to_play', False)
            create_game(browser, private_game=private_game_flag, go_to_game=go_to_play_flag)

        elif step_type == "enter_game":
            nick_name_json = payload.get('nickname', "")
            role_flag = "owner" if payload.get('role') in ["owner", "Owner"] else "visitor"
            skip_flag = payload.get('skip', False)
            enter_game(browser, nickname=nick_name_json, role=role_flag, skip=skip_flag)

        elif step_type == "create_turn" and payload.get('type') == "picture":
            header_text_flag = payload.get('header_text', "")
            image_url_flag = payload.get('image_url', "")
            text_flag = payload.get('text', "")
            create_turn_picture(browser, header_text=header_text_flag, image_url=image_url_flag, text=text_flag)

        elif step_type == "create_turn" and payload.get('type') == "video":
            header_text_flag = payload.get('header_text', "")
            video_url_flag = payload.get('video_url', "")
            text_flag = payload.get('text', "")
            create_turn_video(browser, header_text=header_text_flag, video_url=video_url_flag, text=text_flag)

        elif step_type == "save_field":
            save_field(browser)

        elif step_type == "go_to_lobby":
            get_lobby(browser)