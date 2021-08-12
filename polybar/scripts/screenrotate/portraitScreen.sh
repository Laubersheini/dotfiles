xrandr --output eDP --rotate left
xinput set-prop "Wacom HID 5214 Finger" "Coordinate Transformation Matrix" 0 -1 1 1 0 0 0 0 1
xinput set-prop "Wacom HID 5214 Pen Pen (0x80205d80)" "Coordinate Transformation Matrix" 0 -1 1 1 0 0 0 0 1
xinput set-prop "Wacom HID 5214 Pen Eraser (0x80205d80)" "Coordinate Transformation Matrix" 0 -1 1 1 0 0 0 0 1


##rotate screen gestures
killall lisgd
lisgd -o 3 -d /dev/input/by-path/platform-AMDI0010:00-event -m 1000 -t 40 -T 40 -g '2,LR,*,*,R,xdotool key Super+Shift+Right' -g '2,RL,*,*,R,xdotool key Super+Shift+Left' -g '2,UD,*,*,R,xdotool key Super+Shift+q' -g '3,LR,*,*,R,python /home/david/Nextcloud/programmierkram/i3_move_workspace/move_to_right_workspace.py' -g '3,RL,*,*,R,python /home/david/Nextcloud/programmierkram/i3_move_workspace/move_to_left_workspace.py' -g '1,DRUL,*,*,R,xdotool key Super+w' -g '1,ULDR,*,*,R,xdotool key Super+e'
