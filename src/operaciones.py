def check_nan(df: pd.DataFrame) -> None:
    
    nan_cols = df.isna().mean()  * 100  

    display(f'N nan cols: {len(nan_cols[nan_cols>0])}')
    display(nan_cols[nan_cols>0])
    
    
    plt.figure(figsize=(10, 6))  

    sns.heatmap(df.isna(), 
                yticklabels=False,
                cmap='viridis',
                cbar=False
               )

    plt.show();
    
    
    def limpiar_type(x):
    
    if x == "Unprovoked":
        return 'Unprovoked'
    elif x == "Provoked":
        return 'Provoked'
    elif x == "Sea Disaster":
        return 'Unprovoked' 
    elif x == 'Boat':
        return 'Provoked'
    elif x== 'Boating':
        return 'Provoked'
  
    return 'Unknown'


def limpiar_fatal(x):
    if x == 'N':
        return 'False'
    elif x == ' N':
        return 'False'
    elif x == 'N ':
        return 'False'
    elif x== 'Y':
        return 'True'

    return 'UNKNOWN'

def tipo (x) :
    Arms = "ARMS"
    Leg = 'LEGS'
    Fatal = 'FATAL'
    Ribs = 'RIBS'
    Noinjury = 'NO INJURY'
    x = x.lower()
    if type(x) != str:
        return 'Unknown'
    else:
        for a in Arms:
            if re.search (a,x):
                x = Arms
                return x
        for l in leg:
            if re.search (l,x):
                x = Leg
                return x
        for i in fatal:
            if re.search (i,x):
                x = Fatal
                return x 
        for r in ribs:
            if re.search (r,x):
                x = Ribs
                return x
        for n in noinjury:
            if re.search (n,x):
                x = Noinjury
                return x
        return 'Unknown'
    
    
    
