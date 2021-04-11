from .models import managedb
from .controller import controller, inputs
from .views import views, inputviews


class Application:

    def __init__(self):
        self.view = views.Views()
        self.inputviews = inputviews.InputViews()
        self.inputs = inputs.Input(self.inputviews)
        self.pgetter = managedb.PlayerDb()
        self.tgetter = managedb.TournamentDb()
        self.ctrler = controller.Controller(self.view, self.inputs,
                                            self.pgetter, self.tgetter)

    def run(self):
        self.ctrler.run()
