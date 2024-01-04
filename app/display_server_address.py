from config import Config  # Import your Config class from config.py

def main():
    server_address = Config.SERVER_ADDRESS
    print(f'Server Address: {server_address}')

if __name__ == '__main__':
    main()
