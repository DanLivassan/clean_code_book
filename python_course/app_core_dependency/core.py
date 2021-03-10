class DepModule:

    def start(self):
        raise NotImplemented

    def stop(self):
        raise NotImplemented


class MockModule(DepModule):
    def start(self):
        print(f"[{self.__class__.__name__}] start()")

    def stop(self):
        print(f"[{self.__class__.__name__}] stop()")


class Core(DepModule):
    def __init__(self, database: DepModule, webserver: DepModule):
        self.database = database
        self.webserver = webserver

    def start(self):
        print(f"[{self.__class__.__name__}] is starting...")
        self.database.start()
        self.webserver.start()
        print(f"[{self.__class__.__name__}] is started!")

    def stop(self):
        print(f"[{self.__class__.__name__}] is stopping ...")
        self.database.stop()
        self.webserver.stop()
        print(f"[{self.__class__.__name__}] is stopped!")


class DataBase(DepModule):

    def __init__(self, database_name, database_port):
        self.database_name = database_name
        self.database_port = database_port

    def start(self):
        print(f"[{self.__class__.__name__}] is starting {self.database_name} at port {self.database_port}")
        print(f"[{self.__class__.__name__}] is started!")

    def stop(self):
        print(f"[{self.__class__.__name__}] is stopping {self.database_name} at port {self.database_port}")
        print(f"[{self.__class__.__name__}] is stopped!")


class WebServer(DepModule):

    def __init__(self, webserver_name, webserver_port):
        self.webserver_name = webserver_name
        self.webserver_port = webserver_port

    def start(self):
        print(f"[{self.__class__.__name__}] is starting {self.webserver_name} at port {self.webserver_port}")
        print(f"[{self.__class__.__name__}] is started!")

    def stop(self):
        print(f"[{self.__class__.__name__}] is stopping {self.webserver_name} at port {self.webserver_port}")
        print(f"[{self.__class__.__name__}] is stopped!")


if __name__ == "__main__":
    database = DataBase("database1", 3306)
    webserver = WebServer("database1", 8080)
    core = Core(database, webserver)
    core.start()
    core.stop()
