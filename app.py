from summarizer import generate_summary

def main():
    print("Paste the call transcript below (empty line to finish):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    transcript = "\n".join(lines)

    result = generate_summary(transcript)

    print("\n--- SUMMARY ---")
    print(result["summary"])

    print("\n--- KEY POINTS ---")
    for p in result["key_points"]:
        print("-", p)

    print("\n--- ACTION ITEMS ---")
    for a in result["action_items"]:
        print("-", a)


if __name__ == "__main__":
    main()
