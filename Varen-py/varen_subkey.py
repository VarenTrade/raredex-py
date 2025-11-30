import logging

from varen_py.account.subkey_account import SubkeyAccount
from varen_py.api.api_client import VarenApiClient
from varen_py.api.ws_client import VarenWebsocketClient
from varen_py.environment import Environment
from varen_py.utils import raise_value_error


class VarenSubkey:
    """VarenSubkey class for L2-only authentication using subkeys.

    This class extends Varen functionality but uses SubkeyAccount for L2-only
    authentication without requiring L1 credentials.

    Args:
        env (Environment): Environment
        l2_private_key (str): L2 private key (required)
        l2_address (str): L2 address of the main account (required)
        logger (logging.Logger, optional): Logger. Defaults to None.
        ws_timeout (int, optional): WebSocket read timeout in seconds. Defaults to None (uses default).

    Examples:
        >>> from varen_py import VarenSubkey
        >>> from varen_py.environment import Environment
        >>> paradex = VarenSubkey(
        ...     env=Environment.TESTNET,
        ...     l2_private_key="0x...",
        ...     l2_address="0x..."
        ... )
        >>> # With custom timeout
        >>> varen = VarenSubkey(
        ...     env=Environment.TESTNET,
        ...     l2_private_key="0x...",
        ...     l2_address="0x...",
        ...     ws_timeout=30
        ... )
    """

    def __init__(
        self,
        env: Environment,
        l2_private_key: str,
        l2_address: str,
        logger: logging.Logger | None = None,
        ws_timeout: int | None = None,
    ):
        if env is None:
            return raise_value_error("ParadexSubkey: Invalid environment")

        # Validate required parameters
        if not l2_private_key:
            raise_value_error("ParadexSubkey: L2 private key is required")
        if not l2_address:
            raise_value_error("ParadexSubkey: L2 address is required")

        self.env = env
        self.logger: logging.Logger = logger or logging.getLogger(__name__)

        # Load api client and system config
        self.api_client = ParadexApiClient(env=env, logger=logger)
        self.ws_client = ParadexWebsocketClient(env=env, logger=logger, ws_timeout=ws_timeout)
        self.config = self.api_client.fetch_system_config()

        # Initialize SubkeyAccount with L2-only credentials
        self.account = SubkeyAccount(
            config=self.config,
            l2_private_key=l2_private_key,
            l2_address=l2_address,
        )

        # Initialize both API client and WebSocket client with the account
        self.api_client.init_account(self.account)
        self.ws_client.init_account(self.account)

    async def init_account(self):
        """Initialize account for L2-only authentication.

        This method is provided for compatibility with the Paradex interface,
        but the account is already initialized in __init__ for subkeys.
        """
        # Account is already initialized in __init__ for subkeys
        self.logger.info("SubkeyAccount already initialized in constructor")
        return self.account
