import re
from datetime import datetime
import requests

def kelvin_to_celsius(kelvin_temp):
    celsius_temp = float(kelvin_temp) - 273.15
    return str(round(celsius_temp, 2))

#weather function
def weather_data_recieve(status,user_input,prev_input):

    def read_file(filepath):
    # Initialize an empty list to store the non-comment lines
        non_comment_lines = []

    # Open the file in read mode
        with open(filepath, 'r') as file:
            # Read the lines from the file
            lines = file.readlines()

            # Filter out the lines that do not start with "#"
            non_comment_lines = [line.strip() for line in lines if not line.startswith("#")]

        return non_comment_lines

    
    data = read_file("Open weather map API.txt")
    api_key=data[0]
    CityList={"binh duong","ho chi minh","ha noi","hue","da nang","vinh","nghe an"}
    City = user_input.lower()
    type_of_data_list={"temperature","humidity","report","description"} 
    type_of_data=""
    for j in type_of_data_list:
        if j in user_input:
            type_of_data=j     
    if status==2: 
        type_of_data=""
        for j in type_of_data_list:
            if j in prev_input:
                type_of_data=j 
        

        City=user_input 
    
    if status==0:
        for i in CityList:
            if i in City:
                City=i
        if City not in CityList:
            return 2, "Sorry, that city may not be in my dataset, can you try to type the name of the city again?"
            
    # Make a request to the OpenWeatherMap API
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={City}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
    except:
        return 0,"sorry, I can not connect to weather server"
    # Extract relevant information from the response
    wanswer=""
    try:
        temperature = str(data["main"]["temp"])
        temperature2=kelvin_to_celsius(temperature)
        humidity = str(data["main"]["humidity"])
    except:
        return 0, "I am sorry, I cannot check the weather status in the city you want."
    weather_description = str(data["weather"][0]["description"])
    if type_of_data=="temperature":       
        wanswer=temperature2+ "Celsius"
    elif type_of_data=="humidity":       
        wanswer=humidity +"percent"
    else:        
        wanswer=weather_description   
    return 0, f'Here is the answer based on your request, weather {type_of_data} in {City} is: {wanswer}'


def handle_real_time():
    # Get the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."

#open the dataset
def read_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                pattern = r'\[Q\]\s(.*?)\s\[G\]\s(.*?)\s\[R\]\s(.*?)\s\[A\]\s(.*)'
                match = re.search(pattern, line)
                if match:
                    question, guessing_keywords, required_keywords, answer = match.groups()
                    dataset.append((question.lower(), guessing_keywords.lower().split(', '), required_keywords.lower().split(', '), answer))
                else:
                    pass

    return dataset

def calculate_probability(guessing_keywords, user_input):
    keyword_count = len(guessing_keywords)
    overlapping_count = sum(keyword in user_input for keyword in guessing_keywords)
    return overlapping_count / keyword_count

def get_answer(question, guessing_keywords, required_keywords, dataset):
    max_probability = 0
    best_answer = None

    for item in dataset:
        keywords = item[2]
        if all(keyword in question for keyword in keywords):
            probability = calculate_probability(guessing_keywords, question)
            if probability > max_probability:
                max_probability = probability
                best_answer = item[3]

    return best_answer

#process input from user to get answer
def data_processing(userinput,frame,status,previous_input):
    dataset = read_dataset("data.txt")
    if status == 1:
        
        new_guessing_keywords = previous_input
        new_required_keywords = previous_input
        new_answer=userinput.lower()
        dataset.append((previous_input, new_guessing_keywords, new_required_keywords, new_answer))

        # Add the new answer to the data.txt file
        with open("data.txt", "a") as file:
            file.write(f"[Q] {previous_input} [G] {', '.join(new_guessing_keywords)} [R] {', '.join(new_required_keywords)} [A] {new_answer}\n")
            file.close()
        return 0, "Chatbot: Thanks for teaching me!"
    if status==2:
        Wstatus, weather_response=weather_data_recieve(status,userinput,previous_input)
        return Wstatus, weather_response
     
    user_input = userinput.lower()

    
    matching_answer = None
    for item in dataset:
        guessing_keywords = item[1]
        required_keywords = item[2]
        if all(keyword in user_input for keyword in required_keywords):
            if item[3].startswith("SpecialFunction:"):
                    # Check for special functions 
                    special_function = item[3].split(":")[1].strip().lower()
                    
                    if special_function == "realtime":
                        special_function_response = handle_real_time()
                        return 0, "Chatbot:" + special_function_response
                    if special_function == "weatherdata":
                        try:
                            Wstatus, weather_response=weather_data_recieve(status,userinput,previous_input)
                            return Wstatus, weather_response 
                        except:
                            return 0, "I am sorry, perhaps your syntax is incorrect or your Internet connection has a issue"
                    else:
                        return 0, "I am sorry, this syntax is invalid, can you try again for another syntax?"
            matching_answer = get_answer(user_input, guessing_keywords, required_keywords, dataset)
            if matching_answer:        
                    return 0, "Chatbot:" + matching_answer
        
    return 1, "Chatbot: I'm sorry. Perhaps my dataset is not prepared for this question.\n Can you help me provide the answer?"
    
