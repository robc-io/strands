import json
import sys

if __name__ == '__main__':
    network = sys.argv[1]
    ticker = sys.argv[2]

    config_file = "./config/" + network + "/tbears_cli_config.json"
    config = json.loads(open(config_file, "rb").read())

    config["deploy"]["scoreParams"]["ticker_name"] = ticker

    print(json.dumps(config))
