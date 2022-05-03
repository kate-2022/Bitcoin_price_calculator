import tkinter as tk
from tkinter import ttk
import requests

class BitcoinPriceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x250")
        self.title("Bitcoin-Preis-Rechner")
        # print(self.style.theme_names())
        # print(self.style.theme_used())

        BitcoinToEuroFrame(self).pack(fill="both")

class BitcoinToEuroFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.COINDESK_API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
        self.euro_value = tk.StringVar(value="Hier wird dann der Preis in Euro angezeigt..")

        bitcoin_label = ttk.Label(self, text="Anzahl Bitcoin:", font=("Arial", 12))
        bitcoin_label.pack(side="top", fill="x", padx=10, pady=10)

        self.bitcoin_entry = ttk.Entry(self, font=("Arial", 14))
        self.bitcoin_entry.pack(side="top", fill="x", padx=5, pady=2)

        euro_label = ttk.Label(self, text="Preis in Euro:", font=("Arial", 12))
        euro_label.pack(side="top", fill="x", padx=5, pady=2)

        euro_display = ttk.Label(self, textvariable=self.euro_value, font=("Arial", 12))
        euro_display.pack(side="top", fill="x", padx=5, pady=20)

        calculate_button = ttk.Button(self, text="Berechnung durchführen", command=self.calculate_price)
        calculate_button.pack(side="bottom",fill="x", pady=10, padx=10, ipady=10, ipadx=10)

    def calculate_price(self):
        try:
            response = requests.get(self.COINDESK_API_URL)
            response_dict = response.json()
            current_bitcoin_price_euro = response_dict["bpi"]["EUR"]["rate_float"]
            calculated_price_euro = float(self.bitcoin_entry.get())* current_bitcoin_price_euro
            self.euro_value.set("{:.2f}".format(calculated_price_euro))
        except ValueError:
            print("Bitte einen gültigen Zahlenwert eingeben!")

root = BitcoinPriceConverter()
root.mainloop()