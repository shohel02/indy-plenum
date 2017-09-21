from plenum.server.plugin.token.constants import TOKEN_LEDGER_ID
from plenum.server.plugin.token.transactions import TokenTransactions


LEDGER_IDS = {TOKEN_LEDGER_ID, }
AcceptableTxnTypes = {TokenTransactions.MINT_PUBLIC.value,
                      TokenTransactions.XFER.value}