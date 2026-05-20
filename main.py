import os
from dotenv import load_dotenv
import anthropic
import sys
from functions.get_files_info import get_files_from_wd

load_dotenv()
_api_key = os.getenv("ANTHROPIC_API_KEY")
client=anthropic.Anthropic(api_key=_api_key)
def main():
    conversation_history=[]
    verbose_flag=False
    if len(sys.argv)<2:
        print("Error: Please provide a prompt.")
        print("Usage: python script.py 'Your prompt here'")
        sys.exit(1)
    if len(sys.argv)==3 and sys.argv[2]=="--verbose":
        verbose_flag=True
        
   
    prompt=sys.argv[1]
    conversation_history.append({"role": "user", "content": prompt})
    MODEL="claude-sonnet-4-6"
    response = client.messages.create(
    model=MODEL,
    max_tokens=100,
    messages=conversation_history
)
    print(response.content[0].text)
    conversation_history.append({"role": "assistant", "content": response.content[0].text})
    input_tokens=response.usage.input_tokens
    output_tokens=response.usage.output_tokens
    total_tokens=input_tokens+output_tokens
    if verbose_flag:
        print(f"User Prompt:  {prompt}")
        print(f"Output (Response) Tokens: {output_tokens}")
        print(f"Total Tokens Used:       {total_tokens}")

if __name__ == "__main__":
    main()
    #print(get_files_from_wd("calculator"))

