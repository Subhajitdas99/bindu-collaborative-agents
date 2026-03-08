import os
from coordinator_agent import coordinator

def print_banner():
    print("\n==============================")
    print(" BindU Collaborative Agents ")
    print("==============================")
    print("Type your question and press Enter.")
    print("Type 'exit' or 'quit' to stop.\n")


def main():
    print_banner()

    while True:
        try:
            user_input = input("User > ")

            if user_input.lower() in ["exit", "quit"]:
                print("\nShutting down agent system...")
                break

            if user_input.strip() == "":
                continue

            print("\nCoordinator thinking...\n")

            response = coordinator(user_input)

            print("Agent >", response)
            print("\n--------------------------------\n")

        except KeyboardInterrupt:
            print("\n\nSystem interrupted. Goodbye.")
            break

        except Exception as e:
            print("\nError occurred:", str(e))
            print("Please try again.\n")


if __name__ == "__main__":
    main()