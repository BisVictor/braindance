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
                if payload.get('type') == "picture":
                    header_text_flag = payload.get('header_text', "")
                    image_url_flag = payload.get('image_url', "")
                    text_flag = payload.get('text', "")
                    create_turn_picture(browser, header_text=header_text_flag, image_url=image_url_flag, text=text_flag)

                elif payload.get('type') == "video":
                    header_text_flag = payload.get('header_text', "")
                    video_url_flag = payload.get('video_url', "")
                    text_flag = payload.get('text', "")
                    create_turn_video(browser, header_text=header_text_flag, video_url=video_url_flag, text=text_flag)
            
            case "wait_for_removed":
                seconds_sleep = payload.get('seconds', "")
                wait_for_removed(seconds_sleep)

            
            case "save_field":
                save_field(browser)
            
            case "open_panel":
                modal = payload.get('modal', "")
                match modal:
                    case "classes":
                        open_modal(browser, S_BTN_CLASSES, S_BTN_CLASSES_BTN_ADD)
                    case "info":
                        open_modal(browser, S_BTN_INFO, S_BTN_INFO_ENTER_GAME)
                    case "minimap":
                        open_modal(browser, S_BTN_MINIMAP, S_BTN_MINIMAP_MAP_ICON)
                    case "go_to_lobby":
                        get_lobby(browser)
                    case _:
                        raise ValueError(f"Unexpected step_type: {step_type}")
                    
            case "close_panel":
                modal = payload.get('modal', "")
                match modal:
                    case "classes":
                        close_modal(browser, S_BTN_CLASSES, S_BTN_CLASSES_BTN_ADD)
                    case "info":
                        close_modal(browser, S_BTN_INFO, S_BTN_INFO_ENTER_GAME)
                    case "minimap":
                        close_modal(browser, S_BTN_MINIMAP, S_BTN_MINIMAP_MAP_ICON)
                    
                    
                    case _:
                        raise ValueError(f"Unexpected step_type: {step_type}")
            case _:
                raise ValueError(f"Unexpected step_type: {step_type}")