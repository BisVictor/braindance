from game import *
from lobby import *
from game_panels import *
from support_f import wait_for_removed
import json


def execute_steps(browser, filename):
    with open(filename, 'r') as file:
        steps = json.load(file)
    
    for step in steps:
        step_type = step['type']
        payload = step.get('payload', {})

        match step_type:
            case "create_game":
                private_game_flag = payload.get('private', False)
                go_to_play_flag = payload.get('go_to_play', False)
                create_game(browser, private_game=private_game_flag, go_to_game=go_to_play_flag)
            
            case "enter_game":
                nick_name_json = payload.get('nickname', "")
                role_flag = "owner" if payload.get('role') in ["owner", "Owner"] else "visitor"
                skip_flag = payload.get('skip', False)
                enter_game(browser, nickname=nick_name_json, role=role_flag, skip=skip_flag)
            
            case "create_turn":
                turn_type = payload.get('type')
                if turn_type == "picture":
                    data = payload.get('data', {})
                    header_text_flag = data.get('header_text', "")
                    url_flag = data.get('image_url', "")
                    text_flag = data.get('text', "")
                    create_turn(browser, turn_type, header_text=header_text_flag, url=url_flag, text=text_flag)

                elif turn_type == "video":
                    data = payload.get('data', {})
                    header_text_flag = data.get('header_text', "")
                    url_flag = data.get('video_url', "")
                    text_flag = data.get('text', "")
                    create_turn(browser, turn_type, header_text=header_text_flag, url=url_flag, text=text_flag)

                else:
                    raise ValueError(f"Unexpected turn_type: {turn_type}")
                         
            case "wait_for_removed":
                seconds_sleep = payload.get('seconds', "")
                wait_for_removed(seconds_sleep)

            
            case "save_field":
                save_field(browser)
            
            case "open_panel":
                modal = payload.get('modal', "")           
                if modal in panel_settings:
                    open_modal(browser, *panel_settings[modal], modal)
                elif modal == "go_to_lobby":
                    get_lobby(browser)
                else:
                    raise ValueError(f"Unexpected step_type: {modal}")
                    
            case "close_panel":
                modal = payload.get('modal', "")           
                if modal in panel_settings:
                    close_modal(browser, *panel_settings[modal], modal)
                else:
                    raise ValueError(f"Unexpected step_type: {modal}")