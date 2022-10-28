from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def on_created(self, event):
        filename : str = event.src_path.replace("C:\\Users\\Ineas\\Desktop\\pr4python\\", "").replace(".txt", "").lower()
        f=open(filename+'.txt', "r")
        strin=f.read()
        f.close()
        print(strin)

observer = Observer()
observer.schedule(Handler(), path="C:\\Users\\Ineas\\Desktop\\pr4python")
observer.start()
print()
try:
    while 1:
        pass
except KeyboardInterrupt:
    observer.stop()
    print("Handler stoped")

