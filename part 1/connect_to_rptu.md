#API access via ai-api.rz.rptu.de with RPTU VPN 

 

Using your RPTU vpn, you can get access to various open source models, including API access to 30+ LLMs: 

 

codellama:70b            

codellama:7b-code    

codellama:7b-instruct    

codellama:7b-python  

deepseek-r1:14b  

deepseek-r1:1.5b  

deepseek-r1:32b   

deepseek-r1:70b   

deepseek-r1:7b   

deepseek-r1:8b   

deepseek-r1:latest   

falcon3:10b       

gemma3:27b    

gpt-oss:120b    

gpt-oss:20b    

llama3.2:1b    

llama3.2:3b   

llama3.2-vision:latest   

llama3.3:70b   

llama4:128x17b  

llama4:16x17b   

llama4:maverick   

llama4:scout   

mistral:7b  

mistral-large:123b   

mistral-large:latest  

mixtral:8x22b  

mixtral:8x7b    

qwen2.5vl:72b   

qwen3:235b    

qwen3-coder:30b   

 

For requesting the API (https://ai-api.rz.rptu.de/api/generate): 
Setup the vpn access via https://rz.rptu.de/en/services/network-and-telephony/network-connection/vpn-access 
Connect through the WireGuard and make sure that VPN works correctly 
You could then request the model via python code through: 

import requests 

url = "https://ai-api.rz.rptu.de/api/generate" 

payload = { 
    "model": "mistral-large:latest", 
    "prompt": "Why is the sky blue?", 
    "stream": False 
} 

headers = { 

    "Content-Type": "application/json" 

} 

response = requests.post(url, json=payload, headers=headers) 

# Print the full (non-streaming) response 

data = response.json() 

print(data["response"]) 