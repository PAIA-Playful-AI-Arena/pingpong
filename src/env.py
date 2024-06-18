from os import path

ASSET_DIR = path.join(path.dirname(__file__), "../asset")
ASSET_IMAGE_DIR = path.join(path.dirname(__file__), "../asset/img")

BG_PATH = path.join(ASSET_IMAGE_DIR, "bg.png")
BOARD1P_PATH = path.join(ASSET_IMAGE_DIR, "board_1p.png")
BOARD2P_PATH = path.join(ASSET_IMAGE_DIR, "board_2p.png")
OBSTACLE_PATH = path.join(ASSET_IMAGE_DIR, "obstacle.png")
BALL_PATH = path.join(ASSET_IMAGE_DIR, "ball.png")

ASSET_IMG_URL = "https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/pingpong/main/asset/img/"
BG_URL = ASSET_IMG_URL + "bg.png"
BOARD1P_URL = ASSET_IMG_URL+"board_1p.png"
BOARD2P_URL = ASSET_IMG_URL+"board_2p.png"
BALL_URL = ASSET_IMG_URL+"ball.png"
OBSTACLE_URL = ASSET_IMG_URL+"obstacle.png"
BG_LEFT_WIDTH=400