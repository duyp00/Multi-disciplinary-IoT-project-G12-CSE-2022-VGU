Group: G12
-
**Members:**

1. Nguyễn Mạnh Thành Long - 10422045
2. Phạm Duy - 10422022
3. Bùi Đình Anh Huy - 10422098
4. Nguyễn Trương Anh Tuấn - 10422082
5. Phạm Đào Quốc Dũng - 10422020

Usage:

Run Main.py.
Before signing in, create an account by typing in any username and password. Then it will show 2 panels. The left-side panel is an AI camera. The right-side one is a chatbot assistant.
-
•	AI cam:

Click the IoT button. Fill in username and key.
Feed connection 1 is for label data.
Feed connection 2 is for confidence value.
Fill in the feed key of the feed you want. Then, close the IoT window and click on detect button. Class names can be found in labels.txt file. You can pause the camera by clicking the 'disable' button.
Due to GPU memory limitation, I trained the model with batch size of just 16. (I set epochs to 1000 hoping to compensate this, but the model is small and weak so it usually mistakes 'face+whitemask' for 'face'. I found a very weird thing that it’s only wrong at far or close distance). The fruit training dataset is quite easy for real-life scenarios (ideal white background, single fruit). Animal test result is acceptable.
-
•	Chatbot: (some more questions and answers may be added)

User can find questions in data.txt and ask the assistant. Keep in mind that this chatbot is not intelligent, it only works with limited knowledge about a specific field/topic. Hence, you need to ask exactly questions prepared in data.txt for it to understand. With unprepared questions, you can teach it the answers. This assistant can give you computer's local time. Through internet, it has access to live weather data. You need to ask about specific condition (temp, humidity, sky condition) and provide city name you want to get the information. Using this assistant, you can quickly get info about weather conditions in many cities just by remembering simple questions
-
*Some questions about weather:*
1. > **weather temperature**
2. > **weather humidity**
3. > **weather now**

**There might be some bugs**
