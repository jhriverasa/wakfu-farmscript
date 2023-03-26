import Constants as cts


class appState:
    def __init__(self):
        # This should define the initial state of the app
        self.selectedJob = None
        self.selectedZone = None
        self.selectedKey = None
        self.status = cts.CONST_STATUS_WAITING

    def __str__(self) -> str:
        return str({self.selectedJob, self.selectedZone, self.selectedKey, self.status})
