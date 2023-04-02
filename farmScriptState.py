import constants as cts


class appState:
    def __init__(self):
        # This should define the initial state of the app
        self.selectedJob = None
        self.selectedZone = None
        self.selectedResource = None
        self.selectedKey = None
        self.status = cts.STATUS_WAITING
        self.isStartButtonEnabled = False
        self.isStopButtonEnabled = False
        self.isZoneComboEnabled = False
        self.isResourceComboEnabled = False
        self.isKeyComboEnabled = False

    def __str__(self) -> str:
        return str(
            {
                self.selectedJob,
                self.selectedZone,
                self.selectedResource,
                self.selectedKey,
                self.status,
                self.isStartButtonEnabled,
                self.isStopButtonEnabled,
                self.isZoneComboEnabled,
                self.isResourceComboEnabled,
                self.isKeyComboEnabled,
            }
        )
