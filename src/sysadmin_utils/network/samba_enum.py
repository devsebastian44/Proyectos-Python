from smb.SMBConnection import SMBConnection
import socket

def enumerate_shares(target_ip: str, user: str = 'Guest', password: str = '', my_name: str = 'Client', remote_name: str = 'Server'):
    """
    Enumerates shares on a Samba/SMB server.
    """
    conn = SMBConnection(user, password, my_name, remote_name, use_ntlm_v2=True)
    
    print(f"Connecting to {target_ip}...")
    try:
        if conn.connect(target_ip, 445):
            print(f"Connected to {target_ip}")
            
            # List shares
            shares = conn.listShares()
            print("\nAvailable Shares:")
            for share in shares:
                print(f" - {share.name} ({share.type})")
                try:
                    # Try to list content of share if possible (like 'Respaldo' in original script)
                    # This is just a basic enumeration, listing root files of the share
                    files = conn.listPath(share.name, '/')
                    print(f"   [+] Access OK: Found {len(files)} files/dirs")
                except Exception:
                    pass

            conn.close()
        else:
            print("Failed to connect.")
    except Exception as e:
        print(f"Connection error: {e}")

