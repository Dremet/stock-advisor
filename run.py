from functions import *

urls={
    "munichre":"https://www.onvista.de/aktien/Muenchener-Rueck-Aktie-DE0008430026",
    "frosta":"https://www.onvista.de/aktien/FROSTA-AG-Aktie-DE0006069008",
    "apple":"https://www.onvista.de/aktien/Apple-Aktie-US0378331005",
    "strabag":"https://www.onvista.de/aktien/STRABAG-SE-Aktie-AT000000STR1",
    "3m":"https://www.onvista.de/aktien/3M-Aktie-US88579Y1010",
    "biontech":"https://www.onvista.de/aktien/BIONTECH-SE-Aktie-US09075V1026",
    "fortescue_metals":"https://www.onvista.de/aktien/FORTESCUE-METALS-GROUP-LTD-Aktie-AU000000FMG4",
    "nexgen_energy":"https://www.onvista.de/aktien/NEXGEN-ENERGY-Aktie-CA65340P1062",
    "uranium_energy":"https://www.onvista.de/aktien/URANIUM-ENERGY-CORP-Aktie-US9168961038",
    "blue_sky_uranium":"https://www.onvista.de/aktien/BLUE-SKY-URANIUM-Aktie-CA0960495079",
    "sto":"https://www.onvista.de/aktien/STO-SE-CO-KGAA-Aktie-DE0007274136",
    "sfc_energy":"https://www.onvista.de/aktien/SFC-ENERGY-AG-Aktie-DE0007568578",
    "thor_industries":"https://www.onvista.de/aktien/THOR-INDUSTRIES-INC-Aktie-US8851601018"
}

con=sqlite3.connect('stock_prices.db')
cur=con.cursor()

for name, url in urls.items():
    price = download_current_onvista_price(url)
    save_current_price_to_sqlite(cur, name, price)

con.commit()
con.close()