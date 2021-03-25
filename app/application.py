from .models import managedb
from .controller import controller
from .views import views


class Application:

    def __init__(self):
        self.view = views.Views()
        self.pgetter = managedb.PlayerDb()
        self.tgetter = managedb.TournamentDb()
        self.ctrler = controller.Controller(self.view, self.pgetter, self.tgetter)

    def run(self):
        self.ctrler.run()
