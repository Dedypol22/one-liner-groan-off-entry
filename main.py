import os

# One-line dad joke: "dates" does double duty (calendar dates / romantic
# dates), and "bringing up" too (mentioning the past / surfacing reminders).
# Punchline lands on the last word; nothing in the line explains the joke.
LINE = "My calendar dumped me — it couldn't stop bringing up my past dates."

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
