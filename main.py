

def main():
    '''
    This is a software that allow users to use same hardware ( keyboard , mouse , trackpad)
    to control multiple devices.
    In this we have 2 system at present where 1 system is primary machine ( whos hardware will be shared)
    one secondary machine ( who will accept the hardware)
    and at present this system is desgined to work for hyprland on linux as i needed that
    '''


    print(f"{ get_ip_address()} -> user IP address")
    print("Welcome to vmode \n Press 1 if you are server \n Press 2 if you are client")
    user_input = int(input("Enter your resoponse here"))

    if(user_input == 1):
        primary_server()
    
    else:
        server_ip = input("Enter servers ip")
        client_server(server_ip)

if __name__ == "__main__":
    main()
    

