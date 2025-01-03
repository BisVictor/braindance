import json

def transform(input_file, new_file):
    try:           
        with open(input_file, "r", encoding="utf-8") as file:
            input_data = json.load(file)       
        required_keys = ["title", "img_src", "text"]
        for key in required_keys:
            if key not in input_data:
                raise KeyError(f"Key '{key}' not found in input data.")
     
        output_data = {
            "type": "create_turn",
            "payload": {
                "type": "picture",
                "data": {
                    "header_text": input_data["title"].capitalize(),
                    "image_url": input_data["img_src"],
                    "text": input_data["text"]
                }
            }
        }
       
        with open(new_file, "w", encoding="utf-8") as file:
            json.dump(output_data, file, ensure_ascii=False, indent=4)
        print(f"Data successfully transformed and saved to {new_file}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from file '{input_file}'.")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



