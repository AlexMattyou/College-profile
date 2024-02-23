from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# model_name = "microsoft/DialoGPT-large"
# tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side='left')
# model = AutoModelForCausalLM.from_pretrained(model_name)

# def chat(text, chatHistoryIds=None):
#     inputIds = tokenizer.encode(text + tokenizer.eos_token, return_tensors="pt")
#     bot_inputIds = torch.cat([chatHistoryIds, inputIds], dim=-1) if chatHistoryIds is not None else inputIds
#     chatHistoryIds = model.generate(bot_inputIds, max_length=1000, pad_token_id=tokenizer.eos_token_id)
#     output = tokenizer.decode(chatHistoryIds[:, bot_inputIds.shape[-1]:][0], skip_special_tokens=True)
#     return output, chatHistoryIds


def say():
    text = input("YOU: ")
    if text == "STOP":
        print("Bye!")
        return
    response, chatHistoryIds = "bot's reply" # chat(text)
    print(f"BOT: {response}")
    say()
    
say()
