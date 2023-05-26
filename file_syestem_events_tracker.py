import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/manue/OneDrive/Documentos/Programacion/python"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"{event.src_path} ha sido creado")

    def on_modified(self, event):
        print(f"{event.src_path} se ha modificado")

    def on_moved(self, event):
        print(f"se ha movido {event.src_path} a {event.dest_path}")

    def on_deleted(self, event):
        print(f"se borro {event.src_path}")

observer = Observer()
event_handler = FileEventHandler()
observer.schedule(event_handler, path=from_dir, recursive=True)
observer.start()
     
try:
    while True:
        time.sleep(2)
        print('ejecutando...')
except KeyboardInterrupt:
    print('detenido')
    observer.stop()

observer.join()