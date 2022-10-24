symbolsList = ['TLT','AAPL','AMD','NOC','IBM','UPS']

#symbolsList = ['DDD', 'MMM', 'ABT', 'ABBV', 'ANF', 'ASO', 'ACAD', 'ACN', 'ATVI', 'ADBE', 'AMD', 'MSOS', 'AFRM', 'AFL', 'AGNC', 'ABNB', 'AKAM', 'AA', 'BABA', 'ALGN', 'APT', 'GOOGL', 'GOOG', 'AMLP', 'MO', 'AMRN', 'AMZN', 'AMBA', 'AMC', 'AAL', 'AEO', 'AXP', 'AIG', 'ABC', 'AMGN', 'AMRS', 'ADI', 'AVXL', 'BUD', 'NLY', 'AR', 'APA', 'APO', 'APPH', 'AAPL', 'AMAT', 'AAOI', 'MT', 'ADM', 'ANET', 'ARKF', 'ARKG', 'ARKK', 'ARVL', 'AHT', 'ASML', 'ASTS', 'AZN', 'T', 'ATER', 'TEAM', 'ACB', 'ADSK', 'ADP', 'AZO', 'AVYA', 'CAR', 'BIDU', 'BKKT', 'BK', 'VXX', 'GOLD', 'BBWI', 'BHC', 'BAX', 'BDX', 'BBBY', 'BRK.B', 'BBY', 'BYND', 'BILI', 'BILL', 'BIIB', 'BNTX', 'BTBT', 'BAC', 'BB', 'BLK', 'BX', 'BLNK', 'SQ', 'APRN', 'BA', 'BKNG', 'BSX', 'BP', 'BRCC', 'BMY', 'AVGO', 'BURL', 'CZR', 'CEI', 'CCJ', 'CPB', 'CWH', 'GOOS', 'CSIQ', 'GOEV', 'CGC', 'COF', 'CPRI', 'CAH', 'CCL', 'CVNA', 'SAVA', 'CAT', 'CBOE', 'CNC', 'CF', 'CHPT', 'CHTR', 'CC', 'CVX', 'CHWY', 'CMG', 'CI', 'CSCO', 'C', 'CLAR', 'CLF', 'CLX', 'NET', 'CLOV', 'CLVS', 'CME', 'CODX', 'KO', 'COIN', 'CL', 'CMCSA', 'CAG', 'COP', 'STZ', 'CSTM', 'WISH', 'CLR', 'GLW', 'COST', 'CTRA', 'COTY', 'COUP', 'CPNG', 'CRSP', 'CRON', 'CRWD', 'CSX', 'CVS', 'DHI', 'DHR', 'DNMR', 'DDOG', 'PLAY', 'ASHR', 'DE', 'DAL', 'DB', 'DVN', 'DKS', 'APPS', 'DWAC', 'FAZ', 'DUST', 'JNUG', 'LABD', 'TZA', 'YINN', 'ERX', 'FAS', 'NUGT', 'JDST', 'SOXL', 'SOXS', 'TNA', 'LABU', 'DFS', 'DISH', 'DIS', 'DOCU', 'DG', 'DLTR', 'DPZ', 'DASH', 'DOW', 'DKNG', 'DBX', 'DD', 'BROS', 'KODK', 'EBAY', 'EDIT', 'EW', 'SOLO', 'EA', 'ELV', 'EMR', 'ET', 'NRGV', 'ENVX', 'ENPH', 'EPD', 'EOG', 'EQT', 'MJ', 'SILJ', 'JETS', 'ETSY', 'EXAS', 'EXPE', 'EXPR', 'XOM', 'FFIV', 'FFIE', 'FSLY', 'FAZE', 'FDX', 'RACE', 'AG', 'FSLR', 'FISV', 'FSR', 'FIVE', 'FLR', 'FL', 'F', 'FOXA', 'FCX', 'ULCC', 'FUBO', 'FCEL', 'FUTU', 'GME', 'GPS', 'GD', 'GE', 'GM', 'GNUS', 'GETY', 'GILD', 'URA', 'GSAT', 'GS', 'GT', 'GPRO', 'GRAB', 'GRWG', 'GSK', 'HAL', 'HBI', 'HOG', 'HIG', 'HL', 'MOMO', 'HLF', 'HSY', 'HES', 'HIMX', 'HD', 'HON', 'HRL', 'HPQ', 'HSBC', 'HUM', 'HUT', 'HYMC', 'HYLN', 'ITW', 'ILMN', 'INFN', 'INO', 'INTC', 'IBM', 'IP', 'INTU', 'ISRG', 'FXE', 'UUP', 'TAN', 'BKLN', 'IVR', 'QQQ', 'SARK', 'IQ', 'IRBT', 'IRNT', 'IAU', 'EWZ', 'EWC', 'EWG', 'EWJ', 'EWW', 'EWY', 'SLV', 'TLT', 'IEF', 'FXI', 'IVV', 'ICLN', 'HYG', 'LQD', 'IBB', 'EMB', 'EFA', 'EEM', 'EWU', 'IWM', 'TIP', 'IYR', 'ITB', 'JD', 'JBLU', 'JKS', 'JNJ', 'YY', 'JPM', 'JMIA', 'JNPR', 'KMB', 'KMI', 'KGC', 'KKR', 'KLAC', 'KSS', 'KHC', 'KWEB', 'KR', 'LRCX', 'LVS', 'LMND', 'LEN', 'LI', 'LLY', 'LL', 'LMT', 'RIDE', 'LOW', 'LCID', 'LULU', 'LUMN', 'LITE', 'LAZR', 'LYFT', 'M', 'MNKD', 'MARA', 'MRO', 'MPC', 'MAR', 'MRVL', 'MA', 'MTCH', 'MAT', 'MCD', 'MCK', 'MDT', 'MELI', 'MRK', 'META', 'MET', 'MGM', 'MCHP', 'MU', 'MSFT', 'MSTR', 'MVIS', 'MRNA', 'MDLZ', 'MDB', 'MNST', 'MS', 'MOS', 'COOP', 'NNDM', 'NNOX', 'NCR', 'NEOG', 'NTAP', 'NTES', 'NFLX', 'EDU', 'NEGG', 'NEM', 'NKE', 'NKLA', 'NIO', 'NOK', 'JWN', 'NSC', 'NOC', 'NCLH', 'NOV', 'NVAX', 'NUE', 'NTNX', 'NTR', 'NVDA', 'NXPI', 'OXY', 'OCGN', 'OKTA', 'OLN', 'ON', 'OPEN', 'ORCL', 'OSTK', 'PACB', 'PGY', 'PLTR', 'PANW', 'PARA', 'PRTY', 'PYPL', 'PSFE', 'PTON', 'PENN', 'PEP', 'WOOF', 'PBR', 'PFE', 'PCG', 'PM', 'PSX', 'PHUN', 'PDD', 'PINS', 'PXD', 'PAA', 'PLUG', 'PNC', 'PSNY', 'PPG', 'PG', 'BITO', 'SVXY', 'UCO', 'UVXY', 'VIXY', 'SSO', 'TBT', 'TQQQ', 'SQQQ', 'SDS', 'UPRO', 'QCOM', 'QS', 'RRC', 'RTX', 'REGN', 'REV', 'RH', 'RNG', 'RIOT', 'RAD', 'RIVN', 'HOOD', 'RBLX', 'RKT', 'ROKU', 'ROST', 'RCL', 'RUM', 'SPGI', 'SABR', 'CRM', 'SRPT', 'SLB', 'SCHW', 'SE', 'STX', 'XLC', 'XLE', 'XLF', 'XLY', 'XLP', 'XLV', 'XLI', 'XLU', 'XLB', 'XLK', 'NOW', 'SHOP', 'SIG', 'SIRI', 'SKX', 'SKLZ', 'SWKS', 'SDC', 'SNAP', 'SNDL', 'SNOW', 'SOFI', 'SONO', 'SONY', 'SRNE', 'SO', 'LUV', 'SWN', 'DIA', 'GLD', 'FEZ', 'SPY', 'XBI', 'XHB', 'XME', 'XOP', 'KRE', 'XRT', 'ANY', 'SAVE', 'SPLK', 'SPOT', 'SBUX', 'STEM', 'SFIX', 'STNE', 'SSYS', 'SYK', 'SU', 'SPWR', 'SYF', 'SYY', 'SST', 'TMUS', 'TSM', 'TTWO', 'TAL', 'TNDM', 'TPR', 'TGT', 'TTCF', 'TECK', 'TDOC', 'TELL', 'TME', 'THC', 'TSLA', 'WEAT', 'TEVA', 'TXN', 'TTD', 'TMO', 'TLRY', 'TJX', 'TOL', 'MODG', 'TSCO', 'RIG', 'TRIP', 'TWLO', 'TWTR', 'UBER', 'ULTA', 'UAA', 'UA', 'UNP', 'UAL', 'UPS', 'URI', 'X', 'UNG', 'USO', 'UNH', 'U', 'OLED', 'UPST', 'URBN', 'USB', 'UWMC', 'VFC', 'VALE', 'VLO', 'GDX', 'GDXJ', 'OIH', 'SMH', 'VXRT', 'VZ', 'VRTX', 'VERU', 'VTRS', 'VIPS', 'SPCE', 'V', 'VOD', 'UVIX', 'WBA', 'WMT', 'WBD', 'WM', 'W', 'WB', 'WFC', 'WDC', 'WE', 'WY', 'WPM', 'WHR', 'WMB', 'WDAY', 'WKHS', 'WW', 'WYNN', 'XPEV', 'AUY', 'YETI', 'ZEN', 'Z', 'ZIM', 'ZM', 'ZS']
symbolsList = ['MMM', 'ABT', 'ABBV', 'ANF', 'ASO', 'ACAD', 'ACN', 'ATVI', 'ADBE', 'AMD', 'AFRM', 'AFL', 'ABNB', 'AKAM', 'AA', 'BABA', 'ALGN', 'GOOGL', 'GOOG', 'AMLP', 'MO', 'AMZN', 'AMBA', 'AXP', 'AIG', 'ABC', 'AMGN', 'ADI', 'BUD', 'NLY', 'AR', 'APA', 'APO', 'AAPL', 'AMAT', 'MT', 'ADM', 'ANET', 'ARKF', 'ARKG', 'ARKK', 'ASML', 'AZN', 'T', 'TEAM', 'ADSK', 'ADP', 'AZO', 'CAR', 'BIDU', 'BK', 'VXX', 'BBWI', 'BAX', 'BDX', 'BRK.B', 'BBY', 'BILL', 'BIIB', 'BNTX', 'BAC', 'BLK', 'BX', 'SQ', 'BA', 'BKNG', 'BSX', 'BP', 'BMY', 'AVGO', 'BURL', 'CZR', 'CCJ', 'CPB', 'CWH', 'GOOS', 'CSIQ', 'COF', 'CPRI', 'CAH', 'CVNA', 'SAVA', 'CAT', 'CBOE', 'CNC', 'CF', 'CHTR', 'CC', 'CVX', 'CHWY', 'CMG', 'CI', 'CSCO', 'C', 'CLF', 'CLX', 'NET', 'CME', 'KO', 'COIN', 'CL', 'CMCSA', 'CAG', 'COP', 'STZ', 'CLR', 'GLW', 'COST', 'CTRA', 'COUP', 'CPNG', 'CRSP', 'CRWD', 'CSX', 'CVS', 'DHI', 'DHR', 'DDOG', 'PLAY', 'ASHR', 'DE', 'DAL', 'DVN', 'DKS', 'DWAC', 'FAZ', 'DUST', 'JNUG', 'LABD', 'TZA', 'YINN', 'ERX', 'FAS', 'NUGT', 'JDST', 'SOXS', 'TNA', 'DFS', 'DIS', 'DOCU', 'DG', 'DLTR', 'DPZ', 'DASH', 'DOW', 'DBX', 'DD', 'BROS', 'EBAY', 'EW', 'EA', 'ELV', 'EMR', 'ENVX', 'ENPH', 'EPD', 'EOG', 'EQT', 'JETS', 'ETSY', 'EXAS', 'EXPE', 'XOM', 'FFIV', 'FDX', 'RACE', 'FSLR', 'FISV', 'FIVE', 'FLR', 'FL', 'FOXA', 'FCX', 'FUTU', 'GME', 'GD', 'GE', 'GM', 'GILD', 'URA', 'GS', 'GSK', 'HAL', 'HOG', 'HIG', 'HLF', 'HSY', 'HES', 'HD', 'HON', 'HRL', 'HPQ', 'HSBC', 'HUM', 'ITW', 'ILMN', 'INTC', 'IBM', 'IP', 'INTU', 'ISRG', 'FXE', 'UUP', 'TAN', 'BKLN', 'QQQ', 'SARK', 'IRBT', 'IAU', 'EWZ', 'EWC', 'EWG', 'EWJ', 'EWW', 'EWY', 'SLV', 'TLT', 'IEF', 'FXI', 'IVV', 'ICLN', 'HYG', 'LQD', 'IBB', 'EMB', 'EFA', 'EEM', 'EWU', 'IWM', 'TIP', 'IYR', 'ITB', 'JD', 'JKS', 'JNJ', 'YY', 'JPM', 'JNPR', 'KMB', 'KMI', 'KKR', 'KLAC', 'KSS', 'KHC', 'KWEB', 'KR', 'LRCX', 'LVS', 'LMND', 'LEN', 'LI', 'LLY', 'LMT', 'LOW', 'LULU', 'LITE', 'M', 'MRO', 'MPC', 'MAR', 'MRVL', 'MA', 'MTCH', 'MAT', 'MCD', 'MCK', 'MDT', 'MELI', 'MRK', 'META', 'MET', 'MGM', 'MCHP', 'MU', 'MSFT', 'MSTR', 'MRNA', 'MDLZ', 'MDB', 'MNST', 'MS', 'MOS', 'COOP', 'NCR', 'NTAP', 'NTES', 'NFLX', 'EDU', 'NEM', 'NKE', 'JWN', 'NSC', 'NOC', 'NOV', 'NVAX', 'NUE', 'NTNX', 'NTR', 'NVDA', 'NXPI', 'OXY', 'OKTA', 'OLN', 'ON', 'ORCL', 'OSTK', 'PANW', 'PARA', 'PYPL', 'PENN', 'PEP', 'PFE', 'PM', 'PSX', 'PDD', 'PINS', 'PXD', 'PLUG', 'PNC', 'PPG', 'PG', 'SVXY', 'UCO', 'VIXY', 'SSO', 'TBT', 'TQQQ', 'SQQQ', 'SDS', 'UPRO', 'QCOM', 'RRC', 'RTX', 'REGN', 'RH', 'RNG', 'RIVN', 'RBLX', 'ROKU', 'ROST', 'RCL', 'SPGI', 'CRM', 'SRPT', 'SLB', 'SCHW', 'SE', 'STX', 'XLC', 'XLE', 'XLF', 'XLY', 'XLP', 'XLV', 'XLI', 'XLU', 'XLB', 'XLK', 'NOW', 'SHOP', 'SIG', 'SKX', 'SWKS', 'SNOW', 'SONY', 'SO', 'LUV', 'DIA', 'GLD', 'FEZ', 'SPY', 'XBI', 'XHB', 'XME', 'XOP', 'KRE', 'XRT', 'SAVE', 'SPLK', 'SPOT', 'SBUX', 'SYK', 'SU', 'SPWR', 'SYF', 'SYY', 'TMUS', 'TSM', 'TTWO', 'TNDM', 'TPR', 'TGT', 'TECK', 'TDOC', 'THC', 'TSLA', 'TXN', 'TTD', 'TMO', 'TJX', 'TOL', 'MODG', 'TSCO', 'TRIP', 'TWLO', 'TWTR', 'UBER', 'ULTA', 'UNP', 'UAL', 'UPS', 'URI', 'X', 'UNG', 'USO', 'UNH', 'U', 'OLED', 'UPST', 'URBN', 'USB', 'VFC', 'VLO', 'GDX', 'GDXJ', 'OIH', 'SMH', 'VZ', 'VRTX', 'V', 'WBA', 'WMT', 'WM', 'W', 'WFC', 'WDC', 'WY', 'WPM', 'WHR', 'WMB', 'WDAY', 'WYNN', 'YETI', 'ZEN', 'Z', 'ZIM', 'ZM', 'ZS']
#symbolsList = ['PLAY']

def getSymbols():
    return symbolsList