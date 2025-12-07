from ycprox.core.secrets import vault

def main():
    print("Hello from ycprox!")


def test_vault():
    vault.set_oauth_token("1234567890")
    print(f"Token is {vault.get_oauth_token()}")
    vault.delete_oauth_token()
    print(f"Token is {vault.get_oauth_token()}")

if __name__ == "__main__":
    main()