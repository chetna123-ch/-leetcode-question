import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df=pd.DataFrame(players)
    rows,columns=df.shape
    return [rows,columns]