import requests
import json

api_key = "sk-XXX"

class ChatContextPool:
    def __init__(self):
        self.pool = {}

    def add_message(self, user_id, role, content):
        if user_id not in self.pool:
            self.pool[user_id] = []

        self.pool[user_id].append({"role": role, "content": content})

    def get_context(self, user_id):
        return self.pool.get(user_id, [])  # 如果没有则返回空列表

    def request_chat_gpt(self, user_id, user_message, api_key, temperature=0.7):
        self.add_message(user_id, "user", user_message)

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {#"gpt-3.5-turbo",
            "model": 'gpt-3.5-turbo',
            "messages": self.get_context(user_id),
            "temperature": temperature
        }
        
        # print(data)

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )

        result = response.json()
        # print(result)
        generated_text = result["choices"][0]["message"]["content"]

        self.add_message(user_id, "assistant", generated_text)

        return generated_text

def chat():
    chat_pool = ChatContextPool()

    url='https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png'

    # 读取label_text.txt文件,读取每一行的内容,用逗号隔开
    description = ''
    with open('label_text.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            word = line.split('|')[0]
            score = float(line.split('|')[1])
            description += '(' + word + ',' + str(score) + '),'

    msg="参考以下信息，每个括号中包含场景中存在的事物以及其重要程度(准确度)："+description+'''想象出一个场景，并回答以下两个问题。\n
    1. 请用一句话形容这个场景。\n
    2. 请详细描述这个场景，并分析这段描述是否符合常理。\n
    '''
    #将msg写到msg.txt文件中
    with open('msg.txt', 'a') as f:
        f.write(msg)
        f.write('$\n')
    import os
    os.remove('label_text.txt')
    
    # ask
    print("提问:", msg)
    response1 = chat_pool.request_chat_gpt("user1", msg , api_key)
    print("回答:", response1)