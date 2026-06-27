import os
from ne_agent import NEAgent
from ne_agent.tui import boot_screen, print_status, print_result, console
from rich.text import Text

def load_corpus(data_dir="data"):
    corpus = {}
    for lang in ["assamese", "khasi", "mizo", "garo"]:
        path = os.path.join(data_dir, f"{lang}_mono_500.txt")
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                corpus[lang] = [line.strip() for line in f if line.strip()]
            print(f"  ✓ {lang}: {len(corpus[lang])} sentences")
        else:
            print(f"  ✗ {lang}: not found")
    return corpus

if __name__ == "__main__":
    boot_screen()
    console.print(Text("  Loading corpus and building index...", style="dim white"))
    
    agent = NEAgent()
    corpus = load_corpus()
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
