from brownie import network, config, MockV3Aggregator, accounts
from web3 import Web3

DECIMALS = 8
LOCAL_CHAIN_ENVIROMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork", "mainnet-fork-dev"]


def get_account():

    # if network.show_active() == "development": red de persistencia
    if (
        network.show_active() in LOCAL_CHAIN_ENVIROMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):  # pseudo persistencia con ganache
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"La red activa es:{network.show_active()}")
    print(f"Desplegando el Mock!!")
    MockV3Aggregator.deploy(
        DECIMALS, Web3.toWei(2000, "ether"), {"from": get_account()}
    )
    print(f"Mocks desplegado")
