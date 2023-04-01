CONST_TEXT_ALL = "All"

# Path Constants
IMG_PATH = "img\\"
MINER_RES_PATH = IMG_PATH + "miner_res\\"
ICONS_PATH = IMG_PATH + "icons\\"
FARMER_RES_PATH = IMG_PATH + "farmer_res\\"


# GUI Constants
CONST_GUI_FRAME_SELECTJOBANDZONE_TEXT = "< Select profession and Zone >"
CONST_GUI_FRAME_SELECTRESOURCE_TEXT = "< Select resource >"
CONST_GUI_FRAME_ASSIGNAKEY = "< Assign a key >"

CONST_GUI_BUTTON_START_TEXT = "Start"
CONST_GUI_BUTTON_STOP_TEXT = "Stop"


# Jobs Constants
CONST_JOB_MINER = "Miner"
CONST_JOB_LUMBERJACK = "Lumberjack"
CONST_JOB_FARMER = "Farmer"
CONST_JOB_FISHERMAN = "Fisherman"
CONST_JOB_HERBALIST = "Herbalist"
CONST_JOB_TRAPPER = "Trapper"

# Zones Constants
CONST_ZONE_ASTRUB = "Astrub"
CONST_ZONE_AMAKNA = "Amakna"
CONST_ZONE_BRAKMAR = "Brakmar"
CONST_ZONE_WILD_ESTATE = "Wild Estate"

# Statuses Constants
CONST_STATUS_WAITING = "Waiting..."
CONST_STATUS_ACTIVE = "Active"
CONST_STATUS_STOPPED = "Stopped"

# String Key Constants
CONST_KEY_STR_F1 = "Key.f1"
CONST_KEY_STR_F2 = "Key.f2"
CONST_KEY_STR_F3 = "Key.f3"
CONST_KEY_STR_F4 = "Key.f4"
CONST_KEY_STR_F5 = "Key.f5"
CONST_KEY_STR_F6 = "Key.f6"
CONST_KEY_STR_F7 = "Key.f7"
CONST_KEY_STR_F8 = "Key.f8"
CONST_KEY_STR_F9 = "Key.f9"
CONST_KEY_STR_F10 = "Key.f10"
CONST_KEY_STR_F11 = "Key.f11"
CONST_KEY_STR_F12 = "Key.f12"

# Miner Resources

CONST_RESOURCE_MINER_IRON = "Iron ore"
CONST_RESOURCE_MINER_FINEST_SEA_SALT = "Finest sea salt"
CONST_RESOURCE_MINER_CLASSIC_CARBON = "Classic carbon"
CONST_RESOURCE_MINER_COPPER = "Copper ore"
CONST_RESOURCE_MINER_SHADOWY_COBALT = "Shadowy cobalt"
CONST_RESOURCE_MINER_BRONZE_NUGGET = "Bronze nugget ore"

CONST_RESOURCE_MINER_RUGGED_QUARTZ = "Rugged quartz"


# Farmer Resources
CONST_RESOURCE_FARMER_WHEAT = "Wheat"
CONST_RESOURCE_FARMER_ARTICHOKE = "Artichoke"
CONST_RESOURCE_FARMER_TUBERBULB = "Tuberbulb"
CONST_RESOURCE_FARMER_BARLEY = "Barley"

# Resources by zone
CONST_ZONE_RESOURCES_MINER_ASTRUB = [
    CONST_RESOURCE_MINER_IRON,
    CONST_RESOURCE_MINER_FINEST_SEA_SALT,
    CONST_RESOURCE_MINER_CLASSIC_CARBON,
    CONST_RESOURCE_MINER_COPPER,
    CONST_RESOURCE_MINER_SHADOWY_COBALT,
]

CONST_ZONE_RESOURCES_MINER_WILDESTATE = [
    CONST_RESOURCE_MINER_RUGGED_QUARTZ,
]

CONST_ZONE_RESOURCES_FARMER_ASTRUB = [
    CONST_RESOURCE_FARMER_WHEAT,
    CONST_RESOURCE_FARMER_ARTICHOKE,
    CONST_RESOURCE_FARMER_TUBERBULB,
    CONST_RESOURCE_FARMER_BARLEY,
]


# Action Icon Names
CONST_ICON_ACTION_FARMING_CUT = "farming-cut-icon.png"
CONST_ICON_ACTION_FARMING_SEEDS = "farming-harvest-icon.png"
CONST_ICON_ACTION_FARMING_REAP = "farming-reap-icon.png"
CONST_ICON_ACTION_MINING_HARVEST = "mining-harvest-icon.png"


## Available Actions by resource

CONST_ICON_FOR_ACTIONS_FARMER = {
    CONST_RESOURCE_FARMER_WHEAT: {
        "harvest": CONST_ICON_ACTION_FARMING_REAP,
        "seeds": CONST_ICON_ACTION_FARMING_SEEDS,
    },
    CONST_RESOURCE_FARMER_ARTICHOKE: {
        "harvest": CONST_ICON_ACTION_FARMING_CUT,
        "seeds": CONST_ICON_ACTION_FARMING_SEEDS,
    },
    CONST_RESOURCE_FARMER_TUBERBULB: {
        "harvest": CONST_ICON_ACTION_FARMING_CUT,
        "seeds": CONST_ICON_ACTION_FARMING_SEEDS,
    },
    CONST_RESOURCE_FARMER_BARLEY: {
        "harvest": CONST_ICON_ACTION_FARMING_REAP,
        "seeds": CONST_ICON_ACTION_FARMING_SEEDS,
    }
}

