from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Charger le CSV au démarrage
df = pd.read_csv('recommandations.csv')

# Convertir les colonnes de chaînes en listes
df['rec_content_based'] = df['rec_content_based'].apply(lambda x: list(map(int, x.split(';'))))
df['rec_collaborative'] = df['rec_collaborative'].apply(lambda x: list(map(int, x.split(';'))))

@app.get("/get_recos")
def get_recos(user_id: int, method: str):
    if method not in ['content_based', 'collaborative']:
        raise HTTPException(status_code=400, detail="Méthode invalide")
    
    row = df[df['user_id'] == user_id]
    if row.empty:
        raise HTTPException(status_code=404, detail="User non trouvé")
    
    recs = row[f'rec_{method}'].values[0]
    return {"user_id": user_id, "method": method, "recommendations": recs}
