import os
import subprocess

MODEL_NAME = "mistral"
MODEL_DIR = "../model/local/"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)


def ensure_model_downloaded(model=MODEL_NAME):
    os.makedirs(MODEL_DIR, exist_ok=True)
    # Check if model is already present (Ollama stores models in its own cache, but we simulate local dir)
    # Download model using Ollama if not present
    print(f"📥 Downloading model '{model}' with Ollama (if not already present)...")
    subprocess.run(["ollama", "pull", model], check=True)


def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def summarize_with_ollama(input_text, model=MODEL_NAME):
    # Truncate text if too long for the model context window
    max_length = 2000  # adjust as needed for your model
    if len(input_text) > max_length:
        input_text = input_text[:max_length] + "..."
    prompt = (
        "You are an expert text summarizer. "
        "Write a concise summary (3-5 sentences) of the following text, focusing only on the most important points. "
        "Do NOT repeat the original text.\n\n"
        f"Text:\n{input_text}\n\nSummary:"
    )
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8").strip()


def save_summary(summary, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary)


if __name__ == "__main__":
    input_file = "input/sample.txt"
    output_file = "output/summary.txt"

    ensure_model_downloaded()
    text = load_text(input_file)
    print("Input text is: ", text)
    print("🔍 Summarizing...")
    summary_text = summarize_with_ollama(text)
    print("✅ Summary generated:", summary_text)
    save_summary(summary_text, output_file)
    print("✅ Summary saved to:", output_file)

