

def from_wiki_articles_to_steps(input_data):
    number_of_steps = len(input_data)    
               
    
    all_step_data = []
    for step in range (number_of_steps):
        one_step_data = {
        "type": "create_turn",
        "payload": {
            "type": "picture",
            "data": {
                "header_text": input_data[step]["title"].capitalize(),
                "image_url": input_data[step]["img_src"],
                "text": input_data[step]["text"]
            }
        }
    }   
        all_step_data.append(one_step_data)
    #print(all_step_data)
    return all_step_data
        



    

       
        
    


