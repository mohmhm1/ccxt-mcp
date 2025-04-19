# CCXT MCP Server

A Model Context Protocol (MCP) server that provides trading functionality through the CCXT library.

![ScreenRecording2025-04-19at17 22 45-ezgif com-speed](https://github.com/user-attachments/assets/1fd98f5d-60b0-449c-98d9-7eca23a9cf0f)

![cursor](https://github.com/user-attachments/assets/d90caaec-e23b-45f7-a6db-2cbfcd4568ce)


## Features

- Fetch ticker data for any symbol
- Get order book data
- View recent trades
- Create orders (market, limit, etc.)
- Cancel orders
- Fetch account balance
- Trading analysis prompts
- Order management guidance
- Testnet support
- Supports any exchange that CCXT supports
- Cached exchange instances for better performance

## Project Structure

```
src/ccxt_mcp/
├── __init__.py              # Main server file
├── utils/
│   └── exchange.py          # Exchange management with testnet support
├── tools/
│   ├── fetch_ticker.py      # Ticker data tool
│   ├── fetch_order_book.py  # Order book tool
│   ├── fetch_trades.py      # Trades tool
│   ├── create_order.py      # Order creation tool
│   ├── cancel_order.py      # Order cancellation tool
│   └── fetch_balance.py     # Balance fetching tool
└── prompts/
    ├── trading_analysis.py  # Trading analysis prompt
    ├── order_management.py  # Order management prompt
    └── testnet_guidance.py  # Testnet guidance prompt
```

## Setup to run MCP server
#### Prerequisites:
These are instructions for Claude Desktop but this mcp server could be used for any MCP Client.

1. Download github repo:
```bash
git clone https://github.com/pcriadoperez/ccxt-mcp.git
```
2. Enter folder
`cd ccxt-mcp`

3. Install mcp server
`mcp install run.py`

4. Open Claude desktop -> Settings -> Developer -> Edit config
- Add your env variables
- You may have Replace in command you uv location (You can find it running `which uv`)
- It should look like the below config

```json
{
  "mcpServers": {
    "CCXT Trading Server": {
      "command": "/Users/pablo/.local/bin/uv",
      "args": [
        "run",
        "--with",
        "ccxt",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/Users/pablo/github/ccxt-mcp-2/run.py"
      ],
      "env":{
          "BINANCE_APIKEY": "BINANCE_APIKEY",
          "BINANCE_SECRET": "BINANCE_SECRET"
      }
    }
  }
}
```

5. Close and open claude

## Setup for contributing

1. Clone the repository:
```bash
git clone https://github.com/pcriadoperez/ccxt-mcp.git
cd ccxt-mcp
```

2. Install dependencies:
```bash
uv pip install -e .
```

3. Set up environment variables:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your API keys
# Add your exchange API keys in the format:
# {EXCHANGE_ID}_API_KEY=your_api_key
# {EXCHANGE_ID}_SECRET=your_secret
```

## Dev usage

1. Run the Dev MCP server:
```bash
mcp dev run.py
```


## Security

- Never commit your `.env` file
- Use environment variables for API keys
- Consider using a secrets management service for production
- Testnet is recommended for development and testing

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT 
