#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import random

banner1="""
 █████╗ ███╗   ██╗██╗   ██╗██████╗ ██╗███████╗
██╔══██╗████╗  ██║██║   ██║██╔══██╗██║██╔════╝
███████║██╔██╗ ██║██║   ██║██████╔╝██║███████╗
██╔══██║██║╚██╗██║██║   ██║██╔══██╗██║╚════██║
██║  ██║██║ ╚████║╚██████╔╝██████╔╝██║███████║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝
                                            
"""
banner2="""

   ▄████████ ███▄▄▄▄   ███    █▄  ▀█████████▄   ▄█     ▄████████ 
  ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ ███    ███    ███ 
  ███    ███ ███   ███ ███    ███   ███    ███ ███▌   ███    █▀  
  ███    ███ ███   ███ ███    ███  ▄███▄▄▄██▀  ███▌   ███        
▀███████████ ███   ███ ███    ███ ▀▀███▀▀▀██▄  ███▌ ▀███████████ 
  ███    ███ ███   ███ ███    ███   ███    ██▄ ███           ███ 
  ███    ███ ███   ███ ███    ███   ███    ███ ███     ▄█    ███ 
  ███    █▀   ▀█   █▀  ████████▀  ▄█████████▀  █▀    ▄████████▀  
                                                                 

"""
banner3="""
 ▄▄▄·  ▐ ▄ ▄• ▄▌▄▄▄▄· ▪  .▄▄ · 
▐█ ▀█ •█▌▐██▪██▌▐█ ▀█▪██ ▐█ ▀. 
▄█▀▀█ ▐█▐▐▌█▌▐█▌▐█▀▀█▄▐█·▄▀▀▀█▄
▐█ ▪▐▌██▐█▌▐█▄█▌██▄▪▐█▐█▌▐█▄▪▐█
 ▀  ▀ ▀▀ █▪ ▀▀▀ ·▀▀▀▀ ▀▀▀ ▀▀▀▀ 
"""
banner4="""
▄▀▀█▄   ▄▀▀▄ ▀▄  ▄▀▀▄ ▄▀▀▄  ▄▀▀█▄▄   ▄▀▀█▀▄   ▄▀▀▀▀▄ 
▐ ▄▀ ▀▄ █  █ █ █ █   █    █ ▐ ▄▀   █ █   █  █ █ █   ▐ 
  █▄▄▄█ ▐  █  ▀█ ▐  █    █    █▄▄▄▀  ▐   █  ▐    ▀▄   
 ▄▀   █   █   █    █    █     █   █      █    ▀▄   █  
█   ▄▀  ▄▀   █      ▀▄▄▄▄▀   ▄▀▄▄▄▀   ▄▀▀▀▀▀▄  █▀▀▀   
▐   ▐   █    ▐              █    ▐   █       █ ▐      
        ▐                   ▐        ▐       ▐        
"""
banners=[banner1,banner2,banner3]

def burn():
    print random.choice(banners)
