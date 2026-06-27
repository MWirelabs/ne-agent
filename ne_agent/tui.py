import time
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.rule import Rule

console = Console()

GREETINGS = [
    ("Kumno ngi tip u ia u?", "khasi"),
    ("Angni manda?", "garo"),
    ("Eng nge nia?", "mizo"),
    ("Nongshitla?", "meitei"),
    ("Kemon acho?", "assamese"),
    ("Nangse ema?", "bodo"),
]

def load_banner() -> str:
    try:
        with open("assets/banner.txt") as f:
            return f.read()
    except:
        return "NE-AGENT"

def boot_screen():
    console.clear()
    console.print(Align.center(Text(load_banner(), style="bold orange1")))
    console.print(Align.center(Text("Speaks Northeast.", style="bold white")))
    console.print()
    for phrase, lang in GREETINGS:
        line = Text()
        line.append(f"{phrase}", style="white")
        line.append(f"  [{lang}]", style="bold blue")
        console.print(Align.center(line))
        time.sleep(0.2)
    console.print()
    console.print(Rule(style="orange1"))
    console.print()

def print_status(index_size: int, model: str):
    status = Text()
    status.append("● NE-LID  ", style="orange1")
    status.append("● NE-Embed  ", style="orange1")
    status.append(f"● Ollama {model}  ", style="orange1")
    status.append(f"● FAISS index: {index_size} docs", style="orange1")
    console.print(Align.center(status))
    console.print()
    console.print(Rule(style="orange1"))
    console.print()

def print_result(result: dict):
    lang_line = Text()
    lang_line.append("LANG  ", style="dim white")
    lang_line.append(result["detected_lang"].upper(), style="bold blue")
    lang_line.append(f"  {result['lang_score']}", style="dim white")
    console.print(lang_line)
    console.print()
    if result["retrieved"]:
        console.print(Text("RETRIEVED", style="dim orange1"))
        for d in result["retrieved"]:
            console.print(Text(f"  · {d['text'][:70]}", style="dim white"))
    console.print()
    console.print(Panel(
        Text(result["answer"], style="white"),
        border_style="orange1",
        title=Text("NE-AGENT", style="bold orange1"),
    ))
    console.print()
