#!/usr/bin/env python3
import os, time, random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
import pyfiglet

console = Console()
PASSWORD = "Ahmedggarz39"

tools = [
    "Neural Port Scanner", "Cyber Payload Forge", "AI IP Tracker",
    "Quantum Keylogger Sim", "Drone Mapper", "Photon Tunnel (Ngrok)",
    "GPS Interceptor", "MetaMind Payload", "Update All Tools", "Exit System"
]

def beep():
    print("\a")  # صوت تنبيه بسيط

def login():
    console.print("[bold magenta]Enter system password:[/bold magenta]", end=" ")
    entered = input()
    if entered != PASSWORD:
        console.print("[red]Access Denied![/red]")
        exit()

def show_header():
    ascii_art = pyfiglet.figlet_format("Emperor of Cyber Darkness", font="cybermedium")
    color = random.choice(["cyan", "magenta", "green", "blue"])
    console.clear()
    console.print(f"[bold {color}]{ascii_art}[/{color}]")
    console.print(Panel("Cyber Dominion Interface", title="[cyan]AI CORE BOOTED[/cyan]", style="bold magenta", box=box.ROUNDED))

def show_menu():
    tool_list = "\n".join([f"[{i+1}] {tools[i]}" for i in range(len(tools))])
    console.print(Panel(tool_list, title="[bold cyan]Mainframe Tools[/bold cyan]", box=box.DOUBLE, style="bold blue"))

def update_all_tools():
    console.print("[bold yellow]Updating all tools...[/bold yellow]")
    time.sleep(1)
    os.system("git pull")
    console.print("[green]Tools updated successfully![/green]")

def run_tool(index):
    name = tools[index-1]
    console.print(f"[bold green]Launching:[/bold green] {name}")
    time.sleep(1)
    
    if name == "AI IP Tracker":
        ip = input("Enter IP to trace: ")
        console.print(f"[cyan]Simulating trace for {ip}...[/cyan]")
        time.sleep(2)
        console.print(Panel("Location: UNKNOWN\nStatus: ENCRYPTED\nISP: CLASSIFIED", title="Trace Complete", style="green"))

    elif name == "Update All Tools":
        update_all_tools()

    elif name == "Exit System":
        console.print("[bold red]Shutting down...[/bold red]")
        exit()

    else:
        console.print("[yellow]This tool is not yet implemented. Coming soon...[/yellow]")

def main():
    beep()
    login()
    while True:
        show_header()
        show_menu()
        try:
            choice = int(console.input("[bold magenta]Choose Module ➤ [/bold magenta]"))
            if 1 <= choice <= len(tools):
                run_tool(choice)
                input("[cyan]Press Enter to return to mainframe...[/cyan]")
            else:
                console.print("[red]Invalid option.[/red]")
        except ValueError:
            console.print("[red]Numbers only.[/red]")

if __name__ == "__main__":
    main()
