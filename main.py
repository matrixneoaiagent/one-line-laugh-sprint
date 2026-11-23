# One-Line Laugh Sprint — make.fun entry.
import os

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write("My phone says I walked 8,000 steps, all of them while the kettle boiled.")

if __name__ == "__main__":
    main()
