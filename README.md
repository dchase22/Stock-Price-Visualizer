# Stock Price Visualizer

A simple Python script that fetches historical stock data using **yfinance** and visualizes it with **Plotly**. This tool allows you to quickly see the closing price of a stock over a user-specified period.

---

## Features

- Fetch historical stock data for any ticker symbol.
- Choose the time period for the data:
  - `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max`
- Interactive line chart of the stock's closing price using Plotly.
- Customizable chart colors and labels.

---

## Installation

Make sure you have Python installed (3.7+ recommended). Install the required packages:

```bash
pip install yfinance plotly
