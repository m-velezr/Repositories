import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path

def cargarArchivos():
    ruta = Path(__file__).parent
    charges_data_path = ruta/"data"/"charges_data.csv"
    personal_data_path =ruta/"data"/"personal_data.csv"
    plan_data_path = ruta/"data"/"plan_data.csv"
    return charges_data_path,personal_data_path, plan_data_path
    

def explanatory_analysis(charges_data_path, personal_data_path, plan_data_path):
    
    
    charges = pd.read_csv(charges_data_path)
    personal = pd.read_csv(personal_data_path)
    plan = pd.read_csv(plan_data_path)

   
    monthly_charges_mean = round(stats.trim_mean(charges["monthlyCharges"].dropna(), 0.1))
    charges["monthlyCharges"] = charges["monthlyCharges"].fillna(monthly_charges_mean)

   
    charges["totalCharges"] = charges["totalCharges"].fillna(charges["monthlyCharges"] * charges["tenure"])

   
    condi = [
        ((charges["tenure"] > 0) & (charges["tenure"] <= 24)),
        ((charges["tenure"] > 24) & (charges["tenure"] <= 48)),
        ((charges["tenure"] > 48) & (charges["tenure"] <= 60)),
        (charges["tenure"] > 60)
    ]
    opc = ["group1", "group2", "group3", "group4"]

    charges["tenureBinned"] = np.select(condi, opc, default="Other")

  
    charges_data_updated = charges.copy()

    
    churn_pct = round(((charges_data_updated["Churn"] == "Yes").sum() / charges_data_updated["Churn"].shape[0]) * 100)

    
    data_merge_one = pd.merge(charges_data_updated, personal, on="customerID")
    data_merged = pd.merge(data_merge_one, plan, on="customerID", how="left")

   
    pct_age_above_60 = round(((data_merged["age"] > 60).sum() / data_merged["age"].shape[0]) * 100)

   
    internet_service_counts = data_merged["internetService"].value_counts().to_dict()

    results = {
        "monthly_charges_mean": monthly_charges_mean,
        "charges_data_updated": charges_data_updated,
        "churn_pct": churn_pct,
        "data_merged": data_merged,
        "pct_age_above_60": pct_age_above_60,
        "internet_service_counts": internet_service_counts
    }
    return results

charges_data_path, personal_data_path, plan_data_path = cargarArchivos()

explanatory_analysis(charges_data_path, personal_data_path, plan_data_path)