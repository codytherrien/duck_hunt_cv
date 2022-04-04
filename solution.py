import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.hub.load(
    'ultralytics/yolov5', 
    'custom', 
    path='best.pt',
    force_reload=True
).to(device).eval()

"""
Replace following with your own algorithm logic
Two random coordinate generator has been provided for testing purposes.
Manual mode where you can use your mouse as also been added for testing purposes.
"""

def GetLocation(move_type, action_space, current_frame):

    #Use relative coordinates to the current position of the "gun", defined as an integer below
    if move_type == "relative":
        """
        North = 0
        North-East = 1
        East = 2
        South-East = 3
        South = 4
        South-West = 5
        West = 6
        North-West = 7
        NOOP = 8
        """
        coordinate = action_space.sample() 
    #Use absolute coordinates for the position of the "gun", coordinate space are defined below
    else:
        """
        (x,y) coordinates
        Upper left = (0,0)
        Bottom right = (W, H) 
        """
        moves = []
        results = model(current_frame)
        try:
            for box in results.xyxy[0]:
                if box[-1] == 15:
                    middle = {
                        'coordinate' : (
                            int((box[3] - box[1]) / 2 + box[1]),
                            int((box[2] - box[0]) / 2 + box[0])# - 10
                        ),
                        'move_type' : move_type
                    }
                    moves += [middle]
            if len(moves) == 0:
                return [{'coordinate' : coordinate, 'move_type' : move_type}]
        except:
            coordinate = action_space.sample()
            return [{'coordinate' : coordinate, 'move_type' : move_type}]
        
    return moves