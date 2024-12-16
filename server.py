from flask import Flask, request, jsonify
from Dragon import utils, BundleFinder, ScanAllTx, BulkWalletChecker, TopTraders, TimestampTransactions, purgeFiles, CopyTradeWalletFinder, TopHolders, EarlyBuyers, checkProxyFile
walletCheck = BulkWalletChecker()
topTraders = TopTraders()
app = Flask(__name__)


# To get PNLs
@app.route('/getpnls/wallet', methods=['POST'])
def get_wallet_data():
    data = request.get_json()
    wallets = data.get('wallets', [])
    walletData = walletCheck.fetchWalletData(wallets, threads=99, skipWallets=False, useProxies=False)
    return jsonify({"status": "success", "data": walletData}), 200

# To get Top Traders for given address
@app.route('/toptraders/mint', methods=['POST'])
def get_TopWallets_data():
    data = request.get_json()
    addresses = data.get('mint', [])
    tradersData = topTraders.topTraderData(addresses, threads=99, useProxies=False)
    return jsonify({"status": "success", "data": tradersData}), 200

if __name__ == '__main__':
    print(app.url_map)  # Debug route map
    app.run(host='0.0.0.0', port=3001, debug=True)



# from flask import Flask, request, jsonify
# from Dragon import utils, BundleFinder, ScanAllTx, BulkWalletChecker, TopTraders, TimestampTransactions, purgeFiles, CopyTradeWalletFinder, TopHolders, EarlyBuyers, checkProxyFile
# app = Flask(__name__)

# if __name__ == '__main__':
#     print(app.url_map)  # Debug route map
#     app.run(host='0.0.0.0', port=3001, debug=True)

# purgeFiles = utils.purgeFiles
# clear = utils.clear
# walletCheck = BulkWalletChecker()



# @app.route('/getpnls/wallet', methods=['POST'])
# def get_wallet_data():
#     try:
#         # Parse JSON input
#         data = request.get_json()
#         wallets = data.get('wallets', [])
        
#         if not wallets or not isinstance(wallets, list):
#             return jsonify({"error": "Invalid or missing 'wallets' parameter. It must be a list of wallet addresses."}), 400
        
#         # Process wallets
#         walletData = walletCheck.fetchWalletData(wallets, threads=5, skipWallets=False, useProxies=False)
        
#         # Return response as JSON
#         return jsonify({"status": "success", "data": walletData}), 200

#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500

# # while True:
# #     try:
# #         solana()
# #         break
# #     except ValueError as e:
# #         utils.clear()
# #         print(e)
