from eth_keys import keys
from eth_utils import to_checksum_address

private_key_hex = "2".zfill(64)

private_key_bytes = bytes.fromhex(private_key_hex)

private_key = keys.PrivateKey(private_key_bytes)

pub_key = private_key.public_key

eth_add = pub_key.to_address()

checksum_address = to_checksum_address(eth_add)

# Print results
print(f"Private Key: {private_key}")
print(f"Public Key: {pub_key}")
print(f"Ethereum Address: {checksum_address}")

