import pandas as pd
from .thresholds import LIMITS
def assess(df: pd.DataFrame):
    df = df.copy()
    def fail(row):
        fails = []
        if "pH" in row and (row["pH"]<LIMITS["pH_min"] or row["pH"]>LIMITS["pH_max"]): fails.append("pH")
        for c,lbl in [("BOD_mg_L","BOD_mg_L"),("COD_mg_L","COD_mg_L"),("NH3_mg_L","NH3_mg_L"),("Ecoli_cfu_100ml","Ecoli_cfu_100ml"),
                      ("PO4_mg_L","PO4_mg_L"),("TSS_mg_L","TSS_mg_L")]:
            if c in row and row[c] > LIMITS[lbl]: fails.append(c)
        return fails
    df["fails"] = df.apply(fail, axis=1)
    df["non_compliant"] = df["fails"].apply(lambda x: 1 if len(x)>0 else 0)
    return df
