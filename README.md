# TkinterTools V1.0
-------------------------------------------------------------------------------------------------------------------
-ScreenSize
  Use to find the screen, desktop or taskbar sizes! 
  
  -ScreenSize.monitor_area
    Entire monitor area!
  
  -ScreenSize.desktop
    Entire desktop!
  
  -ScreenSize.desktop_width and ScreenSize.desktop_height
    Width and height in pixels of the desktop minus the taskbar!
  
  -ScreenSize.monitor_width and ScreenSize.monitor_height
    Width and height in pixels of the monitor!
  
  -ScreenSize.taskbar_thickness
    Windows taskbar thickness!
-------------------------------------------------------------------------------------------------------------------
-SpawnField
  Use to find the perfect window placement!
  Parameters:
    Note: Never put two values on the same axis!
    -field
      Type of area used to calculate!
      "Work" to desktop!
      "Monitor" to monitor!
    -window_width
      Width of window created with tkinter!
    -window_height
      Window height created with tkinter!
    -top
      Distance between window and top! 
      "Center" to center the window on the Y axis!
    -right
      Distance between window and right!
      "Center" to center the window on the X axis!
    -bottom
      Distance between window and bottom!
      "Center" to center the window on the Y axis!
    -left
      Distance between window and left!
      "Center" to center the window on the X axis!
      
  -get_spawn_field_errors
    Identifies common errors, returns false if none is found, otherwise returns the error and resets the positions!
  
  -get_coords
    Returns the X and Y coordinates calculated from the passed parameters!
-------------------------------------------------------------------------------------------------------------------
