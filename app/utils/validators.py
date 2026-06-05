import re

ETH_ADDRESS_PATTERN = re.compile(
    r"^0x[a-fA-F0-9]{40}$"
)

def is_valid_eth_address(
    address: str
):

    return bool(
        ETH_ADDRESS_PATTERN.match(
            address
        )
    )