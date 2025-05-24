import os
import subprocess
import yaml

INFO_PATH = os.path.join(os.path.dirname(__file__), 'data', 'info.yaml')
MODEL_NAME = "mistral"

def load_personal_info():
    with open(INFO_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def chat_with_ollama(question, info, model=MODEL_NAME):
    # Format info as YAML for the prompt
    info_yaml = yaml.dump(info, allow_unicode=True)
    prompt = (
        "You are a helpful assistant. Answer the user's question using ONLY the YAML information below. "
        "If the answer is not in the info, say you don't know.\n\n"
        f"Personal Info (YAML):\n{info_yaml}\n\nQuestion: {question}\nAnswer:"
    )
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8").strip()

def main():
    info = load_personal_info()
    print("👤 Personal info loaded.")
    print("Type your question (or 'exit' to quit):")
    while True:
        question = input("You: ").strip()
        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        answer = chat_with_ollama(question, info)
        print("Bot:", answer)

if __name__ == "__main__":
    main()

