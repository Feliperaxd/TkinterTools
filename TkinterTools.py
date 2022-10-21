from win32api import GetMonitorInfo, MonitorFromPoint

# Use to know the desktop or screen size!
class ScreenSize:


    monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
    monitor_area = monitor_info.get("Monitor")
    desktop = monitor_info.get("Work")

    desktop_width = desktop[2]
    desktop_height = desktop[3]
    monitor_width = monitor_area[2]
    monitor_height = monitor_area[3]
    taskbar_thickness = monitor_height - desktop_height

# Use to find the ideal positioning point!
class SpawnField:


    def __init__(
        self, window_width, window_height, field = 'Work',
        top = None, right = None, bottom = None, left = None
    ):

        self.window_width = window_width
        self.window_height = window_height
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        sc_size = ScreenSize

        fields = {
            'Work': 
            (sc_size.desktop_width, sc_size.desktop_height),
            'Monitor':
            (sc_size.monitor_width, sc_size.monitor_height)
        }
        self.screen_width, self.screen_height = fields[field]
    
    # Find common mistakes!
    def get_spawn_field_errors(
        self
    ):

        if self.right != None and self.left != None:
            self.left = 0
            self.right = None
            return "left and right can't contain values at the same time!"
        elif self.top != None and self.bottom != None:
            self.top = 0
            self.bottom = None
            return "top and bottom can't contain values at the same time!"
        else:
            return False

    # Returns X and Y position according to parameters!
    def get_coords(
        self
    ):

        error = self.get_spawn_field_errors()
        if error:
            print(f'SpawnField ERROR: {error}')
            
        if self.left == 'Center' or self.right == 'Center':
            self.x_position = self.screen_width // 2 - self.window_width // 2      
        elif type(self.left) == int:
            self.x_position = self.left
        elif type(self.right) == int:
            self.x_position = self.screen_width - self.window_width - self.right

        if self.top == 'Center' or self.bottom == 'Center':
            self.y_position = self.screen_height // 2 - self.window_height // 2 
        elif type(self.top) == int:
            self.y_position = self.top
        elif type(self.bottom) == int:
            self.y_position = self.screen_height - self.window_height - self.bottom

        return self.x_position, self.y_position
        