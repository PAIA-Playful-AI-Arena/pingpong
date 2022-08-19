"""
The template of the script for the machine learning process in game pingpong
"""

class MLPlay:
    def __init__(self,  ai_name,*args,**kwargs):
        """
        Constructor

        @param ai_name A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = ai_name
        print(kwargs)

    def update(self, scene_info, *args, **kwargs):
        """
        Generate the command according to the received scene information
        """
        # print(scene_info)
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            return "SERVE_TO_LEFT"
        else:
            return "MOVE_LEFT"

    def reset(self):
        """
        Reset the status
        """
        print("reset "+self.side)
        self.ball_served = False
