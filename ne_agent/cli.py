import os
from ne_agent import NEAgent
from ne_agent.tui import boot_screen, print_status, print_result, console
from rich.text import Text

def load_corpus():
    corpus = {}
    # Look for data next to where cli.py is installed
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    for lang in ["assamese", "khasi", "mizo", "garo"]:
        path = os.path.join(data_dir, f"{lang}_mono_500.txt")
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                corpus[lang] = [line.strip() for line in f if line.strip()]
            console.print(Text(f"  loaded {lang}: {len(corpus[lang])} sentences", style="dim white"))
        else:
            console.print(Text(f"  skipped {lang}: not found", style="dim white"))
    return corpus

def main():
    boot_screen()
    console.print(Text("  Loading corpus and building index...", style="dim white"))
    agent = NEAgent()
    corpus = load_corpus()
    if not corpus:
        console.print(Text("  No corpus found. Add txt files to ne_agent/data/", style="bold red"))
        return
    agent.load_corpus(corpus)
    print_status(agent.retriever.index.ntotal, agent.llm.model)
    while True:
        try:
            query = console.input("[bold orange1]›[/bold orange1] ")
            if query.strip().lower() in ["exit", "quit", ":q"]:
                console.print(Text("\nPhade! (Goodbye)\n", style="bold orange1"))
                break
            if not query.strip():
                continue
            console.print(Text("  thinking...", style="dim white"))
            result = agent.run(query)
            print_result(result)
        except KeyboardInterrupt:
            console.print(Text("\nPhade!\n", style="bold orange1"))
            break

if __name__ == "__main__":
    main()
