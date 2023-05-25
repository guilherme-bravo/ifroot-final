import json 
import requests

def cal_macro(qnt_nome):

    url = f'https://api.edamam.com/api/nutrition-data?app_id=6bed82c3&app_key=753a1ca6aaf26effc79a2d396877c42d%09&nutrition-type=cooking&ingr={qnt_nome}'

    

    if requests.get(url).status_code == 200:
        r = requests.get(url).text

        r = json.loads(r)
        
        try:
            dados = [f"Valor energético:{round(r['totalNutrients']['ENERC_KCAL']['quantity'], 2)} {r['totalNutrients']['ENERC_KCAL']['unit']}",
                    f"Valor de Carboidratos:{round(r['totalNutrients']['CHOCDF']['quantity'],2 )}{r['totalNutrients']['CHOCDF']['unit']}", 
                    f"Total de Proteina:{round(r['totalNutrients']['PROCNT']['quantity'], 2)}{r['totalNutrients']['FAT']['unit']}",
                    f"Total de Gordura:{round(r['totalNutrients']['FAT']['quantity'], 2)}{r['totalNutrients']['FAT']['unit']}"
                    ]
            return dados



        except:
            resultado = ['Algo deu errado.... ( ´･･)ﾉ(._.`)']
            return resultado


