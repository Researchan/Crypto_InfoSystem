import pandas as pd

data = {
"1INCH": {
"CG_id": "1inch",
"CMC_id": "8104"
},
"AAVE": {
"CG_id": "aave",
"CMC_id": "7278"
},
"ACH": {
"CG_id": "alchemy-pay",
"CMC_id": "6958"
},
"ADA": {
"CG_id": "cardano",
"CMC_id": "2010"
},
"AGIX": {
"CG_id": "singularitynet",
"CMC_id": "2424"
},
"ALGO": {
"CG_id": "algorand",
"CMC_id": "4030"
},
"ALICE": {
"CG_id": "my-neighbor-alice",
"CMC_id": "8766"
},
"ALPHA": {
"CG_id": "alpha-finance",
"CMC_id": "7232"
},
"AMB": {
"CG_id": "amber",
"CMC_id": "2081"
},
"ANKR": {
"CG_id": "ankr",
"CMC_id": "3783"
},
"ANT": {
"CG_id": "aragon",
"CMC_id": "1680"
},
"APE": {
"CG_id": "apecoin",
"CMC_id": "18876"
},
"API3": {
"CG_id": "api3",
"CMC_id": "7737"
},
"APT": {
"CG_id": "aptos",
"CMC_id": "21794"
},
"AR": {
"CG_id": "arweave",
"CMC_id": "5632"
},
"ARB": {
"CG_id": "arbitrum",
"CMC_id": "11841"
},
"ARPA": {
"CG_id": "arpa",
"CMC_id": "4039"
},
"ASTR": {
"CG_id": "astar",
"CMC_id": "12885"
},
"ATA": {
"CG_id": "automata",
"CMC_id": "10188"
},
"ATOM": {
"CG_id": "cosmos",
"CMC_id": "3794"
},
"AUDIO": {
"CG_id": "audius",
"CMC_id": "7455"
},
"AVAX": {
"CG_id": "avalanche-2",
"CMC_id": "5805"
},
"AXS": {
"CG_id": "axie-infinity",
"CMC_id": "6783"
},
"BAKE": {
"CG_id": "bakerytoken",
"CMC_id": "7064"
},
"BAL": {
"CG_id": "balancer",
"CMC_id": "5728"
},
"BAND": {
"CG_id": "band-protocol",
"CMC_id": "4679"
},
"BAT": {
"CG_id": "basic-attention-token",
"CMC_id": "1697"
},
"BCH": {
"CG_id": "bitcoin-cash",
"CMC_id": "1831"
},
"BEL": {
"CG_id": "bella-protocol",
"CMC_id": "6928"
},
"BLUR": {
"CG_id": "blur",
"CMC_id": "23121"
},
"BLZ": {
"CG_id": "bluzelle",
"CMC_id": "2505"
},
"BNB": {
"CG_id": "binancecoin",
"CMC_id": "1839"
},
"BNX": {
"CG_id": "binaryx-2",
"CMC_id": "23635"
},
"BTC": {
"CG_id": "bitcoin",
"CMC_id": "1"
},
"C98": {
"CG_id": "coin98",
"CMC_id": "10903"
},
"CELO": {
"CG_id": "celo",
"CMC_id": "5567"
},
"CELR": {
"CG_id": "celer-network",
"CMC_id": "3814"
},
"CFX": {
"CG_id": "conflux-token",
"CMC_id": "7334"
},
"CHR": {
"CG_id": "chromaway",
"CMC_id": "3978"
},
"CHZ": {
"CG_id": "chiliz",
"CMC_id": "4066"
},
"CKB": {
"CG_id": "nervos-network",
"CMC_id": "4948"
},
"COMBO": {
"CG_id": "cocos-bcx",
"CMC_id": "4275"
},
"COMP": {
"CG_id": "compound-governance-token",
"CMC_id": "5692"
},
"COTI": {
"CG_id": "coti",
"CMC_id": "3992"
},
"CRV": {
"CG_id": "curve-dao-token",
"CMC_id": "6538"
},
"CTK": {
"CG_id": "certik",
"CMC_id": "4807"
},
"CTSI": {
"CG_id": "cartesi",
"CMC_id": "5444"
},
"CVX": {
"CG_id": "convex-finance",
"CMC_id": "9903"
},
"DAR": {
"CG_id": "mines-of-dalarnia",
"CMC_id": "11374"
},
"DASH": {
"CG_id": "dash",
"CMC_id": "131"
},
"DENT": {
"CG_id": "dent",
"CMC_id": "1886"
},
"DGB": {
"CG_id": "digibyte",
"CMC_id": "109"
},
"DODO": {
"CG_id": "dodo",
"CMC_id": "7224"
},
"DOGE": {
"CG_id": "dogecoin",
"CMC_id": "74"
},
"DOT": {
"CG_id": "polkadot",
"CMC_id": "6636"
},
"DUSK": {
"CG_id": "dusk-network",
"CMC_id": "4092"
},
"DYDX": {
"CG_id": "dydx",
"CMC_id": "11156"
},
"EDU": {
"CG_id": "edu-coin",
"CMC_id": "24613"
},
"EGLD": {
"CG_id": "elrond-erd-2",
"CMC_id": "6892"
},
"ENJ": {
"CG_id": "enjincoin",
"CMC_id": "2130"
},
"ENS": {
"CG_id": "ethereum-name-service",
"CMC_id": "13855"
},
"EOS": {
"CG_id": "eos",
"CMC_id": "1765"
},
"ETC": {
"CG_id": "ethereum-classic",
"CMC_id": "1321"
},
"ETH": {
"CG_id": "ethereum",
"CMC_id": "1027"
},
"FET": {
"CG_id": "fetch-ai",
"CMC_id": "3773"
},
"FIL": {
"CG_id": "filecoin",
"CMC_id": "2280"
},
"FLM": {
"CG_id": "flamingo-finance",
"CMC_id": "7150"
},
"FLOKI": {
"CG_id": "floki",
"CMC_id": "10804"
},
"FLOW": {
"CG_id": "flow",
"CMC_id": "4558"
},
"FTM": {
"CG_id": "fantom",
"CMC_id": "3513"
},
"FXS": {
"CG_id": "frax-share",
"CMC_id": "6953"
},
"GAL": {
"CG_id": "project-galaxy",
"CMC_id": "5228"
},
"GALA": {
"CG_id": "gala",
"CMC_id": "7080"
},
"GMT": {
"CG_id": "stepn",
"CMC_id": "10180"
},
"GMX": {
"CG_id": "gmx",
"CMC_id": "11857"
},
"GRT": {
"CG_id": "the-graph",
"CMC_id": "6719"
},
"GTC": {
"CG_id": "gitcoin",
"CMC_id": "10052"
},
"HBAR": {
"CG_id": "hedera-hashgraph",
"CMC_id": "4642"
},
"HFT": {
"CG_id": "hashflow",
"CMC_id": "22461"
},
"HIGH": {
"CG_id": "highstreet",
"CMC_id": "11232"
},
"HOOK": {
"CG_id": "hooked-protocol",
"CMC_id": "22764"
},
"HOT": {
"CG_id": "holotoken",
"CMC_id": "2682"
},
"ICP": {
"CG_id": "internet-computer",
"CMC_id": "8916"
},
"ICX": {
"CG_id": "icon",
"CMC_id": "2099"
},
"ID": {
"CG_id": "space-id",
"CMC_id": "21846"
},
"IDEX": {
"CG_id": "aurora-dao",
"CMC_id": "3928"
},
"IMX": {
"CG_id": "immutable-x",
"CMC_id": "10603"
},
"INJ": {
"CG_id": "injective-protocol",
"CMC_id": "7226"
},
"IOST": {
"CG_id": "iostoken",
"CMC_id": "2405"
},
"IOTA": {
"CG_id": "iota",
"CMC_id": ""
},
"IOTX": {
"CG_id": "iotex",
"CMC_id": "2777"
},
"JASMY": {
"CG_id": "jasmycoin",
"CMC_id": "8425"
},
"JOE": {
"CG_id": "joe",
"CMC_id": "11396"
},
"KAVA": {
"CG_id": "kava",
"CMC_id": "4846"
},
"KEY": {
"CG_id": "selfkey",
"CMC_id": "2398"
},
"KLAY": {
"CG_id": "klay-token",
"CMC_id": "4256"
},
"KNC": {
"CG_id": "kyber-network-crystal",
"CMC_id": "9444"
},
"KSM": {
"CG_id": "kusama",
"CMC_id": "5034"
},
"LDO": {
"CG_id": "lido-dao",
"CMC_id": "8000"
},
"LEVER": {
"CG_id": "lever",
"CMC_id": "20873"
},
"LINA": {
"CG_id": "linear",
"CMC_id": "7102"
},
"LINK": {
"CG_id": "chainlink",
"CMC_id": "1975"
},
"LIT": {
"CG_id": "litentry",
"CMC_id": "6833"
},
"LPT": {
"CG_id": "livepeer",
"CMC_id": "3640"
},
"LQTY": {
"CG_id": "liquity",
"CMC_id": "7429"
},
"LRC": {
"CG_id": "loopring",
"CMC_id": "1934"
},
"LTC": {
"CG_id": "litecoin",
"CMC_id": "2"
},
"LUNA2": {
"CG_id": "terra-luna-2",
"CMC_id": ""
},
"LUNC": {
"CG_id": "terra-luna",
"CMC_id": "4172"
},
"MAGIC": {
"CG_id": "magic",
"CMC_id": "14783"
},
"MANA": {
"CG_id": "decentraland",
"CMC_id": "1966"
},
"MASK": {
"CG_id": "mask-network",
"CMC_id": "8536"
},
"MATIC": {
"CG_id": "matic-network",
"CMC_id": "3890"
},
"MINA": {
"CG_id": "mina-protocol",
"CMC_id": "8646"
},
"MKR": {
"CG_id": "maker",
"CMC_id": "1518"
},
"MTL": {
"CG_id": "metal",
"CMC_id": "1788"
},
"NEAR": {
"CG_id": "near",
"CMC_id": "6535"
},
"NEO": {
"CG_id": "neo",
"CMC_id": "1376"
},
"NKN": {
"CG_id": "nkn",
"CMC_id": "2780"
},
"OCEAN": {
"CG_id": "ocean-protocol",
"CMC_id": "3911"
},
"OGN": {
"CG_id": "origin-protocol",
"CMC_id": "5117"
},
"OMG": {
"CG_id": "omisego",
"CMC_id": "1808"
},
"ONE": {
"CG_id": "harmony",
"CMC_id": "2324"
},
"ONT": {
"CG_id": "ontology",
"CMC_id": "2566"
},
"OP": {
"CG_id": "optimism",
"CMC_id": "11840"
},
"PEOPLE": {
"CG_id": "constitutiondao",
"CMC_id": "14806"
},
"PEPE": {
"CG_id": "pepe",
"CMC_id": "24478"
},
"PERP": {
"CG_id": "perpetual-protocol",
"CMC_id": "6950"
},
"PHB": {
"CG_id": "red-pulse",
"CMC_id": "13969"
},
"QNT": {
"CG_id": "quant-network",
"CMC_id": "3155"
},
"QTUM": {
"CG_id": "qtum",
"CMC_id": "1684"
},
"RAD": {
"CG_id": "radicle",
"CMC_id": "6843"
},
"RDNT": {
"CG_id": "radiant-capital",
"CMC_id": "21106"
},
"REEF": {
"CG_id": "reef",
"CMC_id": "6951"
},
"REN": {
"CG_id": "republic-protocol",
"CMC_id": "2539"
},
"RLC": {
"CG_id": "iexec-rlc",
"CMC_id": "1637"
},
"RNDR": {
"CG_id": "render-token",
"CMC_id": "5690"
},
"ROSE": {
"CG_id": "oasis-network",
"CMC_id": "7653"
},
"RSR": {
"CG_id": "reserve-rights-token",
"CMC_id": "3964"
},
"RUNE": {
"CG_id": "thorchain",
"CMC_id": "4157"
},
"RVN": {
"CG_id": "ravencoin",
"CMC_id": "2577"
},
"SAND": {
"CG_id": "the-sandbox",
"CMC_id": "6210"
},
"SFP": {
"CG_id": "safepal",
"CMC_id": "8119"
},
"SHIB": {
"CG_id": "shiba-inu",
"CMC_id": "5994"
},
"SKL": {
"CG_id": "skale",
"CMC_id": "5691"
},
"SNX": {
"CG_id": "havven",
"CMC_id": "2586"
},
"SOL": {
"CG_id": "solana",
"CMC_id": "5426"
},
"SPELL": {
"CG_id": "spell-token",
"CMC_id": "11289"
},
"SSV": {
"CG_id": "ssv-network",
"CMC_id": "12999"
},
"STG": {
"CG_id": "stargate-finance",
"CMC_id": "18934"
},
"STMX": {
"CG_id": "storm",
"CMC_id": "2297"
},
"STORJ": {
"CG_id": "storj",
"CMC_id": "1772"
},
"STX": {
"CG_id": "blockstack",
"CMC_id": "4847"
},
"SUI": {
"CG_id": "sui",
"CMC_id": "20947"
},
"SUSHI": {
"CG_id": "sushi",
"CMC_id": "6758"
},
"SXP": {
"CG_id": "swipe",
"CMC_id": "4279"
},
"T": {
"CG_id": "threshold-network-token",
"CMC_id": "17751"
},
"THETA": {
"CG_id": "theta-token",
"CMC_id": "2416"
},
"TLM": {
"CG_id": "alien-worlds",
"CMC_id": "9119"
},
"TOMO": {
"CG_id": "tomochain",
"CMC_id": "2570"
},
"TRB": {
"CG_id": "tellor",
"CMC_id": "4944"
},
"TRU": {
"CG_id": "truefi",
"CMC_id": "7725"
},
"TRX": {
"CG_id": "tron",
"CMC_id": "1958"
},
"UMA": {
"CG_id": "uma",
"CMC_id": "5617"
},
"UNFI": {
"CG_id": "unifi-protocol-dao",
"CMC_id": "7672"
},
"UNI": {
"CG_id": "uniswap",
"CMC_id": "7083"
},
"USDC": {
"CG_id": "usd-coin",
"CMC_id": "3408"
},
"VET": {
"CG_id": "vechain",
"CMC_id": "3077"
},
"WAVES": {
"CG_id": "waves",
"CMC_id": "1274"
},
"WOO": {
"CG_id": "woo-network",
"CMC_id": "7501"
},
"XEC": {
"CG_id": "ecash",
"CMC_id": "10791"
},
"XEM": {
"CG_id": "nem",
"CMC_id": "873"
},
"XLM": {
"CG_id": "stellar",
"CMC_id": "512"
},
"XMR": {
"CG_id": "monero",
"CMC_id": "328"
},
"XRP": {
"CG_id": "ripple",
"CMC_id": "52"
},
"XTZ": {
"CG_id": "tezos",
"CMC_id": "2011"
},
"XVS": {
"CG_id": "venus",
"CMC_id": "7288"
},
"YFI": {
"CG_id": "yearn-finance",
"CMC_id": "5864"
},
"ZEC": {
"CG_id": "zcash",
"CMC_id": "1437"
},
"ZEN": {
"CG_id": "zencash",
"CMC_id": "1698"
},
"ZIL": {
"CG_id": "zilliqa",
"CMC_id": "2469"
},
"ZRX": {
"CG_id": "0x",
"CMC_id": "1896"
}
}

df = pd.DataFrame.from_dict(data, orient='index')

df.to_excel('output.xlsx', index_label='바이낸스 상장목록')