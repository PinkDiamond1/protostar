from typing import Optional

from protostar.starknet_gateway.network_config import PredefinedNetwork

from .block_explorer import BlockExplorer, ClassHash, ContractAddress, TransactionHash


class StarkScanBlockExplorer(BlockExplorer):
    def __init__(self, network: PredefinedNetwork) -> None:
        super().__init__()
        network_to_domain: dict[PredefinedNetwork, str] = {
            "mainnet": "https://starkscan.co",
            "testnet": "https://testnet.starkscan.co",
        }
        self._domain = network_to_domain[network]

    def get_name(self) -> str:
        return "StarkScan"

    def create_link_to_transaction(self, tx_hash: TransactionHash) -> Optional[str]:
        return f"{self._domain}/tx/0x{tx_hash:064x}"

    def create_link_to_contract(
        self, contract_address: ContractAddress
    ) -> Optional[str]:
        return f"{self._domain}/contract/0x{contract_address:064x}"

    def create_link_to_class(self, class_hash: ClassHash) -> Optional[str]:
        return f"{self._domain}/class/0x{class_hash:064x}"